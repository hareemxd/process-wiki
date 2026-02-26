#!/usr/bin/env python3
"""
publish_confluence.py

Confluence Data Center publisher for a Markdown tree.

What it does:
- Runs md2conf once on the docs root in --local mode to generate .csf files (storage XHTML).
- Publishes folder -> Confluence page tree using index.md / README.md as folder pages.
- Uses YAML front matter key `title:` (if present) for page title; else first H1; else filename.
- Honors pinned Confluence page IDs via: <!-- confluence-page-id: 123456 -->
- Uploads images referenced by each Markdown file as attachments to THAT page.
  If an attachment with the same filename already exists on the page, it UPDATES it (new version).
- Rewrites <img> tags in CSF into <ac:image><ri:attachment .../></ac:image> for uploaded filenames.

Required env vars:
  CONF_BASE_URL        e.g. http://dal1vacon01p:8090
  CONF_SPACE_KEY       e.g. GEP
  CONF_PAT             Confluence PAT
  CONF_ROOT_PAGE_ID    e.g. 119668755

Optional env vars:
  CONF_DOCS_DIR        default: confluence
  CONF_CLEAN_CSF       if "1", deletes existing .csf files under docs root before conversion
"""

import os
import re
import mimetypes
import subprocess
import urllib.parse
from pathlib import Path
from typing import Optional, List, Dict, Tuple

import requests
from bs4 import BeautifulSoup
import frontmatter

# -----------------------
# Config / Environment
# -----------------------
BASE_URL = os.environ.get("CONF_BASE_URL", "").rstrip("/")
SPACE_KEY = os.environ.get("CONF_SPACE_KEY", "")
PAT = os.environ.get("CONF_PAT", "")
ROOT_PAGE_ID = os.environ.get("CONF_ROOT_PAGE_ID", "")
DOCS_DIR = Path(os.environ.get("CONF_DOCS_DIR", "confluence"))
CLEAN_CSF = os.environ.get("CONF_CLEAN_CSF", "0") == "1"

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
# basic Markdown image syntax ![alt](path "title")
MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

# -----------------------
# HTTP helpers
# -----------------------
def request_json(method: str, url: str, **kwargs):
    r = requests.request(method, url, headers=HEADERS_JSON, timeout=60, **kwargs)
    if r.status_code == 401:
        raise RuntimeError(
            f"401 Unauthorized for {url}. Your PAT may be invalid/expired or missing permissions."
        )
    if not r.ok:
        raise RuntimeError(f"{r.status_code} {r.reason} for {url}: {r.text[:1200]}")
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
# Markdown parsing
# -----------------------
def extract_page_id(md_text: str) -> Optional[str]:
    m = PAGE_ID_RE.search(md_text)
    return m.group(1) if m else None

def title_from_yaml_or_h1_or_filename(md_path: Path) -> str:
    raw = md_path.read_text(encoding="utf-8", errors="replace")
    post = frontmatter.loads(raw)

    # YAML front matter `title:`
    t = post.metadata.get("title")
    if isinstance(t, str) and t.strip():
        return t.strip()

    # First H1
    for line in post.content.splitlines():
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()

    return md_path.stem

# -----------------------
# md2conf local conversion
# -----------------------
def parse_domain_for_md2conf() -> str:
    parsed = urllib.parse.urlparse(BASE_URL)
    return parsed.netloc or parsed.path

def clean_csf_files(root: Path):
    for csf in root.rglob("*.csf"):
        try:
            csf.unlink()
        except Exception:
            pass

def preconvert_all_to_csf(docs_dir: Path):
    """
    Run md2conf ONCE on docs root in --local mode so cross-folder references
    like Work Instructions/../assets stay inside root.
    """
    if CLEAN_CSF:
        clean_csf_files(docs_dir)

    domain = parse_domain_for_md2conf()
    cmd = ["python", "-m", "md2conf", str(docs_dir), "--local", "-d", domain]

    # Some builds require a space key even in local mode; if yours errors, uncomment:
    # cmd += ["-s", SPACE_KEY]

    print("Preconverting markdown to .csf via:", " ".join(cmd))
    subprocess.run(cmd, check=True)

def md_file_to_storage(md_path: Path) -> str:
    csf_path = md_path.with_suffix(".csf")
    if not csf_path.exists():
        raise RuntimeError(
            f"Missing CSF for {md_path}. Expected {csf_path}. "
            "Ensure preconvert step ran successfully."
        )
    return csf_path.read_text(encoding="utf-8", errors="replace")

# -----------------------
# Images / attachments
# -----------------------
def normalize_rel_path(rel: str) -> str:
    rel = rel.strip().strip('"').strip("'")
    if re.match(r"^[a-zA-Z]+://", rel) or rel.startswith("#") or rel.startswith("data:"):
        return ""
    return rel

def extract_local_images(md_path: Path, docs_root: Path) -> List[Path]:
    raw = md_path.read_text(encoding="utf-8", errors="replace")
    rels = MD_IMAGE_RE.findall(raw)

    found: List[Path] = []
    root_resolved = docs_root.resolve()

    for rel in rels:
        rel_norm = normalize_rel_path(rel)
        if not rel_norm:
            continue

        candidate = (md_path.parent / rel_norm).resolve()

        # only allow images inside docs root
        try:
            candidate.relative_to(root_resolved)
        except Exception:
            continue

        if candidate.exists() and candidate.is_file():
            found.append(candidate)

    # dedupe
    uniq, seen = [], set()
    for p in found:
        if p not in seen:
            uniq.append(p)
            seen.add(p)
    return uniq

