#!/usr/bin/env python3
"""Lint English Markdown prose for vocabulary, spelling, and grammar.

Reads the "Instead of / Use" vocabulary table and the Dialect Consistency
variant-pair table from the skill's English baseline and reports violations
in the target document: banned vocabulary, common misspellings, doubled
words, ``then``/``than`` misuse, and ``its'`` errors. Heuristic checks -
a/an agreement, spaced-hyphen clause joins, and spelling-dialect mixing -
report as advisory warnings. Dialect findings always measure against the
document's dominant variant, never a fixed dialect.

Fully uppercase tokens (enum and verdict labels such as `REQUEST CHANGES`
or `APPROVE`) are treated as constants, not prose, and are exempt. Quoted
verbatim spans are exempt.

Errors exit non-zero; warnings are advisory and never fail the run.

Usage:
    lint-english.py <file.md> [--rules <rulefile.md> ...] [--group-by-form]
                    [--payload-markdown]

--group-by-form replaces the line-by-line output with one line per matched
form or rule, listing hit count and line numbers - the form to fix in bulk.
Run without the flag for the full per-line detail.

--payload-markdown lints prose inside ```markdown fenced payload blocks -
a payload interior is prose too. Other fence languages stay opaque.

When --rules is omitted, the rule file is discovered relative to this
script (<repo>/languages/en.md).
"""

import argparse
import re
import sys
from pathlib import Path

VOCAB_HEADERS = {"instead of", "use", "zamiast", "forbidden"}
DIALECT_HEADERS = {"american", "us", "british", "uk"}

# Common misspellings - wrong form -> right form. Kept in the tool: a
# mechanical list of errors, not a document style convention.
MISSPELLINGS = {
    "accomodate": "accommodate",
    "accross": "across",
    "adress": "address",
    "arguement": "argument",
    "autonomus": "autonomous",
    "becuase": "because",
    "begining": "beginning",
    "commited": "committed",
    "compatiable": "compatible",
    "defualt": "default",
    "documenation": "documentation",
    "enviroment": "environment",
    "existance": "existence",
    "explicitely": "explicitly",
    "explicity": "explicitly",
    "hte": "the",
    "heigth": "height",
    "maintainance": "maintenance",
    "modifed": "modified",
    "neccessary": "necessary",
    "occured": "occurred",
    "occurence": "occurrence",
    "paramter": "parameter",
    "preceed": "precede",
    "prerequiste": "prerequisite",
    "priviledge": "privilege",
    "procede": "proceed",
    "recieve": "receive",
    "refering": "referring",
    "relevent": "relevant",
    "requier": "require",
    "respository": "repository",
    "retreive": "retrieve",
    "seperate": "separate",
    "specfic": "specific",
    "sucessful": "successful",
    "supercede": "supersede",
    "taht": "that",
    "teh": "the",
    "thier": "their",
    "transfered": "transferred",
    "treshold": "threshold",
    "unneccesary": "unnecessary",
    "untill": "until",
    "usefull": "useful",
    "validaton": "validation",
    "verfiy": "verify",
    "wether": "whether",
    "wich": "which",
    "widht": "width",
    "writting": "writing",
}

# Comparatives that demand "than" - "X then" after one is a misspelling.
THAN_MISUSE = re.compile(
    r"\b(more|less|fewer|better|worse|other|another|rather|earlier|later"
    r"|faster|slower|stronger|weaker|higher|lower|larger|smaller|greater"
    r"|sooner|longer|shorter|wider|narrower|bigger|easier|harder|heavier"
    r"|lighter|older|younger|newer|cheaper|dearer|safer|simpler|deeper"
    r"|closer|further|farther|darker|brighter|clearer)\s+then\b",
    re.IGNORECASE)

# Doubled words that are legal English and not a defect.
DOUBLED_OK = {"that that", "had had"}

# Acronyms pronounced letter by letter - the first letter's name decides
# the article ("an SQL database", "a PDF file"). Other all-caps tokens are
# pronounced as words and fall back to the ordinary first-sound rule
# ("a README", "a NASA mission").
LETTERED_ACRONYMS = {
    "adr", "ai", "ansi", "api", "ascii", "crm", "erp", "faq", "ftp",
    "hdd", "html", "http", "https", "id", "io", "kpi", "lcd", "ldap",
    "led", "lsp", "md", "mcp", "nfs", "npm", "odbc", "oled", "os",
    "pdf", "rca", "rdbms", "rfc", "rgb", "rpm", "rss", "saml", "sdk",
    "sftp", "sgml", "sla", "smb", "sms", "spdx", "sql", "ssd", "ssh", "ssl",
    "svg", "tls", "ui", "xml", "xsd", "xsl",
}

