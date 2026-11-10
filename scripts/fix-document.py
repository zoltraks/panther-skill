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
code span` is escaped to `&#124;`, missing blank lines around lists
and tables are inserted, and a run of consecutive blank lines collapses
to one. The loop repeats to a fixed point so one repair
cannot shadow another.

Classes outside that set - headings, fences, links, reflow notes - are
structural or judgment calls and are reported, never touched. A finding
that survives the loop is listed as unrepairable.
"""

import argparse
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VALIDATE = os.path.join(HERE, "validate-document.py")
TABLE = os.path.join(HERE, "format-table.py")
REFLOW = os.path.join(HERE, "reflow-prose.py")

FAIL_RE = re.compile(r"FAIL .+?:line (\d+): (.+)$", re.M)

MECHANICAL = (
    "semicolon in prose", "spaced bold markers",
    "literal pipe inside code span",
    "no blank line before",
    "no blank line after",
    "consecutive blank lines",
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


LIST_LEAD = re.compile(r"^\s*[-*+] ")


def load_panther_config(path):
    """Read panther.json from the document's directory or an ancestor.

    Reuses the loader inside validate-document.py so the key format stays
    single-sourced - `semicolon_repair` selects aside|period|comma joins,
    `list_line_repair` selects join|blank|skip for marker-led
    continuation lines.
    """
    spec = importlib.util.spec_from_file_location("vd", VALIDATE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    cfg, _ = mod.load_config(path)
    return cfg if isinstance(cfg, dict) else {}


def fix_semicolon(line, mode="aside"):
    # "aside" keeps the canonical repair - "; " mid-sentence becomes the
    # aside separator, a trailing ';' a period. "period" splits into two
    # sentences, capitalizing the new one. "comma" joins with ", ".
    # Spans exempted by the validator stay untouched in every mode.
    if mode == "period":
        line = re.sub(r"; ([a-z])", lambda m: ". " + m.group(1).upper(), line)
        line = line.replace("; ", ". ")
        return re.sub(r";(?=\s*$)", ".", line)
    if mode == "comma":
        line = line.replace("; ", ", ")
        return re.sub(r";(?=\s*$)", ".", line)
    if "; " in line:
        return line.replace("; ", " - ")
    return re.sub(r";(?=\s*$)", ".", line)


def fix_spaced_bold(line):
    return re.sub(r"(?<![\w*])\*\* (\S[^*]*?\S) \*\*(?!\w)", r"**\1**", line)


def fix_pipe(line):
    # A literal | inside a code span inflates the table's column count -
    # escape it inside the span only.
    return re.sub(r"`[^`]*\|[^`]*`", lambda m: m.group(0).replace("|", "&#124;"), line)


LINK_TAIL = re.compile(r"^(?:[\w./-]+\)+[.,;:]?\s*|.*\]\([^)]*)$")


def _link_tail(line):
    # A wrapped link or URL atom continuation - a bare closing fragment at
    # column zero, or a line still inside an unclosed `](` target. Joining
    # the next line into it or splitting it with a blank line corrupts the
    # link, so repairs never touch this boundary.
    return bool(LINK_TAIL.match(line))


def apply_repair(lines, number, reason, cfg):
    idx = number - 1
    if idx >= len(lines):
        return lines
    if "semicolon in prose" in reason:
        lines[idx] = fix_semicolon(lines[idx], cfg.get("semicolon_repair", "aside"))
    elif "spaced bold markers" in reason:
        lines[idx] = fix_spaced_bold(lines[idx])
    elif "literal pipe inside code span" in reason:
        lines[idx] = fix_pipe(lines[idx])
    elif "no blank line before" in reason or "no blank line after" in reason:
        policy = cfg.get("list_line_repair", "join")
        if (policy == "join" and "before" in reason and LIST_LEAD.match(lines[idx])
                and not _link_tail(lines[idx - 1])):
            nxt = idx + 1
            if nxt >= len(lines) or not LIST_LEAD.match(lines[nxt]):
                # A lone marker-led line after prose is a wrapped aside
                # continuation, not a list - join it back instead of
                # opening a fake list with a blank line.
                lines[idx - 1] = lines[idx - 1].rstrip() + " " + lines[idx].strip()
                del lines[idx]
                return lines
        # Both findings name the same missing boundary - the blank goes
        # between line N-1 and line N in every flagged case.
        if (policy != "skip" and idx > 0 and lines[idx - 1].strip() != ""
                and not _link_tail(lines[idx - 1])):
            lines.insert(idx, "")
    elif "consecutive blank lines" in reason:
        # The validator flags the second blank line of a run - deleting it
        # collapses one duplicate per pass and the loop handles longer runs.
        if lines[idx].strip() == "" and idx > 0 and lines[idx - 1].strip() == "":
            del lines[idx]
    return lines


def read_lines(path):
    raw = open(path, "rb").read()
    return raw.decode("utf-8").replace("\r\n", "\n").split("\n"), b"\r\n" in raw


def write_lines(path, lines, crlf):
    eol = "\r\n" if crlf else "\n"
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(eol.join(lines))
    if crlf:
        print("note: file uses CRLF line endings - preserved")


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
    cfg = load_panther_config(path)
    for _ in range(max_passes):
        before = open(path, "rb").read()
        fails = validate_failures(path)
        mechanical = [
            (n, r) for n, r in fails if any(k in r for k in MECHANICAL)
        ]
        if mechanical:
            lines, crlf = read_lines(path)
            for number, reason in sorted(mechanical, key=lambda item: -int(item[0])):
                lines = apply_repair(lines, int(number), reason, cfg)
            write_lines(path, lines, crlf)
            repaired += len(mechanical)
        # format-table runs after the text repairs - a literal pipe left
        # in a code span would otherwise inflate the table's column count.
        # `table_format: off` opts a repository out entirely, and
        # `table_separator: spaced` emits `| --- |` separators instead of
        # the compact `|---|` form.
        if cfg.get("table_format", "on") != "off":
            sep = (
                ["--spaced-separator"]
                if cfg.get("table_separator") == "spaced"
                else []
            )
            subprocess.run(
                [sys.executable, TABLE, path, *sep],
                capture_output=True,
                check=False,
            )
        # reflow normalizes lines the join-back repair lengthened; on an
        # unwrapped document it abstains with a note, so the call is safe
        # under either prose layout. `prose_reflow: off` opts out.
        if cfg.get("prose_reflow", "on") != "off":
            subprocess.run(
                [sys.executable, REFLOW, path, "--wrap"],
                capture_output=True,
                check=False,
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
