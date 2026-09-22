#!/usr/bin/env python3
"""Mechanical style checker for Markdown documents produced by this skill.

Covers the scriptable items of process/document-checklist.md: structure,
spacing, characters, lists, code fences, and table alignment.

Non-ASCII characters in prose (outside inline code spans) are reported as
warnings, not failures - they may be a deliberate document convention.
Box-drawing characters (U+2500-U+257F) are exempt.

Copy this file into the working repository's `work/` directory (or the
repository root when no `work/` exists) as `validate-document.tmp.py`, run it
on the document file, then remove the copy.

Usage: python validate-document.py <file.md> [--width N] [--payload-markdown]

  --width N            flag lines longer than N characters (tables excluded)
  --payload-markdown   apply a curated subset of checks inside ```markdown
                       fenced blocks (embedded payload documents): trailing
                       whitespace, consecutive blank lines, lone list
                       markers, and heading checks
"""

import argparse
import re
import sys

FENCE = re.compile(r"^\s*(`{3,})\s*(\w*)")
HEADING = re.compile(r"^(#{1,6})\s")
BULLET = re.compile(r"^\s*[-*+] ")
ORDERED = re.compile(r"^\s*\d+\. ")
LONE_ITEM = re.compile(r"^\s*([-*+]|\d+[.)])[ \t]*$")
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


def in_payload(fences, payload_markdown):
    return payload_markdown and bool(fences) and all(
        lang == "markdown" for _, lang in fences
    )


def check_tables(lines, issues):
    i = 0
    fences = []
    sep_styles = set()
    while i < len(lines):
        fence = FENCE.match(lines[i])
        if fence:
            marker = len(fence.group(1))
            if fences and marker >= fences[-1][0]:
                fences.pop()
            else:
                fences.append((marker, fence.group(2)))
            i += 1
            continue
        if fences or not lines[i].startswith("|"):
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
                for c in r:
                    sep_styles.add("spaced" if c != c.strip() else "compact")
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
    if len(sep_styles) > 1:
        issues.append("document mixes spaced and compact table separators")


def main(path, width, payload_markdown):
    raw = open(path, "rb").read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        print(f"FAIL {path}: not decodable as UTF-8, check encoding first "
              "(see conventions/file-encoding.md)")
        return 1

    lines = text.replace("\r\n", "\n").split("\n")
    issues = []
    warnings = []

    h1 = 0
    fences = []
    fence_first = -1
    prev = ""
    for i, line in enumerate(lines):
        n = i + 1
        fence = FENCE.match(line)
        if fence:
            marker = len(fence.group(1))
            if fences and marker >= fences[-1][0]:
                if i > fence_first + 1 and lines[i - 1].strip() == "":
                    issues.append(f"line {n}: blank line at end of code block")
                if i + 1 < len(lines) and lines[i + 1].strip() != "":
                    issues.append(f"line {n}: no blank line after code block")
                fences.pop()
            else:
                if prev.strip() != "" and not HEADING.match(prev):
                    issues.append(f"line {n}: no blank line before code block")
                fence_first = i
                fences.append((marker, fence.group(2)))
            prev = line
            continue

        if line != line.rstrip(" \t"):
            issues.append(f"line {n}: trailing whitespace")

        if fences and not in_payload(fences, payload_markdown):
            if i == fence_first + 1 and line.strip() == "":
                issues.append(f"line {n}: blank line at start of code block")
            prev = line
            continue

        payload = in_payload(fences, payload_markdown)
        indented_code = payload and (len(line) - len(line.lstrip())) >= 4

        if line.strip() == "" and prev.strip() == "":
            issues.append(f"line {n}: consecutive blank lines")

        if LONE_ITEM.match(line):
            issues.append(f"line {n}: lone list marker")

        heading = HEADING.match(line)
        if heading:
            level = len(heading.group(1))
            if not payload:
                if level == 1:
                    h1 += 1
                if level >= 4:
                    issues.append(f"line {n}: heading deeper than H3")
                if line.rstrip().endswith((".", ",", ":", ";", "!", "?")):
                    issues.append(f"line {n}: heading ends with punctuation")

        if not payload:
            if any(q in line for q in TYPO_QUOTES):
                issues.append(f"line {n}: typographic quote or apostrophe")

            prose = INLINE_CODE.sub("", line)
            if ";" in prose:
                issues.append(f"line {n}: semicolon in prose")

            if re.search(r"[\U0001F300-\U0001FAFF☀-➿⬀-⯿]", line):
                issues.append(f"line {n}: emoji or pictograph")

            foreign = [
                c for c in dict.fromkeys(prose)
                if ord(c) > 127 and not 0x2500 <= ord(c) <= 0x257F
            ]
            if foreign:
                warnings.append(
                    f"line {n}: non-ASCII character(s) in prose: "
                    + " ".join(f"U+{ord(c):04X} '{c}'" for c in foreign)
                )

        if width and not line.startswith("|") and len(line) > width:
            issues.append(f"line {n}: {len(line)} chars exceeds width {width}")

        if indented_code:
            prev = line
            continue

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
    parser = argparse.ArgumentParser(
        description="Mechanical style checker for Markdown documents."
    )
    parser.add_argument("file")
    parser.add_argument("--width", type=int, default=0,
                        help="flag lines longer than N characters")
    parser.add_argument("--payload-markdown", action="store_true",
                        help="apply curated checks inside ```markdown blocks")
    parsed = parser.parse_args()
    raise SystemExit(main(parsed.file, parsed.width, parsed.payload_markdown))
