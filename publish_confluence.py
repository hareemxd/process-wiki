#!/usr/bin/env python3
"""
publish_confluence.py

Publishes a directory tree of Markdown files to Confluence Data Center.

Key behaviors:
- Uses markdown-to-confluence's md2conf CLI in --local mode ONCE on the docs root to generate .csf files.
  (This avoids "image path points outside root" when docs reference ../assets/...).
- Walks folders -> Confluence page tree using index.md/README.md as folder pages.
- Honors pinned page IDs via: <!-- confluence-page-id: 123456 -->
- Uses Confluence REST API v1 over HTTP with PAT as Bearer token.
- Uploads referenced local images as attachments to each page and rewrites <img> tags in storage HTML
  to Confluence attachment references.

Required env vars:
  CONF_BASE_URL        e.g. http://dal1vacon01p:8090
  CONF_SPACE_KEY       e.g. GEP
  CONF_PAT             your Confluence PAT
  CONF_ROOT_PAGE_ID    e.g. 119668755

Optional env vars:
  CONF_DOCS_DIR        default: confluence
"""

import os
import re
import mimetypes
import subprocess
import urllib.parse
from pathlib import Path
from typing import Optional, List, Tuple

import requests
from bs4 import BeautifulSoup

# -----------------------
# Config / Environment
# -----------------------
BASE_URL = os.environ.get("CONF_BASE_URL", "").rstrip("/")
SPACE_KEY = os.environ.get("CONF_SPACE_KEY", "")
PAT = os.environ.get("CONF_PAT", "")
ROOT_PAGE_ID = os.environ.get("CONF_ROOT_PAGE_ID", "")
DOCS_DIR = Path(os.environ.get("CONF_DOCS_DIR", "confluence"))

if not (BASE_URL and SPACE_KEY and PAT and ROOT_PAGE_ID):
    raise SystemExit(
        "Missing required env vars: CONF_BASE_URL, CONF_SPACE_KEY, CONF_PAT, CONF_ROOT_PAGE_ID"
    )

API = f"{BASE_URL}/rest/api"

