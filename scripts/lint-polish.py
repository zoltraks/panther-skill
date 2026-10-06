#!/usr/bin/env python3
"""Lint Polish Markdown prose for calques, spliced clauses, and typography.

Reads forbidden-form tables ("Zamiast / Używaj" or "Instead of / Use") from the
skill's rule files and reports each occurrence in the target document. Also runs
heuristic checks: comma splices, "tylko, gdy", bare "per", a correlative
"na tym" opened without a comma, typographic characters under the ASCII
convention, and "w." as an abbreviation.

Fully uppercase tokens (enum and verdict labels such as `REQUEST CHANGES`
or `APPROVE`) are treated as constants, not prose calques, and are exempt.
Quoted verbatim spans are exempt, and a parenthesized qualifier on a banned
form ("trasa (routing)") bounds the ban to that sense and reports a warning.

Errors exit non-zero; warnings are advisory and never fail the run.

Usage:
    lint-polish.py <file.md> [--rules <rulefile.md> ...] [--group-by-form]
                   [--payload-markdown]

--group-by-form replaces the line-by-line output with one line per matched
forbidden form or rule, listing hit count and line numbers - the form to fix
in bulk. Run without the flag for the full per-line detail.

--payload-markdown lints prose inside ```markdown fenced payload blocks -
a payload interior is translated prose, so banned forms apply there too.
Multi-word forbidden forms match each word by declinable stem, so inflected
variants such as `instrukcją wykonywalną` hit the `instrukcja wykonywalna`
form.

When --rules is omitted, rule files are discovered relative to this script
(<repo>/languages/pl.md and <repo>/translations/en-pl/en-pl-software.md).
"""

import argparse
import re
import sys
from pathlib import Path

TABLE_HEADERS = {"zamiast", "instead of", "forbidden"}

# Single common Polish words that are calques only in context - demoted to
# warnings so the check stays a usable gate.
SOFT_STEMS = {
    "pod", "plus", "wskaźnik", "niesie", "niosą", "dotyka", "zyskuje",
    "właściciel", "mieszkają", "żyje", "lustro", "ładunek", "rekord",
    "chudy", "najcięższy", "najlżejszy", "autorytatywny", "wydawniczy",
    "wykonawcz", "powierzchnia", "konsumowana", "zaadresować", "kosztuje",
    "przypięty", "celują", "rekursują", "serwujący", "strażnik", "zastany",
    "brama", "bramka", "bramy", "realna", "realne", "diff", "wyjątek",
    "to jest", "skonsultowano", "rozdzielczy", "podbicie", "trasa",
    "narzędziowy", "narzędziowa", "narzędziowe", "mechanizm procesowy",
    "współpracownik", "atrybucja", "selekcja", "destylacja", "odtwarzalny",
    "rozstrzygnięta", "wykonalne", "zaspokaja", "dopychany", "rządzi",
    "orkiestruje", "wtóruje", "zagęszczona", "wyprodukuj", "nazwany po",
    "wąska", "odchudzony",
}

# Words that open a leading subordinate or adverbial clause - the first comma on
# such a line closes that clause, so it is not a splice.
CLAUSE_OPENERS = {
    "gdy", "jeśli", "jeżeli", "ponieważ", "chociaż", "choć", "aczkolwiek",
    "albowiem", "kiedy", "zanim", "dopóki", "skoro", "gdyby", "aby", "żeby",
    "jak", "nawet", "o", "w", "we", "po", "przy", "podczas", "dla", "przed",
    "za", "na", "bez", "mimo", "oprócz", "zamiast", "dzięki", "wraz",
    "według", "od", "z", "ze", "jednak", "następnie", "najpierw", "potem",
}

