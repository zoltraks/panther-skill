#!/usr/bin/env python3
"""Report a structural census for a Markdown document.

Census only - the agent maps counts to findings, see process/document-audit.md.

Copy this file into the working repository's `work/` directory (or the
repository root when no `work/` exists) as `census-document.tmp.py`, run it on
the target file, then remove the copy.

Usage: python census-document.py <file> [--width N] [--payload-markdown]
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

FENCE = re.compile(r"^\s*([`~]{3,})[ \t]*(.*?)[ \t]*$")
HEADING = re.compile(r"^(#{1,6})[ \t]+(.*?)[ \t]*$")
BULLET = re.compile(r"^\s*([-*+])[ \t]+\S")
ORDERED = re.compile(r"^\s*\d+\.[ \t]+\S")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)[^)]*\)")
MARKER = re.compile(r"\b(TODO|FIXME|TBD|XXX)\b")
SENTENCE_BOUNDARY = re.compile(r"[.!?]['\")]*[ \t]+[A-Z]")
CODE_SPAN = re.compile(r"`[^`]*`")
CONTENTS_TITLE = re.compile(r"^(contents|table of contents|spis tre[śs]ci)\b", re.I)

SPECIALS = {
    "—": "em-dash U+2014",
    "–": "en-dash U+2013",
    "‘": "single quote U+2018",
    "’": "single quote U+2019",
    "“": "double quote U+201C",
    "”": "double quote U+201D",
    "…": "ellipsis U+2026",
    "‑": "non-breaking hyphen U+2011",
    " ": "non-breaking space U+00A0",
}
CAP = 30


def classify(lines: list[str]) -> tuple[list[str], list[tuple[int, str]], int]:
    """Tag each line as prose, code, payload, or fence; collect block tags."""
    state = ["prose"] * len(lines)
    blocks: list[tuple[int, str]] = []
    payloads = 0
    fence_marker = ""
    fence_tag = ""
    for i, line in enumerate(lines):
        match = FENCE.match(line)
        if fence_marker:
            if match and match.group(1)[0] == fence_marker[0] and len(match.group(1)) >= len(fence_marker):
                state[i] = "fence"
                blocks.append((i + 1, fence_tag))
                if fence_tag.split(",")[0].strip().lower() == "markdown":
                    payloads += 1
                fence_marker = ""
            else:
                state[i] = "payload" if fence_tag.split(",")[0].strip().lower() == "markdown" else "code"
        elif match:
            state[i] = "fence"
            fence_marker = match.group(1)
            fence_tag = match.group(2)
    return state, blocks, payloads


def refs(items: list[int]) -> str:
    if not items:
        return "none"
    shown = ", ".join(str(n) for n in items[:CAP])
    return f"{shown} (+{len(items) - CAP} more)" if len(items) > CAP else shown


def is_emoji(ch: str) -> bool:
    return ord(ch) >= 0x1F000 or unicodedata.category(ch) == "So"


def main(argv: list[str]) -> int:
    args: list[str] = []
    flags: set[str] = set()
    width = 100
    skip = False
    for i, arg in enumerate(argv):
        if skip:
            skip = False
            continue
        if arg == "--width" and i + 1 < len(argv):
            width = int(argv[i + 1])
            skip = True
        elif arg.startswith("--width="):
            width = int(arg.split("=", 1)[1])
        elif arg.startswith("--"):
            flags.add(arg)
        else:
            args.append(arg)
    if len(args) != 1:
        print("Usage: python census-document.py <file> [--width N] [--payload-markdown]")
        return 1
    path = Path(args[0]).resolve()
    if not path.is_file():
        print(f"not a file: {path}")
        return 1
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"cannot read {path}: {exc}")
        return 1

    lines = text.splitlines()
    state, blocks, payloads = classify(lines)
    host = {i for i, s in enumerate(state) if s == "prose"}
    scan = set(host)
    if "--payload-markdown" in flags:
        scan |= {i for i, s in enumerate(state) if s == "payload"}

    heads, parens, punct, deep, contents = {}, [], [], [], []
    markers: dict[str, int] = {}
    ordered = 0
    tables, blank_runs, wide, multi = 0, [], [], []
    semis, links, anchors, missing = [], [], [], []
    specials: dict[str, list[int]] = {}
    other_nonascii: dict[str, int] = {}
    emoji: list[int] = []
    marker_hits: list[tuple[int, str]] = []
    blank_start = None
    in_table = False

    for i, line in enumerate(lines):
        if i not in scan:
            blank_start = None
            if state[i] == "fence":
                in_table = False
            continue
        stripped = CODE_SPAN.sub("", line)
        if not line.strip():
            if blank_start is None:
                blank_start = i + 1
            else:
                blank_runs.append(blank_start)
            continue
        blank_start = None
        if len(line) > width:
            wide.append(i + 1)
        if SENTENCE_BOUNDARY.search(stripped):
            multi.append(i + 1)
        if ";" in stripped:
            semis.append(i + 1)
        for ch in stripped:
            if ch in SPECIALS:
                specials.setdefault(ch, []).append(i + 1)
            elif ord(ch) > 127:
                if is_emoji(ch):
                    emoji.append(i + 1)
                else:
                    other_nonascii[ch] = other_nonascii.get(ch, 0) + 1
        if i not in host:
            continue
        head = HEADING.match(line)
        if head:
            depth = len(head.group(1))
            heads[depth] = heads.get(depth, 0) + 1
            title = head.group(2).strip()
            if "(" in title:
                parens.append(i + 1)
            if title.rstrip().endswith((".", ":", ";", "?", "!")):
                punct.append(i + 1)
            if depth > 3:
                deep.append(i + 1)
            if CONTENTS_TITLE.match(title):
                contents.append(i + 1)
            in_table = False
            continue
        bullet = BULLET.match(line)
        if bullet:
            markers[bullet.group(1)] = markers.get(bullet.group(1), 0) + 1
        elif ORDERED.match(line):
            ordered += 1
        if TABLE_ROW.match(line):
            if not in_table:
                tables += 1
                in_table = True
        else:
            in_table = False
        for hit in MARKER.finditer(stripped):
            marker_hits.append((i + 1, hit.group(1)))
        for url in LINK.findall(line):
            if url.startswith(("http://", "https://", "mailto:")):
                continue
            if url.startswith("#"):
                anchors.append(i + 1)
                continue
            links.append((i + 1, url))
            target = url.split("#", 1)[0].split("?", 1)[0]
            if target and not (path.parent / target).resolve().exists():
                missing.append(i + 1)

    print(f"FILE {path}")
    print(f"  lines: {len(lines)}")
    print(f"  bytes: {len(text.encode('utf-8'))}")
    print("HEADINGS")
    print("  depth: " + (", ".join(f"H{d}: {heads.get(d, 0)}" for d in range(1, 7))))
    print(f"  depth>3: {refs(deep)}")
    print(f"  parenthesized: {refs(parens)}")
    print(f"  trailing punctuation: {refs(punct)}")
    print("CONTENTS")
    print(f"  contents section: {'present at ' + str(contents[0]) if contents else 'absent'}")
    print("LISTS")
    print("  bullets: " + (", ".join(f"{k}: {v}" for k, v in sorted(markers.items())) or "none"))
    print(f"  ordered items: {ordered}")
    odd = [k for k in markers if k != "-"]
    print(f"  non-dash markers: {', '.join(odd) if odd else 'none'}")
    print("FENCED BLOCKS")
    tags: dict[str, int] = {}
    for _, tag in blocks:
        key = tag.strip() or "untagged"
        tags[key] = tags.get(key, 0) + 1
    print(f"  total: {len(blocks)}")
    print("  by tag: " + (", ".join(f"{k}: {v}" for k, v in sorted(tags.items())) or "none"))
    print(f"  markdown payloads: {payloads}")
    print("CHARACTERS")
    for ch, name in SPECIALS.items():
        hits = specials.get(ch, [])
        print(f"  {name}: {len(hits)}" + (f" (lines {refs(hits)})" if hits else ""))
    print(f"  semicolons in prose: {len(semis)}" + (f" (lines {refs(semis)})" if semis else ""))
    print(f"  emoji: {len(set(emoji))} line(s)" + (f" (lines {refs(sorted(set(emoji)))})" if emoji else ""))
    if other_nonascii:
        print("  other non-ascii: " + ", ".join(f"{ch} U+{ord(ch):04X} x{n}" for ch, n in sorted(other_nonascii.items())))
    else:
        print("  other non-ascii: none")
    print("PARAGRAPHS")
    print(f"  multi-sentence lines: {len(multi)}" + (f" (lines {refs(multi)})" if multi else ""))
    print(f"  consecutive blank runs: {refs(blank_runs)}")
    print(f"  lines over {width}: {refs(wide)}")
    print("TABLES")
    print(f"  tables: {tables}")
    print("MARKERS")
    if marker_hits:
        counts: dict[str, int] = {}
        for _, m in marker_hits:
            counts[m] = counts.get(m, 0) + 1
        print("  hits: " + ", ".join(f"{m}: {n}" for m, n in sorted(counts.items())))
        print(f"  lines: {refs(sorted({ln for ln, _ in marker_hits}))}")
    else:
        print("  hits: none")
    print("LINKS")
    print(f"  internal links checked: {len(links)}")
    print(f"  anchor links (not resolved): {len(anchors)}")
    print(f"  missing targets: {refs(missing)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
