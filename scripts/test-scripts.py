#!/usr/bin/env python3
"""Smoke-test every Panther maintenance and document-production script.

Runs each script through its non-mutating entry point and checks for a clean
exit or a controlled finding instead of a crash. A controlled finding means
the tool ran and reported - an unhandled traceback means a regression.

Repo validators are asserted against this repository and must exit 0.
Check-mode tools may exit 0 or 1 - both are verdicts, not crashes.
Prints a PASS or FAIL line per tool plus a summary, and exits 0 when all
tools pass, 1 otherwise.

Usage: python scripts/test-scripts.py
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TIMEOUT = 60

# (script, args, accepted exits, required stdout prefix, extra env)
CASES: list[tuple[str, list[str], tuple[int, ...], str | None,
                 dict[str, str] | None]] = [
    ("validate-skill.py", ["."], (0,), None, None),
    ("check-references.py", ["."], (0,), None, None),
    ("check-contents.py", ["."], (0,), None, None),
    ("check-update.py", [], (0,), "STATUS ", None),
    ("detect-encoding.py", ["README.md"], (0,), None, None),
    ("detect-scope.py", ["."], (0,), None, None),
    ("census-document.py", ["README.md"], (0,), None, None),
    ("normalize-chars.py", ["README.md", "--check"], (0, 1), None, None),
    ("split-sentences.py", ["README.md", "--check"], (0, 1), None, None),
    ("split-sentences.py", ["README.md", "--paragraphs", "--check"], (0,), None,
     None),
    ("split-sentences.py", ["README.md", "--flow", "--check"], (0, 1), None,
     None),
    ("wrap-prose.py", ["README.md", "--check"], (0, 1), None, None),
    ("reflow-prose.py", ["README.md", "--wrap", "--check"], (0, 1), None, None),
    ("reflow-prose.py", ["README.md", "--unwrap", "--check"], (0, 1), None, None),
    ("reflow-prose.py", ["README.md", "--justify", "--check"], (0, 1), None,
     None),
    ("format-table.py", ["README.md", "--check"], (0, 1), None, None),
    ("align-comments.py", ["README.md", "--check"], (0, 1), None, None),
    ("align-comments.py", ["conventions/plain-text-comments.md", "--check"], (0,),
     "PASS", None),
    ("check-sections.py", ["README.md", "--type", "types/readme-skill.md"],
     (0, 1), None, None),
    ("check-sections.py",
     ["README.md", "--type", "types/readme-skill.md", "--language",
      "languages/pl.md"], (0, 1), None, None),
    ("validate-document.py", ["README.md"], (0, 1), None, None),
    ("check-document.py", ["README.md"], (0, 1), None, None),
    ("check-document.py",
     ["README.md", "--type", "readme-skill", "--language", "en", "--polish",
      "--layout", "wrap"], (0, 1), "check-document:", None),
    ("diff-content.py", ["README.md"], (0, 1), None, None),
    ("check-parity.py", ["SKILL.md", "README.md"], (0, 1), "check-parity:",
     None),
    ("check-parity.py",
     ["SKILL.md", "README.md", "--terms",
      "translations/en-pl/en-pl-software.md"], (0, 1), None, None),
    ("lint-polish.py", ["README.md"], (0, 1), None, None),
    ("lint-polish.py", ["README.md", "--group-by-form"], (0, 1), None, None),
    ("lint-polish.py", ["README.md", "--payload-markdown"], (0, 1), None, None),
    ("lint-english.py", ["README.md"], (0, 1), None, None),
    ("lint-english.py", ["README.md", "--group-by-form"], (0, 1), None, None),
    ("lint-english.py", ["README.md", "--payload-markdown"], (0, 1), None,
     None),
    ("check-consistency.py", ["README.md"], (0, 1), None, None),
    ("check-consistency.py", ["README.md", "--payload-markdown"], (0, 1),
     None, None),
    ("check-consistency.py", ["README.md", "--group-by-form"], (0, 1), None,
     None),
    ("check-document.py", ["README.md", "--parity", "SKILL.md"], (0, 1),
     "check-document:", None),
    ("check-document.py", ["README.md", "--title-agreement"], (0, 1),
     "check-document:", None),
    ("check-document.py", ["README.md", "--english", "--consistency"],
     (0, 1), "check-document:", None),
    ("safe-replace.py",
     ["README.md", "zzz-not-present-zzz", "yyy", "--check"], (0,), None,
     None),
    ("check-titles.py", ["README.md"], (0,), None, None),
    ("census-document.py", ["README.md"], (0,), None,
     {"PYTHONIOENCODING": "cp1252"}),
    ("validate-document.py", ["README.md"], (0, 1), None,
     {"PYTHONIOENCODING": "cp1252"}),
    ("diff-content.py", ["README.md"], (0, 1), None,
     {"PYTHONIOENCODING": "cp1252", "PYTHONUTF8": "0", "LC_ALL": "C",
      "LANG": "C"}),
]


def run_case(script: str, args: list[str],
             env_extra: dict[str, str] | None = None
             ) -> subprocess.CompletedProcess | None:
    try:
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / script), *args],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=TIMEOUT,
            cwd=ROOT,
            env={**os.environ, **env_extra} if env_extra else None,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None


DEFECT_TABLE = (
    "|| A | B |\n"
    "|  | --- | --- |\n"
    "|  | 1  | 2   |\n"
)

CLEAN_TABLES = (
    "|      | LOW |\n"
    "|------|-----|\n"
    "| CRIT | x   |\n"
    "\n"
    "| Option    | Description |\n"
    "|-----------|-------------|\n"
    "| `--top N` | Limit to N  |\n"
    "|           | items.      |\n"
)


def table_defect_case() -> int:
    """Exercise the table-structure checks against synthetic fixtures."""
    failures = 0
    label = "table-structure fixtures"
    with tempfile.TemporaryDirectory() as tmp:
        bad = Path(tmp) / "defect.md"
        bad.write_text("# Fixture\n\n" + DEFECT_TABLE, encoding="utf-8")
        result = run_case("validate-document.py", [str(bad)])
        if result is None or result.returncode != 1 or not all(
            token in result.stdout
            for token in ("double pipe", "empty in every row",
                          "lack(s) hyphens")
        ):
            print(f"FAIL {label} - defect fixture not reported as expected")
            return 1
        clean = Path(tmp) / "clean.md"
        clean.write_text("# Fixture\n\n" + CLEAN_TABLES, encoding="utf-8")
        result = run_case("validate-document.py", [str(clean)])
        if result is None or result.returncode != 0:
            print(f"FAIL {label} - corner/continuation tables must pass")
            return 1
        result = run_case("format-table.py", [str(bad), "--drop-empty-columns"])
        if result is None or result.returncode != 0 \
                or "dropped empty column" not in result.stdout:
            print(f"FAIL {label} - repair run did not drop the empty column")
            return 1
        result = run_case("validate-document.py", [str(bad)])
        if result is None or result.returncode != 0:
            print(f"FAIL {label} - repaired fixture must validate clean")
            return 1
    print(f"PASS {label}")
    return failures


def heuristic_regressions() -> int:
    """Exercise lint and validator exemptions against synthetic fixtures."""
    failures = 0
    label = "heuristic-exemption fixtures"
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        enum_doc = tmp / "enum.md"
        enum_doc.write_text(
            "# Fixture\n\n"
            "**REQUEST CHANGES**\n\n"
            "Warunki: F-01, F-02, F-03 (przed zamknięciem przeglądu).\n",
            encoding="utf-8")
        result = run_case("lint-polish.py",
                          [str(enum_doc), "--rules", "languages/pl.md"])
        if (result is None or result.returncode != 0
                or "calque" in result.stdout or "spliced" in result.stdout):
            print(f"FAIL {label} - enum label or identifier list still flags")
            failures += 1
        splice_doc = tmp / "splice.md"
        splice_doc.write_text(
            "# Fixture\n\nKonfiguracja jest kompletna, wdrożenie ruszy.\n",
            encoding="utf-8")
        result = run_case("lint-polish.py",
                          [str(splice_doc), "--rules", "languages/pl.md"])
        if result is None or "possible spliced clause" not in result.stdout:
            print(f"FAIL {label} - a real comma splice went silent")
            failures += 1
        calque_doc = tmp / "calque.md"
        calque_doc.write_text(
            "# Fixture\n\n"
            'Sekcja "request path" pozostaje cytatem.\n\n'
            "Rozjazd kontraktu jest oczekiwany.\n\n"
            "Musimy requestować zasób.\n",
            encoding="utf-8")
        result = run_case("lint-polish.py",
                          [str(calque_doc), "--rules", "languages/pl.md",
                           "--rules",
                           "translations/en-pl/en-pl-software.md"],
                          {"PYTHONIOENCODING": "utf-8"})
        if (result is None or result.returncode != 1
                or "calque 'request'" in result.stdout
                or "possible calque 'rozjazd'" not in result.stdout
                or "[ERROR] calque 'requestować'" not in result.stdout):
            print(f"FAIL {label} - qualifier or quote handling regressed")
            failures += 1
        inflected_doc = tmp / "inflected.md"
        inflected_doc.write_text(
            "# Fixture\n\nTa instrukcja jest instrukcją wykonywalną.\n",
            encoding="utf-8")
        result = run_case("lint-polish.py",
                          [str(inflected_doc), "--rules",
                           "translations/en-pl/en-pl-software.md"],
                          {"PYTHONIOENCODING": "utf-8"})
        if (result is None or result.returncode != 1
                or "instrukcją wykonywalną" not in result.stdout):
            print(f"FAIL {label} - inflected multi-word form went silent")
            failures += 1
        payload_doc = tmp / "payload.md"
        payload_doc.write_text(
            "# Fixture\n\n```markdown\nTen blok ma czyste szwy.\n```\n\n"
            "```python\nvalue = 'czyste szwy'\n```\n",
            encoding="utf-8")
        result = run_case("lint-polish.py",
                          [str(payload_doc), "--rules",
                           "translations/en-pl/en-pl-software.md"])
        if result is None or result.returncode != 0:
            print(f"FAIL {label} - fenced content flags without the flag")
            failures += 1
        result = run_case("lint-polish.py",
                          [str(payload_doc), "--rules",
                           "translations/en-pl/en-pl-software.md",
                           "--payload-markdown"])
        if (result is None or result.returncode != 1
                or result.stdout.count("czyste szwy") != 1):
            print(f"FAIL {label} - --payload-markdown missed or over-flagged")
            failures += 1
        heading_doc = tmp / "heading.md"
        heading_doc.write_text("# T\n\n## Sekcja\nTekst bez blanka.\n",
                               encoding="utf-8")
        result = run_case("validate-document.py", [str(heading_doc)])
        if result is None or "no blank line after heading" not in result.stdout:
            print(f"FAIL {label} - missing blank line after heading passes")
            failures += 1
        diacritics = tmp / "diacritics.md"
        diacritics.write_text("# Żółć\n\nŁąka ślimaka ę óą.\n\nŻółć łąka.\n",
                              encoding="utf-8")
        result = run_case("validate-document.py", [str(diacritics)])
        if (result is None or result.returncode != 0
                or result.stdout.count("non-ASCII letter(s)") != 1):
            print(f"FAIL {label} - diacritics did not aggregate into one warn")
            failures += 1
        before = tmp / "before.md"
        after = tmp / "after.md"
        before.write_text("# T\n\nAla — ma kota.\n", encoding="utf-8")
        after.write_text("# T\n\nAla - ma kota.\n", encoding="utf-8")
        result = run_case("diff-content.py",
                          [str(after), "--baseline", str(before),
                           "--normalize-chars"])
        if result is None or result.returncode != 0:
            print(f"FAIL {label} - --normalize-chars still flags the dash swap")
            failures += 1
        norm_doc = tmp / "norm.md"
        norm_doc.write_text("# T\n\nAla — ma kota…\n", encoding="utf-8")
        result = run_case("normalize-chars.py", [str(norm_doc)])
        if (result is None or result.returncode != 0
                or "—" in norm_doc.read_text(encoding="utf-8")):
            print(f"FAIL {label} - normalize-chars did not rewrite the file")
            failures += 1
    print(("PASS" if not failures else "FAIL") + f" {label}")
    return failures


def improvement_regressions() -> int:
    """Exercise the 2026-10 improvement fixes against synthetic fixtures."""
    failures = 0
    label = "improvement fixtures"
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        # I-1: word-boundary replace leaves containing words untouched
        replace_doc = tmp / "replace.md"
        replace_doc.write_text(
            "# T\n\nSekcja niesie ryzyko.\n\nOdniesienia zostają.\n",
            encoding="utf-8")
        result = run_case("safe-replace.py",
                          [str(replace_doc), "niesie", "wnosi"])
        text = replace_doc.read_text(encoding="utf-8")
        if (result is None or result.returncode != 0
                or "wnosi" not in text or "Odniesienia" not in text
                or "Odwnosinia" in text):
            print(f"FAIL {label} - safe-replace corrupted containing words")
            failures += 1
        result = run_case("safe-replace.py",
                          [str(replace_doc), "wnosi", "niesie", "--check"])
        if result is None or result.returncode != 0:
            print(f"FAIL {label} - safe-replace --check on a clean pattern")
            failures += 1

        # I-3: inflected calque forms flag, allowed words stay silent
        inflect_doc = tmp / "inflect.md"
        inflect_doc.write_text(
            "# T\n\n"
            "Funkcja jest przypięta i przypinana.\n\n"
            "Trzeba ją przypiąć przed bramą.\n\n"
            "Raport jest niesiony wraz z ładunku danych.\n\n"
            "Muszę się zastanowić, co zastanawia zespół.\n",
            encoding="utf-8")
        result = run_case("lint-polish.py",
                          [str(inflect_doc), "--rules",
                           "languages/pl.md", "--rules",
                           "translations/en-pl/en-pl-software.md"],
                          {"PYTHONIOENCODING": "utf-8"})
        if (result is None or result.returncode != 1
                or not all(form in result.stdout for form in (
                    "przypięta", "przypiąć", "bram", "niesiony"))
                or "zastanowić" in result.stdout
                or "zastanawia" in result.stdout):
            print(f"FAIL {label} - inflected calque coverage regressed")
            failures += 1

        # I-4: literal pipe inside a table code span flags
        pipe_doc = tmp / "pipe.md"
        pipe_doc.write_text(
            "# T\n\n| Cmd | Desc |\n|-----|------|\n"
            "| `a | b` run | ok |\n",
            encoding="utf-8")
        result = run_case("validate-document.py", [str(pipe_doc)])
        if (result is None or result.returncode != 1
                or "literal pipe inside code span" not in result.stdout):
            print(f"FAIL {label} - pipe inside table code span passes")
            failures += 1

        # I-5 + I-6: declared pairs report DECLARED, repeated spans match
        parity_src = tmp / "src.md"
        parity_tgt = tmp / "tgt.md"
        parity_src.write_text(
            "# T\n\n| S |\n|---|\n| `NOT SPECIFIED` |\n\n"
            + " ".join(["`as unknown as`"] * 6) + "\n",
            encoding="utf-8")
        parity_tgt.write_text(
            "# T\n\n| S |\n|---|\n| `Nieokreślony` |\n\n"
            + " ".join(["`as unknown as`"] * 6) + "\n",
            encoding="utf-8")
        expect_map = tmp / "map.txt"
        expect_map.write_text("NOT SPECIFIED -> Nieokreślony\n",
                              encoding="utf-8")
        result = run_case(
            "check-parity.py",
            [str(parity_src), str(parity_tgt), "--expect-map",
             str(expect_map)])
        if (result is None or result.returncode != 0
                or "DECLARED inline code" not in result.stdout
                or "as unknown as" in result.stdout):
            print(f"FAIL {label} - expect-map or repeated-span parity")
            failures += 1
        result = run_case(
            "check-parity.py",
            [str(parity_src), str(parity_tgt)])
        if (result is None or result.returncode != 1
                or "DELTA inline code" not in result.stdout):
            print(f"FAIL {label} - undeclared code delta must still gate")
            failures += 1

        # I-7: .gitattributes eol=lf downgrades the delta to a NOTE
        (tmp / ".gitattributes").write_text("*.md eol=lf\n",
                                           encoding="utf-8")
        (tmp / "eol-src.md").write_bytes(b"# T\r\n\r\nline\r\n")
        (tmp / "eol-tgt.md").write_bytes(b"# T\n\nline\n")
        result = run_case(
            "check-parity.py",
            [str(tmp / "eol-src.md"), str(tmp / "eol-tgt.md")])
        if (result is None or "matches declared eol=lf" not in result.stdout
                or "DELTA whitespace" in result.stdout):
            print(f"FAIL {label} - gitattributes eol not honored")
            failures += 1
        result = run_case(
            "check-parity.py",
            [str(tmp / "eol-src.md"), str(tmp / "eol-tgt.md"),
             "--eol", "crlf"])
        if (result is None or "contradicts declared eol=crlf"
                not in result.stdout):
            print(f"FAIL {label} - contradicting --eol must still gate")
            failures += 1

        # I-8: one mutated heading reports exactly one finding
        agree_doc = tmp / "agree.md"
        agree_doc.write_text(
            "# T\n\n"
            "| ID | Title |\n|----|-------|\n"
            "| F-01 | Weak [TLS](g.md#tls) setup |\n"
            "| F-02 | Missing rate limiting |\n\n"
            "### F-01: Weak TLS setup\n\nBody.\n\n"
            "### F-02: Missing rate limiting\n\nBody.\n",
            encoding="utf-8")
        result = run_case("check-titles.py", [str(agree_doc)])
        if result is None or result.returncode != 0:
            print(f"FAIL {label} - clean title agreement flagged")
            failures += 1
        agree_doc.write_text(
            agree_doc.read_text(encoding="utf-8").replace(
                "### F-02: Missing rate limiting",
                "### F-02: Mutated title"),
            encoding="utf-8")
        result = run_case("check-titles.py", [str(agree_doc)])
        if (result is None or result.returncode != 1
                or result.stdout.count("MISMATCH") != 1
                or "F-02" not in result.stdout):
            print(f"FAIL {label} - mutated heading must give one finding")
            failures += 1
    print(("PASS" if not failures else "FAIL") + f" {label}")
    return failures


def english_consistency_regressions() -> int:
    """Exercise lint-english and check-consistency on synthetic fixtures."""
    failures = 0
    label = "english-consistency fixtures"
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        # Errors gate: doubled word plus a banned vocabulary form.
        dirty = tmp / "dirty.md"
        dirty.write_text(
            "# T\n\nThe the plan must utilize in order to finish.\n",
            encoding="utf-8")
        result = run_case("lint-english.py", [str(dirty)])
        if (result is None or result.returncode != 1
                or "doubled word" not in result.stdout
                or "in order to" not in result.stdout):
            print(f"FAIL {label} - errors did not gate")
            failures += 1

        # Code spans stand in as placeholders - "a `None` option" is not an
        # article error, and "or `x` or" is not a doubled word.
        code_doc = tmp / "code.md"
        code_doc.write_text(
            "# T\n\nPick a `None` option or `x/` or `y/` value.\n\n"
            "An RFC and a README are fine.\n",
            encoding="utf-8")
        result = run_case("lint-english.py", [str(code_doc)])
        if result is None or result.returncode != 0:
            print(f"FAIL {label} - code-span placeholders still flag")
            failures += 1

        # Minority dialect warns but never gates.
        dialect = tmp / "dialect.md"
        dialect.write_text(
            "# T\n\nThe behavior and color are right.\n\n"
            "The behaviour is right.\n",
            encoding="utf-8")
        result = run_case("lint-english.py", [str(dialect)])
        if (result is None or result.returncode != 0
                or "minority dialect" not in result.stdout):
            print(f"FAIL {label} - dialect warning lost or gated")
            failures += 1

        # Unresolved quoted reference gates; heading and bold-term anchors
        # resolve; literals and weak-context single words stay silent.
        ref_doc = tmp / "refs.md"
        ref_doc.write_text(
            "# T\n\n## Decision Points\n\nText.\n\n"
            'See "Decision Points" and the "Missing Name" section.\n\n'
            'Pick the "none" option or "a README" literal.\n\n'
            "**Bold Term**\n\nDetails under \"Bold Term\".\n",
            encoding="utf-8")
        result = run_case("check-consistency.py", [str(ref_doc)])
        if (result is None or result.returncode != 1
                or result.stdout.count("UNRESOLVED") != 1
                or "Missing Name" not in result.stdout):
            print(f"FAIL {label} - reference resolution regressed")
            failures += 1

        # Heading-vs-heading parallel names never pair as variants, but a
        # quoted drift term pairs with the heading it resembles.
        drift = tmp / "drift.md"
        drift.write_text(
            "# T\n\n## Setup for New Projects\n\n## Setup for Old Projects\n\n"
            "## Document and Agent-Entry Tree\n\n"
            'See "Document and Agent Structure Tree".\n\n'
            "The document and agent entry tree appears here.\n",
            encoding="utf-8")
        result = run_case("check-consistency.py", [str(drift)])
        if (result is None or result.returncode != 1
                or "Setup for New Projects" in result.stdout
                or "UNRESOLVED" not in result.stdout
                or "VARIANT" not in result.stdout
                or "Document and Agent Structure Tree" not in result.stdout):
            print(f"FAIL {label} - variant suppression or detection regressed")
            failures += 1
    print(("PASS" if not failures else "FAIL") + f" {label}")
    return failures


def main() -> int:
    failures = 0
    for script, args, exits, prefix, env_extra in CASES:
        result = run_case(script, args, env_extra)
        label = " ".join([script, *args])
        if result is None:
            print(f"FAIL {label} - no result (timeout or missing executable)")
            failures += 1
            continue
        if "Traceback" in result.stderr:
            print(f"FAIL {label} - unhandled traceback")
            failures += 1
            continue
        if result.returncode not in exits:
            print(f"FAIL {label} - exit {result.returncode}, expected one of {exits}")
            failures += 1
            continue
        if prefix and not result.stdout.startswith(prefix):
            print(f"FAIL {label} - stdout missing '{prefix.strip()}' prefix")
            failures += 1
            continue
        print(f"PASS {label} - exit {result.returncode}")
    failures += table_defect_case()
    failures += heuristic_regressions()
    failures += improvement_regressions()
    failures += english_consistency_regressions()
    print(f"RESULT {len(CASES) + 4 - failures}/{len(CASES) + 4} tools passed")
    return 1 if failures else 0


if __name__ == "__main__":
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(errors="backslashreplace")
    raise SystemExit(main())
