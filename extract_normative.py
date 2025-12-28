#!/usr/bin/env python3
"""
Extract normative statements (shall/should/must/may/needs to) from a PDF into CSV.

Default input:
  /mnt/data/mil-hdbk-61b.pdf

Output columns:
  file, page, keywords, statement
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

# --- Keyword patterns (case-insensitive) ---
# Word-boundaries avoid matching "may" inside "maybe", etc.
NORMATIVE_PATTERNS = {
    "shall": re.compile(r"\bshall\b", re.IGNORECASE),
    "should": re.compile(r"\bshould\b", re.IGNORECASE),
    "must": re.compile(r"\bmust\b", re.IGNORECASE),
    "may": re.compile(r"\bmay\b", re.IGNORECASE),
    "needs to": re.compile(r"\bneeds\s+to\b", re.IGNORECASE),
}

# Simple sentence-ish splitter:
# Splits on . ? ! followed by whitespace/newline, but tries not to split on common abbrevs.
# This is not perfect, but works well enough for most standards/handbooks.
SENTENCE_SPLIT_RE = re.compile(
    r"""
    (?<!\b(?:e|i)\.g)      # not e.g
    (?<!\b(?:i)\.e)        # not i.e
    (?<!\bvs)              # not vs.
    (?<!\bMr)
    (?<!\bMs)
    (?<!\bDr)
    (?<!\bNo)              # not No.
    (?<!\bRev)             # not Rev.
    (?<!\bFig)             # not Fig.
    (?<!\bEq)              # not Eq.
    (?<!\bSec)             # not Sec.
    (?<=[.!?])             # end punctuation
    \s+                    # whitespace
    """,
    re.IGNORECASE | re.VERBOSE,
)


def extract_text_by_page(pdf_path: Path) -> list[tuple[int, str]]:
    """
    Returns a list of (page_number_1_based, text).
    Uses pdfplumber if available; falls back to pypdf.
    """
    pages: list[tuple[int, str]] = []

    try:
        import pdfplumber  # type: ignore
    except Exception:
        pdfplumber = None

    if pdfplumber is not None:
        with pdfplumber.open(str(pdf_path)) as pdf:
            for i, page in enumerate(pdf.pages, start=1):
                text = page.extract_text() or ""
                pages.append((i, text))
        return pages

    # Fallback: pypdf
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception as e:
        raise RuntimeError(
            "Neither pdfplumber nor pypdf is available. Install one:\n"
            "  pip install pdfplumber\n"
            "or\n"
            "  pip install pypdf"
        ) from e

    reader = PdfReader(str(pdf_path))
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        pages.append((i, text))
    return pages


def normalize_pdf_text(text: str) -> str:
    """
    Normalize common PDF extraction artifacts:
    - fix hyphenation across line breaks: "re-\nquire" -> "require"
    - collapse repeated whitespace
    """
    # Fix hyphenated line breaks
    text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)

    # Turn newlines into spaces (keep some structure but avoid mid-sentence breaks)
    text = re.sub(r"\s*\n+\s*", " ", text)

    # Collapse whitespace
    text = re.sub(r"\s{2,}", " ", text).strip()
    return text


def split_into_statements(text: str) -> list[str]:
    """
    Split normalized text into sentence-like statements.
    Also splits on semicolons if they produce very long sentences.
    """
    if not text:
        return []

    # First pass: sentence-ish split
    parts = SENTENCE_SPLIT_RE.split(text)

    statements: list[str] = []
    for p in parts:
        p = p.strip()
        if not p:
            continue

        # If a statement is extremely long, further split on semicolons
        if len(p) > 450 and ";" in p:
            subparts = [s.strip() for s in p.split(";") if s.strip()]
            statements.extend(subparts)
        else:
            statements.append(p)

    return statements


def find_normative_keywords(statement: str) -> list[str]:
    hits = []
    for name, pat in NORMATIVE_PATTERNS.items():
        if pat.search(statement):
            hits.append(name)
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description="Extract normative statements from a PDF into CSV.")
    ap.add_argument(
        "--pdf",
        default="/mnt/data/mil-hdbk-61b.pdf",
        help="Path to the input PDF (default: /mnt/data/mil-hdbk-61b.pdf)",
    )
    ap.add_argument(
        "--out",
        default="mil-hdbk-61b_normative_statements.csv",
        help="Output CSV filename (default: mil-hdbk-61b_normative_statements.csv)",
    )
    ap.add_argument(
        "--min-len",
        type=int,
        default=20,
        help="Ignore statements shorter than this many chars (default: 20)",
    )
    ap.add_argument(
        "--dedupe",
        action="store_true",
        help="Dedupe identical statements across pages (useful if headers/footers get picked up)",
    )
    args = ap.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        print(f"ERROR: PDF not found: {pdf_path}", file=sys.stderr)
        return 2

    pages = extract_text_by_page(pdf_path)

    rows: list[dict[str, str]] = []
    seen: set[str] = set()

    for page_num, raw_text in pages:
        norm_text = normalize_pdf_text(raw_text)
        statements = split_into_statements(norm_text)

        for st in statements:
            st_clean = st.strip()

            if len(st_clean) < args.min_len:
                continue

            hits = find_normative_keywords(st_clean)
            if not hits:
                continue

            # Optional dedupe (normalize a little more for comparison)
            if args.dedupe:
                key = re.sub(r"\s+", " ", st_clean).strip().lower()
                if key in seen:
                    continue
                seen.add(key)

            rows.append(
                {
                    "file": str(pdf_path.name),
                    "page": str(page_num),
                    "keywords": ", ".join(hits),
                    "statement": st_clean,
                }
            )

    out_path = Path(args.out)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["file", "page", "keywords", "statement"])
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {len(rows)} normative statements to: {out_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
