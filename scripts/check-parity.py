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

Each check prints one PARITY, DELTA, DECLARED, or NOTE line; DELTA details
follow indented. Exit code is 0 when no DELTA was reported, 1 otherwise.

With --expect-map <file>, deltas the map declares report as DECLARED notes
instead of DELTA failures. The file lists one `SRC -> TGT` pair per line -
`#` comments and blank lines allowed, surrounding backticks stripped, and
` / ` separates alternative targets - plus `link:#anchor -> -N` or `+N`
lines declaring an expected change in that anchor's link count. Glossary
files passed through --terms seed the same map: a source term's preferred
variants are expected renderings, not losses.

With --eol lf|crlf, or a `.gitattributes` `eol=` declaration found walking
up from the target, a line-ending delta that matches the declared
convention reports as NOTE instead of DELTA.

Usage:
    python check-parity.py <source.md> <target.md> [--terms <glossary.md> ...]
        [--expect-map <file> ...] [--eol lf|crlf]
"""

import argparse
import fnmatch
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
    """Multiset of inline code spans outside fenced blocks, with line refs.

    Returns (Counter of span text, {span text: [1-based line numbers]}).
    Spans inside fenced blocks are excluded from both files - a fence that
    opens or closes differently in the translation shifts spans between the
    inline and fenced contexts and surfaces as a genuine count delta.
    """
    found = []
    locations = {}
    for i, line in enumerate(lines):
        if inside_spans(i, spans):
            continue
        for span in INLINE_CODE.findall(line):
            found.append(span)
            locations.setdefault(span, []).append(i + 1)
    return Counter(found), locations


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


def code_diff(src_counter, tgt_counter, expected, src_loc, tgt_loc,
              tgt_text_lower, limit=10):
    """Split the missing-spans diff into declared, technical, prose groups.

    `expected` maps lowercased source spans to lists of declared target
    renderings. A missing span whose declared target occurs in the target
    text reports as DECLARED, as does an extra span that is the declared
    rendering of a missing source span.
    """
    missing = src_counter - tgt_counter
    extra = tgt_counter - src_counter
    missing_srcs = {span.lower() for span in missing}
    variant_src = {variant.lower(): src
                   for src, variants in expected.items()
                   for variant in variants}
    declared, deltas, notes = [], [], []

    def refs(loc, span):
        lines = loc.get(span, [])[:6]
        return (" at line(s) " + ",".join(str(n) for n in lines)
                if lines else "")

    for span, n in list(missing.items()):
        target_variants = expected.get(span.lower(), [])
        hit = next((v for v in target_variants
                    if count_term(tgt_text_lower, v) > 0), None)
        if hit is not None:
            declared.append(
                f"missing in target x{n}: `{span[:80]}` renders as "
                f"declared `{hit}`{refs(src_loc, span)}")
            continue
        detail = f"missing in target x{n}: `{span[:80]}`{refs(src_loc, span)}"
        if target_variants:
            detail += (" - declared target(s) "
                       f"{', '.join(target_variants)[:60]} not found")
        (deltas if looks_technical(span) else notes).append(detail)
    extra_list = []
    for span, n in extra.items():
        src = variant_src.get(span.lower())
        if src is not None and src in missing_srcs:
            original = next(
                s for s in missing if s.lower() == src)
            declared.append(
                f"extra in target x{n}: `{span[:80]}` is declared "
                f"rendering of `{original[:80]}`{refs(tgt_loc, span)}")
            continue
        extra_list.append(f"extra in target x{n}: `{span[:80]}`"
                          f"{refs(tgt_loc, span)}")
    if len(extra_list) > limit:
        extra_list = extra_list[:limit] + [
            f"... and {len(extra.items()) - limit} more"]
    notes.extend(extra_list)
    return declared[:limit], deltas[:limit], notes[:limit]


def load_expect_map(paths):
    """Parse declared `SRC -> TGT` pairs and `link:` directives.

    File format: one `SRC -> TGT` pair per line, `#` comments and blank
    lines allowed, surrounding backticks stripped, ` / ` separating
    alternative targets. A `link:#anchor -> -N` or `+N` line declares an
    expected change in that anchor's link count. Returns
    ({src_lower: [targets]}, {anchor: signed delta}).
    """
    pairs = {}
    links = {}
    for path in paths:
        p = Path(path)
        if not p.exists():
            continue
        for raw in p.read_text(encoding="utf-8").split("\n"):
            line = raw.strip()
            if not line or line.startswith("#") or "->" not in line:
                continue
            left, right = [s.strip().strip("`").strip()
                           for s in line.split("->", 1)]
            if not left or not right:
                continue
            if left.lower().startswith("link:"):
                anchor = left[5:].lstrip("#").strip()
                try:
                    links[anchor] = links.get(anchor, 0) + int(right)
                except ValueError:
                    pass
                continue
            variants = [v.strip() for v in re.split(r"\s+/\s+", right)
                        if v.strip()]
            if variants:
                pairs.setdefault(left.lower(), []).extend(variants)
    return pairs, links


def declared_eol(target_path, override):
    """Resolve the declared line-ending convention for the target file.

    `--eol` wins; otherwise the nearest `.gitattributes` found walking up
    from the target declares `eol=lf|crlf` (or `text`/`text=auto` as
    "auto") for matching patterns. Returns 'lf', 'crlf', 'auto', or None.
    """
    if override:
        return override
    path = Path(target_path).resolve()
    attrs_file = None
    for directory in [path.parent, *path.parents]:
        probe = directory / ".gitattributes"
        if probe.is_file():
            attrs_file = probe
            break
    if attrs_file is None:
        return None
    name = path.name
    try:
        rel = path.relative_to(attrs_file.parent).as_posix()
    except ValueError:
        rel = name
    declared = None
    for raw_line in attrs_file.read_text(
            encoding="utf-8", errors="replace").split("\n"):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        pattern = parts[0]
        if "/" in pattern:
            matched = fnmatch.fnmatch(rel, pattern.lstrip("/"))
        else:
            matched = fnmatch.fnmatch(name, pattern)
        if not matched:
            continue
        for attr in parts[1:]:
            if attr.startswith("eol="):
                declared = attr[4:]
            elif attr in ("text", "text=auto"):
                declared = "auto"
            elif attr in ("-text", "-eol"):
                declared = None
    return declared


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
                        help="glossary file with a Terminology table - "
                             "drives the concordance hint report and seeds "
                             "the expected-translation map")
    parser.add_argument("--expect-map", type=Path, action="append",
                        default=[], metavar="FILE",
                        help="file of declared SRC -> TGT pairs and "
                             "link:#anchor -> +/-N directives - matching "
                             "deltas report as DECLARED, not DELTA")
    parser.add_argument("--eol", choices=["lf", "crlf"], default=None,
                        help="declared line-ending convention for the "
                             "target - a matching delta reports as NOTE "
                             "(overrides .gitattributes)")
    args = parser.parse_args()

    src_lines, src_raw = read_doc(args.source)
    tgt_lines, tgt_raw = read_doc(args.target)
    src_text = "\n".join(src_lines)
    tgt_text = "\n".join(tgt_lines)
    src_spans = fence_spans(src_lines)
    tgt_spans = fence_spans(tgt_lines)
    deltas = []
    declared_total = 0

    expected = {}
    for eng, variants in load_terms(args.terms):
        slot = expected.setdefault(eng.lower(), [])
        slot.extend(v for v in variants if v not in slot)
    map_pairs, link_deltas = load_expect_map(args.expect_map)
    for src, variants in map_pairs.items():
        slot = expected.setdefault(src, [])
        slot.extend(v for v in variants if v not in slot)

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
    # prose-like spans may legitimately differ (translated label text);
    # declared pairs report as DECLARED, not DELTA
    src_code, src_loc = code_spans(src_lines, src_spans)
    tgt_code, tgt_loc = code_spans(tgt_lines, tgt_spans)
    code_declared, code_deltas, code_notes = code_diff(
        src_code, tgt_code, expected, src_loc, tgt_loc, tgt_text.lower())
    report(deltas, "inline code",
           f"{sum(src_code.values())} source spans / "
           f"{sum(tgt_code.values())} target spans", code_deltas)
    for line in code_declared:
        print(f"DECLARED inline code - {line}")
    declared_total += len(code_declared)
    for note in code_notes:
        print(f"NOTE inline code - {note}")

    # Link markup integrity: a `]#` starved of its `(`, or a `](` never
    # closed, is a malformed link - the corruption class a scripted anchor
    # rewrite produces when it eats delimiters. Checked before resolution so
    # broken markup cannot masquerade as a missing anchor.
    details = []
    for bad in sorted(set(re.findall(r"\]#[^(]", tgt_text))):
        details.append(f"malformed link markup in target: ']{bad[1:]}' without '('")
    orphan = len(re.findall(r"\]\(", tgt_text)) - len(
        re.findall(r"\]\([^)]*\)", tgt_text)
    )
    if orphan > 0:
        details.append(f"malformed link markup in target: {orphan} ']( ' without closing ')'")

    # Anchors: every #anchor link in target resolves against target
    # headings, and per-anchor link counts match unless a link: directive
    # declares the change
    tgt_anchors = ANCHOR_LINK.findall(tgt_text)
    src_anchors = ANCHOR_LINK.findall(src_text)
    tgt_slugs = {slugify(text) for _, _, text in tgt_heads}
    seen = set()
    anchor_declared = []
    for anchor in tgt_anchors:
        if anchor not in tgt_slugs and anchor not in seen:
            seen.add(anchor)
            details.append(f"unresolved anchor in target: '#{anchor}'")
    src_by = Counter(src_anchors)
    tgt_by = Counter(tgt_anchors)
    for anchor in sorted(set(src_by) | set(tgt_by)):
        diff = tgt_by.get(anchor, 0) - src_by.get(anchor, 0)
        if diff == 0:
            continue
        declared_delta = link_deltas.get(anchor)
        if declared_delta is not None and diff == declared_delta:
            anchor_declared.append(
                f"anchor '#{anchor}' link count "
                f"{src_by.get(anchor, 0)} -> {tgt_by.get(anchor, 0)} "
                "as declared")
        else:
            details.append(
                f"anchor '#{anchor}' links: source "
                f"{src_by.get(anchor, 0)}, target {tgt_by.get(anchor, 0)}")
    report(deltas, "anchors",
           f"{len(tgt_anchors)} links, {len(tgt_slugs)} target slugs",
           details)
    for line in anchor_declared:
        print(f"DECLARED anchors - {line}")
    declared_total += len(anchor_declared)

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
        eol_detail = ("line-ending style differs: source "
                      + ("CRLF" if src_crlf else "LF") + ", target "
                      + ("CRLF" if tgt_crlf else "LF"))
        declared = declared_eol(args.target, args.eol)
        if declared == ("crlf" if tgt_crlf else "lf"):
            print(f"NOTE whitespace/bytes - {eol_detail} - matches "
                  f"declared eol={declared}")
        elif declared == "auto":
            print(f"NOTE whitespace/bytes - {eol_detail} - repository "
                  "declares text normalization, on-disk style follows "
                  "the checkout")
        elif declared is not None:
            details.append(eol_detail + f" - contradicts declared "
                           f"eol={declared}")
        else:
            details.append(eol_detail)
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

    verdict = (f"FAIL ({len(deltas)} delta categor"
               f"{'y' if len(deltas) == 1 else 'ies'}: "
               f"{', '.join(deltas)})" if deltas else "PASS")
    if declared_total:
        verdict += f" - {declared_total} declared delta(s)"
    print(f"check-parity: {verdict}")
    return 1 if deltas else 0


if __name__ == "__main__":
    reconfigure_stdio()
    sys.exit(main())