# Words whose initial sound is a consonant despite a vowel letter -
# "a" is correct ("a unique", "a user", "a European", "a one-time").
A_SOUNDS = {
    "unique", "unicorn", "unified", "unifier", "uniform", "uniformed",
    "union", "unipolar", "unit", "unite", "united", "unity", "universal",
    "universe", "university", "unix", "unisex", "unilateral", "use",
    "used", "useful", "useless", "user", "users", "using", "usual",
    "usually", "us", "usb", "usage", "usable", "usability", "utility",
    "utilities", "utilitarian",
    "utensil", "european", "eureka", "eucalyptus", "eulogy", "one",
    "once", "ones", "one-time", "one-off", "one-way", "ouija",
    "one-time", "once-over",
}

# Words whose initial sound is a vowel despite a consonant letter -
# "an" is correct ("an hour", "an honest answer").
AN_SOUNDS = {
    "hour", "hours", "hourly", "honest", "honestly", "honesty", "honor",
    "honors", "honored", "honoring", "honour", "honourable", "heir",
    "heirs", "heirloom", "herb", "herbs",
}

# Capital letters whose letter-name opens with a vowel sound - acronyms
# starting with them take "an" ("an HTTP service", "an SQL database").
VOWEL_LETTERS = set("AEFHILMNORSX")

# A spaced hyphen that opens a subject-verb clause - banned by the
# "Spaced Hyphens" rule: a spaced hyphen never joins two clauses.
CLAUSE_SUBJECT = re.compile(
    r"\S - (it |this |they |there |which |that |so |as a result|"
    r"the agent|the user)", re.IGNORECASE)
CLAUSE_VERB = re.compile(
    r"[a-z]{3,} - [a-z]+ (is|are|was|were|has|have|had|can|will|would"
    r"|must|should|does|do|may|not|never|always)\b", re.IGNORECASE)


def reconfigure_stdio():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="backslashreplace")
        except Exception:
            pass


def strip_code(line):
    """Replace inline code spans with a placeholder.

    A `#` stands in for the span so adjacent prose words do not collapse
    together - "a `None` option" stays "a # option" instead of becoming a
    phantom "a option" article error.
    """
    return re.sub(r"`[^`]*`", "#", line)


def iter_prose_lines(path, payload_markdown=False):
    """Yield (lineno, text) for prose lines outside fenced code blocks.

    With payload_markdown, lines inside ```markdown fenced blocks are
    yielded too - a payload interior is prose and needs the same checks.
    """
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
        yield lineno, strip_code(raw)


def load_vocabulary(rules_paths):
    """Parse "Instead of / Use" tables. Returns [(form, replacement, qual)].

    A parenthesized qualifier on the forbidden column ("leverage (as a
    verb)") bounds the ban to that sense - hits report as warnings.
    """
    pairs = []
    seen = set()
    for rules in rules_paths:
        if not rules.exists():
            continue
        in_table = False
        for line in rules.read_text(encoding="utf-8").split("\n"):
            cells = [c.strip() for c in line.split("|")]
            if line.startswith("|") and len(cells) >= 4:
                first = cells[1].strip("`").lower()
                if first in VOCAB_HEADERS:
                    in_table = True
                    continue
                if in_table:
                    if set(cells[1] + cells[2]) <= set("- "):
                        continue
                    qualifier = ", ".join(re.findall(r"\((.*?)\)", cells[1]))
                    bad = re.sub(r"\(.*?\)", "", cells[1]).strip()
                    good = re.sub(r"\(.*?\)", "", cells[2]).strip()
                    if bad:
                        for form in bad.split(" / "):
                            form = form.strip().strip("`")
                            if form and form.lower() not in seen:
                                seen.add(form.lower())
                                pairs.append((form, good, qualifier))
            elif in_table:
                in_table = False
    return pairs


def load_dialect(rules_paths):
    """Parse the Dialect Consistency pair table. Returns [(us, uk)]."""
    pairs = []
    for rules in rules_paths:
        if not rules.exists():
            continue
        in_table = False
        for line in rules.read_text(encoding="utf-8").split("\n"):
            cells = [c.strip() for c in line.split("|")]
            if line.startswith("|") and len(cells) >= 4:
                first = cells[1].strip("`").lower()
                second = cells[2].strip("`").lower()
                if first in DIALECT_HEADERS and second in DIALECT_HEADERS:
                    in_table = True
                    continue
                if in_table:
                    if set(cells[1] + cells[2]) <= set("-: "):
                        continue
                    us = cells[1].strip("`").lower()
                    uk = cells[2].strip("`").lower()
                    if us and uk:
                        pairs.append((us, uk))
            elif in_table:
                in_table = False
    return pairs