# Fixed Polish idioms that contain a calque-flagged stem - a match inside one of
# these phrases is correct usage, not a calque.
ALLOWED_PHRASES = {
    "pod opieką", "pod kątem", "pod względem", "pod tym względem",
    "pod warunkiem", "pod presją", "pod kontrolą", "pod adresem",
    "pod hasłem", "pod nazwą", "pod postacią",
    # `wskaźnik` flags the odnośnik calque - a raw code pointer is legitimate.
    "surowy wskaźnik", "surowego wskaźnika", "surowym wskaźnikiem",
    "surowe wskaźniki", "surowych wskaźników", "surowymi wskaźnikami",
    # Verbatim-kept English names whose stems collide with calque verbs -
    # `requestować` stem-matches `Request`, `awaitować` matches `Await`.
    "pull request", "pull requestów", "pull requesta", "pull requestem",
    # Settled code-domain `walidacja` senses that the `validate` trap row would
    # otherwise flag - input and data validation keep the loanword.
    "walidacji wejścia", "walidacja wejścia", "walidacji danych",
    "walidacja danych", "brakującej walidacji", "brakująca walidacja",
    "powtórzoną walidację", "powtórzona walidacja", "powieloną walidację",
    "powielona walidacja",
    # The `równoważny` trap covers the document/mechanism sense of `equivalent` -
    # `równoważność` as the abstract property (behavioral equivalence) is legal.
    "równoważność", "równoważności",
    "pull requesty", "merge request", "change request", "async/await",
}

# Words that legitimately follow a comma (conjunctions, relatives,
# prepositions, common adverbs, abbreviations).
COMMA_OK = {
    "i", "oraz", "a", "ale", "jednak", "lub", "albo", "ani", "czy", "czyli",
    "tj.", "tzn.", "np.", "itp.", "itd.", "m.in.", "w", "we", "z", "ze", "na",
    "do", "o", "po", "przy", "dla", "od", "przez", "za", "pod", "nad", "przed",
    "bez", "między", "według", "wg", "ku", "u", "jak", "że", "żeby", "aby",
    "by", "co", "który", "która", "które", "którzy", "których", "której",
    "któremu", "którym", "gdzie", "gdy", "kiedy", "jeśli", "jeżeli", "chociaż",
    "choć", "bo", "ponieważ", "gdyż", "więc", "natomiast", "nawet", "to",
    "mimo", "poza", "wraz", "dzięki", "zamiast", "oprócz", "wskutek", "innymi",
    "inaczej", "zwłaszcza", "szczególnie", "tylko", "także", "również",
    "wreszcie", "potem", "najpierw", "następnie", "wówczas", "wtedy", "zanim",
    "dopóki", "skoro", "czy", "bądź", "nie", "tak", "tedy", "zatem", "toteż",
    "lecz", "czego", "czym", "kim", "podczas", "jako", "ponadto", "wobec",
    "nigdy", "zawsze", "stąd", "wszędzie", "gdziekolwiek", "gdyby",
    "aż", "chyba", "którą", "którymi", "komu", "czemu", "czyj", "czyją",
    "czyje", "ile", "skąd", "dokąd", "żebym", "żebyś", "żebyśmy", "żebyście",
    "abym", "abyś", "abyśmy", "abyście", "gdybym", "gdybyś", "gdybyśmy",
    "będąc",
}

TYPOGRAPHIC = {
    "„": "typographic open quote", "”": "typographic close quote",
    "“": "typographic open quote", "’": "typographic apostrophe",
    "‘": "typographic apostrophe", "–": "półpauza", "—": "pauza",
    "…": "ellipsis character", "→": "arrow character",
    "«": "guillemet", "»": "guillemet",
}


def reconfigure_stdio():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="backslashreplace")
        except Exception:
            pass


def strip_code(line):
    """Remove inline code spans from a line."""
    return re.sub(r"`[^`]*`", "", line)


def iter_prose_lines(path, payload_markdown=False):
    """Yield (lineno, text) for prose lines outside fenced code blocks.

    With payload_markdown, lines inside ```markdown fenced blocks are yielded
    too - a payload interior is translated prose and needs the same checks.
    """
    fences = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
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


def stem(word):
    """Reduce an infinitive or inflected form to a matchable stem."""
    for ending in ("ować", "iwać", "ać", "eć", "ić", "yć"):
        if word.endswith(ending) and len(word) - len(ending) >= 3:
            return word[: -len(ending)]
    return word


# Word endings that mark Polish declension - dropping one yields a stem that
# prefix-matches the inflected variants of a form (`instrukcja` -> `instrukcj`
# covers `instrukcją`, `instrukcji`, `instrukcję`).
WEAK_ENDINGS = set("aeiouąęć")


