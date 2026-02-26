#!/usr/bin/env python3
"""
publish_confluence.py

Publishes a Markdown directory tree to Confluence Data Center.

Key behaviors:
- Runs md2conf once on the docs root in --local mode to generate .csf files.
- Folder -> Confluence page tree using index.md / README.md as folder pages.
- Page title resolution:
  1) YAML front matter: title:
  2) first H1 (# ...)
  3) filename stem
- Honors pinned Confluence page IDs via: <!-- confluence-page-id: 123456 -->

Images/attachments:
- md2conf CSF may reference images as:
    <ri:attachment ri:filename="PAR_assets_MBSE_peerreviewmetamodel.png"/>
  but your Confluence stores attachments with the original filename:
    peerreviewmetamodel.png
- Therefore this script:
  1) uploads/updates attachments using the REAL basename (peerreviewmetamodel.png)
  2) rewrites CSF so ri:filename values become basenames (strips PAR_ prefixes and any path)

Required env vars:
  CONF_BASE_URL        e.g. http://dal1vacon01p:8090
  CONF_SPACE_KEY       e.g. GEP
  CONF_PAT             Confluence PAT (Bearer)
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
from typing import Optional, List, Dict

import requests
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

# Markdown image: ![alt](path "optional title")
MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

# CSF attachment references: <ri:attachment ri:filename="...">
RI_ATTACH_RE = re.compile(
    r"""(<ri:attachment\b[^>]*\bri:filename\s*=\s*['"])([^'"]+)(['"][^>]*/?>)""",
    re.IGNORECASE,
)

# Some CSFs may also use <ri:url ri:value="..."> inside <ac:image>
RI_URL_RE = re.compile(
    r"""(<ri:url\b[^>]*\bri:value\s*=\s*['"])([^'"]+)(['"][^>]*/?>)""",
    re.IGNORECASE,
)

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
        raise RuntimeError(f"{r.status_code} {r.reason} for {url}: {r.text[:1500]}")
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

    t = post.metadata.get("title")
    if isinstance(t, str) and t.strip():
        return t.strip()

    for line in post.content.splitlines():
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()

    return md_path.stem

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

        # Only allow images inside docs root
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

# -----------------------
# md2conf local conversion
# -----------------------
def parse_domain_for_md2conf() -> str:
    parsed = urllib.parse.urlparse(BASE_URL)
    return parsed.netloc or parsed.path  # host[:port]

def clean_csf_files(root: Path):
    for csf in root.rglob("*.csf"):
        try:
            csf.unlink()
        except Exception:
            pass

def preconvert_all_to_csf(docs_dir: Path):
    if CLEAN_CSF:
        clean_csf_files(docs_dir)

    domain = parse_domain_for_md2conf()
    cmd = ["python", "-m", "md2conf", str(docs_dir), "--local", "-d", domain]

    # If your md2conf build complains that space isn't specified even in local mode:
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
# CSF normalization (strip PAR_ / paths to basenames)
# -----------------------
def _basename(s: str) -> str:
    # strip query/fragment, normalize slashes
    s = s.split("?", 1)[0].split("#", 1)[0].replace("\\", "/")
    return Path(s).name

def normalize_csf_image_refs_to_basenames(storage_html: str) -> str:
    """
    Rewrite CSF so any ri:attachment or ri:url filename/value becomes basename-only.
    This fixes "unknown attachment" when Confluence stores attachments under the real filename.
    """

    def repl_attach(m: re.Match) -> str:
        prefix, val, suffix = m.group(1), m.group(2), m.group(3)
        return f"{prefix}{_basename(val)}{suffix}"

    def repl_url(m: re.Match) -> str:
        prefix, val, suffix = m.group(1), m.group(2), m.group(3)
        return f"{prefix}{_basename(val)}{suffix}"

    out = RI_ATTACH_RE.sub(repl_attach, storage_html)
    out = RI_URL_RE.sub(repl_url, out)
    return out

# -----------------------
# Attachments (upsert by REAL basename)
# -----------------------
def list_attachments_by_filename(page_id: str) -> Dict[str, str]:
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
        raise RuntimeError(f"401 Unauthorized uploading attachment to page {page_id}.")
    if not r.ok:
        raise RuntimeError(f"Attachment upload failed {r.status_code}: {r.text[:1500]}")
    return r.json()

def update_existing_attachment(page_id: str, attachment_id: str, file_path: Path):
    url = f"{API}/content/{page_id}/child/attachment/{attachment_id}/data"
    fname = file_path.name
    ctype = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"

    files = {"file": (fname, file_path.read_bytes(), ctype)}
    headers = dict(HEADERS_BIN)
    headers["X-Atlassian-Token"] = "no-check"

    r = requests.post(url, headers=headers, files=files, timeout=120)
    if r.status_code == 401:
        raise RuntimeError(f"401 Unauthorized updating attachment on page {page_id}.")
    if not r.ok:
        raise RuntimeError(f"Attachment update failed {r.status_code}: {r.text[:1500]}")
    return r.json()

def upsert_attachment(page_id: str, file_path: Path, existing: Dict[str, str]):
    fname = file_path.name
    if fname in existing:
        update_existing_attachment(page_id, existing[fname], file_path)
    else:
        resp = upload_new_attachment(page_id, file_path)
        try:
            new_id = resp["results"][0]["id"]
            existing[fname] = new_id
        except Exception:
            existing.update(list_attachments_by_filename(page_id))

def ensure_attachments_present(page_id: str, md_path: Path):
    imgs = extract_local_images(md_path, DOCS_DIR)
    if not imgs:
        return
    existing = list_attachments_by_filename(page_id)
    for fp in imgs:
        upsert_attachment(page_id, fp, existing)

# -----------------------
# Publish logic
# -----------------------
def publish_md(md_path: Path, parent_page_id: str) -> str:
    md_text = md_path.read_text(encoding="utf-8", errors="replace")
    title = title_from_yaml_or_h1_or_filename(md_path)
    pinned_id = extract_page_id(md_text)

    storage = md_file_to_storage(md_path)
    storage = normalize_csf_image_refs_to_basenames(storage)

    if pinned_id:
        existing_page = get_page(pinned_id, expand="version")
        page_id = existing_page["id"]
        current_version = int(existing_page["version"]["number"])

        # Upload/update attachments by real basename
        ensure_attachments_present(page_id, md_path)

        update_page(page_id, title, current_version + 1, storage)
        print(f"Updated (pinned): {title} -> {page_id}")
        return page_id

    found = find_child_by_title(parent_page_id, title)
    if found:
        page_id = found["id"]
        existing_page = get_page(page_id, expand="version")
        current_version = int(existing_page["version"]["number"])

        ensure_attachments_present(page_id, md_path)
        update_page(page_id, title, current_version + 1, storage)

        print(f"Updated: {title} -> {page_id}")
        return page_id

    created = create_page(title, parent_page_id, storage)
    page_id = created["id"]

    ensure_attachments_present(page_id, md_path)

    # bump version once (keeps consistent history)
    existing_page = get_page(page_id, expand="version")
    current_version = int(existing_page["version"]["number"])
    update_page(page_id, title, current_version + 1, storage)

    print(f"Created: {title} -> {page_id}")
    return page_id

def walk_tree(folder: Path, parent_page_id: str):
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

    get_page(ROOT_PAGE_ID, expand="version")
    preconvert_all_to_csf(DOCS_DIR)
    walk_tree(DOCS_DIR, ROOT_PAGE_ID)
    print("Done.")

if __name__ == "__main__":
    main()