def quoted_spans(text):
    """Verbatim quoted spans - cited material is not the document's prose."""
    return [hit.span() for hit in re.finditer(r"\"[^\"]*\"|'[^']*'", text)]


def in_spans(match, spans):
    return any(start <= match.start() and match.end() <= end
               for start, end in spans)


def word_pattern(word):
    """Regex fragment matching one word and its common English inflections.

    Short words (<=3 chars) match exactly; longer words prefix-match so
    `utilize` covers `utilized`, `utilizes`, and `utilization`.
    """
    if len(word) <= 3:
        return r"\b" + re.escape(word) + r"\b"
    return re.escape(word) + r"\w*"


# Nouns that can adjectivize - a "verb + article + noun" banned form like
# "perform an update" is only a nominalization when the noun closes the
# phrase. "Performs an update check" uses `update` as a modifier, so the
# hit demotes to a warning.
MODIFIABLE_NOUNS = {
    "update", "upgrade", "change", "fix", "improvement", "review", "test",
    "check", "report", "install", "installation", "build", "release",
}

FUNCTION_WORDS = {
    "a", "an", "the", "of", "to", "in", "on", "for", "and", "or", "but",
    "nor", "as", "at", "by", "is", "it", "its", "be", "with", "when",
    "that", "this", "which", "who", "from", "into", "than", "then",
    "if", "not", "no", "so", "such", "after", "before", "during",
}


def check_vocabulary(lineno, text, pairs, findings):
    lowered = text.lower()
    exempt = quoted_spans(lowered)
    for forbidden, replacement, qualifier in pairs:
        words = forbidden.lower().split(" ")
        pieces = [word_pattern(w) for w in words]
        pattern = re.compile(r"\b" + r"\s+".join(pieces))
        for match in pattern.finditer(lowered):
            if in_spans(match, exempt):
                continue
            if text[match.start():match.end()].isupper():
                continue
            adjectivized = False
            if (len(words) >= 2 and words[-1] in MODIFIABLE_NOUNS):
                tail = re.match(r"\s+([a-z]+)", lowered[match.end():])
                if tail and tail.group(1) not in FUNCTION_WORDS:
                    adjectivized = True
            if qualifier or adjectivized:
                note = ("the ban covers the (%s) sense" % qualifier
                        if qualifier
                        else "'%s' may modify the following word" % words[-1])
                findings.append(
                    ("warn", lineno,
                     "possible vocabulary '%s' - %s; use '%s'"
                     % (match.group(0), note, replacement),
                     "vocabulary: %s" % forbidden))
                continue
                findings.append(
                    ("warn", lineno,
                     "possible vocabulary '%s' - the ban covers the (%s) "
                     "sense; use '%s'"
                     % (match.group(0), qualifier, replacement),
                     "vocabulary: %s" % forbidden))
                continue
            findings.append(
                ("error", lineno,
                 "vocabulary '%s' - use '%s'"
                 % (match.group(0), replacement),
                 "vocabulary: %s" % forbidden))


def check_misspellings(lineno, text, findings):
    lowered = text.lower()
    exempt = quoted_spans(lowered)
    for wrong, right in MISSPELLINGS.items():
        for match in re.finditer(r"\b" + re.escape(wrong) + r"\b", lowered):
            if in_spans(match, exempt):
                continue
            if text[match.start():match.end()].isupper():
                continue
            findings.append(
                ("error", lineno,
                 "misspelling '%s' - use '%s'"
                 % (match.group(0), right),
                 "misspelling: %s" % wrong))


def check_doubled(lineno, text, findings):
    for match in re.finditer(r"\b([a-z]{2,})\s+\1\b", text, re.IGNORECASE):
        if match.group(0).lower() in DOUBLED_OK:
            continue
        findings.append(
            ("error", lineno,
             "doubled word '%s'" % match.group(0),
             "doubled word"))


def check_than(lineno, text, findings):
    for match in THAN_MISUSE.finditer(text):
        findings.append(
            ("error", lineno,
             "'%s then' - use 'than' after a comparative"
             % match.group(0).split(" ")[0],
             "then/than"))
    if re.search(r"\bits'\b", text, re.IGNORECASE):
        findings.append(
            ("error", lineno,
             "\"its'\" - use 'its' or 'it is'", "its'"))


def expected_article(word):
    """Return 'a' or 'an' for the article that should precede a word."""
    if not word:
        return None
    wl = word.lower()
    if len(word) >= 2 and word.isupper():
        if wl in LETTERED_ACRONYMS:
            return "an" if word[0] in VOWEL_LETTERS else "a"
        return "an" if wl[0] in "aeiou" else "a"
    if wl in AN_SOUNDS:
        return "an"
    if wl in A_SOUNDS or wl.startswith("u-"):
        return "a"
    return "an" if wl[0] in "aeiou" else "a"