def list_attachments_by_filename(page_id: str) -> Dict[str, str]:
    """
    Returns filename -> attachmentId for attachments directly under this page.
    """
    out: Dict[str, str] = {}
    start = 0
    limit = 200

    while True:
        data = request_json(
            "GET",
            f"{API}/content/{page_id}/child/attachment",
            params={"limit": limit, "start": start},
        )
        for a in data.get("results", []):
            title = a.get("title")
            aid = a.get("id")
            if title and aid:
                out[title] = aid

        size = data.get("size", 0)
        if size < limit:
            break
        start += limit

    return out

def upload_new_attachment(page_id: str, file_path: Path):
    url = f"{API}/content/{page_id}/child/attachment"
    fname = file_path.name
    ctype = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"

    files = {"file": (fname, file_path.read_bytes(), ctype)}
    headers = dict(HEADERS_BIN)
    headers["X-Atlassian-Token"] = "no-check"

    r = requests.post(url, headers=headers, files=files, timeout=120)
    if r.status_code == 401:
        raise RuntimeError(f"401 Unauthorized uploading attachment to page {page_id}. Check PAT permissions.")
    if not r.ok:
        raise RuntimeError(f"Attachment upload failed {r.status_code}: {r.text[:1200]}")
    return r.json()

def update_existing_attachment(page_id: str, attachment_id: str, file_path: Path):
    """
    Uploads a new version of an existing attachment.
    """
    url = f"{API}/content/{page_id}/child/attachment/{attachment_id}/data"
    fname = file_path.name
    ctype = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"

    files = {"file": (fname, file_path.read_bytes(), ctype)}
    headers = dict(HEADERS_BIN)
    headers["X-Atlassian-Token"] = "no-check"

    r = requests.post(url, headers=headers, files=files, timeout=120)
    if r.status_code == 401:
        raise RuntimeError(f"401 Unauthorized updating attachment on page {page_id}. Check PAT permissions.")
    if not r.ok:
        raise RuntimeError(f"Attachment update failed {r.status_code}: {r.text[:1200]}")
    return r.json()

def upsert_attachment_by_filename(page_id: str, file_path: Path, existing: Dict[str, str]):
    """
    If filename exists on the page, upload a new version. Else create new attachment.
    Updates `existing` mapping in-place.
    """
    fname = file_path.name
    if fname in existing:
        update_existing_attachment(page_id, existing[fname], file_path)
    else:
        resp = upload_new_attachment(page_id, file_path)
        # response structure: results[0].id etc. Be defensive.
        try:
            new_id = resp["results"][0]["id"]
            existing[fname] = new_id
        except Exception:
            # fallback: refresh mapping if parsing failed
            existing.update(list_attachments_by_filename(page_id))

def rewrite_imgs_to_attachments(storage_html: str, uploaded_files: List[Path]) -> str:
    """
    Replace <img src=".../name.png"> with:
      <ac:image><ri:attachment ri:filename="name.png"/></ac:image>
    Only for filenames we uploaded (or upserted) for this page.
    """
    if not uploaded_files:
        return storage_html

    names = {p.name for p in uploaded_files}
    soup = BeautifulSoup(storage_html, "html.parser")

    # Leave existing <ac:image> blocks alone. Only rewrite literal <img>.
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
    imgs = extract_local_images(md_path, DOCS_DIR)
    if not imgs:
        return storage_html

    existing = list_attachments_by_filename(page_id)
    for fp in imgs:
        upsert_attachment_by_filename(page_id, fp, existing)

    return rewrite_imgs_to_attachments(storage_html, imgs)

# -----------------------
# Publish logic
# -----------------------
def publish_md(md_path: Path, parent_page_id: str) -> str:
    md_text = md_path.read_text(encoding="utf-8", errors="replace")
    title = title_from_yaml_or_h1_or_filename(md_path)
    pinned_id = extract_page_id(md_text)

    storage = md_file_to_storage(md_path)

    # pinned page id -> always update that page
    if pinned_id:
        existing_page = get_page(pinned_id, expand="version")
        page_id = existing_page["id"]
        current_version = int(existing_page["version"]["number"])

        storage2 = ensure_attachments_and_rewrite(page_id, md_path, storage)
        update_page(page_id, title, current_version + 1, storage2)
        print(f"Updated (pinned): {title} -> {page_id}")
        return page_id

    # find by title under parent, else create
    found = find_child_by_title(parent_page_id, title)
    if found:
        page_id = found["id"]
        existing_page = get_page(page_id, expand="version")
        current_version = int(existing_page["version"]["number"])

        storage2 = ensure_attachments_and_rewrite(page_id, md_path, storage)
        update_page(page_id, title, current_version + 1, storage2)
        print(f"Updated: {title} -> {page_id}")
        return page_id

    created = create_page(title, parent_page_id, storage)
    page_id = created["id"]

    # if we uploaded attachments and rewrote html, bump version once
    storage2 = ensure_attachments_and_rewrite(page_id, md_path, storage)
    existing_page = get_page(page_id, expand="version")
    current_version = int(existing_page["version"]["number"])
    update_page(page_id, title, current_version + 1, storage2)

    print(f"Created: {title} -> {page_id}")
    return page_id

def walk_tree(folder: Path, parent_page_id: str):
    """
    Folder -> Confluence tree:
    - folder/index.md (or README.md) becomes a folder page.
    - other .md files become children under the folder page.
    - recurse into subfolders; ignore assets/.
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
    if not DOCS_DIR.exists():
        raise SystemExit(f"Docs dir not found: {DOCS_DIR}")

    # Ensure root page exists / accessible
    get_page(ROOT_PAGE_ID, expand="version")

    # Convert everything to CSF once
    preconvert_all_to_csf(DOCS_DIR)

    # Publish the tree
    walk_tree(DOCS_DIR, ROOT_PAGE_ID)
    print("Done.")

if __name__ == "__main__":
    main()
