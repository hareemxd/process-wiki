#!/usr/bin/env python3
"""
Publish Markdown tree to Confluence over HTTP (no TLS), matching pages by title under a parent.

- Walks a content root directory (e.g., MBSE_Style_Guide/confluence)
- Each folder becomes a Confluence page (using folder/index.md as the folder page)
- Each markdown file becomes a Confluence child page
- Updates pages by title lookup within the space (scoped by parent via hierarchy)
- Uploads local images as attachments and rewrites Markdown image refs to Confluence attachment images

Limitations:
- Markdown->HTML is not full Confluence "storage" fidelity but works well for common formatting.
- If you rely heavily on Confluence-specific macros, you’ll need custom handling.
"""

from __future__ import annotations

import os
import re
import sys
import mimetypes
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup
import markdown as md
from dotenv import load_dotenv


# ----------------------------
# Config + helpers
# ----------------------------

IMG_MD_PATTERN = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

def die(msg: str, code: int = 1) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(code)

def env(name: str, default: Optional[str] = None, required: bool = False) -> str:
    v = os.getenv(name, default)
    if required and (v is None or v.strip() == ""):
        die(f"Missing required env var: {name}")
    return v or ""

def md_title(md_text: str, fallback: str) -> str:
    # First Markdown H1 (# Title)
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback

def safe_filename(p: Path) -> str:
    return p.name


@dataclass
class PageRef:
    id: str
    title: str


class ConfluenceClient:
    def __init__(self, base_url: str, user: str, token: str, space: str, verify: bool = True):
        self.base_url = base_url.rstrip("/")
        self.space = space
        self.session = requests.Session()
        self.session.auth = (user, token)
        self.session.headers.update({"Accept": "application/json"})
        self.verify = verify

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def get_page_by_title(self, title: str) -> Optional[Dict]:
        # Confluence Server/DC REST v1: /rest/api/content?spaceKey=...&title=...
        r = self.session.get(
            self._url("/rest/api/content"),
            params={"spaceKey": self.space, "title": title, "expand": "version,ancestors"},
            verify=self.verify,
            timeout=60,
        )
        r.raise_for_status()
        data = r.json()
        results = data.get("results", [])
        return results[0] if results else None

    def read_page(self, page_id: str) -> Dict:
        r = self.session.get(
            self._url(f"/rest/api/content/{page_id}"),
            params={"expand": "version,ancestors"},
            verify=self.verify,
            timeout=60,
        )
        r.raise_for_status()
        return r.json()

    def create_page(self, title: str, parent_id: str, storage_value: str) -> PageRef:
        payload = {
            "type": "page",
            "title": title,
            "space": {"key": self.space},
            "ancestors": [{"id": parent_id}],
            "body": {"storage": {"value": storage_value, "representation": "storage"}},
        }
        r = self.session.post(
            self._url("/rest/api/content"),
            json=payload,
            verify=self.verify,
            timeout=60,
        )
        r.raise_for_status()
        data = r.json()
        return PageRef(id=data["id"], title=data["title"])

    def update_page(self, page_id: str, title: str, storage_value: str) -> PageRef:
        existing = self.read_page(page_id)
        ver = int(existing["version"]["number"]) + 1
        payload = {
            "id": page_id,
            "type": "page",
            "title": title,
            "version": {"number": ver},
            "body": {"storage": {"value": storage_value, "representation": "storage"}},
        }
        r = self.session.put(
            self._url(f"/rest/api/content/{page_id}"),
            json=payload,
            verify=self.verify,
            timeout=60,
        )
        r.raise_for_status()
        data = r.json()
        return PageRef(id=data["id"], title=data["title"])

    def list_attachments(self, page_id: str) -> List[Dict]:
        r = self.session.get(
            self._url(f"/rest/api/content/{page_id}/child/attachment"),
            params={"limit": 200},
            verify=self.verify,
            timeout=60,
        )
        r.raise_for_status()
        return r.json().get("results", [])

    def upload_attachment(self, page_id: str, file_path: Path) -> None:
        # If attachment exists, Confluence will create a new version if we POST with same filename.
        # Must send X-Atlassian-Token: no-check for multipart.
        filename = safe_filename(file_path)
        mime, _ = mimetypes.guess_type(str(file_path))
        mime = mime or "application/octet-stream"

        with file_path.open("rb") as f:
            files = {"file": (filename, f, mime)}
            headers = {"X-Atlassian-Token": "no-check"}
            r = self.session.post(
                self._url(f"/rest/api/content/{page_id}/child/attachment"),
                files=files,
                headers=headers,
                verify=self.verify,
                timeout=120,
            )
            r.raise_for_status()