def check_article(lineno, text, findings):
    for match in re.finditer(r"\b(a|an)\s+([A-Za-z]+)", text):
        article, word = match.group(1).lower(), match.group(2)
        expected = expected_article(word)
        if expected is None or expected == article:
            continue
        findings.append(
            ("warn", lineno,
             "article '%s %s' - '%s' is expected before '%s'"
             % (article, word, expected, word),
             "a/an"))


def check_hyphen_join(lineno, text, findings):
    if CLAUSE_SUBJECT.search(text) or CLAUSE_VERB.search(text):
        findings.append(
            ("warn", lineno,
             "spaced hyphen joins clauses - split into separate sentences",
             "hyphen clause join"))


def check_dialect(prose, dialect_pairs, findings):
    """Flag forms on the minority side of the document's dominant dialect.

    The dominant variant is whichever side of the pair table the document
    uses most - the document's own convention wins, so findings are always
    advisory and never name a fixed dialect as mandatory.
    """
    us_hits = {}  # pair -> [lineno]
    uk_hits = {}
    for us, uk in dialect_pairs:
        for lineno, text in prose:
            for match in re.finditer(r"\b" + re.escape(us) + r"\b",
                                     text, re.IGNORECASE):
                us_hits.setdefault((us, uk), []).append(lineno)
            for match in re.finditer(r"\b" + re.escape(uk) + r"\b",
                                     text, re.IGNORECASE):
                uk_hits.setdefault((us, uk), []).append(lineno)
    us_total = sum(len(v) for v in us_hits.values())
    uk_total = sum(len(v) for v in uk_hits.values())
    if not us_total and not uk_total:
        return
    if us_total == uk_total:
        findings.append(
            ("warn", 0,
             "dialect is mixed with no dominant variant "
             "(american %d, british %d)" % (us_total, uk_total),
             "dialect census"))
        return
    dominant = "american" if us_total > uk_total else "british"
    minority = uk_hits if dominant == "american" else us_hits
    for (us, uk), lines in minority.items():
        form = uk if dominant == "american" else us
        better = us if dominant == "american" else uk
        for lineno in sorted(set(lines)):
            findings.append(
                ("warn", lineno,
                 "minority dialect '%s' - dominant variant is '%s' "
                 "(%s, %d hit(s))"
                 % (form, better, dominant,
                    us_total if dominant == "american" else uk_total),
                 "dialect: %s" % form))


def main():
    reconfigure_stdio()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--rules", type=Path, action="append", default=[])
    parser.add_argument("--group-by-form", action="store_true",
                        help="group findings by matched form instead of "
                             "listing every line")
    parser.add_argument("--payload-markdown", action="store_true",
                        help="lint prose inside ```markdown fenced payload "
                             "blocks")
    args = parser.parse_args()

    rules = args.rules
    if not rules:
        root = Path(__file__).resolve().parent.parent
        rules = [root / "languages" / "en.md"]
    pairs = load_vocabulary(rules)
    dialect_pairs = load_dialect(rules)

    prose = list(iter_prose_lines(args.file, args.payload_markdown))
    findings = []
    for lineno, text in prose:
        if text.strip().startswith("<!--"):
            continue
        check_vocabulary(lineno, text, pairs, findings)
        check_misspellings(lineno, text, findings)
        check_doubled(lineno, text, findings)
        check_than(lineno, text, findings)
        check_article(lineno, text, findings)
        check_hyphen_join(lineno, text, findings)
    check_dialect(prose, dialect_pairs, findings)

    errors = sum(1 for f in findings if f[0] == "error")
    if args.group_by_form:
        groups = {}
        for severity, lineno, message, key in findings:
            groups.setdefault(key, []).append((severity, lineno, message))
        for key, items in groups.items():
            lines = ", ".join(str(ln) for _, ln, _ in items)
            severities = {s for s, _, _ in items}
            tag = "ERROR" if "error" in severities else "WARN"
            hint = items[0][2].split(" - ", 1)[-1]
            print("[%s] %s: %d hit(s) at line(s) %s - %s"
                  % (tag, key, len(items), lines, hint))
    else:
        for severity, lineno, message, _key in findings:
            print("%s:%d: [%s] %s"
                  % (args.file, lineno, severity.upper(), message))
    print("lint-english: %d error(s), %d warning(s), %d vocabulary form(s) "
          "loaded, %d dialect pair(s) loaded"
          % (errors, len(findings) - errors, len(pairs), len(dialect_pairs)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
