import os
import re
import mimetypes
from pathlib import Path
import requests
from bs4 import BeautifulSoup

# ---- Config ----
BASE_URL = os.environ.get("CONF_BASE_URL", "").rstrip("/")
SPACE_KEY = os.environ.get("CONF_SPACE_KEY", "")
PAT = os.environ.get("CONF_PAT", "")
ROOT_PAGE_ID = os.environ.get("CONF_ROOT_PAGE_ID", "")
DOCS_DIR = Path(os.environ.get("CONF_DOCS_DIR", "MBSE_Style_Guide/confluence"))

if not (BASE_URL and SPACE_KEY and PAT and ROOT_PAGE_ID):
    raise SystemExit("Missing required env vars: CONF_BASE_URL, CONF_SPACE_KEY, CONF_PAT, CONF_ROOT_PAGE_ID")

API = f"{BASE_URL}/rest/api"

# ---- Auth (PAT as Bearer) ----
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

def request_json(method: str, url: str, **kwargs):
    r = requests.request(method, url, headers=HEADERS_JSON, timeout=30, **kwargs)
    if r.status_code == 401:
        raise RuntimeError(f"401 Unauthorized for {url}. Your PAT likely needs Bearer (we are using Bearer). Check PAT validity/permissions.")
    if not r.ok:
        raise RuntimeError(f"{r.status_code} {r.reason} for {url}: {r.text[:500]}")
    return r.json()

def get_page(page_id: str, expand="version,ancestors"):
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
    # Search children under a parent and match by title
    data = request_json("GET", f"{API}/content/{parent_id}/child/page", params={"limit": 200})
    for p in data.get("results", []):
        if p.get("title") == title:
            return p
    return None

def extract_page_id(md_text: str):
    m = PAGE_ID_RE.search(md_text)
    return m.group(1) if m else None

def md_title_from_file(md_path: Path):
    # Use first H1 if present; else file stem
    txt = md_path.read_text(encoding="utf-8")
    for line in txt.splitlines():
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()
    return md_path.stem

def md_to_storage(md_text: str) -> str:
    # Use markdown-to-confluence library converter
    # Package API differs by version; this import pattern works for the published project in most cases.
    from markdown_to_confluence import MarkdownToConfluence

    converter = MarkdownToConfluence()
    return converter.convert(md_text)

def normalize_rel_path(rel: str) -> str:
    rel = rel.strip().strip('"').strip("'")
    # ignore URLs and anchors
    if re.match(r"^[a-zA-Z]+://", rel) or rel.startswith("#"):
        return ""
    return rel

def upload_attachment(page_id: str, file_path: Path):
    # POST multipart/form-data to /child/attachment
    url = f"{API}/content/{page_id}/child/attachment"
    fname = file_path.name
    ctype = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"

    files = {
        "file": (fname, file_path.read_bytes(), ctype),
    }
    # Atlassian requires this header to bypass XSRF check on attachments:
    headers = dict(HEADERS_BIN)
    headers["X-Atlassian-Token"] = "no-check"

    r = requests.post(url, headers=headers, files=files, timeout=60)
    if r.status_code == 401:
        raise RuntimeError(f"401 uploading attachment to page {page_id}. Check PAT permissions.")
    if not r.ok:
        raise RuntimeError(f"Attachment upload failed {r.status_code}: {r.text[:500]}")
    return r.json()