def word_pattern(word):
    """Regex fragment matching one declined Polish word form.

    Verb endings strip to the infinitive stem; a longer word ending in a weak
    declinable vowel drops it so inflections match (`pojednani` covers
    `pojednania`, `końcow` covers `końcowym`). Shorter roots keep a plain
    prefix match so common stems like `bram-` do not over-flag `bramka`.
    """
    root = stem(word.lower())
    if len(root) <= 3:
        return r"\b" + re.escape(root) + r"\b"
    if (len(root) >= 6 and root[-1] in WEAK_ENDINGS) or root.endswith("owy"):
        return re.escape(root[:-1]) + r"\w*"
    return re.escape(root) + r"\w*"


def load_forbidden(rules_paths):
    """Parse forbidden-form tables. Returns [(forbidden, replacement, qualifier)].

    A parenthesized qualifier on the forbidden column ("trasa (routing)")
    bounds the ban to that sense - hits report as warnings, not errors.
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
                if first in TABLE_HEADERS:
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


def word_is_soft(forbidden):
    base = forbidden.split("(")[0].strip().lower()
    return base in SOFT_STEMS or stem(base) in SOFT_STEMS


def allowed_spans(lowered):
    """Spans of fixed idioms whose calque-flagged stems are correct usage."""
    return [
        hit.span()
        for phrase in ALLOWED_PHRASES
        for hit in re.finditer(re.escape(phrase), lowered)
    ]


def quoted_spans(lowered):
    """Verbatim quoted spans - a cited foreign-language quote is legal content."""
    return [
        hit.span()
        for hit in re.finditer(r"[\"„«][^\"”»]*[\"”»]", lowered)
    ]


def check_forbidden(lineno, text, pairs, findings):
    lowered = text.lower()
    allowed = allowed_spans(lowered) + quoted_spans(lowered)
    for forbidden, replacement, qualifier in pairs:
        pieces = [word_pattern(w) for w in forbidden.lower().split(" ")]
        pattern = re.compile(r"\b" + r"\s+".join(pieces))
        for match in pattern.finditer(lowered):
            if any(start <= match.start() and match.end() <= end
                   for start, end in allowed):
                continue
            if text[match.start():match.end()].isupper():
                continue
            if qualifier:
                findings.append(
                    ("warn", lineno,
                     "possible calque '%s' - the ban covers the (%s) sense; "
                     "use '%s'" % (match.group(0), qualifier, replacement),
                     "calque: %s" % forbidden)
                )
                continue
            severity = "warn" if word_is_soft(forbidden) else "error"
            findings.append(
                (severity, lineno,
                 "calque '%s' - use '%s'" % (match.group(0), replacement),
                 "calque: %s" % forbidden)
            )


def first_prose_word(text):
    """First meaningful word of the line, after list/quote/heading markers."""
    stripped = re.sub(r"^[#>\s]*", "", text)
    stripped = re.sub(r"^[-*+]\s+|^\d+\.\s+|^-\s*\[[ x]\]\s*", "", stripped)
    stripped = stripped.lstrip("*`_\"'")
    match = re.match(r"\w+", stripped.lower())
    return match.group(0) if match else ""


def check_mechanical(lineno, text, findings, splice=True):
    if "tylko, gdy" in text.lower():
        findings.append(("error", lineno,
                         "'tylko, gdy' - write 'tylko wtedy, gdy'",
                         "tylko, gdy"))
    if re.search(r"\bna tym\s+(że|gdzie|jak|czy|ile|w jakim)\b", text.lower()):
        findings.append(
            ("error", lineno,
             "'na tym X' - the correlative clause needs a comma: 'na tym, X'",
             "na tym clause"))
    if re.search(r"\bper\s+\w", text):
        findings.append(("error", lineno,
                         "'per X' - write 'dla każdego X'", "per X"))
    if re.search(r"\bw\.\s*\d", text):
        findings.append(("warn", lineno,
                         "'w.' - do not abbreviate 'wierszy'", "w. abbrev"))
    if re.search(r"~\s*\d", text):
        findings.append(("warn", lineno,
                         "'~N' - write 'ok. N' or 'około N'", "~N"))
    if re.search(r"\bNiej\b", text):
        findings.append(("warn", lineno,
                         "'Niej' - possible misspelling of a negated "
                         "adjective", "Niej"))
    if re.search(r"\bparitet\b", text.lower()):
        findings.append(("error", lineno,
                         "'paritet' - misspelling of 'parytet'", "paritet"))
    for char, name in TYPOGRAPHIC.items():
        if char in text:
            findings.append(("error", lineno,
                             "typographic %s %r" % (name, char),
                             "typographic char"))
    if ";" in text:
        findings.append(("error", lineno, "semicolon in prose", "semicolon"))

    # Participial opener: a line opening with an adverbial participle clause
    # ("Wnosząc...", "Zbadawszy...") needs a comma after that clause.
    first = first_prose_word(text)
    opens_participle = bool(first) and re.search(r"(ąc|wszy|łszy)$", first)
    if (opens_participle and "," not in text
            and not text.strip().startswith(("#", "|"))):
        findings.append(
            ("warn", lineno,
             "participial opener - add a comma after the '-ąc/-wszy' clause",
             "participial opener"))

    # Comma-splice heuristic: a comma followed by a word that opens neither a
    # subordinate clause nor a prepositional phrase. Tables and list items are
    # skipped - their commas are usually enumerations. Commas inside
    # parentheses always sit inside a parenthetical phrase and are exempt.
    # Flagged commas inside a series closed by a conjunction ("X, Y i Z") are
    # an enumeration, not a splice, and stay silent - enumeration items may
    # carry parenthesized references such as "(F-01)". When the line opens
    # with a subordinate or participial clause ("Gdy ...", "Jeśli ...",
    # "Odwołując ..."), the first comma on the line closes that clause and is
    # exempt. A comma before an identifier token such as "F-02" or "ADR-3" is
    # a list separator, not a splice.
    if not splice:
        return
    lowered = text.lower()
    skip_first = first in CLAUSE_OPENERS or opens_participle
    item = r"(?:[^,.;:()]|\([^()]*\))+?"
    enum_spans = [
        m.span() for m in re.finditer(
            r",\s*" + item + r"(?:\s*,\s*" + item + r")*\s+"
            r"(?:i|oraz|lub|albo)\s+" + item, lowered)
    ]
    paren_spans = [
        m.span() for m in re.finditer(r"\([^()]*\)", lowered)
    ]
    for match in re.finditer(r",\s+(\w+)", lowered):
        word = match.group(1)
        if word in COMMA_OK or word[0].isdigit():
            continue
        if re.search(r"(ąc|wszy|łszy)$", word):
            continue
        if re.match(r"-\d", lowered[match.end():]):
            continue
        if any(start <= match.start() < end for start, end in enum_spans):
            continue
        if any(start <= match.start() < end for start, end in paren_spans):
            continue
        if skip_first:
            skip_first = False
            continue
        findings.append(
            ("warn", lineno,
             "possible spliced clause - ', %s' does not open a "
             "subordinate phrase" % word,
             "spliced clause")
        )


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
                             "blocks, whose interiors are translated text")
    args = parser.parse_args()

    rules = args.rules
    if not rules:
        root = Path(__file__).resolve().parent.parent
        rules = [
            root / "languages" / "pl.md",
            root / "translations" / "en-pl" / "en-pl-software.md",
        ]
    pairs = load_forbidden(rules)

    findings = []
    for lineno, text in iter_prose_lines(args.file, args.payload_markdown):
        stripped = text.strip()
        if stripped.startswith("<!--"):
            continue
        is_table = stripped.startswith("|")
        is_list = bool(re.match(r"^[-*+]\s|^\d+\.\s|^\s+[-*+]\s", text))
        check_forbidden(lineno, text, pairs, findings)
        check_mechanical(lineno, text, findings,
                         splice=not (is_table or is_list))

    errors = sum(1 for f in findings if f[0] == "error")
    if args.group_by_form:
        groups = {}
        for severity, lineno, message, key in findings:
            groups.setdefault(key, []).append((severity, lineno, message))
        for key, items in groups.items():
            lines = ", ".join(str(ln) for _, ln, _ in items)
            severities = {s for s, _, _ in items}
            tag = "ERROR" if "error" in severities else "WARN"
            hint = (items[0][2].split(" - ", 1)[-1]
                    if key.startswith("calque:")
                    else items[0][2].split(" - ", 1)[0])
            print("[%s] %s: %d hit(s) at line(s) %s - %s"
                  % (tag, key, len(items), lines, hint))
    else:
        for severity, lineno, message, _key in findings:
            print("%s:%d: [%s] %s"
                  % (args.file, lineno, severity.upper(), message))
    print("lint-polish: %d error(s), %d warning(s), %d forbidden forms loaded"
          % (errors, len(findings) - errors, len(pairs)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
