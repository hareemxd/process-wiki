import csv
import os
import re
from collections import defaultdict
from pathlib import Path

# --- CONFIG ---
# Column positions (1-based): A=1, B=2, C=3, D=4, E=5
COL_KEYWORD = 1
COL_FILE = 2
COL_LINE = 3
COL_TEXT = 4
COL_REQID = 5

REQID_RE = re.compile(r"\bCM-REQ-\d+\b", re.IGNORECASE)

def norm_path(p: str) -> Path:
    """
    Normalize a path from the CSV.
    - If it's absolute and exists, use it.
    - Else, try interpreting it relative to the current repo root.
    """
    p = p.strip().strip('"')
    candidate = Path(p)

    if candidate.is_absolute() and candidate.exists():
        return candidate

    # If CSV includes absolute paths from another machine, try to map by suffix
    # using just the tail relative to repo root.
    # Example: .../process-wiki/Configuration Management Handbook/... -> find that tail.
    return Path(p)

def apply_changes_to_file(file_path: Path, changes: list[dict]) -> list[str]:
    """
    Apply tag edits to one file.
    Changes must be sorted in descending line order.
    Returns a list of status messages.
    """
    statuses = []

    if not file_path.exists():
        statuses.append(f"SKIP (missing file): {file_path}")
        return statuses

    lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()

    for ch in changes:
        line_no = ch["line_no"]
        keyword = ch["keyword"]
        reqid = ch["reqid"]

        if line_no < 1 or line_no > len(lines):
            statuses.append(f"SKIP (bad line {line_no}): {file_path}")
            continue

        idx = line_no - 1
        original = lines[idx]

        # Already tagged with a CM-REQ id somewhere on the line? skip.
        if REQID_RE.search(original):
            statuses.append(f"OK (already tagged) {file_path}:{line_no}")
            continue

        tag = f"<!-- {reqid} | {keyword} -->"

        # If the exact tag already exists, skip
        if tag in original:
            statuses.append(f"OK (tag already present) {file_path}:{line_no}")
            continue

        # Append tag with a preceding space (keeps markdown readable)
        lines[idx] = original.rstrip() + " " + tag
        statuses.append(f"UPDATED {file_path}:{line_no} ({reqid})")

    file_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return statuses

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Apply CM-REQ tags to markdown files from a register CSV (Requirement ID in column E)."
    )
    parser.add_argument(
        "csv_path",
        help="Path to the register CSV copy (pipe/real CSV export). Requirement ID must be in column E."
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repo root to resolve relative paths (default: current directory)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without editing files."
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    csv_path = Path(args.csv_path).resolve()

    if not csv_path.exists():
        raise SystemExit(f"CSV not found: {csv_path}")

    # Read rows and group by file
    by_file = defaultdict(list)
    total_rows = 0
    usable_rows = 0

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            total_rows += 1
            if not row or len(row) < COL_REQID:
                continue

            # Skip header rows
            if total_rows == 1 and "Keyword" in row[0]:
                continue

            keyword = row[COL_KEYWORD - 1].strip().upper()
            file_raw = row[COL_FILE - 1].strip()
            line_raw = row[COL_LINE - 1].strip()
            reqid = row[COL_REQID - 1].strip().upper()

            # Only apply rows that have a requirement ID filled in
            if not reqid:
                continue

            if not re.match(r"^CM-REQ-\d+$", reqid, re.IGNORECASE):
                # Allow you to catch typos early
                print(f"SKIP (bad reqid '{reqid}') row {total_rows}")
                continue

            try:
                line_no = int(line_raw)
            except ValueError:
                print(f"SKIP (bad line '{line_raw}') row {total_rows}")
                continue

            file_path = norm_path(file_raw)
            # If it’s a relative path, resolve against repo root
            if not file_path.is_absolute():
                file_path = (repo_root / file_path).resolve()

            by_file[file_path].append({
                "keyword": keyword,
                "line_no": line_no,
                "reqid": reqid,
                "text": row[COL_TEXT - 1].strip() if len(row) >= COL_TEXT else "",
            })
            usable_rows += 1

    print(f"Rows read: {total_rows}")
    print(f"Rows with ReqID in col E: {usable_rows}")
    print(f"Files to edit: {len(by_file)}")

    all_status = []

    for file_path, changes in by_file.items():
        # Sort descending line number to avoid drift issues if you later expand to multi-line edits
        changes.sort(key=lambda c: c["line_no"], reverse=True)

        if args.dry_run:
            for ch in changes:
                all_status.append(f"DRYRUN would tag {file_path}:{ch['line_no']} as {ch['reqid']} | {ch['keyword']}")
            continue

        statuses = apply_changes_to_file(file_path, changes)
        all_status.extend(statuses)

    # Print summary
    updated = sum(1 for s in all_status if s.startswith("UPDATED"))
    skipped = sum(1 for s in all_status if s.startswith("SKIP"))
    ok = sum(1 for s in all_status if s.startswith("OK"))

    print("\n--- Summary ---")
    print(f"UPDATED: {updated}")
    print(f"OK:      {ok}")
    print(f"SKIP:    {skipped}")

    # Write a report you can attach to a PR
    report_path = repo_root / "governance" / "tag-apply-report.txt"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(all_status) + "\n", encoding="utf-8")
    print(f"\nWrote report: {report_path}")

if __name__ == "__main__":
    main()
