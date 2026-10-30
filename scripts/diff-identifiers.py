#!/usr/bin/env python3
"""Census or diff identifier tokens between document versions.

Fact-preserving rewrites - a humanize pass, a correction pass, a reformat -
must prove that every identifier survived. This tool counts occurrences of
identifier-shaped tokens (the `PREFIX-NN` family used by requirement, decision,
reference, and use-case identifiers) in one file, or diffs the census between a
before and an after file.

The default pattern matches one or more uppercase letters, a hyphen, and digits
(`[A-Z]+-[0-9]+`); a custom pattern is accepted via `--pattern`.

Single-file mode prints the census sorted by identifier. Diff mode prints a
three-part report: identifiers absent from the after file (DROPPED), counts
that changed (DELTA, expected when a section citing them was deleted), and new
identifiers (ADDED). A clean voice rewrite shows no DROPPED or ADDED entries,
and every DELTA traces to an intended deletion.

`--check` in diff mode exits 1 when any identifier is dropped or added -
count deltas alone are reported but do not fail the check.

Run this file in place from the skill repository -
`python <skill-root>/scripts/diff-identifiers.py` - and copy it under a
`.tmp.` name into the working repository's `work/` directory only when the
skill root cannot be invoked, removing the copy afterward.

Usage: python diff-identifiers.py <file.md>
       python diff-identifiers.py --before <old.md> --after <new.md> [--check]
                                   [--pattern REGEX]
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

DEFAULT_PATTERN = r"[A-Z]+-[0-9]+"


def census(path: Path, pattern: re.Pattern) -> Counter:
    text = path.read_text(encoding="utf-8-sig")
    return Counter(pattern.findall(text))


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Census or diff identifier tokens between file versions")
    ap.add_argument("file", nargs="?")
    ap.add_argument("--before")
    ap.add_argument("--after")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--pattern", default=DEFAULT_PATTERN)
    args = ap.parse_args()

    pattern = re.compile(args.pattern)

    if args.before or args.after:
        if not (args.before and args.after):
            ap.error("--before and --after go together")
        old = census(Path(args.before), pattern)
        new = census(Path(args.after), pattern)
        dropped = sorted(set(old) - set(new))
        added = sorted(set(new) - set(old))
        deltas = sorted(
            (k, old[k], new[k])
            for k in set(old) & set(new) if old[k] != new[k])
        for k in dropped:
            print(f"DROPPED {k} ({old[k]} -> 0)")
        for k in added:
            print(f"ADDED {k} (0 -> {new[k]})")
        for k, o, n in deltas:
            print(f"DELTA {k} ({o} -> {n})")
        print(f"diff-identifiers: {len(dropped)} dropped, {len(added)} added, "
              f"{len(deltas)} delta(s)")
        if args.check and (dropped or added):
            return 1
        return 0

    if not args.file:
        ap.error("a file or --before/--after is required")
    counts = census(Path(args.file), pattern)
    for k in sorted(counts):
        print(f"{counts[k]:5d} {k}")
    print(f"diff-identifiers: {len(counts)} distinct identifier(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
