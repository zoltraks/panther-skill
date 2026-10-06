#!/usr/bin/env python3
"""Compare the structural fingerprint of a rendered document to its source.

Checks the translation/revision parity items of process/translate-document.md
mechanically: heading level sequence, fenced-block count and language tags,
table geometry, list item counts, HTML comment markers, inline code spans,
internal anchor links, and file-level whitespace and byte conventions.
Heading *text* is never compared - a faithful render rewords it.

Designed for a faithful render where structure is preserved one-to-one. For a
declared adapted render every delta is still reported - the audit decides
whether each one matches the adaptation contract.

Run this file in place from the skill repository -
`python <skill-root>/scripts/check-parity.py` - and pass the source document
followed by the rendered document. Copy it under a `.tmp.` name into the
working repository's `work/` directory only when the skill root cannot be
invoked, and remove the copy afterward.

Usage:
    python check-parity.py <source.md> <target.md> [--terms <glossary.md> ...]

With --terms, each given glossary's Terminology table (| English | Polish |)
is cross-counted: an English term appearing at least twice in the source but
with none of its Polish variants present in the target is reported as a NOTE -
a concordance hint, not a verdict, since context forms are legitimate.

Each check prints one PARITY, DELTA, or NOTE line; DELTA details follow
indented. Exit code is 0 when no DELTA was reported, 1 otherwise.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

FENCE = re.compile(r"^\s*(`{3,}|~{3,})\s*([\w-]*)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
INLINE_CODE = re.compile(r"`([^`\n]+)`")
ANCHOR_LINK = re.compile(r"\[[^\]]*\]\(#([^)\s]+)\)")
BULLET = re.compile(r"^\s*[-*+] ")
ORDERED = re.compile(r"^\s*\d+\. ")

TERM_HEADERS = {"english", "term", "source term"}


def reconfigure_stdio():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="backslashreplace")
        except Exception:
            pass


def read_doc(path):
    """Return (lines, raw_bytes) with universal-newline text."""
    raw = Path(path).read_bytes()
    text = raw.decode("utf-8")
    return text.replace("\r\n", "\n").replace("\r", "\n").split("\n"), raw


def fence_spans(lines):
    """Return list of (open_idx, close_idx, lang) for fenced blocks."""
    spans = []
    open_idx = None
    open_len = 0
    for i, line in enumerate(lines):
        match = FENCE.match(line)
        if not match:
            continue
        marker = match.group(1)
        if open_idx is None:
            open_idx = i
            open_len = len(marker)
            open_lang = match.group(2)
        elif len(marker) >= open_len and marker[0] == lines[open_idx].strip()[0]:
            spans.append((open_idx, i, open_lang))
            open_idx = None
    if open_idx is not None:
        spans.append((open_idx, len(lines), open_lang))
    return spans


def inside_spans(i, spans):
    return any(start <= i < end for start, end, _ in spans)


def headings(lines, spans):
    """Return [(line_no, level, text)] outside fenced blocks."""
    result = []
    for i, line in enumerate(lines):
        if inside_spans(i, spans):
            continue
        match = HEADING.match(line)
        if match:
            result.append((i + 1, len(match.group(1)), match.group(2)))
    return result


def slugify(text):
    """GitHub-style anchor slug: lowercase, drop punctuation, dash spaces."""
    slug = text.strip().lower()
    slug = re.sub(r"`", "", slug)
    slug = re.sub(r"[^\w\- ]", "", slug, flags=re.UNICODE)
    return slug.replace(" ", "-")


def tables(lines, spans):
    """Return [(line_no, rows, cols)] for pipe tables outside fences."""
    result = []
    i = 0
    while i < len(lines):
        if inside_spans(i, spans) or not lines[i].lstrip().startswith("|"):
            i += 1
            continue
        start = i
        while i < len(lines) and lines[i].lstrip().startswith("|"):
            i += 1
        block = lines[start:i]
        cols = max(
            len([c for c in row.strip().strip("|").split("|")])
            for row in block
        )
        result.append((start + 1, len(block), cols))
    return result


def list_counts(lines, spans):
    bullets = ordered = 0
    for i, line in enumerate(lines):
        if inside_spans(i, spans):
            continue
        if BULLET.match(line):
            bullets += 1
        elif ORDERED.match(line):
            ordered += 1
    return bullets, ordered


def html_comments(text):
    """Return all HTML comment bodies (single or multi-line)."""
    return re.findall(r"<!--(.*?)-->", text, re.S)


def code_spans(lines, spans):
    """Multiset of inline code spans outside fenced blocks."""
    found = []
    for i, line in enumerate(lines):
        if inside_spans(i, spans):
            continue
        found.extend(INLINE_CODE.findall(line))
    return Counter(found)


def load_terms(paths):
    """Parse glossary Terminology tables. Returns [(english, [polish...])]."""
    pairs = []
    seen = set()
    for path in paths:
        p = Path(path)
        if not p.exists():
            continue
        in_table = False
        for line in p.read_text(encoding="utf-8").split("\n"):
            cells = [c.strip() for c in line.split("|")]
            if line.startswith("|") and len(cells) >= 4:
                if cells[1].strip("`").lower() in TERM_HEADERS:
                    in_table = True
                    continue
                if in_table:
                    if set(cells[1] + cells[2]) <= set("- "):
                        continue
                    eng = re.sub(r"\(.*?\)", "", cells[1]).strip("`").strip()
                    pol = re.sub(r"\(.*?\)", "", cells[2]).strip("`").strip()
                    if eng and pol:
                        variants = [
                            v.strip().strip("`")
                            for v in re.split(r"\s+/\s+", pol)
                            if v.strip()
                        ]
                        key = eng.lower()
                        if key and variants and key not in seen:
                            seen.add(key)
                            pairs.append((eng, variants))
            elif in_table:
                in_table = False
    return pairs


def count_term(text_lower, term):
    """Word-boundary count of a possibly multiword term in lowered text."""
    pattern = re.compile(r"(?<!\w)" + re.escape(term.lower()) + r"(?!\w)")
    return len(pattern.findall(text_lower))


def count_variant(text_lower, variant):
    """Stem-prefix count - inflected forms of the preferred variant count.

    Each word of the variant keeps a stem of at least 4 characters (or 3 for
    short words) and is allowed any suffix, so `aplikacji`, `aplikację`, and
    `aplikacjach` all count for `aplikacja`.
    """
    words = variant.lower().split()
    stemmed = [
        re.escape(w if len(w) <= 4 else w[:-1]) + r"\w*" for w in words
    ]
    pattern = re.compile(r"(?<!\w)" + r"\s+".join(stemmed) + r"(?!\w)")
    return len(pattern.findall(text_lower))


def looks_technical(span):
    """A code span that names a path, identifier, or fixed machine value."""
    if any(c in span for c in "/\\._-=:()[]{}<>|&%$#@!~^*+;?'"):
        return True
    if " " not in span.strip():
        return True
    return bool(re.search(r"[\dA-Z]", span))


def code_diff(src_counter, tgt_counter, limit=10):
    """Split the missing-spans diff into technical deltas and prose notes."""
    missing = src_counter - tgt_counter
    extra = tgt_counter - src_counter
    deltas, notes = [], []
    for span, n in list(missing.items()):
        target = deltas if looks_technical(span) else notes
        target.append(f"missing in target x{n}: `{span[:80]}`")
    extra_list = [
        f"extra in target x{n}: `{span[:80]}`" for span, n in extra.items()
    ]
    if len(extra_list) > limit:
        extra_list = extra_list[:limit] + [
            f"... and {len(extra.items()) - limit} more"]
    notes.extend(extra_list)
    return deltas[:limit], notes[:limit]


def report(deltas, label, ok_msg, details):
    if details:
        deltas.append(label)
        print(f"DELTA {label} - {ok_msg}")
        for detail in details:
            print(f"    {detail}")
    else:
        print(f"PARITY {label} - {ok_msg}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    parser.add_argument("--terms", type=Path, action="append", default=[],
                        metavar="GLOSSARY",
                        help="glossary file with a Terminology table for a "
                             "concordance hint report")
    args = parser.parse_args()

    src_lines, src_raw = read_doc(args.source)
    tgt_lines, tgt_raw = read_doc(args.target)
    src_text = "\n".join(src_lines)
    tgt_text = "\n".join(tgt_lines)
    src_spans = fence_spans(src_lines)
    tgt_spans = fence_spans(tgt_lines)
    deltas = []

    print(f"check-parity: {args.source} vs {args.target}")

    # Line count
    details = []
    if len(src_lines) != len(tgt_lines):
        details.append(
            f"source {len(src_lines)} lines, target {len(tgt_lines)} lines")
    report(deltas, "line count",
           f"source {len(src_lines)}, target {len(tgt_lines)}", details)

    # Headings: level sequence
    src_heads = headings(src_lines, src_spans)
    tgt_heads = headings(tgt_lines, tgt_spans)
    src_seq = [level for _, level, _ in src_heads]
    tgt_seq = [level for _, level, _ in tgt_heads]
    details = []
    if len(src_seq) != len(tgt_seq):
        details.append(f"source has {len(src_seq)} headings, "
                       f"target has {len(tgt_heads)}")
    for pos, (a, b) in enumerate(zip(src_seq, tgt_seq)):
        if a != b:
            details.append(
                f"first level divergence at heading #{pos + 1}: "
                f"source line {src_heads[pos][0]} is H{a}, "
                f"target line {tgt_heads[pos][0]} is H{b}")
            break
    report(deltas, "headings",
           f"{len(src_seq)} source / {len(tgt_seq)} target, "
           "level sequence " +
           ("identical" if src_seq == tgt_seq else "differs"), details)

    # Fences: count and language-tag sequence of openers
    src_tags = [lang for _, _, lang in src_spans]
    tgt_tags = [lang for _, _, lang in tgt_spans]
    details = []
    if len(src_tags) != len(tgt_tags):
        details.append(f"source has {len(src_tags)} fenced blocks, "
                       f"target has {len(tgt_spans)}")
    for pos, (a, b) in enumerate(zip(src_tags, tgt_tags)):
        if a != b:
            details.append(
                f"block #{pos + 1} tag differs: source "
                f"'{a or '(untagged)'}' at line {src_spans[pos][0] + 1}, "
                f"target '{b or '(untagged)'}' at line "
                f"{tgt_spans[pos][0] + 1}")
            break
    if src_tags and tgt_tags and len(src_tags) != len(tgt_tags):
        longer, shorter = (tgt_spans, src_spans) \
            if len(tgt_tags) > len(src_tags) else (src_spans, tgt_spans)
        side = "target" if len(tgt_tags) > len(src_tags) else "source"
        for extra in longer[len(shorter):]:
            details.append(f"extra fenced block in {side} opened at "
                           f"line {extra[0] + 1}")
    report(deltas, "fences",
           f"{len(src_tags)} source / {len(tgt_tags)} target blocks",
           details)

    # Tables: count and geometry
    src_tabs = tables(src_lines, src_spans)
    tgt_tabs = tables(tgt_lines, tgt_spans)
    details = []
    if len(src_tabs) != len(tgt_tabs):
        details.append(f"source has {len(src_tabs)} tables, "
                       f"target has {len(tgt_tabs)}")
    for pos, (a, b) in enumerate(zip(src_tabs, tgt_tabs)):
        if (a[1], a[2]) != (b[1], b[2]):
            details.append(
                f"table #{pos + 1} geometry differs: source "
                f"{a[1]}x{a[2]} at line {a[0]}, target {b[1]}x{b[2]} "
                f"at line {b[0]}")
    report(deltas, "tables",
           f"{len(src_tabs)} source / {len(tgt_tabs)} target", details)

    # Lists: item counts
    src_b, src_o = list_counts(src_lines, src_spans)
    tgt_b, tgt_o = list_counts(tgt_lines, tgt_spans)
    details = []
    if src_b != tgt_b:
        details.append(f"bullet items: source {src_b}, target {tgt_b}")
    if src_o != tgt_o:
        details.append(f"ordered items: source {src_o}, target {tgt_o}")
    report(deltas, "lists",
           f"bullets {src_b}/{tgt_b}, ordered {src_o}/{tgt_o}", details)

    # HTML comments: byte-identical bodies
    src_com = [c.strip() for c in html_comments(src_text)]
    tgt_com = [c.strip() for c in html_comments(tgt_text)]
    details = []
    if len(src_com) != len(tgt_com):
        details.append(f"source has {len(src_com)} comments, "
                       f"target has {len(tgt_com)}")
    for pos, (a, b) in enumerate(zip(src_com, tgt_com)):
        if a != b:
            details.append(f"comment #{pos + 1} differs: "
                           f"'{a[:60]}' vs '{b[:60]}'")
    report(deltas, "html comments",
           f"{len(src_com)} source / {len(tgt_com)} target", details)

    # Inline code spans: technical spans must survive byte-identical;
    # prose-like spans may legitimately differ (translated label text)
    src_code = code_spans(src_lines, src_spans)
    tgt_code = code_spans(tgt_lines, tgt_spans)
    code_deltas, code_notes = code_diff(src_code, tgt_code)
    report(deltas, "inline code",
           f"{sum(src_code.values())} source spans / "
           f"{sum(tgt_code.values())} target spans", code_deltas)
    for note in code_notes:
        print(f"NOTE inline code - {note}")

    # Anchors: every #anchor link in target resolves against target headings
    tgt_anchors = ANCHOR_LINK.findall(tgt_text)
    src_anchors = ANCHOR_LINK.findall(src_text)
    tgt_slugs = {slugify(text) for _, _, text in tgt_heads}
    seen = set()
    details = []
    for anchor in tgt_anchors:
        if anchor not in tgt_slugs and anchor not in seen:
            seen.add(anchor)
            details.append(f"unresolved anchor in target: '#{anchor}'")
    if len(src_anchors) != len(tgt_anchors):
        details.append(f"anchor links: source {len(src_anchors)}, "
                       f"target {len(tgt_anchors)}")
    report(deltas, "anchors",
           f"{len(tgt_anchors)} links, {len(tgt_slugs)} target slugs",
           details)

    # Whitespace and byte conventions
    details = []
    src_trail = sum(1 for l in src_lines if l != l.rstrip(" \t"))
    tgt_trail = sum(1 for l in tgt_lines if l != l.rstrip(" \t"))
    if tgt_trail:
        details.append(f"target has {tgt_trail} line(s) with trailing "
                       f"whitespace (source has {src_trail})")
    src_blanks = sum(
        1 for a, b in zip(src_lines, src_lines[1:]) if not a.strip() and not b.strip())
    tgt_blanks = sum(
        1 for a, b in zip(tgt_lines, tgt_lines[1:]) if not a.strip() and not b.strip())
    if src_blanks != tgt_blanks:
        details.append(f"consecutive-blank-line runs: source {src_blanks}, "
                       f"target {tgt_blanks}")
    src_eof = src_raw.endswith(b"\n") and not src_raw.endswith(b"\n\n")
    tgt_eof = tgt_raw.endswith(b"\n") and not tgt_raw.endswith(b"\n\n")
    if src_eof != tgt_eof:
        details.append("EOF newline convention differs: source "
                       + ("single-LF" if src_eof else "other")
                       + ", target "
                       + ("single-LF" if tgt_eof else "other"))
    src_crlf = b"\r\n" in src_raw
    tgt_crlf = b"\r\n" in tgt_raw
    if src_crlf != tgt_crlf:
        details.append("line-ending style differs: source "
                       + ("CRLF" if src_crlf else "LF") + ", target "
                       + ("CRLF" if tgt_crlf else "LF"))
    src_bom = src_raw.startswith(b"\xef\xbb\xbf")
    tgt_bom = tgt_raw.startswith(b"\xef\xbb\xbf")
    if src_bom != tgt_bom:
        details.append("BOM presence differs")
    report(deltas, "whitespace/bytes",
           "file-level conventions compared", details)

    # Glossary concordance hints
    for terms_path in args.terms:
        pairs = load_terms([terms_path])
        if not pairs:
            print(f"NOTE terms - no Terminology table found in {terms_path}")
            continue
        src_lower = src_text.lower()
        tgt_lower = tgt_text.lower()
        misses = 0
        for eng, variants in pairs:
            if count_term(src_lower, eng) < 2:
                continue
            if not any(count_variant(tgt_lower, v) for v in variants):
                misses += 1
                print(f"NOTE term '{eng}' - appears "
                      f"{count_term(src_lower, eng)}x in source but no "
                      f"preferred variant ({' / '.join(variants)[:60]}) "
                      "found in target")
        print(f"PARITY terms ({terms_path.name}) - {len(pairs)} entries "
              f"scanned, {misses} hint(s)")

    print(f"check-parity: {'FAIL' if deltas else 'PASS'} "
          f"({len(deltas)} delta categor{'y' if len(deltas) == 1 else 'ies'}"
          + (": " + ", ".join(deltas) if deltas else "") + ")")
    return 1 if deltas else 0


if __name__ == "__main__":
    reconfigure_stdio()
    sys.exit(main())
