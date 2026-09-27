#!/usr/bin/env python3
"""Split packed sentences inside prose paragraphs onto individual logical lines.

Documents that follow the one-sentence-per-paragraph convention may contain
lines packing two or more sentences, either written that way or produced by a
mechanical rewrap. The tool detects mid-line sentence boundaries inside plain
paragraph blocks and emits each sentence starting on its own line, re-wrapping
the affected sentences to the document's width convention.

Only plain paragraph blocks are processed. List items and their continuation
lines, headings, tables, blockquotes, fenced blocks, indented code, HTML
comments, and frontmatter stay opaque - packed sentences inside list items are
an element-level convention, not a defect (see
conventions/markdown-dialects.md).

Copy this file into the working repository's `work/` directory (or the
repository root when no `work/` exists) as `split-sentences.tmp.py`, run it on
the document file, then remove the copy.

Usage: python split-sentences.py <file.md> [--check] [--width N]
                                   [--payload-markdown]

  --check              report lines carrying a mid-line sentence boundary
                       without writing, exit 1 when any exist
  --width N            re-wrap split sentences to this limit, default 100
  --payload-markdown   also process prose inside ```markdown fenced blocks
                       (embedded payload documents); other fence languages
                       always stay opaque
"""

import argparse
import re
import sys

FENCE = re.compile(r"^\s*(`{3,})\s*(\w*)")
ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])([ \t]+)(.*)$")
LONE_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s*$")
QUOTE = re.compile(r"^(\s*)((?:>\s*)+)(.*)$")
HEADING = re.compile(r"^\s*#")
CODE_SPAN = re.compile(r"`+[^`]*`+")
BOUNDARY = re.compile(r"[.!?][\"')\]]*\s+(?=[A-Z\"'(\[*`0-9])")
ABBR = re.compile(
    r"(e\.g|i\.e|etc|vs|cf|approx|No|Nos|Fig|fig|Dr|Mr|Mrs|St"
    r"|vol|pp|sec|al|ed)\.\s*$"
)
TERMINAL = re.compile(r"[.!?:][\"')\]]*$")

LEAD_PUNCT = r"[(\[{'\"]*"
TRAIL_PUNCT = r"[\")\].,;:!?}\"]*(?:'[a-zA-Z]*)?[\"')\].,;:!?}]*"
PROTECTED = re.compile(
    r"(" + LEAD_PUNCT + r"`+[^`]*`+" + TRAIL_PUNCT + r")"
    r"|(" + LEAD_PUNCT + r"\[[^]]*\]\([^)]*\)" + TRAIL_PUNCT + r")"
    r"|(https?://\S+)"
)
BOUNDARY_END = ",.:;?!)]}"


def decode(raw):
    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        return raw.decode("utf-16"), "utf-16"
    return raw.decode("utf-8"), "utf-8"


def atoms(text):
    """Split text into atoms. Protected spans are single unbreakable atoms."""
    result = []
    pos = 0
    for match in PROTECTED.finditer(text):
        result.extend(text[pos:match.start()].split(" "))
        result.append(match.group(0))
        pos = match.end()
    result.extend(text[pos:].split(" "))
    return [a for a in result if a != ""]


def boundary_split(parts, width):
    """Prefer breaking after an atom ending with a clause-boundary mark."""
    for j in range(len(parts) - 1, 0, -1):
        head_len = len(" ".join(parts[: j + 1]))
        if head_len < width * 2 // 5:
            return None
        if parts[j].rstrip()[-1:] in BOUNDARY_END:
            return parts[: j + 1], parts[j + 1 :]
    return None


def wrap_text(text, width):
    """Wrap one sentence's text into physical lines no longer than width."""
    if len(text) <= width:
        return [text]
    out = []
    cur = ""
    parts = []
    for atom in atoms(text):
        if not parts:
            cur, parts = atom, [atom]
            continue
        if len(cur) + 1 + len(atom) <= width:
            cur += " " + atom
            parts.append(atom)
            continue
        split = boundary_split(parts, width)
        if split:
            head, tail = split
            out.append(" ".join(head))
            carry = tail + [atom]
        else:
            out.append(cur)
            carry = [atom]
        cur = carry[0]
        parts = [carry[0]]
        for extra in carry[1:]:
            if len(cur) + 1 + len(extra) <= width:
                cur += " " + extra
                parts.append(extra)
            else:
                out.append(cur)
                cur = extra
                parts = [extra]
    out.append(cur)
    return out


def boundary_positions(line):
    """Column positions where a new sentence starts inside the line."""
    spans = [(m.start(), m.end()) for m in CODE_SPAN.finditer(line)]
    out = []
    for m in BOUNDARY.finditer(line):
        if any(s <= m.start() < e for s, e in spans):
            continue
        if ABBR.search(line[: m.end()].rstrip()):
            continue
        out.append(m.end())
    return out


def split_line(line):
    """Split a line at its mid-line sentence boundary positions."""
    pts = boundary_positions(line)
    if not pts:
        return [line]
    out = []
    prev = 0
    for p in pts:
        out.append(line[prev:p].rstrip())
        prev = p
    out.append(line[prev:])
    return out


def processable(fences, payload_markdown):
    """A line is prose when every open fence is a markdown payload fence."""
    if not fences:
        return True
    if not payload_markdown:
        return False
    return all(lang == "markdown" for _, lang in fences)


