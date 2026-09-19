#!/usr/bin/env python3
"""Canonical table formatter implementing the table rules in the language
files (languages/english.md, languages/polish.md).

Copy this file into the working repository's `work/` directory (or the
repository root when no `work/` exists) as `format-table.tmp.py`, run it
on the document file, verify that all `|` separators align vertically, then
remove the copy.

Usage: python format-table.py <document.md>
"""

import re
import sys


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


def main(path):
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
    in_fence = False
    fence_len = 0
    while i < len(lines):
        line = lines[i]
        fence = re.match(r"^\s*(`{3,})", line)
        if fence:
            marker = len(fence.group(1))
            if not in_fence:
                fence_len = marker
                in_fence = True
            elif marker >= fence_len:
                in_fence = False
            out.append(line)
            i += 1
            continue
        if not in_fence and line.startswith("|"):
            block = []
            while i < len(lines) and lines[i].startswith("|"):
                block.append(lines[i])
                i += 1
            rows = [parse_row(l) for l in block]
            ncols = max(len(r) for r in rows)
            rows = [r + [""] * (ncols - len(r)) for r in rows]
            widths = [1] * ncols
            for r in rows:
                if is_sep(r):
                    continue
                for j, c in enumerate(r):
                    widths[j] = max(widths[j], len(c))
            for r in rows:
                if is_sep(r):
                    out.append("|" + "|".join("-" * (w + 2) for w in widths) + "|")
                else:
                    out.append("| " + " | ".join(c.ljust(widths[j]) for j, c in enumerate(r)) + " |")
            tables += 1
        else:
            out.append(line)
            i += 1

    eol = "\r\n" if crlf else "\n"
    open(path, "wb").write(eol.join(out).encode(encoding))
    print(f"formatted {tables} tables")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