HEADERS_JSON = {
    "Authorization": f"Bearer {PAT}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

HEADERS_BIN = {
    "Authorization": f"Bearer {PAT}",
    "Accept": "application/json",
}

PAGE_ID_RE = re.compile(r"<!--\s*confluence-page-id:\s*(\d+)\s*-->")
MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")

# -----------------------
# HTTP helpers
# -----------------------
def request_json(method: str, url: str, **kwargs):
    r = requests.request(method, url, headers=HEADERS_JSON, timeout=60, **kwargs)

    # 401 here usually means PAT not accepted or lacks permissions.
    if r.status_code == 401:
        raise RuntimeError(
            f"401 Unauthorized for {url}. "
            "Your PAT may be invalid, expired, not a Confluence PAT, or missing permissions."
        )
    if not r.ok:
        raise RuntimeError(f"{r.status_code} {r.reason} for {url}: {r.text[:800]}")
    return r.json()

def get_page(page_id: str, expand: str = "version,ancestors"):
    return request_json("GET", f"{API}/content/{page_id}", params={"expand": expand})

def create_page(title: str, parent_id: str, storage_value: str):
    payload = {
        "type": "page",
        "title": title,
        "space": {"key": SPACE_KEY},
        "ancestors": [{"id": str(parent_id)}],
        "body": {"storage": {"value": storage_value, "representation": "storage"}},
    }
    return request_json("POST", f"{API}/content", json=payload)

def update_page(page_id: str, title: str, next_version: int, storage_value: str):
    payload = {
        "id": str(page_id),
        "type": "page",
        "title": title,
        "version": {"number": next_version},
        "body": {"storage": {"value": storage_value, "representation": "storage"}},
    }
    return request_json("PUT", f"{API}/content/{page_id}", json=payload)

def find_child_by_title(parent_id: str, title: str):
    # Lists child pages; match by title.
    data = request_json(
        "GET",
        f"{API}/content/{parent_id}/child/page",
        params={"limit": 200},
    )
    for p in data.get("results", []):
        if p.get("title") == title:
            return p
    return None

# -----------------------
# Markdown / CSF conversion
# -----------------------
def md_title_from_file(md_path: Path) -> str:
    txt = md_path.read_text(encoding="utf-8", errors="replace")
    for line in txt.splitlines():
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()
    return md_path.stem

def extract_page_id(md_text: str) -> Optional[str]:
    m = PAGE_ID_RE.search(md_text)
    return m.group(1) if m else None

def parse_domain_for_md2conf() -> str:
    # md2conf wants DOMAIN like host[:port], not scheme.
    parsed = urllib.parse.urlparse(BASE_URL)
    return parsed.netloc or parsed.path

def preconvert_all_to_csf(docs_dir: Path):
    """
    Run md2conf ONCE on the docs root in --local mode.
    This allows cross-folder assets like Work Instructions/.. -> assets/.. within the same root.
    """
    domain = parse_domain_for_md2conf()

    # Note: md2conf may require --space even in local mode depending on version.
    # If yours errors "space not specified", add ["-s", SPACE_KEY] below.
    cmd = ["python", "-m", "md2conf", str(docs_dir), "--local", "-d", domain]

    # Uncomment if your md2conf requires it for local conversion:
    # cmd += ["-s", SPACE_KEY]

    print("Preconverting markdown to .csf via:", " ".join(cmd))
    subprocess.run(cmd, check=True)

def md_file_to_storage(md_path: Path) -> str:
    csf_path = md_path.with_suffix(".csf")
    if not csf_path.exists():
        raise RuntimeError(
            f"Missing CSF for {md_path}. "
            f"Expected {csf_path}. Ensure preconvert step ran successfully."
        )
    return csf_path.read_text(encoding="utf-8", errors="replace")

# -----------------------
# Images / Attachments
# -----------------------
def normalize_rel_path(rel: str) -> str:
    rel = rel.strip().strip('"').strip("'")
    if re.match(r"^[a-zA-Z]+://", rel) or rel.startswith("#") or rel.startswith("data:"):
        return ""
    return rel

def extract_local_images(md_path: Path) -> List[Path]:
    md_text = md_path.read_text(encoding="utf-8", errors="replace")
    rels = MD_IMAGE_RE.findall(md_text)
    found: List[Path] = []

    for rel in rels:
        rel_norm = normalize_rel_path(rel)
        if not rel_norm:
            continue
        candidate = (md_path.parent / rel_norm).resolve()

        # Only allow images within DOCS_DIR root
        try:
            candidate.relative_to(DOCS_DIR.resolve())
        except Exception:
            continue

        if candidate.exists() and candidate.is_file():
            found.append(candidate)

    # Deduplicate
    uniq = []
    seen = set()
    for p in found:
        if str(p) not in seen:
            uniq.append(p)
            seen.add(str(p))
    return uniq

def upload_attachment(page_id: str, file_path: Path):
    url = f"{API}/content/{page_id}/child/attachment"
    fname = file_path.name
    ctype = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"

    files = {"file": (fname, file_path.read_bytes(), ctype)}
    headers = dict(HEADERS_BIN)
    headers["X-Atlassian-Token"] = "no-check"  # required for attachment upload

    r = requests.post(url, headers=headers, files=files, timeout=120)
    if r.status_code == 401:
        raise RuntimeError(f"401 Unauthorized uploading attachment to page {page_id}. Check PAT permissions.")
    if not r.ok:
        raise RuntimeError(f"Attachment upload failed {r.status_code}: {r.text[:800]}")
    return r.json()

def rewrite_imgs_to_attachments(storage_html: str, uploaded_files: List[Path]) -> str:
    """
    Replace <img src="...something.../name.png"> with:
      <ac:image><ri:attachment ri:filename="name.png"/></ac:image>
    for any uploaded filename.
    """
    if not uploaded_files:
        return storage_html

    names = {p.name for p in uploaded_files}
    soup = BeautifulSoup(storage_html, "html.parser")

    for img in soup.find_all("img"):
        src = img.get("src", "")
        name = Path(src).name
        if name in names:
            ac_image = soup.new_tag("ac:image")
            ri_attach = soup.new_tag("ri:attachment")
            ri_attach.attrs["ri:filename"] = name
            ac_image.append(ri_attach)
            img.replace_with(ac_image)

    return str(soup)

def ensure_attachments_and_rewrite(page_id: str, md_path: Path, storage_html: str) -> str:
    imgs = extract_local_images(md_path)
    if not imgs:
        return storage_html

    for fp in imgs:
        upload_attachment(page_id, fp)

    return rewrite_imgs_to_attachments(storage_html, imgs)

# -----------------------
# Publish logic
# -----------------------
def publish_md(md_path: Path, parent_page_id: str) -> str:
    md_text = md_path.read_text(encoding="utf-8", errors="replace")
    title = md_title_from_file(md_path)
    pinned_id = extract_page_id(md_text)

    storage = md_file_to_storage(md_path)

    # If page id pinned, always update that page
    if pinned_id:
        existing = get_page(pinned_id, expand="version")
        page_id = existing["id"]
        current_version = int(existing["version"]["number"])

        storage2 = ensure_attachments_and_rewrite(page_id, md_path, storage)
        update_page(page_id, title, current_version + 1, storage2)
        print(f"Updated (pinned): {title} -> {page_id}")
        return page_id

    # Otherwise find/create under parent by title
    found = find_child_by_title(parent_page_id, title)
    if found:
        page_id = found["id"]
        existing = get_page(page_id, expand="version")
        current_version = int(existing["version"]["number"])

        storage2 = ensure_attachments_and_rewrite(page_id, md_path, storage)
        update_page(page_id, title, current_version + 1, storage2)
        print(f"Updated: {title} -> {page_id}")
        return page_id

    created = create_page(title, parent_page_id, storage)
    page_id = created["id"]
    # Attachments require a second update if we rewrite HTML.
    storage2 = ensure_attachments_and_rewrite(page_id, md_path, storage)
    existing = get_page(page_id, expand="version")
    current_version = int(existing["version"]["number"])
    update_page(page_id, title, current_version + 1, storage2)
    print(f"Created: {title} -> {page_id}")
    return page_id

def walk_tree(folder: Path, parent_page_id: str):
    """
    Folder -> Confluence page mapping:
    - folder/index.md (or README.md) becomes a folder page.
    - other .md files become children under the folder page.
    - subfolders recurse; assets/ is ignored.
    """
    index = None
    for name in ("index.md", "README.md"):
        p = folder / name
        if p.exists():
            index = p
            break

    folder_page_id = parent_page_id
    if index:
        folder_page_id = publish_md(index, parent_page_id)

    for md in sorted(folder.glob("*.md")):
        if md.name.lower() in ("index.md", "readme.md"):
            continue
        publish_md(md, folder_page_id)

    for sub in sorted([p for p in folder.iterdir() if p.is_dir()]):
        if sub.name.lower() == "assets":
            continue
        walk_tree(sub, folder_page_id)

def main():
    # Make DOCS_DIR relative to current working directory if needed
    if not DOCS_DIR.exists():
        raise SystemExit(f"Docs dir not found: {DOCS_DIR}")

    # Ensure root page exists / is accessible
    get_page(ROOT_PAGE_ID, expand="version")

    # Convert everything to CSF once (prevents "outside root path" image errors)
    preconvert_all_to_csf(DOCS_DIR)

    # Publish the tree
    walk_tree(DOCS_DIR, ROOT_PAGE_ID)
    print("Done.")

if __name__ == "__main__":
    main()
