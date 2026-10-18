#!/usr/bin/env python3
"""Check a document's internal references and terminology for consistency.

Two kinds of findings:

- ``UNRESOLVED``  - a quoted name in a reference context ("in \"Section
  Name\"", 'the "Term" section') matches no heading and no defined bold
  term. Errors; they fail the run.
- ``VARIANT``     - two similar names appear to denote one thing
  ("document and agent-entry tree" vs "document and agent structure
  tree"). Warnings; advisory only.

Quoted text counts as a reference only when the context signals one: a
connector word ("in", "see", "per", "the", "of", ...) precedes the quote,
or a noun such as "section" follows it. Single-word names need the strong
form; quoted literals ("write a README", the "none" option) are ignored.

Reference targets are the document's own anchors: every heading, plus
``**Term**:`` and ``| **Term** |`` definition rows - the bold-term style
procedure manuals use for glossary-like entries. Matching normalizes
case, punctuation, and hyphenation, so ``"Agent-Entry Tree"`` resolves to
the ``Agent Entry Tree`` heading.

With ``--payload-markdown``, anchors and references inside ```markdown
fenced blocks count too; other fence languages stay opaque.

Usage:

    check-consistency.py <file.md> [--payload-markdown] [--group-by-form]

Exits 1 on unresolved references, 0 otherwise.
"""

import argparse
import re
import sys
from pathlib import Path

CONNECTOR_STRONG = {
    "in", "see", "under", "per", "into", "through", "within", "from",
    "described", "defined", "named", "called", "section", "sections",
    "heading", "appendix", "subsection",
}
CONNECTOR_WEAK = {"the", "of", "to", "as", "via", "per"}
POST_NOUNS = ("section", "heading", "appendix", "subsection",
              "section.", "section,", "table")

QUOTE_RE = re.compile(r'"([A-Z][^"\n]{1,80})"')
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
BOLD_DEF_RE = re.compile(
    r"^\s*(?:[-*+]|\d+[.)])\s+\*\*([^*]{1,80})\*\*\s*[:—–-]")
BOLD_CELL_RE = re.compile(r"^\|\s*\*\*([^*]{1,80})\*\*\s*\|")
BOLD_ONLY_RE = re.compile(r"^\*\*([^*]{1,80})\*\*\s*:?\s*$")
WORD_RE = re.compile(r"[a-z0-9]+")


def norm(text):
    """Normalize a name: lowercase alnum tokens, hyphen/punct-insensitive."""
    return " ".join(WORD_RE.findall(text.lower()))


def tokens(text):
    return WORD_RE.findall(text.lower())


def strip_code(line):
    """Replace inline code spans with a placeholder (see lint-english)."""
    return re.sub(r"`[^`]*`", "#", line)


def prose_lines(path, payload_markdown):
    """Yield (lineno, text) outside fenced blocks; markdown payloads too."""
    fences = []
    for lineno, raw in enumerate(
            path.read_text(encoding="utf-8").split("\n"), 1):
        stripped = raw.strip()
        match = re.match(r"^(```+|~~~+)(.*)$", stripped)
        if match:
            if fences:
                fences.pop()
            else:
                fences.append(match.group(2).strip().split(" ")[0])
            continue
        if fences and not (
            payload_markdown and all(lang == "markdown" for lang in fences)
        ):
            continue
        yield lineno, raw


def collect_anchors(lines):
    """Headings and bold-term definitions -> {norm: info dict}."""
    anchors = {}
    for lineno, raw in lines:
        line = strip_code(raw).strip()
        head = HEADING_RE.match(raw.strip())
        if head:
            text = head.group(2).strip()
            if text and not text.startswith("|"):
                key = norm(text)
                if key and key not in anchors:
                    anchors[key] = {
                        "display": text, "line": lineno, "kind": "heading"}
            continue
        for pattern in (BOLD_DEF_RE, BOLD_CELL_RE):
            match = pattern.match(line)
            if match:
                term = match.group(1).strip()
                key = norm(term)
                if key and key not in anchors:
                    anchors[key] = {
                        "display": term, "line": lineno, "kind": "term"}
                break
        else:
            match = BOLD_ONLY_RE.match(line)
            if match:
                term = match.group(1).strip()
                key = norm(term)
                if key and key not in anchors:
                    anchors[key] = {
                        "display": term, "line": lineno, "kind": "term"}
    return anchors


def reference_context(before, after, word_count):
    """Does the surrounding text signal a section reference?

    Returns True when a connector precedes the quote or a noun like
    "section" follows it. Single-word names require the strong form so
    literals like the "none" option stay out.
    """
    after_stripped = after.lstrip()
    for noun in POST_NOUNS:
        if after_stripped.lower().startswith(noun):
            return True
    words = re.findall(r"[a-zA-Z]+", before)
    if not words:
        return False
    last = words[-1].lower()
    if last in CONNECTOR_STRONG:
        return True
    if word_count >= 2 and last in CONNECTOR_WEAK:
        return True
    return False


def collect_references(lines):
    """Quoted names in reference context -> [(lineno, display, norm)]."""
    refs = []
    for lineno, raw in lines:
        line = strip_code(raw)
        stripped = line.strip()
        if HEADING_RE.match(stripped) or stripped.startswith(">"):
            continue
        if stripped.startswith("|") and set(stripped) <= set("|-: "):
            continue
        if stripped.startswith("<!--"):
            continue
        for match in QUOTE_RE.finditer(line):
            name = match.group(1).strip()
            # '#' marks a stripped inline-code span - a quote like
            # "File `NAME`" is a literal template, not a reference.
            if "#" in name or any(c in name for c in "/\\:") \
                    or name.endswith(".md"):
                continue
            n = norm(name)
            if not n:
                continue
            if reference_context(line[:match.start()], line[match.end():],
                                 len(n.split())):
                refs.append((lineno, name, n))
    return refs


