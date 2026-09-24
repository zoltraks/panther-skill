#!/usr/bin/env python3
"""Check `## Contents` table line numbers against actual `## ` section positions.

Scope:
  - Every Markdown file carrying a `## Contents` or `## Spis treści` section is
    checked: each row's stated line number must sit within `--tolerance` lines of a
    document-level `## ` heading.
  - Fenced code blocks are opaque: example tables and headings inside fences, such
    as the ` ```markdown ` sample in `STYLE.md`, are payload, not structure.
  - Matching is positional, not by section name: row labels are abbreviated (for
    example "How To Use" stands for "How To Use This Skill"), so only the stated
    line numbers are verified.

Payload files under `templates/` and `docs/` are example artifacts, and `work/`
holds scratch material - none of them are rule documents, so they are not scanned.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


FENCE = re.compile(r"^[ ]{0,3}(```+|~~~+)")
HEADING = re.compile(r"^## ")
CONTENTS_HEADING = re.compile(r"^## (Contents|Spis treści)\s*$")
TABLE_ROW = re.compile(r"^\|")
LINE_COLUMNS = {"line", "wiersz"}

EXCLUDED_DIRS = ("docs", "templates", "work")


def document_lines(text: str) -> list[tuple[int, str]]:
    """Return (line_number, line) pairs outside fenced code blocks."""
    pairs: list[tuple[int, str]] = []
    fenced = False
    fence_char = ""
    fence_length = 0
    for number, line in enumerate(text.splitlines(), start=1):
        match = FENCE.match(line)
        if fenced:
            if match and match.group(1)[0] == fence_char and len(match.group(1)) >= fence_length:
                fenced = False
            continue
        if match:
            fenced = True
            fence_char = match.group(1)[0]
            fence_length = len(match.group(1))
            continue
        pairs.append((number, line))
    return pairs


def cells(row: str) -> list[str]:
    return [cell.strip() for cell in row.split("|")[1:-1]]


def contents_tables(lines: list[tuple[int, str]]) -> list[list[tuple[int, str]]]:
    """Return the row lists of every table directly under a Contents heading."""
    tables: list[list[tuple[int, str]]] = []
    for index, (_, line) in enumerate(lines):
        if not CONTENTS_HEADING.match(line):
            continue
        cursor = index + 1
        while cursor < len(lines) and not lines[cursor][1].strip():
            cursor += 1
        rows: list[tuple[int, str]] = []
        while cursor < len(lines) and TABLE_ROW.match(lines[cursor][1]):
            rows.append(lines[cursor])
            cursor += 1
        if len(rows) >= 3:
            tables.append(rows)
    return tables


def check_file(source: Path, label: str, tolerance: int, issues: list[str]) -> bool:
    try:
        text = source.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        issues.append(f"{label}: file is not UTF-8")
        return False

    lines = document_lines(text)
    heading_lines = [number for number, line in lines if HEADING.match(line)]
    tables = contents_tables(lines)
    if not tables:
        return False

    for rows in tables:
        header = cells(rows[0][1])
        column = 1
        for position, name in enumerate(header):
            if name.lower() in LINE_COLUMNS:
                column = position
                break
        for row_number, row in rows[2:]:
            row_cells = cells(row)
            if len(row_cells) <= column:
                issues.append(f"{label}:{row_number}: contents row has no line column: {row}")
                continue
            stated = row_cells[column]
            if not stated.isdigit():
                issues.append(
                    f"{label}:{row_number}: contents row has no numeric line: {row_cells[0]}"
                )
                continue
            target = int(stated)
            if not heading_lines:
                issues.append(
                    f"{label}:{row_number}: contents entry '{row_cells[0]}' points at line "
                    f"{target} but the file has no `## ` sections"
                )
                continue
            nearest = min(heading_lines, key=lambda heading: abs(heading - target))
            if abs(nearest - target) > tolerance:
                issues.append(
                    f"{label}:{row_number}: contents entry '{row_cells[0]}' points at line "
                    f"{target}, nearest `## ` section is at line {nearest}"
                )
    return True


def main() -> int:
    paths: list[str] = []
    tolerance = 3
    iterator = iter(sys.argv[1:])
    for argument in iterator:
        if argument == "--tolerance":
            tolerance = int(next(iterator))
        elif argument.startswith("--tolerance="):
            tolerance = int(argument.split("=", 1)[1])
        else:
            paths.append(argument)

    if len(paths) != 1:
        print("Usage: python tools/check-contents.py <file-or-directory> [--tolerance N]")
        return 1

    target = Path(paths[0]).resolve()
    if target.is_file():
        sources = [target]
        root = target.parent
    elif target.is_dir():
        sources = sorted(target.rglob("*.md"))
        root = target
    else:
        print(f"FAIL path does not exist: {target}")
        return 1

    issues: list[str] = []
    checked = 0
    for source in sources:
        relative = source.relative_to(root)
        if relative.parts[0] in EXCLUDED_DIRS or relative.parts[0].startswith("."):
            continue
        if check_file(source, str(relative), tolerance, issues):
            checked += 1

    if issues:
        for message in issues:
            print(f"FAIL {message}")
        print(f"{len(issues)} issue(s) found")
        return 1

    print(f"PASS {checked} contents table(s) verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
