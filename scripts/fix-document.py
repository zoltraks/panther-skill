#!/usr/bin/env python3
"""Mechanical-repair tool for the safe validate-document finding classes.

Run this file in place from the skill repository -
`python <skill-root>/scripts/fix-document.py` - and run it on the document
file. Copy it under a `.tmp.` name into the working repository's `work/`
directory (or the repository root when no `work/` exists) only when the
skill root cannot be invoked, and remove the copy afterward.

Usage: python fix-document.py <document.md> [--check] [--passes N]

  --check   report the repairable findings without writing - exit 1 when
            any remain, 0 when the file is clean
  --passes  maximum repair iterations (default 6)

The tool drives the siblings it ships with: `format-table.py` realigns
tables first, then each `validate-document.py` finding is repaired when it
belongs to a safe mechanical class - `semicolon in prose` becomes the
house aside separator ` - ` (a period at line end), `literal pipe inside
code span` is escaped to `&#124;`, and missing blank lines around lists
and tables are inserted. The loop repeats to a fixed point so one repair
cannot shadow another.

Classes outside that set - headings, fences, links, reflow notes - are
structural or judgment calls and are reported, never touched. A finding
that survives the loop is listed as unrepairable.
"""

import argparse
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VALIDATE = os.path.join(HERE, "validate-document.py")
TABLE = os.path.join(HERE, "format-table.py")

FAIL_RE = re.compile(r"FAIL .+?:line (\d+): (.+)$", re.M)

MECHANICAL = (
    "semicolon in prose",
    "literal pipe inside code span",
    "no blank line before",
    "no blank line after",
)


def validate_failures(path):
    """Parse validate-document.py FAIL lines into (line, reason) tuples."""
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    out = subprocess.run(
        [sys.executable, VALIDATE, path],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    ).stdout or ""
    return FAIL_RE.findall(out)


def fix_semicolon(line):
    # "; " mid-sentence becomes the aside separator; a trailing ';'
    # becomes a period. Spans exempted by the validator stay untouched.
    if "; " in line:
        return line.replace("; ", " - ")
    return re.sub(r";(?=\s*$)", ".", line)


def fix_pipe(line):
    # A literal | inside a code span inflates the table's column count -
    # escape it inside the span only.
    return re.sub(r"`[^`]*\|[^`]*`", lambda m: m.group(0).replace("|", "&#124;"), line)


def apply_repair(lines, number, reason):
    idx = number - 1
    if idx >= len(lines):
        return lines
    if "semicolon in prose" in reason:
        lines[idx] = fix_semicolon(lines[idx])
    elif "literal pipe inside code span" in reason:
        lines[idx] = fix_pipe(lines[idx])
    elif "no blank line before" in reason or "no blank line after" in reason:
        # Both findings name the same missing boundary - the blank goes
        # between line N-1 and line N in every flagged case.
        if idx > 0 and lines[idx - 1].strip() != "":
            lines.insert(idx, "")
    return lines


def read_lines(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read().split("\n")


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines))


def main(path, check_only, max_passes):
    if not os.path.isfile(path):
        print(f"fix-document: {path} - not found")
        return 2

    if check_only:
        repairable = [
            (n, r) for n, r in validate_failures(path)
            if any(k in r for k in MECHANICAL)
        ]
        if repairable:
            for n, r in repairable:
                print(f"FIXABLE {path}:line {n}: {r}")
            print(f"fix-document: {path} - {len(repairable)} repairable finding(s)")
            return 1
        print(f"fix-document: {path} - clean")
        return 0

    repaired = 0
    for _ in range(max_passes):
        before = open(path, "rb").read()
        fails = validate_failures(path)
        mechanical = [
            (n, r) for n, r in fails if any(k in r for k in MECHANICAL)
        ]
        if mechanical:
            lines = read_lines(path)
            for number, reason in sorted(mechanical, key=lambda item: -int(item[0])):
                lines = apply_repair(lines, int(number), reason)
            write_lines(path, lines)
            repaired += len(mechanical)
        # format-table runs after the text repairs - a literal pipe left
        # in a code span would otherwise inflate the table's column count.
        subprocess.run(
            [sys.executable, TABLE, path], capture_output=True, check=False
        )
        if open(path, "rb").read() == before:
            break

    remaining = validate_failures(path)
    hard = [
        (n, r) for n, r in remaining if not any(k in r for k in MECHANICAL)
    ]
    for n, r in remaining:
        tag = "REMAIN" if (n, r) in hard else "FIXED-LATE"
        print(f"{tag} {path}:line {n}: {r}")
    if not remaining:
        print(f"fix-document: {path} - PASS ({repaired} repair(s))")
        return 0
    print(
        f"fix-document: {path} - {repaired} repair(s), "
        f"{len(remaining)} finding(s) remain"
    )
    return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Apply safe mechanical repairs to a Markdown document."
    )
    parser.add_argument("path")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--passes", type=int, default=6)
    sys.exit(main(parser.parse_args().path, parser.parse_args().check,
                  parser.parse_args().passes))