def count_occurrences(norm_lines, key):
    """How many prose lines contain the normalized name as a phrase."""
    if not key:
        return 0
    pattern = re.compile(r"(?:^|\s)" + re.escape(key) + r"(?:\s|$)")
    return sum(1 for text in norm_lines if pattern.search(" " + text + " "))


def subsequence_gap(short, long_):
    """Is short a subsequence of long with an interior gap?

    A contiguous prefix or suffix ("Sources of Truth" inside
    "Project-Specific Sources of Truth") is legitimate scoping, not
    drift - only a gap inside the match counts.
    """
    pos = []
    it = enumerate(long_)
    for token in short:
        for i, t in it:
            if t == token:
                pos.append(i)
                break
        else:
            return False
    return pos != list(range(pos[0], pos[0] + len(pos)))


def similar(a, b):
    """Do two normalized names look like variants of one term?"""
    ta, tb = a.split(), b.split()
    if len(ta) < 3 or len(tb) < 3:
        return False
    if len(ta) < len(tb) and subsequence_gap(ta, tb):
        return True
    if len(tb) < len(ta) and subsequence_gap(tb, ta):
        return True
    # Shared prefix and suffix covering the bulk of both names.
    prefix = 0
    while prefix < min(len(ta), len(tb)) and ta[prefix] == tb[prefix]:
        prefix += 1
    suffix = 0
    while (suffix < min(len(ta), len(tb)) - prefix
           and ta[-1 - suffix] == tb[-1 - suffix]):
        suffix += 1
    return prefix >= 2 and suffix >= 1


def main():
    parser = argparse.ArgumentParser(
        description="Check internal references and terminology consistency")
    parser.add_argument("file", type=Path)
    parser.add_argument("--payload-markdown", action="store_true",
                        help="scan inside ```markdown fenced blocks too")
    parser.add_argument("--group-by-form", action="store_true",
                        help="group findings by name instead of by line")
    args = parser.parse_args()

    if not args.file.exists():
        print("check-consistency: %s: no such file" % args.file)
        return 2

    lines = list(prose_lines(args.file, args.payload_markdown))
    anchors = collect_anchors(lines)
    refs = collect_references(lines)
    norm_lines = [" ".join(tokens(strip_code(raw))) for _, raw in lines]

    findings = []

    def resolves(name, key):
        if key in anchors:
            return True
        # Path-qualified reference: "Parent - Child" resolves when the
        # final segment is itself an anchor ("Appendix - Template
        # Library" -> the "Template Library" heading).
        if " - " in name and norm(name.rsplit(" - ", 1)[1]) in anchors:
            return True
        return False

    unresolved = [(ln, name, n) for ln, name, n in refs
                  if not resolves(name, n)]
    for lineno, name, _ in unresolved:
        findings.append(
            ("error", lineno,
             "UNRESOLVED '\"%s\"' - no heading or defined term matches"
             % name, "unresolved"))

    # Terminology drift: every anchor plus every quoted name, deduplicated.
    terms = {}
    for key, info in anchors.items():
        terms[key] = {"display": info["display"], "line": info["line"],
                      "heading": info["kind"] == "heading"}
    for lineno, name, n in refs:
        if n not in terms:
            terms[n] = {"display": name, "line": lineno, "heading": False}

    keys = sorted(terms)
    flagged = set()
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            if a == b or not similar(a, b):
                continue
            # Two plain headings are usually deliberate parallel names
            # ("Setup for X" vs "Setup for Y"), not drift - drift shows
            # when a name outside the heading set varies from it.
            if terms[a]["heading"] and terms[b]["heading"]:
                continue
            pair = frozenset((a, b))
            if pair in flagged:
                continue
            count_a = count_occurrences(norm_lines, a)
            count_b = count_occurrences(norm_lines, b)
            if not count_a or not count_b:
                continue
            minor, major = (a, b) if count_a <= count_b else (b, a)
            minor_n, major_n = (count_a, count_b) if minor == a \
                else (count_b, count_a)
            flagged.add(pair)
            findings.append(
                ("warn", terms[minor]["line"],
                 "VARIANT '%s' - similar to '%s' (%d vs %d occurrences); "
                 "unify on one form"
                 % (terms[minor]["display"], terms[major]["display"],
                    minor_n, major_n),
                 "variant: %s" % minor))

    errors = sum(1 for f in findings if f[0] == "error")
    warnings = sum(1 for f in findings if f[0] == "warn")

    if args.group_by_form:
        grouped = {}
        for severity, lineno, message, key in findings:
            grouped.setdefault((severity, key), []).append((lineno, message))
        for (severity, key), hits in grouped.items():
            tag = "ERROR" if severity == "error" else "WARN"
            lines_ = ", ".join(str(ln) for ln, _ in hits)
            print("%s:%s [%s] %s (%d hit(s))"
                  % (args.file, lines_, tag, hits[0][1], len(hits)))
    else:
        for severity, lineno, message, _ in findings:
            tag = "ERROR" if severity == "error" else "WARN"
            where = "%s:%s" % (args.file, lineno) if lineno else str(args.file)
            print("%s: [%s] %s" % (where, tag, message))

    print("check-consistency: %d error(s), %d warning(s), "
          "%d anchor(s), %d reference(s)"
          % (errors, warnings, len(anchors), len(refs)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
