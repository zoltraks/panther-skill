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
    print(f"RESULT {len(CASES) + 1 - failures}/{len(CASES) + 1} tools passed")
    return 1 if failures else 0


if __name__ == "__main__":
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(errors="backslashreplace")
    raise SystemExit(main())
