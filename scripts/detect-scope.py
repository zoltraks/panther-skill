#!/usr/bin/env python3
"""Report document-scope signals for a directory.

Census only - the agent maps signals to a scope, see process/document-workflow.md
and process/scope-discovery.md.

Copy this file into the working repository's `work/` directory (or the
repository root when no `work/` exists) as `detect-scope.tmp.py`, run it on the
target directory, then remove the copy.

Usage: python detect-scope.py <directory>
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

SKIP_DIRS = {
    ".git", ".svn", ".hg", "node_modules", "bin", "obj", "build",
    ".venv", "venv", "__pycache__", ".idea", ".vscode",
}
MANIFEST_NAMES = {
    "Cargo.toml", "package.json", "pyproject.toml", "go.mod", "pom.xml",
    "build.gradle", "composer.json", "Gemfile", "setup.py", "CMakeLists.txt",
}
MANIFEST_SUFFIXES = {".sln", ".csproj", ".fsproj", ".vbproj"}
VERSIONED_DIRS = (
    "feature", "change", "plan", "refactoring", "report",
    "standard", "template", "archive", "reference", "skill",
)
DOC_SUFFIXES = {".md", ".markdown", ".rst", ".txt"}
EXTRA_SUFFIXES = {".yaml", ".yml", ".json", ".example"}


def walk_files(root: Path):
    for current, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith("."))
        for name in sorted(files):
            yield Path(current) / name


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def read_head(path: Path, limit: int = 60) -> str:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            return "".join(handle.readlines()[:limit])
    except OSError:
        return ""


def find_first(root: Path, name: str, max_depth: int = 4) -> Path | None:
    for path in walk_files(root):
        if path.name == name and len(path.relative_to(root).parts) <= max_depth:
            return path
    return None


def find_dot_dir(root: Path, name: str, max_depth: int = 4) -> Path | None:
    for current, dirs, _files in os.walk(root):
        parts = Path(current).relative_to(root).parts
        if len(parts) > max_depth:
            dirs[:] = []
            continue
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        if name in dirs:
            return Path(current) / name
    return None


def emit(lines: list[str]) -> None:
    if lines:
        print("\n".join(lines))


def skill_signals(root: Path, out: list[str]) -> None:
    skill = root / "SKILL.md"
    out.append(f"  SKILL.md present: {'yes' if skill.is_file() else 'no'}")
    frontmatter = "no"
    if skill.is_file():
        head = read_head(skill, 40)
        if head.startswith("---") and "name:" in head and "description:" in head:
            frontmatter = "yes (name, description)"
    out.append(f"  frontmatter name/description: {frontmatter}")


def sphinx_signals(root: Path, out: list[str]) -> None:
    conf = find_first(root, "conf.py")
    master = "no"
    if conf is not None:
        master = f"yes ({rel(root, conf)})" if "master_doc" in read_head(conf, 400) else "no"
    out.append(f"  conf.py with master_doc: {master}")
    toctree = "no"
    for path in walk_files(root):
        if path.name == "index.rst" and ".. toctree::" in read_head(path, 200):
            toctree = f"yes ({rel(root, path)})"
            break
    out.append(f"  index.rst with toctree: {toctree}")
    make = find_first(root, "Makefile") or find_first(root, "make.bat")
    out.append(f"  Makefile or make.bat: {f'yes ({rel(root, make)})' if make else 'no'}")
    sphinx_req = "no"
    for path in walk_files(root):
        if path.name.startswith("requirements") and path.suffix == ".txt":
            if "sphinx" in read_head(path, 200).lower():
                sphinx_req = f"yes ({rel(root, path)})"
                break
    out.append(f"  sphinx in requirements: {sphinx_req}")


def guided_signals(root: Path, out: list[str]) -> list[str]:
    guidelines = root / "docs" / "GUIDELINES.md"
    out.append(f"  docs/GUIDELINES.md: {'yes' if guidelines.is_file() else 'no'}")
    readme = root / "README.md"
    out.append(f"  README.md at root: {'yes' if readme.is_file() else 'no'}")
    mention = "no"
    if readme.is_file() and "GUIDELINES" in read_head(readme, 400):
        mention = "yes"
    out.append(f"  README mentions guidelines: {mention}")
    markers: list[str] = []
    for entry in sorted(root.iterdir()) if root.is_dir() else []:
        if entry.name in MANIFEST_NAMES or entry.suffix in MANIFEST_SUFFIXES:
            markers.append(entry.name)
        elif entry.is_dir() and entry.name in {"src", "source", "lib", "app"}:
            markers.append(f"{entry.name}/")
        elif entry.is_dir() and any(
            (entry / m).exists() for m in MANIFEST_NAMES
        ):
            markers.append(f"{entry.name}/ (manifest)")
        elif entry.is_dir() and any(
            p.suffix in MANIFEST_SUFFIXES for p in entry.iterdir() if p.is_file()
        ):
            markers.append(f"{entry.name}/ (project file)")
    out.append(f"  code markers: {', '.join(markers) if markers else 'none'}")
    docs = root / "docs"
    found = []
    for name in VERSIONED_DIRS:
        subdir = docs / name
        if subdir.is_dir():
            count = sum(1 for p in subdir.iterdir() if p.is_dir())
            found.append(f"docs/{name}({count} subdirs)" if count else f"docs/{name}")
    out.append(f"  structured docs dirs: {', '.join(found) if found else 'none'}")
    if docs.is_dir():
        upper = sorted(
            p.stem for p in docs.iterdir()
            if p.is_file() and p.suffix == ".md" and p.stem.isupper()
        )
        out.append(f"  uppercase docs: {', '.join(upper) if upper else 'none'}")
    return markers


def collection_signals(root: Path, markers: list[str], out: list[str]) -> None:
    out.append(f"  documents-only shape: {'yes' if not markers else 'no'}")
    docs = root / "docs"
    for name in ("standard", "template", "archive"):
        subdir = docs / name
        count = sum(1 for p in subdir.rglob("*.md")) if subdir.is_dir() else 0
        out.append(f"  docs/{name}: {f'yes ({count} docs)' if count else 'no'}")


def multi_signals(root: Path, out: list[str]) -> None:
    projects = []
    for entry in sorted(root.iterdir()) if root.is_dir() else []:
        if not entry.is_dir() or entry.name in SKIP_DIRS or entry.name.startswith("."):
            continue
        signals = []
        if (entry / "README.md").is_file():
            signals.append("README")
        if (entry / "docs").is_dir():
            signals.append("docs/")
        if any((entry / m).exists() for m in MANIFEST_NAMES):
            signals.append("manifest")
        if signals:
            projects.append(f"{entry.name} ({'+'.join(signals)})")
    out.append(f"  project-like top dirs: {', '.join(projects) if projects else 'none'}")
    root_docs = sum(
        1 for p in (root / "docs").rglob("*.md")
    ) if (root / "docs").is_dir() else 0
    out.append(f"  root docs .md count: {root_docs}")


def mkdocs_signals(root: Path, out: list[str]) -> None:
    config = find_first(root, "mkdocs.yml") or find_first(root, "mkdocs.yaml")
    out.append(
        f"  mkdocs.yml or mkdocs.yaml: {f'yes ({rel(root, config)})' if config else 'no'}"
    )
    site_name = "no"
    if config is not None:
        site_name = "yes" if "site_name" in read_head(config, 200) else "no"
    out.append(f"  site_name key: {site_name}")
    nav = "no"
    if config is not None:
        nav = "yes" if re.search(r"^nav:", read_head(config, 400), re.MULTILINE) else "no"
    out.append(f"  nav key: {nav}")
    index = root / "docs" / "index.md"
    out.append(f"  docs/index.md: {'yes' if index.is_file() else 'no'}")


def docusaurus_signals(root: Path, out: list[str]) -> None:
    config = None
    for path in walk_files(root):
        if path.name.startswith("docusaurus.config"):
            config = path
            break
    out.append(
        f"  docusaurus.config.*: {f'yes ({rel(root, config)})' if config else 'no'}"
    )
    docs = (root / "docs").is_dir() or (root / "website" / "docs").is_dir()
    out.append(f"  docs or website/docs: {'yes' if docs else 'no'}")
    pages = (root / "src" / "pages").is_dir() or (
        root / "website" / "src" / "pages"
    ).is_dir()
    out.append(f"  src/pages: {'yes' if pages else 'no'}")
    sidebars = find_first(root, "sidebars.js") or find_first(root, "sidebars.ts")
    out.append(
        f"  sidebars.js or sidebars.ts: {f'yes ({rel(root, sidebars)})' if sidebars else 'no'}"
    )


def vitepress_signals(root: Path, out: list[str]) -> None:
    vitepress = find_dot_dir(root, ".vitepress")
    out.append(
        f"  .vitepress directory: {f'yes ({rel(root, vitepress)})' if vitepress else 'no'}"
    )
    config = "no"
    if vitepress is not None:
        names = sorted(
            p.name for p in vitepress.iterdir()
            if p.is_file() and p.name.startswith("config")
        )
        config = f"yes ({', '.join(names)})" if names else "no"
    out.append(f"  config file in .vitepress: {config}")


def gitbook_signals(root: Path, out: list[str]) -> None:
    dot_config = root / ".gitbook.yaml"
    out.append(f"  .gitbook.yaml: {'yes' if dot_config.is_file() else 'no'}")
    summary = root / "SUMMARY.md"
    outline = "no"
    if summary.is_file():
        head = read_head(summary, 80)
        has_links = re.search(r"\[[^\]]+\]\([^)]+\.md\)", head)
        has_groups = re.search(r"^#{1,2} ", head, re.MULTILINE)
        outline = "yes" if has_links or has_groups else "no"
    out.append(f"  SUMMARY.md with outline: {outline}")


def document_census(root: Path, out: list[str]) -> None:
    counts: dict[str, dict[str, int]] = {}
    for path in walk_files(root):
        suffix = path.suffix.lower()
        if suffix not in DOC_SUFFIXES:
            continue
        top = path.relative_to(root).parts
        key = top[0] if len(top) > 1 else "(root)"
        counts.setdefault(key, {}).setdefault(suffix, 0)
        counts[key][suffix] += 1
    for key in sorted(counts):
        per = ", ".join(f"{s}={n}" for s, n in sorted(counts[key].items()))
        out.append(f"  {key}: {per}")


def docs_subdirs(root: Path, out: list[str]) -> None:
    docs = root / "docs"
    if not docs.is_dir():
        out.append("  docs/ subdirectories: no docs/ directory")
        return
    found = []
    for entry in sorted(docs.iterdir()):
        if entry.is_dir():
            count = sum(
                1 for p in entry.rglob("*")
                if p.is_file() and p.suffix.lower() in DOC_SUFFIXES
            )
            found.append(f"{entry.name}/ ({count} docs)")
    out.append(f"  docs/ subdirectories: {', '.join(found) if found else 'none'}")


def artifact_census(root: Path, out: list[str]) -> None:
    counts: dict[str, int] = {}
    for path in walk_files(root):
        if path.name in MANIFEST_NAMES:
            continue
        if path.suffix.lower() not in EXTRA_SUFFIXES:
            continue
        top = path.relative_to(root).parts
        key = top[0] if len(top) > 1 else "(root)"
        counts[key] = counts.get(key, 0) + 1
    per = ", ".join(f"{k}={n}" for k, n in sorted(counts.items()))
    out.append(f"  non-document artifacts: {per if per else 'none'}")


def ignored_dirs(root: Path, out: list[str]) -> None:
    gitignore = root / ".gitignore"
    found = []
    if gitignore.is_file():
        for raw in read_head(gitignore, 400).splitlines():
            line = raw.strip()
            if not line or line.startswith(("#", "!")) or "*" in line:
                continue
            name = line.rstrip("/").lstrip("/")
            if not name or "/" in name:
                continue
            is_dir = (root / name).is_dir()
            if not line.endswith("/") and not is_dir:
                continue
            found.append(f"{name}/ ({'present' if is_dir else 'absent'})")
    out.append(f"  ignored directories: {', '.join(found) if found else 'none'}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python detect-scope.py <directory>")
        return 1
    root = Path(sys.argv[1]).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}")
        return 1

    print(f"Scope signal census for: {root}")
    print("agent-skill")
    skill_signals(root, lines := [])
    emit(lines)
    print("sphinx-docs")
    sphinx_signals(root, lines := [])
    emit(lines)
    print("guided-project")
    markers = guided_signals(root, lines := [])
    emit(lines)
    print("docs-collection")
    collection_signals(root, markers, lines := [])
    emit(lines)
    print("multi-project")
    multi_signals(root, lines := [])
    emit(lines)
    print("mkdocs-site")
    mkdocs_signals(root, lines := [])
    emit(lines)
    print("docusaurus-site")
    docusaurus_signals(root, lines := [])
    emit(lines)
    print("vitepress-site")
    vitepress_signals(root, lines := [])
    emit(lines)
    print("gitbook-site")
    gitbook_signals(root, lines := [])
    emit(lines)
    print("document census")
    document_census(root, lines := [])
    emit(lines)
    print("directory census")
    lines = []
    docs_subdirs(root, lines)
    artifact_census(root, lines)
    ignored_dirs(root, lines)
    emit(lines)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
