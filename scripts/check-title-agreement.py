#!/usr/bin/env python3
"""Check that summary-table titles agree with their `## ID: title` headings.

Translated audit and review documents pair each `### ID: title` heading
with a summary-table row keyed by the same ID. This script anchors on the
ID - whichever column holds it - takes the title from the `Title`/`Tytul`
header column (or the column right after the ID when no such header
exists), and compares it with the heading text verbatim after link
stripping and whitespace normalization.

A mutated heading or table title reports one MISMATCH line; an ID present
on only one side reports MISSING-ROW or MISSING-HEADING. Exit code is 0
when no findings exist, 1 otherwise.

Run this file in place from the skill repository -
`python <skill-root>/scripts/check-title-agreement.py` - and copy it under
a `.tmp.` name into the working repository's `work/` directory only when
the skill root cannot be invoked, removing the copy afterward.

Usage:
    python check-title-agreement.py <file.md> [--verbose]
"""

import argparse
import re
import sys
from pathlib import Path

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
ID_TITLE = re.compile(r"^([A-Za-z][\w.-]*)\s*:\s*(.+?)\s*$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
TITLE_HEADERS = {"title", "tytul", "tytuł", "name", "nazwa"}
STRICT_ID = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$")


def reconfigure_stdio():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="backslashreplace")
        except Exception:
            pass


def fenced(lines):
    """Set of 0-based line indices inside fenced code blocks."""
    inside = set()
    open_idx = None
    for i, line in enumerate(lines):
        if FENCE.match(line):
            if open_idx is None:
                open_idx = i
            else:
                inside.update(range(open_idx, i + 1))
                open_idx = None
    return inside


def normalize_title(text, drop_links=False):
    """Strip markup so table cell and heading compare verbatim.

    Markdown links resolve to their inner text by default - a heading
    `Weak TLS configuration` matches a cell `Weak [TLS](...) configuration`.
    With `drop_links=True` links vanish entirely - a heading that omits the
    linked qualifier still matches. Backticks, `&#124;`, and emphasis
    markers normalize away, and whitespace collapses.
    """
    if drop_links:
        text = re.sub(r"\[([^\]]*)\]\([^)]*\)", "", text)
    else:
        text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("&#124;", "|").replace("`", "")
    text = re.sub(r"[*_~]", "", text)
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", text).strip()


def titles_match(table_title, heading_title):
    """Verbatim after normalization, under either link convention."""
    return (normalize_title(table_title) == normalize_title(heading_title)
            or normalize_title(table_title, drop_links=True)
            == normalize_title(heading_title, drop_links=True))


def split_row(line):
    """Cells of a table row, honoring escaped pipes."""
    body = line.strip().strip("|")
    cells = re.split(r"(?<!\\)\|", body)
    return [c.strip() for c in cells]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--verbose", action="store_true",
                        help="list every matched pair, not just findings")
    args = parser.parse_args()

    text = args.file.read_text(encoding="utf-8-sig")
    lines = text.split("\n")
    skip = fenced(lines)

    headings = {}
    for i, line in enumerate(lines):
        if i in skip:
            continue
        match = HEADING.match(line)
        if not match:
            continue
        pair = ID_TITLE.match(match.group(2).replace("`", ""))
        if pair:
            headings[pair.group(1)] = (i + 1, pair.group(2))

    rows = {}
    for i, line in enumerate(lines):
        if i in skip or not line.lstrip().startswith("|"):
            continue
        cells = split_row(line)
        if len(cells) < 2:
            continue
        id_idx = next(
            (j for j, c in enumerate(cells)
             if c.strip("`") in headings
             or STRICT_ID.match(c.strip("`"))), None)
        if id_idx is None:
            continue
        doc_id = cells[id_idx].strip("`")
        # Header row determines the title column when it names one;
        # otherwise the column right after the ID carries the title.
        header = None
        for back in range(i - 1, -1, -1):
            if back in skip or not lines[back].lstrip().startswith("|"):
                break
            header_cells = [c.strip().lower()
                            for c in split_row(lines[back])]
            if any(h in TITLE_HEADERS for h in header_cells):
                header = header_cells
                break
        title_idx = None
        if header:
            title_idx = next(
                (j for j, h in enumerate(header)
                 if h in TITLE_HEADERS), None)
        if title_idx is None:
            title_idx = id_idx + 1
        if title_idx < len(cells):
            rows.setdefault(doc_id, (i + 1, cells[title_idx]))

    print(f"check-title-agreement: {args.file}")
    findings = 0
    for doc_id, (hline, htitle) in sorted(headings.items()):
        if doc_id not in rows:
            print(f"MISSING-ROW {doc_id} - heading at line {hline} has no "
                  "summary-table row")
            findings += 1
            continue
        rline, rtitle = rows[doc_id]
        if not titles_match(rtitle, htitle):
            print(f"MISMATCH {doc_id} - table title '{rtitle[:70]}' "
                  f"(line {rline}) vs heading '{htitle[:70]}' "
                  f"(line {hline})")
            findings += 1
        elif args.verbose:
            print(f"OK {doc_id} - table line {rline}, "
                  f"heading line {hline}")
    for doc_id, (rline, rtitle) in sorted(rows.items()):
        if doc_id not in headings:
            print(f"MISSING-HEADING {doc_id} - table row at line {rline} "
                  f"('{rtitle[:60]}') has no `ID: title` heading")
            findings += 1

    print(f"check-title-agreement: {len(headings)} heading(s) checked, "
          f"{findings} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    reconfigure_stdio()
    sys.exit(main())
