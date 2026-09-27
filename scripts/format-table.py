#!/usr/bin/env python3
"""Canonical table formatter implementing the table rules in the language
files (languages/en.md, languages/pl.md).

Copy this file into the working repository's `work/` directory (or the
repository root when no `work/` exists) as `format-table.tmp.py`, run it
on the document file, verify that all `|` separators align vertically, then
remove the copy.

Usage: python format-table.py <document.md> [--check] [--payload-markdown]

  --check              report tables that would be reformatted and exit 1,
                       without writing the file
  --payload-markdown   also format tables inside ```markdown fenced blocks
                       (embedded payload documents); other fence languages
                       always stay opaque
"""

import argparse
import re
import sys

FENCE = re.compile(r"^\s*(`{3,})\s*(\w*)")


def decode(raw):
    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        return raw.decode("utf-16"), "utf-16"
    return raw.decode("utf-8"), "utf-8"


def parse_row(line):
    parts = line.split("|")
    cells = parts[1:-1] if parts and parts[-1].strip() == "" else parts[1:]
    return [c.strip() for c in cells]


def is_sep(cells):
    return len(cells) > 0 and all(set(c) <= set("-:") and "-" in c for c in cells)


def format_block(block):
    rows = [parse_row(l) for l in block]
    ncols = max(len(r) for r in rows)
    rows = [r + [""] * (ncols - len(r)) for r in rows]
    widths = [1] * ncols
    for r in rows:
        if is_sep(r):
            continue
        for j, c in enumerate(r):
            widths[j] = max(widths[j], len(c))
    out = []
    for r in rows:
        if is_sep(r):
            out.append("|" + "|".join("-" * (w + 2) for w in widths) + "|")
        else:
            out.append(
                "| " + " | ".join(c.ljust(widths[j]) for j, c in enumerate(r)) + " |"
            )
    return out


def in_payload(fences, payload_markdown):
    return payload_markdown and bool(fences) and all(
        lang == "markdown" for _, lang in fences
    )


def main(path, check_only, payload_markdown):
    raw = open(path, "rb").read()
    crlf = b"\r\n" in raw
    try:
        text, encoding = decode(raw)
    except UnicodeDecodeError:
        print(f"FAIL {path}: not decodable as UTF-8 or UTF-16, "
              "check encoding first (see conventions/file-encoding.md)")
        return 1
    lines = text.replace("\r\n", "\n").split("\n")

    out, i, tables = [], 0, 0
    fences = []
    changed = []
    while i < len(lines):
        line = lines[i]
        fence = FENCE.match(line)
        if fence:
            marker = len(fence.group(1))
            if fences and marker >= fences[-1][0]:
                fences.pop()
            else:
                fences.append((marker, fence.group(2)))
            out.append(line)
            i += 1
            continue
        if (not fences or in_payload(fences, payload_markdown)) \
                and line.startswith("|"):
            block = []
            start = i
            while i < len(lines) and lines[i].startswith("|"):
                block.append(lines[i])
                i += 1
            formatted = format_block(block)
            if formatted != block:
                changed.append(start + 1)
            out.extend(formatted)
            tables += 1
        else:
            out.append(line)
            i += 1

    if check_only:
        for n in changed:
            print(f"line {n}: table would be reformatted")
        if changed:
            print(f"{len(changed)} table(s) need formatting")
            return 1
        print(f"PASS {path}: {tables} table(s) already aligned")
        return 0

    eol = "\r\n" if crlf else "\n"
    open(path, "wb").write(eol.join(out).encode(encoding))
    print(f"formatted {tables} tables")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Format Markdown tables with source-width alignment."
    )
    parser.add_argument("file")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--payload-markdown", action="store_true")
    parsed = parser.parse_args()
    raise SystemExit(main(parsed.file, parsed.check, parsed.payload_markdown))
