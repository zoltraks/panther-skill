#!/usr/bin/env python3
"""Apply explicit old -> new literal replacement pairs to a document.

Bulk edits done with a global replace trust that every site the pattern hits is a
site meant to change - that trust fails whenever the pattern also matches inside
code, URLs, or neighboring prose. This tool takes an explicit pair list instead:
each entry is a literal old string and its replacement, and the tool asserts every
old occurs exactly the expected number of times (default one) before writing.

Pairs are read from a UTF-8 pairs file, one pair per two lines:

    ---- old ----
    <old text, one or more lines>
    ---- new ----
    <new text, one or more lines>
    ---- next ----

Block form keeps multi-line replacements possible; a simpler line form also
works - `old => new` on a single line (the `=>` separator must be unique in the
line). Blank lines and `#` comments at the top level are ignored.

`--check` performs a dry run: it reports matched, missing, and over-matched
pairs without writing, and exits 1 when any pair fails its count assertion or
two pair olds overlap.

Encoding and line-ending style are preserved - the file is decoded as UTF-8
(or UTF-8 with BOM when present), modified in memory, and written back with
the same encoding.

Run this file in place from the skill repository -
`python <skill-root>/scripts/apply-pairs.py` - and copy it under a `.tmp.`
name into the working repository's `work/` directory only when the skill root
cannot be invoked, removing the copy afterward.

Usage: python apply-pairs.py <file.md> <pairs.txt> [--check] [--count N]

  --check    report what each pair would do without writing; exit 1 on any
             failed count assertion or overlap
  --count N  expected occurrences per pair old, default 1
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_pairs(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8-sig")
    pairs: list[tuple[str, str]] = []
    lines = text.split("\n")
    # Block form detection
    if any(l.strip() == "---- old ----" for l in lines):
        i = 0
        while i < len(lines):
            if lines[i].strip() == "---- old ----":
                i += 1
                old_buf = []
                while i < len(lines) and lines[i].strip() != "---- new ----":
                    old_buf.append(lines[i]); i += 1
                i += 1  # skip ---- new ----
                new_buf = []
                while (i < len(lines) and lines[i].strip() != "---- next ----"
                       and lines[i].strip() != "---- old ----"):
                    new_buf.append(lines[i]); i += 1
                if i < len(lines) and lines[i].strip() == "---- next ----":
                    i += 1
                old = "\n".join(old_buf).strip("\n")
                new = "\n".join(new_buf).strip("\n")
                if old:
                    pairs.append((old, new))
            else:
                i += 1
        return pairs
    # Line form
    for raw in lines:
        line = raw.rstrip("\n")
        if not line.strip() or line.strip().startswith("#"):
            continue
        if line.count(" => ") != 1:
            print(f"apply-pairs: pairs line without a unique ' => ': {line[:60]}",
                  file=sys.stderr)
            sys.exit(2)
        old, new = line.split(" => ")
        pairs.append((old, new))
    return pairs


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Apply explicit literal old->new pairs with count assertions")
    ap.add_argument("file")
    ap.add_argument("pairs")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--count", type=int, default=1)
    args = ap.parse_args()

    doc = Path(args.file)
    pairs_path = Path(args.pairs)
    for p in (doc, pairs_path):
        if not p.is_file():
            print(f"apply-pairs: not a file: {p}", file=sys.stderr)
            return 2
    pairs = parse_pairs(pairs_path)
    if not pairs:
        print("apply-pairs: no pairs parsed", file=sys.stderr)
        return 2

    raw = doc.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")

    failed = False
    olds = [o for o, _ in pairs]
    for idx, (old, new) in enumerate(pairs, 1):
        n = text.count(old)
        status = "ok" if n == args.count else "FAIL"
        if n != args.count:
            failed = True
        print(f"pair {idx}: {status} ({n} occurrence(s), expected {args.count}) "
              f"{old[:60]!r}")
        for jdx, other in enumerate(olds):
            if idx - 1 != jdx and old in other:
                print(f"  overlap: pair {idx} old is a substring of pair {jdx + 1}")
                failed = True
    if args.check or failed:
        print(f"apply-pairs: {'check only' if args.check else 'aborted'} - "
              f"{len(pairs)} pair(s), "
              f"{'no write' if args.check or failed else 'written'}")
        return 1 if failed else 0
    for old, new in pairs:
        text = text.replace(old, new, args.count)
    out = text.encode("utf-8")
    doc.write_bytes((b"\xef\xbb\xbf" + out) if bom else out)
    print(f"apply-pairs: applied {len(pairs)} pair(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
