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

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TIMEOUT = 60

# (script, args, accepted exits, required stdout prefix)
CASES: list[tuple[str, list[str], tuple[int, ...], str | None]] = [
    ("validate-skill.py", ["."], (0,), None),
    ("check-references.py", ["."], (0,), None),
    ("check-contents.py", ["."], (0,), None),
    ("check-update.py", [], (0,), "STATUS "),
    ("detect-encoding.py", ["README.md"], (0,), None),
    ("detect-scope.py", ["."], (0,), None),
    ("census-document.py", ["README.md"], (0,), None),
    ("split-sentences.py", ["README.md", "--check"], (0, 1), None),
    ("split-sentences.py", ["README.md", "--paragraphs", "--check"], (0,), None),
    ("wrap-prose.py", ["README.md", "--check"], (0, 1), None),
    ("reflow-prose.py", ["README.md", "--wrap", "--check"], (0, 1), None),
    ("reflow-prose.py", ["README.md", "--unwrap", "--check"], (0, 1), None),
    ("format-table.py", ["README.md", "--check"], (0, 1), None),
    ("align-comments.py", ["README.md", "--check"], (0, 1), None),
    ("validate-document.py", ["README.md"], (0, 1), None),
    ("diff-content.py", ["README.md"], (0, 1), None),
]


def run_case(script: str, args: list[str]) -> subprocess.CompletedProcess | None:
    try:
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / script), *args],
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
            cwd=ROOT,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None


def main() -> int:
    failures = 0
    for script, args, exits, prefix in CASES:
        result = run_case(script, args)
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
    print(f"RESULT {len(CASES) - failures}/{len(CASES)} tools passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
