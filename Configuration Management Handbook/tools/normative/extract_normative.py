import re
import csv
from pathlib import Path

# Keywords to track (add others if you want, e.g., "REQUIRED", "RECOMMENDED")
KEYWORDS = ["SHALL", "MUST", "SHOULD", "MAY", "WILL"]

# Pattern A: "CM-REQ-001 (SHALL)" in the same line
PATTERN_ID_KEYWORD = re.compile(
    r"\b(?P<id>CM-REQ-\d{3,})\b.*?\(\s*(?P<kw>%s)\s*\)" % "|".join(KEYWORDS),
    re.IGNORECASE
)

# Pattern B: any line containing a keyword (for finding *untagged* normative language)
PATTERN_ANY_KEYWORD = re.compile(
    r"\b(?P<kw>%s)\b" % "|".join(KEYWORDS),
    re.IGNORECASE
)

def iter_markdown_files(root: Path):
    # Skip common build/cache/vendor dirs
    skip_dirs = {".git", ".github", "node_modules", "site", "dist", "build", ".venv", "__pycache__"}
    for p in root.rglob("*.md"):
        if any(part in skip_dirs for part in p.parts):
            continue
        yield p

def main():
    repo_root = Path(".").resolve()

    tagged = []
    untagged = []

    for md in iter_markdown_files(repo_root):
        lines = md.read_text(encoding="utf-8", errors="replace").splitlines()
        for i, line in enumerate(lines, start=1):
            # Tagged requirement lines
            m = PATTERN_ID_KEYWORD.search(line)
            if m:
                tagged.append({
                    "id": m.group("id").upper(),
                    "keyword": m.group("kw").upper(),
                    "file": md.as_posix(),
                    "line": i,
                    "text": line.strip(),
                })
                continue

            # Untagged normative language lines (contains SHALL/MUST/SHOULD/MAY/WILL)
            k = PATTERN_ANY_KEYWORD.search(line)
            if k:
                # ignore code fences and headings-only noise if you want; keep simple for now
                untagged.append({
                    "id": "",
                    "keyword": k.group("kw").upper(),
                    "file": md.as_posix(),
                    "line": i,
                    "text": line.strip(),
                })

    out_dir = repo_root / "governance"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Write CSV (tagged)
    csv_path = out_dir / "normative-register.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "keyword", "file", "line", "text"])
        w.writeheader()
        for row in sorted(tagged, key=lambda r: (r["id"], r["file"], r["line"])):
            w.writerow(row)

    # Write Markdown summary
    md_path = out_dir / "normative-register.md"
    with md_path.open("w", encoding="utf-8") as f:
        f.write("# Normative Language Register (Auto-Generated)\n\n")
        f.write("## Tagged requirements (CM-REQ-###)\n\n")
        if not tagged:
            f.write("_No tagged requirements found._\n\n")
        else:
            f.write("| ID | Keyword | File | Line | Text |\n")
            f.write("|---|---|---|---:|---|\n")
            for r in sorted(tagged, key=lambda r: (r["id"], r["file"], r["line"])):
                text = r["text"].replace("|", "\\|")
                f.write(f"| {r['id']} | {r['keyword']} | {r['file']} | {r['line']} | {text} |\n")

        f.write("\n## Untagged normative language (needs review)\n\n")
        f.write("These lines contain RFC-2119 keywords but are **not tagged** with a CM-REQ ID.\n\n")
        if not untagged:
            f.write("_No untagged normative language found._\n")
        else:
            f.write("| Keyword | File | Line | Text |\n")
            f.write("|---|---|---:|---|\n")
            for r in sorted(untagged, key=lambda r: (r["file"], r["line"])):
                text = r["text"].replace("|", "\\|")
                f.write(f"| {r['keyword']} | {r['file']} | {r['line']} | {text} |\n")

    print(f"Wrote: {csv_path}")
    print(f"Wrote: {md_path}")
    print(f"Tagged requirements: {len(tagged)}")
    print(f"Untagged keyword lines: {len(untagged)}")

if __name__ == "__main__":
    main()
