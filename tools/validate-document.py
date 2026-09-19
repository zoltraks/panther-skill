#!/usr/bin/env python3
"""Mechanical style checker for Markdown documents produced by this skill.

Covers the scriptable items of process/document-checklist.md: structure,
spacing, characters, lists, code fences, and table alignment.

Copy this file into the working repository's `work/` directory (or the
repository root when no `work/` exists) as `validate-document.tmp.py`, run it
on the document file, then remove the copy.

Usage: python validate-document.py <file.md>
"""

import re
import sys

FENCE = re.compile(r"^\s*(`{3,})")
HEADING = re.compile(r"^(#{1,6})\s")
BULLET = re.compile(r"^\s*[-*+] ")
ORDERED = re.compile(r"^\s*\d+\. ")
TYPO_QUOTES = "“”‘’‚„«»"
INLINE_CODE = re.compile(r"`[^`]*`")


def is_sep(cells):
    return len(cells) > 0 and all(set(c) <= set("-:") and "-" in c for c in cells)


def parse_row(line):
    parts = line.split("|")
    cells = parts[1:-1] if parts and parts[-1].strip() == "" else parts[1:]
    return [c.strip() for c in cells]


def raw_cells(line):
    parts = line.split("|")
    return parts[1:-1] if parts and parts[-1].strip() == "" else parts[1:]


def check_tables(lines, issues):
    i = 0
    while i < len(lines):
        if not lines[i].startswith("|"):
            i += 1
            continue
        block = []
        start = i
        while i < len(lines) and lines[i].startswith("|"):
            block.append(lines[i])
            i += 1
        rows = [raw_cells(l) for l in block]
        ncols = max(len(r) for r in rows)
        widths = [0] * ncols
        for r in rows:
            if is_sep([c.strip() for c in r]):
                continue
            for j in range(ncols):
                cell = r[j].strip() if j < len(r) else ""
                widths[j] = max(widths[j], len(cell))
        for offset, r in enumerate(rows):
            if len(r) != ncols:
                issues.append(f"line {start + offset + 1}: ragged table row")
                continue
            if is_sep([c.strip() for c in r]):
                for j, cell in enumerate(r):
                    if len(cell) != widths[j] + 2:
                        issues.append(
                            f"line {start + offset + 1}: separator cell width mismatch"
                        )
                        break
                continue
            for j, cell in enumerate(r):
                if len(cell) != widths[j] + 2:
                    issues.append(
                        f"line {start + offset + 1}: table cell not padded to column width"
                    )
                    break


def main(path):
    raw = open(path, "rb").read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        print(f"FAIL {path}: not decodable as UTF-8, check encoding first "
              "(see conventions/file-encoding.md)")
        return 1

    lines = text.replace("\r\n", "\n").split("\n")
    issues = []

    h1 = 0
    in_fence = False
    fence_len = 0
    fence_first = -1
    prev = ""
    for i, line in enumerate(lines):
        n = i + 1
        fence = FENCE.match(line)
        if fence:
            marker = len(fence.group(1))
            if not in_fence:
                if prev.strip() != "" and not HEADING.match(prev):
                    issues.append(f"line {n}: no blank line before code block")
                fence_first = i
                fence_len = marker
                in_fence = True
            elif marker >= fence_len:
                if i > fence_first + 1 and lines[i - 1].strip() == "":
                    issues.append(f"line {n}: blank line at end of code block")
                if i + 1 < len(lines) and lines[i + 1].strip() != "":
                    issues.append(f"line {n}: no blank line after code block")
                in_fence = False
            prev = line
            continue
        if in_fence:
            if i == fence_first + 1 and line.strip() == "":
                issues.append(f"line {n}: blank line at start of code block")
            prev = line
            continue

        if line != line.rstrip(" \t"):
            issues.append(f"line {n}: trailing whitespace")
        if line.strip() == "" and prev.strip() == "":
            issues.append(f"line {n}: consecutive blank lines")

        heading = HEADING.match(line)
        if heading:
            level = len(heading.group(1))
            if level == 1:
                h1 += 1
            if level >= 4:
                issues.append(f"line {n}: heading deeper than H3")
            if line.rstrip().endswith((".", ",", ":", ";", "!", "?")):
                issues.append(f"line {n}: heading ends with punctuation")

        if any(q in line for q in TYPO_QUOTES):
            issues.append(f"line {n}: typographic quote or apostrophe")

        prose = INLINE_CODE.sub("", line)
        if ";" in prose:
            issues.append(f"line {n}: semicolon in prose")

        if re.search(r"[\U0001F300-\U0001FAFF☀-➿⬀-⯿]", line):
            issues.append(f"line {n}: emoji or pictograph")

        structural = BULLET.match(line) or ORDERED.match(line) or line.startswith("|")
        prev_structural = BULLET.match(prev) or ORDERED.match(prev) or prev.startswith("|")
        continuation = line[:1] in (" ", "\t") and line.strip() != ""
        prev_continuation = prev[:1] in (" ", "\t") and prev.strip() != ""
        if structural and prev.strip() != "" and not prev_structural and not prev_continuation:
            issues.append(f"line {n}: no blank line before list or table")
        if (
            prev_structural
            and not structural
            and not continuation
            and line.strip() != ""
        ):
            issues.append(f"line {n}: no blank line after list or table")

        prev = line

    warnings = []
    if h1 == 0:
        warnings.append("document has no H1 title (allowed for notes, verify the type)")
    if h1 > 1:
        warnings.append(f"document has {h1} H1 headings (verify numbered-chapter dialect)")

    check_tables(lines, issues)

    for message in warnings:
        print(f"WARN {path}:{message}")
    if issues:
        for message in issues:
            print(f"FAIL {path}:{message}")
        print(f"{len(issues)} issue(s) found")
        return 1
    print(f"PASS {path}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate-document.py <file.md>")
        raise SystemExit(1)
    raise SystemExit(main(sys.argv[1]))