# ----------------------------
# Markdown -> Confluence storage (simple)
# ----------------------------

def md_to_html(md_text: str) -> str:
    # CommonMark-ish conversion
    return md.markdown(
        md_text,
        extensions=[
            "tables",
            "fenced_code",
            "codehilite",
            "toc",
            "sane_lists",
        ],
        output_format="html5",
    )

def rewrite_images_to_attachments(md_text: str, md_file: Path, attachments: List[Path]) -> str:
    """
    Find markdown image refs, collect local files, and rewrite them to a token we can convert later.
    We'll convert tokens into Confluence <ac:image> blocks after Markdown->HTML.
    """
    def repl(m: re.Match) -> str:
        alt = (m.group(1) or "").strip()
        raw = (m.group(2) or "").strip()

        # Ignore web images
        if raw.startswith("http://") or raw.startswith("https://"):
            return m.group(0)

        # Resolve local path relative to md file
        img_path = (md_file.parent / raw).resolve()
        if not img_path.exists():
            print(f"WARN: image not found: {raw} referenced by {md_file}")
            return m.group(0)

        attachments.append(img_path)

        # Replace with a marker that survives markdown conversion
        # e.g. [[CONFLUENCE_IMAGE:filename.png|alt text]]
        return f"[[CONFLUENCE_IMAGE:{img_path.name}|{alt}]]"

    return IMG_MD_PATTERN.sub(repl, md_text)

def html_markers_to_confluence_storage(html: str) -> str:
    """
    Convert [[CONFLUENCE_IMAGE:filename|alt]] markers into Confluence storage image tags.
    """
    soup = BeautifulSoup(html, "html.parser")
    full = str(soup)

    marker_pat = re.compile(r"\[\[CONFLUENCE_IMAGE:([^|\]]+)\|([^\]]*)\]\]")

    def repl(m: re.Match) -> str:
        filename = m.group(1).strip()
        alt = m.group(2).strip()
        # Confluence storage: <ac:image><ri:attachment ri:filename="..."/></ac:image>
        # Add alt via ac:alt if desired
        alt_attr = f' ac:alt="{alt}"' if alt else ""
        return f'<ac:image{alt_attr}><ri:attachment ri:filename="{filename}"/></ac:image>'

    return marker_pat.sub(repl, full)

def build_storage_from_md(md_text: str) -> str:
    html = md_to_html(md_text)
    storage = html_markers_to_confluence_storage(html)
    return storage


# ----------------------------
# Tree publish
# ----------------------------

def collect_pages(content_root: Path) -> Tuple[Path, List[Path]]:
    if not content_root.exists():
        die(f"Content root not found: {content_root}")
    md_files = sorted([p for p in content_root.rglob("*.md") if p.is_file()])
    return content_root, md_files

def parent_chain_ids(page: Dict) -> List[str]:
    # ancestors from root->...->parent
    return [a["id"] for a in page.get("ancestors", [])]

def is_under_parent(found_page: Dict, target_parent_id: str) -> bool:
    # A page is considered under parent if its ancestor chain contains that parent id
    return target_parent_id in parent_chain_ids(found_page)

def ensure_page_by_title_under_parent(
    cf: ConfluenceClient,
    title: str,
    parent_id: str,
    storage_value: str
) -> PageRef:
    existing = cf.get_page_by_title(title)
    if existing and is_under_parent(existing, parent_id):
        return cf.update_page(existing["id"], title, storage_value)
    return cf.create_page(title, parent_id, storage_value)

