#!/usr/bin/env python3
"""Reflow Markdown prose between wrapped and logical-line layouts.

Two directions exist:

--wrap    splits prose lines longer than --width at whitespace, preferring
          clause boundaries; continuation lines indent to the item's text
          column and blockquote continuations repeat the quote marker.

--unwrap  joins hard-wrapped continuation lines back into single logical
          lines inside paragraphs, list items, and blockquotes.

Both directions preserve the document's structure: fenced code blocks,
frontmatter, HTML comments, headings, tables, indented code blocks, setext
underlines, horizontal rules, and bold pseudo-headings stay opaque, and so
does every fenced block whose language is not `markdown` unless
--payload-markdown is given.

--unwrap only ever joins a line into the previous one when the accumulated
text does not end with sentence-final punctuation (`.`, `!`, `?`) or a
label colon (`:`), so separate sentences sharing one paragraph block stay
on their own lines - it converts wrapping, not sentence layout. Combine
with `split-sentences.py --paragraphs` when the task also asks for one
sentence per paragraph.

The wrap direction never joins lines and the unwrap direction never splits
them, so a document that already matches its own convention is unchanged.
Run `--unwrap --check` on a logical-line document to find wrapped
fragments, or `--wrap --check` on a wrapped document to find over-width
lines.

Copy this file into the working repository's `work/` directory (or the
repository root when no `work/` exists) as `reflow-prose.tmp.py`, run it on
the document file, then remove the copy.

Usage: python reflow-prose.py <file.md> (--wrap | --unwrap)
                                [--width N] [--payload-markdown] [--check]

  --wrap               split over-width prose lines (same algorithm as the
                       deprecated wrap-prose.py)
  --unwrap             join wrapped continuation lines into logical lines
  --width N            maximum line length for --wrap, default 100
  --payload-markdown   also process prose inside ```markdown fenced blocks
                       (embedded payload documents); other fence languages
                       always stay opaque
  --check              report findings without writing, exit 1 when the
                       file does not match the requested direction
"""

import argparse
import os
import re
import sys

