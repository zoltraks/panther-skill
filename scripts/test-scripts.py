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
    ("diff-content.py", ["README.md"], (0, 1), None, None),
    ("lint-polish.py", ["README.md"], (0, 1), None, None),
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
                           "translations/en-pl/en-pl-software.md"])
        if (result is None or result.returncode != 1
                or "calque 'request'" in result.stdout
                or "possible calque 'rozjazd'" not in result.stdout
                or "[ERROR] calque 'requestować'" not in result.stdout):
            print(f"FAIL {label} - qualifier or quote handling regressed")
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
    print(f"RESULT {len(CASES) + 2 - failures}/{len(CASES) + 2} tools passed")
    return 1 if failures else 0


if __name__ == "__main__":
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(errors="backslashreplace")
    raise SystemExit(main())