def paragraph_line(line, list_stack):
    """A split candidate: unindented prose that is not a structural element."""
    if not line.strip():
        return False
    if line != line.lstrip():
        return False                     # list continuation or indented code
    if ITEM.match(line) or LONE_ITEM.match(line):
        return False                     # list item
    if QUOTE.match(line):
        return False                     # blockquote
    if HEADING.match(line):
        return False                     # heading
    if line.startswith("|"):
        return False                     # table row
    if list_stack and list_stack[-1] > 0:
        return False                     # inside a list's content column
    return True


def main(path, width, payload_markdown, check_only):
    raw = open(path, "rb").read()
    crlf = b"\r\n" in raw
    try:
        text, encoding = decode(raw)
    except UnicodeDecodeError:
        print(f"FAIL {path}: not decodable as UTF-8 or UTF-16, "
              "check encoding first (see conventions/file-encoding.md)")
        return 1
    lines = text.replace("\r\n", "\n").split("\n")

    # Pass 1 - classify every line and collect paragraph blocks.
    kind = {}
    fences = []
    in_front = lines[0].strip() == "---" if lines else False
    in_comment = False
    list_stack = []
    for n, line in enumerate(lines, 1):
        s = line.strip()
        indent = len(line) - len(line.lstrip())

        fence = FENCE.match(line)
        if fence:
            marker_len, lang = len(fence.group(1)), fence.group(2)
            if fences and marker_len >= fences[-1][0]:
                fences.pop()
            else:
                fences.append((marker_len, lang))
            list_stack = []
            kind[n] = "FENCE"
            continue
        if in_front:
            if n != 1 and s == "---":
                in_front = False
            kind[n] = "FRONT"
            continue
        if in_comment:
            if "-->" in line:
                in_comment = False
            kind[n] = "HTML"
            continue
        if s.startswith("<!--") or ("<!--" in line and "-->" not in line):
            in_comment = "-->" not in line
            kind[n] = "HTML"
            continue
        if not processable(fences, payload_markdown):
            kind[n] = "OPAQUE"
            continue
        if not s:
            kind[n] = "BLANK"
            continue
        item = ITEM.match(line)
        if item:
            content_col = indent + len(item.group(2)) + len(item.group(3))
            while list_stack and list_stack[-1] > indent:
                list_stack.pop()
            list_stack.append(content_col)
            kind[n] = "ITEM"
            continue
        while list_stack and indent < list_stack[-1]:
            list_stack.pop()
        if paragraph_line(line, list_stack):
            kind[n] = "PARA"
        else:
            kind[n] = "OPAQUE"

    blocks = []
    cur_block = []
    for n in range(1, len(lines) + 1):
        if kind[n] == "PARA":
            cur_block.append(n)
        else:
            if cur_block:
                blocks.append(cur_block)
                cur_block = []
    if cur_block:
        blocks.append(cur_block)

    if check_only:
        found = []
        for b in blocks:
            for n in b:
                if len(split_line(lines[n - 1])) > 1:
                    found.append(n)
        for n in found:
            print(f"line {n}: mid-line sentence boundary: "
                  f"{lines[n - 1].strip()[:60]}...")
        if found:
            print(f"{len(found)} line(s) pack multiple sentences")
            return 1
        print(f"PASS {path}: every paragraph sentence starts on a line")
        return 0

    # Pass 2 - rebuild the flagged blocks one sentence per logical line.
    repl = {}
    split_count = 0
    for b in blocks:
        segs_per_line = [(n, split_line(lines[n - 1])) for n in b]
        if not any(len(s) > 1 for _, s in segs_per_line):
            continue
        units = []
        cur_u = None
        for n, segs in segs_per_line:
            for k, seg in enumerate(segs):
                if cur_u is None:
                    cur_u = {"pieces": [], "dirty": k > 0}
                if k == 0 and len(segs) == 1:
                    cur_u["pieces"].append(("orig", n))
                else:
                    cur_u["pieces"].append(("text", seg))
                    cur_u["dirty"] = True
                if TERMINAL.search(seg.strip()):
                    units.append(cur_u)
                    cur_u = None
        if cur_u:
            units.append(cur_u)
        out_b = []
        for u in units:
            if not u["dirty"]:
                out_b.extend(lines[v - 1] for _, v in u["pieces"])
            else:
                split_count += 1
                text = " ".join(
                    (lines[v - 1] if p == "orig" else v).strip()
                    for p, v in u["pieces"]
                ).strip()
                if text:
                    out_b.extend(wrap_text(text, width))
        repl[b[0]] = out_b

    if not repl:
        print(f"PASS {path}: every paragraph sentence starts on a line")
        return 0

    block_starts = {b[0]: b for b in blocks}
    result = []
    i = 1
    while i <= len(lines):
        if i in repl:
            result.extend(repl[i])
            i += len(block_starts[i])
        else:
            result.append(lines[i - 1])
            i += 1

    eol = "\r\n" if crlf else "\n"
    open(path, "wb").write(eol.join(result).encode(encoding))
    print(f"split {split_count} sentence(s) across {len(repl)} paragraph block(s)")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Split packed sentences onto individual logical lines."
    )
    parser.add_argument("file")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--width", type=int, default=100)
    parser.add_argument("--payload-markdown", action="store_true")
    parsed = parser.parse_args()
    raise SystemExit(
        main(parsed.file, parsed.width, parsed.payload_markdown, parsed.check)
    )
