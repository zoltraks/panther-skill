#!/usr/bin/env python3
"""Check relative file references across all Panther rule documents.

Scope:
  - SKILL.md and README.md are checked strictly: every backticked or linked path
    ending in a document suffix must resolve (bare names in SKILL.md are skipped
    because that file lists template basenames without their directory).
  - Every other rule document is checked conservatively: only paths under a
    known skill directory are verified, so filename examples such as
    `hardware/chip.md` or `CHANGELOG.md` are ignored.

Payload files under `templates/` and `docs/` are example artifacts, and `work/`
holds scratch material - none of them are rule documents, so they are not scanned.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


CODE_SPAN = re.compile(r"`([^`]+)`")
MARKDOWN_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")
PATH_SUFFIX = re.compile(r"(?:\.md|\.py|\.json|\.txt)$", re.IGNORECASE)

ROOT_FILES = ("SKILL.md", "README.md")
KNOWN_DIRS = {
    "tools", "types", "languages", "scopes", "conventions", "process",
    "principles", "templates", "evals",
}
EXCLUDED_DIRS = ("docs", "templates", "work")


def candidates(text: str) -> set[str]:
    values: set[str] = set()
    values.update(match.group(1) for match in CODE_SPAN.finditer(text))
    values.update(match.group(1) for match in MARKDOWN_LINK.finditer(text))
    return {
        value.strip()
        for value in values
        if PATH_SUFFIX.search(value.strip())
        and not value.strip().startswith(("http://", "https://", "mailto:", "#", "<"))
        and " " not in value.strip()
        and "<" not in value
        and ">" not in value
    }


def check_root_file(root: Path, name: str, issues: list[str]) -> None:
    source = root / name
    if not source.is_file():
        issues.append(f"missing navigation document: {name}")
        return
    text = source.read_text(encoding="utf-8")
    for raw in sorted(candidates(text)):
        value = raw.split("#", 1)[0]
        if not value or value.startswith("<"):
            continue
        if name == "SKILL.md" and "/" not in value and not value.startswith("./"):
            continue
        candidate = (source.parent / value).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            issues.append(f"{name}: reference escapes skill directory: {raw}")
            continue
        if not candidate.is_file():
            issues.append(f"{name}: reference does not resolve: {raw}")


def check_rule_file(root: Path, source: Path, issues: list[str]) -> None:
    label = source.relative_to(root)
    text = source.read_text(encoding="utf-8")
    for raw in sorted(candidates(text)):
        value = raw.split("#", 1)[0]
        if not value or value.startswith("<"):
            continue
        top = value.lstrip("./").split("/", 1)[0]
        if "/" not in value or top not in KNOWN_DIRS:
            continue
        candidate = (root / value).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            issues.append(f"{label}: reference escapes skill directory: {raw}")
            continue
        if not candidate.is_file():
            issues.append(f"{label}: reference does not resolve: {raw}")


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else Path.cwd().resolve()
    issues: list[str] = []

    for name in ROOT_FILES:
        check_root_file(root, name, issues)

    for source in sorted(root.rglob("*.md")):
        relative = source.relative_to(root)
        if str(relative) in ROOT_FILES:
            continue
        if relative.parts[0] in EXCLUDED_DIRS:
            continue
        check_rule_file(root, source, issues)

    if issues:
        for message in issues:
            print(f"FAIL {message}")
        print(f"{len(issues)} issue(s) found")
        return 1

    print("PASS root navigation references resolve")
    print("PASS rule document references resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