def publish_file(
    cf: ConfluenceClient,
    md_file: Path,
    parent_page_id: str
) -> PageRef:
    md_text = md_file.read_text(encoding="utf-8", errors="replace")
    title = md_title(md_text, md_file.stem)

    attachments: List[Path] = []
    md_text = rewrite_images_to_attachments(md_text, md_file, attachments)
    storage = build_storage_from_md(md_text)

    page_ref = ensure_page_by_title_under_parent(cf, title, parent_page_id, storage)

    # Upload attachments (dedupe by name)
    if attachments:
        existing_atts = {a["title"] for a in cf.list_attachments(page_ref.id)}
        for img_path in attachments:
            if img_path.name in existing_atts:
                # still upload to create new version? usually safe to skip for speed
                continue
            cf.upload_attachment(page_ref.id, img_path)

    print(f"OK: {title} -> pageId={page_ref.id}")
    return page_ref

def publish_tree(cf: ConfluenceClient, content_root: Path, root_parent_id: str) -> None:
    """
    Folder structure rule:
    - A folder's 'index.md' is the page for that folder.
    - Other md files in that folder become children of the folder page.
    - Subfolders become children of the folder page (via their index.md).

    If a folder has no index.md, we create a folder page with the folder name.
    """
    # Build a map folder -> pageId
    folder_page_ids: Dict[Path, str] = {}

    # Ensure root folder page exists based on content_root/index.md if present,
    # otherwise publish children directly under provided parent.
    root_index = content_root / "index.md"
    if root_index.exists():
        root_page = publish_file(cf, root_index, root_parent_id)
        folder_page_ids[content_root] = root_page.id
    else:
        folder_page_ids[content_root] = root_parent_id

    # Walk folders top-down
    for folder in sorted([p for p in content_root.rglob("*") if p.is_dir()]):
        if folder == content_root:
            continue

        parent_folder = folder.parent
        parent_page_id = folder_page_ids.get(parent_folder, root_parent_id)

        index_md = folder / "index.md"
        if index_md.exists():
            folder_page = publish_file(cf, index_md, parent_page_id)
            folder_page_ids[folder] = folder_page.id
        else:
            # Create a stub page for folder
            title = folder.name
            storage = f"<p><em>Auto-generated folder page for {title}</em></p>"
            folder_page = ensure_page_by_title_under_parent(cf, title, parent_page_id, storage)
            folder_page_ids[folder] = folder_page.id
            print(f"OK: {title} (folder) -> pageId={folder_page.id}")

        # Publish other md files in this folder
        for md_file in sorted(folder.glob("*.md")):
            if md_file.name.lower() == "index.md":
                continue
            publish_file(cf, md_file, folder_page_ids[folder])


def main() -> None:
    load_dotenv(".env.local")

    base_url = env("CONFLUENCE_BASE_URL", required=True)
    space = env("CONFLUENCE_SPACE", required=True)
    user = env("CONFLUENCE_USER", required=True)
    token = env("CONFLUENCE_TOKEN", required=True)

    branch = os.getenv("BRANCH", "") or os.getenv("GIT_BRANCH", "")
    if not branch:
        # Try local git
        try:
            import subprocess
            branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()
        except Exception:
            branch = "staging"

    if branch == "main":
        parent_id = env("CONFLUENCE_PARENT_PAGE_ID_PROD", required=True)
    elif branch == "staging":
        parent_id = env("CONFLUENCE_PARENT_PAGE_ID_STAGING", required=True)
    else:
        print(f"Skipping publish for branch '{branch}'")
        return

    content_root = Path("MBSE_Style_Guide/confluence").resolve()
    if not content_root.exists():
        # allow running from repo root too
        alt = Path("confluence").resolve()
        if alt.exists():
            content_root = alt
        else:
            die("Could not find confluence content folder. Expected MBSE_Style_Guide/confluence or ./confluence")

    cf = ConfluenceClient(base_url=base_url, user=user, token=token, space=space, verify=True)

    print(f"Publishing from: {content_root}")
    print(f"Confluence: {base_url}  space={space}  branch={branch}  parentPageId={parent_id}")

    publish_tree(cf, content_root, parent_id)
    print("DONE")


if __name__ == "__main__":
    main()