FENCE = re.compile(r"^\s*(`{3,})\s*(\w*)")
ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])([ \t]+)(.*)$")
LONE_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s*$")
QUOTE = re.compile(r"^(\s*)((?:>\s*)+)(.*)$")
RULE_LINE = re.compile(r"^\s*(={2,}|-{2,}|\*{3,}|_{3,})\s*$")
PSEUDO_HEAD = re.compile(r"^\*{1,2}[^*\n]+\*{1,2}:?\s*$")
SENT_END = re.compile(r"[.!?:][\"')\]`}*]*\s*$")
LEAD_PUNCT = r"[(\[{'\"]*"
TRAIL_PUNCT = r"[\")\].,;:!?}\"]*(?:'[a-zA-Z]*)?[\"')\].,;:!?}]*"
PROTECTED = re.compile(
    r"(" + LEAD_PUNCT + r"`+[^`]*`+" + TRAIL_PUNCT + r")"           # code span + adjacent punct
    r"|(" + LEAD_PUNCT + r"\[[^]]*\]\([^)]*\)" + TRAIL_PUNCT + r")"  # inline link + adjacent punct
    r"|(https?://\S+)"                                              # bare URL
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
    """Prefer breaking after an atom ending with a clause-boundary mark.

    Returns (head_atoms, tail_atoms) or None when no good boundary exists.
    """
    for j in range(len(parts) - 1, 0, -1):
        head_len = len(" ".join(parts[: j + 1]))
        if head_len < width * 2 // 5:
            return None
        if parts[j].rstrip()[-1:] in BOUNDARY_END:
            return parts[: j + 1], parts[j + 1 :]
    return None


def wrap_line(line, width):
    """Split one logical line into physical lines no longer than width.

    The list marker or blockquote marker is part of the protected prefix and
    is never separated from the first atom. Continuation lines indent to the
    column where the item's text starts; blockquote continuations repeat the
    quote marker.
    """
    if len(line) <= width:
        return [line]
    item = ITEM.match(line) or LONE_ITEM.match(line)
    quote = QUOTE.match(line)
    if item:
        lead = item.group(1)
        marker = item.group(2) + (item.group(3) if item.lastindex >= 3 else "")
        body = item.group(4) if item.lastindex >= 4 else ""
        task = re.match(r"\[[ xX]\][ \t]+", body)
        if task:
            marker += task.group(0)
            body = body[task.end() :]
        cont = lead + " " * len(marker)
    elif quote:
        lead, marker = quote.group(1), quote.group(2)
        body = quote.group(3)
        cont = lead + marker
    else:
        lead = line[: len(line) - len(line.lstrip())]
        marker = ""
        body = line[len(lead) :]
        cont = lead
    prefix = lead + marker
    if not body.strip():
        return [line]
    out = []
    cur = prefix
    parts = []
    for atom in atoms(body):
        if not parts:
            cur = prefix + atom
            parts = [atom]
            continue
        if len(cur) + 1 + len(atom) <= width:
            cur += " " + atom
            parts.append(atom)
            continue
        split = boundary_split(parts, width - len(prefix))
        if split:
            head, tail = split
            out.append((prefix if not out else cont) + " ".join(head))
            carry = tail + [atom]
        else:
            out.append(cur)
            carry = [atom]
        cur = cont + carry[0]
        parts = [carry[0]]
        for extra in carry[1:]:
            if len(cur) + 1 + len(extra) <= width:
                cur += " " + extra
                parts.append(extra)
            else:
                out.append(cur)
                cur = cont + extra
                parts = [extra]
    out.append(cur)
    return out


def processable(fences, payload_markdown):
    """A line is prose when every open fence is a markdown payload fence."""
    if not fences:
        return True
    if not payload_markdown:
        return False
    return all(lang == "markdown" for _, lang in fences)


def main(path, mode, width, payload_markdown, check_only):
    raw = open(path, "rb").read()
    crlf = b"\r\n" in raw
    try:
        text, encoding = decode(raw)
    except UnicodeDecodeError:
        print(f"FAIL {path}: not decodable as UTF-8 or UTF-16, "
              "check encoding first (see conventions/file-encoding.md)")
        return 1
    lines = text.replace("\r\n", "\n").split("\n")

    out = []
    fences = []          # stack of (marker length, language)
    in_front = lines[0].strip() == "---" if lines else False
    in_comment = False
    list_stack = []      # content columns of open list items
    wrapped = 0
    unbreakable = []
    joins = []           # unwrap: line numbers merged into a previous line
    open_ok = False      # unwrap: last emitted line may absorb a continuation
    open_min = 0         # unwrap: minimum indent a continuation must reach
    open_quote = False   # unwrap: last emitted line is a quote line

    for n, line in enumerate(lines, 1):
        s = line.strip()
        indent = len(line) - len(line.lstrip())

        fence = FENCE.match(line)
        if fence:
            marker_len, lang = len(fence.group(1)), fence.group(2)
            if fences:
                if marker_len >= fences[-1][0]:
                    fences.pop()
            else:
                fences.append((marker_len, lang))
            list_stack = []
            open_ok = False
            out.append(line)
            continue

        if in_front:
            if n != 1 and s == "---":
                in_front = False
            out.append(line)
            open_ok = False
            continue

        if in_comment:
            if "-->" in line:
                in_comment = False
            out.append(line)
            open_ok = False
            continue
        if s.startswith("<!--") or ("<!--" in line and "-->" not in line):
            in_comment = "-->" not in line
            out.append(line)
            open_ok = False
            continue

        if not processable(fences, payload_markdown):
            out.append(line)
            open_ok = False
            continue

        if not s:
            out.append(line)
            open_ok = False
            continue

        item = ITEM.match(line)
        quote = QUOTE.match(line)

        if mode == "wrap":
            if item:
                content_col = indent + len(item.group(2)) + len(item.group(3))
                while list_stack and list_stack[-1] > indent:
                    list_stack.pop()
                list_stack.append(content_col)
            else:
                while list_stack and indent < list_stack[-1]:
                    list_stack.pop()
                base = list_stack[-1] if list_stack else 0
                if s.startswith(("#", "|")) or indent >= base + 4:
                    out.append(line)    # heading, table row, or indented code
                    continue
            if len(line) > width:
                if check_only:
                    unbreakable.append((n, len(line), line.strip()[:60]))
                else:
                    parts = wrap_line(line, width)
                    if len(parts) > 1:
                        wrapped += 1
                    for piece in parts:
                        if len(piece) > width:
                            unbreakable.append((n, len(piece), piece.strip()[:60]))
                    out.extend(parts)
                    continue
            out.append(line)
            continue

        # --unwrap mode below this point
        if item or LONE_ITEM.match(line):
            # A list item never joins a previous line, it starts a new
            # logical line whose continuations align to its text column.
            if item:
                content_col = indent + len(item.group(2)) + len(item.group(3))
                task = re.match(r"\[[ xX]\][ \t]+", item.group(4))
                if task:
                    content_col += len(task.group(0))
                while list_stack and list_stack[-1] > indent:
                    list_stack.pop()
                list_stack.append(content_col)
                open_ok = not SENT_END.search(item.group(4).strip())
            else:
                open_ok = False
                content_col = indent
            open_min = content_col
            open_quote = False
            out.append(line)
            continue

        while list_stack and indent < list_stack[-1]:
            list_stack.pop()
        base = list_stack[-1] if list_stack else 0

        if quote:
            body = quote.group(3).strip()
            if open_ok and open_quote:
                out[-1] = out[-1].rstrip() + " " + body
                joins.append(n)
                open_ok = not SENT_END.search(body)
                continue
            out.append(line)
            open_ok = not SENT_END.search(body)
            open_min = indent
            open_quote = True
            continue

        if s.startswith(("#", "|", "<")) or RULE_LINE.match(s) or \
                PSEUDO_HEAD.match(s) or indent >= base + 4:
            # heading, table row, HTML line, horizontal rule or setext
            # underline, pseudo-heading, or indented code block
            out.append(line)
            open_ok = False
            continue

        if open_ok and not open_quote and open_min <= indent < open_min + 4:
            out[-1] = out[-1].rstrip() + " " + s
            joins.append(n)
            open_ok = not SENT_END.search(s)
            continue

        out.append(line)
        open_ok = not SENT_END.search(s)
        open_min = indent
        open_quote = False

    if check_only:
        if mode == "wrap":
            for n, size, preview in unbreakable:
                print(f"line {n}: {size} chars > {width}: {preview}...")
            if unbreakable:
                print(f"{len(unbreakable)} line(s) exceed {width}")
                return 1
            print(f"PASS {path}: no line exceeds {width}")
            return 0
        for n in joins:
            print(f"line {n}: wrapped continuation joins into a previous line")
        if joins:
            print(f"{len(joins)} line(s) would join")
            return 1
        print(f"PASS {path}: no wrapped continuations")
        return 0

    eol = "\r\n" if crlf else "\n"
    tmp = path + ".tmp-write"
    try:
        with open(tmp, "wb") as handle:
            handle.write(eol.join(out).encode(encoding))
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)
    if mode == "wrap":
        print(f"wrapped {wrapped} lines to width {width}")
        for n, size, preview in unbreakable:
            print(f"note: line {n} still {size} chars (unbreakable span): {preview}...")
    else:
        print(f"unwrapped {len(joins)} continuation line(s)")
        for n in joins[:20]:
            print(f"note: line {n} joined into a previous line")
        if len(joins) > 20:
            print(f"note: ... and {len(joins) - 20} more")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Reflow Markdown prose: wrap to a width or unwrap "
                    "wrapped continuations into logical lines."
    )
    parser.add_argument("file")
    direction = parser.add_mutually_exclusive_group(required=True)
    direction.add_argument("--wrap", action="store_true")
    direction.add_argument("--unwrap", action="store_true")
    parser.add_argument("--width", type=int, default=100)
    parser.add_argument("--payload-markdown", action="store_true")
    parser.add_argument("--check", action="store_true")
    parsed = parser.parse_args()
    mode = "wrap" if parsed.wrap else "unwrap"
    raise SystemExit(
        main(parsed.file, mode, parsed.width, parsed.payload_markdown,
             parsed.check)
    )