def ensure_attachments(page_id: str, md_path: Path, storage_html: str) -> str:
    """
    Upload local images referenced in markdown (relative paths) as attachments,
    then rewrite <img src="..."> and Confluence storage image tags if needed.
    """
    md_text = md_path.read_text(encoding="utf-8")
    rels = MD_IMAGE_RE.findall(md_text)

    # Resolve referenced files relative to the md file
    to_upload = []
    for rel in rels:
        rel_norm = normalize_rel_path(rel)
        if not rel_norm:
            continue
        candidate = (md_path.parent / rel_norm).resolve()
        # Must be inside DOCS_DIR
        try:
            candidate.relative_to(DOCS_DIR.resolve())
        except Exception:
            continue
        if candidate.exists() and candidate.is_file():
            to_upload.append(candidate)

    if not to_upload:
        return storage_html

    # Upload each file as attachment
    for fp in sorted(set(to_upload)):
        upload_attachment(page_id, fp)

    # Rewrite img src to attachment reference (simple approach):
    # Confluence storage format commonly uses <ri:attachment ri:filename="..."/>
    # We'll replace <img ... src=".../file.png"...> with a Confluence image macro.
    soup = BeautifulSoup(storage_html, "html.parser")
    for img in soup.find_all("img"):
        src = img.get("src", "")
        name = Path(src).name
        if any(fp.name == name for fp in to_upload):
            # Replace <img> with Confluence storage image tag
            # <ac:image><ri:attachment ri:filename="file.png"/></ac:image>
            ac_image = soup.new_tag("ac:image")
            ri_attach = soup.new_tag("ri:attachment")
            ri_attach.attrs["ri:filename"] = name
            ac_image.append(ri_attach)
            img.replace_with(ac_image)

    return str(soup)

def publish_md(md_path: Path, parent_page_id: str):
    md_text = md_path.read_text(encoding="utf-8")
    title = md_title_from_file(md_path)
    pinned_id = extract_page_id(md_text)

    storage = md_to_storage(md_text)

    # Create/update page
    if pinned_id:
        existing = get_page(pinned_id, expand="version")
        page_id = existing["id"]
        current_version = int(existing["version"]["number"])
        storage2 = ensure_attachments(page_id, md_path, storage)
        updated = update_page(page_id, title, current_version + 1, storage2)
        return updated["id"]

    # otherwise find child by title under parent; if exists update; else create
    found = find_child_by_title(parent_page_id, title)
    if found:
        page_id = found["id"]
        existing = get_page(page_id, expand="version")
        current_version = int(existing["version"]["number"])
        storage2 = ensure_attachments(page_id, md_path, storage)
        updated = update_page(page_id, title, current_version + 1, storage2)
        return updated["id"]
    else:
        created = create_page(title, parent_page_id, storage)
        page_id = created["id"]
        storage2 = ensure_attachments(page_id, md_path, storage)
        # bump version once to include attachments if we rewrote anything
        existing = get_page(page_id, expand="version")
        current_version = int(existing["version"]["number"])
        update_page(page_id, title, current_version + 1, storage2)
        return page_id

def walk_tree(root: Path, root_page_id: str):
    """
    Folder -> page mapping:
    - If folder has index.md, that represents the folder page.
    - Children .md files become child pages.
    - Subfolders recurse; their index.md becomes child page under current folder page.
    """
    index = None
    for name in ("index.md", "README.md"):
        p = root / name
        if p.exists():
            index = p
            break

    # Determine the Confluence page id for this folder page:
    folder_page_id = root_page_id
    if index:
        folder_page_id = publish_md(index, root_page_id)

    # Publish markdown files (excluding index/readme)
    for md in sorted(root.glob("*.md")):
        if md.name.lower() in ("index.md", "readme.md"):
            continue
        publish_md(md, folder_page_id)

    # Recurse subfolders
    for sub in sorted([p for p in root.iterdir() if p.is_dir()]):
        # Skip assets folder (don’t publish as pages)
        if sub.name.lower() == "assets":
            continue
        walk_tree(sub, folder_page_id)

def main():
    if not DOCS_DIR.exists():
        raise SystemExit(f"Docs dir not found: {DOCS_DIR}")

    # Sanity check root page exists
    get_page(ROOT_PAGE_ID, expand="version")
    walk_tree(DOCS_DIR, ROOT_PAGE_ID)
    print("Done.")

if __name__ == "__main__":
    main()
