#!/usr/bin/env python3
"""Replace text in a document with whole-word boundaries by default.

A bare substring replacement corrupts words that contain the pattern as a
fragment - `niesie` -> `wnosi` also rewrites `odniesienia` into
`odwnosinia`. This tool replaces only whole-word matches
(`(?<!\\w)old(?!\\w)`) and reports the residue: words that still contain the
old text as a fragment, and words that contain the new text inside a longer
token - the corruption signature a raw replace would have produced.

`--raw` performs a deliberate substring replacement - the residue report
still prints, so a raw run shows the neighbors it could not protect.

`--check` performs a dry run: it reports what would be replaced and what the
residue would look like, and exits 1 when the pattern also occurs inside
longer words - a signal that a `--raw` run would corrupt them - or when a
raw run would leave corruption-signature words behind.

Encoding and line-ending style are preserved - the file is decoded as UTF-8
(or UTF-8 with BOM when present), modified in memory, and written back with
the same encoding.

Run this file in place from the skill repository -
`python <skill-root>/scripts/safe-replace.py` - and copy it under a `.tmp.`
name into the working repository's `work/` directory only when the skill
root cannot be invoked, removing the copy afterward.

Usage:
    python safe-replace.py <file.md> <old> <new> [--raw] [--check]
"""

import argparse
import re
import sys
from pathlib import Path


def reconfigure_stdio():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="backslashreplace")
        except Exception:
            pass


def line_of(text, offset):
    return text.count("\n", 0, offset) + 1


def containing_words(text, token):
    """Whole-word occurrences that contain `token` as a strict fragment.

    Returns [(line_number, word)] for matches where the matched word is not
    exactly `token` - these are the neighbors a raw replace would corrupt
    (for the old token) or the corruption signature (for the new token).
    """
    pattern = re.compile(r"\w*" + re.escape(token) + r"\w*")
    return [
        (line_of(text, m.start()), m.group(0))
        for m in pattern.finditer(text)
        if m.group(0) != token
    ]


def report_residue(label, hits):
    for lineno, word in hits[:10]:
        print(f"WARN line {lineno}: {label}: `{word}`")
    if len(hits) > 10:
        print(f"WARN ... and {len(hits) - 10} more")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("old")
    parser.add_argument("new")
    parser.add_argument("--raw", action="store_true",
                        help="literal substring replacement - corrupts words "
                             "that contain the pattern as a fragment")
    parser.add_argument("--check", action="store_true",
                        help="dry run - report counts and residue, write "
                             "nothing")
    args = parser.parse_args()

    raw = args.file.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig" if bom else "utf-8")

    boundary = re.compile(r"(?<!\w)" + re.escape(args.old) + r"(?!\w)")
    if args.raw:
        count = text.count(args.old)
        result = text.replace(args.old, args.new)
    else:
        result, count = boundary.subn(args.new, text)

    if args.check:
        if args.raw:
            old_hits = containing_words(result, args.old)
            new_hits = containing_words(result, args.new)
            print(f"safe-replace --check: raw run would replace {count} "
                  f"occurrence(s) of '{args.old}'")
            report_residue("word still contains the pattern", old_hits)
            report_residue("corruption signature contains the replacement",
                           new_hits)
            return 1 if new_hits else 0
        all_occurrences = len(re.findall(re.escape(args.old), text))
        inside_words = all_occurrences - count
        print(f"safe-replace --check: would replace {count} of "
              f"{all_occurrences} occurrence(s) of '{args.old}' - "
              f"{inside_words} sit(s) inside longer words")
        report_residue("word contains the pattern, not the word",
                       containing_words(text, args.old))
        return 1 if inside_words else 0

    if count:
        if not args.raw:
            inside = containing_words(text, args.old)
            if inside:
                print("safe-replace: note - word(s) containing the pattern "
                      "were left untouched:")
                report_residue("contains the pattern, not the word", inside)
        args.file.write_bytes(
            result.encode("utf-8-sig" if bom else "utf-8"))
        print(f"safe-replace: replaced {count} occurrence(s) of "
              f"'{args.old}' in {args.file}")
    else:
        print(f"safe-replace: no occurrence of '{args.old}' in {args.file}")

    if args.raw:
        new_hits = containing_words(result, args.new)
        if new_hits:
            print("safe-replace: WARNING - word(s) containing the replacement "
                  "inside a longer token:")
            report_residue("possible corruption", new_hits)
    return 0


if __name__ == "__main__":
    reconfigure_stdio()
    sys.exit(main())
