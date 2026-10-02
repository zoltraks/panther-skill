#!/usr/bin/env python3
"""Check a document's sections against a type file's Section Names table.

Reads the ``## Section Names`` table of a ``types/<name>.md`` rule file and
compares the target document's headings against it:

- ``MISSING required``    - a required section is absent (fails the check)
- ``MISSING recommended`` - a recommended section is absent (warning)
- ``UNUSUAL``             - a section marked unusual for the type is present
- ``NOTE unexpected``     - a heading not listed in the table (informational)

Usage:

    python check-sections.py <file.md> --type <types/name.md>
        [--language <languages/code.md>] [--payload-markdown]

``--language`` accepts a language baseline file whose per-type section-name
table maps English section names to localized ones; localized headings then
match their canonical English names.

Exits 1 when a required section is missing, 0 otherwise.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

H1_ONLY_TITLE = True


def heading_text(line: str) -> str | None:
    match = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
    return match.group(2) if match else None


def is_fence(line: str) -> tuple[str, int] | None:
    match = re.match(r"^\s*(`{3,}|~{3,})", line)
    return (match.group(1)[0], len(match.group(1))) if match else None


def iter_headings(text: str, payload_markdown: bool) -> list[tuple[int, str]]:
    """Return (level, text) of headings outside fenced code blocks.

    With payload_markdown, headings whose innermost enclosing fence is tagged
    ``markdown`` are included too; other fence languages stay opaque.
    """
    headings: list[tuple[int, str]] = []
    fences: list[tuple[str, int, str]] = []
    for raw in text.splitlines():
        fence = is_fence(raw)
        if fence:
            char, length = fence
            if fences and char == fences[-1][0] and length >= fences[-1][1]:
                fences.pop()
            else:
                tag = raw.lstrip(char).strip().lower()
                fences.append((char, length, tag))
            continue
        if fences and not (payload_markdown and fences[-1][2] == "markdown"):
            continue
        found = heading_text(raw)
        if found:
            level = len(re.match(r"^#+", raw).group(0))
            headings.append((level, found))
    return headings


def parse_section_table(type_file: Path) -> tuple[dict[str, str], bool]:
    """Parse the ``## Section Names`` table from a type file.

    Returns (name -> requirement) and whether a table was found at all.
    """
    lines = type_file.read_text(encoding="utf-8", errors="replace").splitlines()
    start = next(
        (i for i, l in enumerate(lines) if l.strip().lower() == "## section names"),
        None,
    )
    if start is None:
        return {}, False
    table: dict[str, str] = {}
    found_table = False
    for line in lines[start + 1 :]:
        stripped = line.strip()
        if stripped.startswith("## "):
            break
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) < 2:
            continue
        first = cells[0].lower()
        if first in ("section", "name", "") or set(cells[1]) <= set("-: "):
            found_table = True
            continue
        requirement = cells[1].lower()
        if requirement in ("required", "recommended", "optional", "unusual"):
            table[cells[0]] = requirement
            found_table = True
    return table, found_table


def parse_language_aliases(lang_file: Path, type_slug: str,
                           english_names: set[str]) -> dict[str, str]:
    """Map localized section names back to their canonical English names.

    Language files carry tables like ``| type-slug | English Name | Local |``;
    rows matching the type slug and a canonical name contribute an alias.
    """
    aliases: dict[str, str] = {}
    try:
        text = lang_file.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return aliases
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) < 3:
            continue
        if cells[0].lower() == type_slug and cells[1] in english_names:
            aliases[cells[2].lower()] = cells[1]
    return aliases


def normalize(name: str) -> str:
    """Lowercase and strip a leading numbered-chapter prefix like ``3.1. ``."""
    return re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", name.strip()).lower()


def matches(heading: str, name: str) -> bool:
    """A heading matches a canonical name exactly or as ``Name <version>``."""
    heading_n, name_n = normalize(heading), normalize(name)
    if heading_n == name_n:
        return True
    if heading_n.startswith(name_n + " "):
        remainder = heading_n[len(name_n) + 1 :]
        return bool(re.match(r"^[\d(v\[]", remainder))
    return False


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="document to check")
    parser.add_argument("--type", dest="type_file", type=Path, required=True,
                        help="path to the types/<name>.md rule file")
    parser.add_argument("--language", type=Path, default=None,
                        help="languages/<code>.md for localized section names")
    parser.add_argument("--payload-markdown", action="store_true",
                        help="include headings inside ```markdown fences")
    args = parser.parse_args(argv)

    if not args.file.is_file():
        print(f"ERROR document not found: {args.file}")
        return 1
    if not args.type_file.is_file():
        print(f"ERROR type file not found: {args.type_file}")
        return 1

    requirements, found_table = parse_section_table(args.type_file)
    if not found_table:
        print(f"NOTE {args.type_file.name}: no Section Names table - open set")
        return 0

    type_slug = args.type_file.stem
    headings = iter_headings(
        args.file.read_text(encoding="utf-8", errors="replace"),
        args.payload_markdown,
    )
    sections = [text for level, text in headings if not (H1_ONLY_TITLE and level == 1)]

    aliases: dict[str, str] = {}
    if args.language:
        aliases = parse_language_aliases(
            args.language, type_slug, set(requirements)
        )

    def canonical(heading: str) -> str | None:
        for name in requirements:
            if matches(heading, name):
                return name
        alias = aliases.get(normalize(heading))
        if alias:
            return alias
        return None

    matched = {canonical(h) for h in sections if canonical(h)}
    failures = warnings = 0
    for name, requirement in requirements.items():
        if name in matched:
            if requirement == "unusual":
                print(f"UNUSUAL {name} - does not fit the {type_slug} type")
                warnings += 1
            continue
        if requirement == "required":
            print(f"MISSING required {name}")
            failures += 1
        elif requirement == "recommended":
            print(f"MISSING recommended {name}")
            warnings += 1
    for heading in sections:
        if canonical(heading) is None:
            print(f"NOTE unexpected heading: {heading}")
    if not failures and not warnings:
        print(f"PASS {args.file}: sections conform to the {type_slug} type")
    else:
        print(f"RESULT {failures} missing required, {warnings} warning(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(errors="backslashreplace")
    sys.stderr.reconfigure(errors="backslashreplace")
    sys.exit(main(sys.argv[1:]))
