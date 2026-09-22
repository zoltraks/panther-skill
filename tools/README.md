# Panther Tooling

## Purpose

> **Scope:** Document-production and skill-maintenance scripts
> **Key items:** encoding detection, scope signals, sentence splitting, prose wrapping,
> table formatting, document validation, content diffing, document census, skill
> validation, reference integrity, self-update check

These scripts support deterministic production of documents and maintenance of Panther itself.

They do not modify documents beyond the specific task each tool performs.

## Tool Classes

### Document-Production Tools

Copy `detect-encoding.py`, `detect-scope.py`, `split-sentences.py`, `wrap-prose.py`,
`format-table.py`, `validate-document.py`, `diff-content.py`, and `census-document.py` into
the working repository's `work/` directory under a `.tmp.` name before use.

If `work/` does not exist, use an existing `temp` or `temporary` directory.

When the project declares a temporary directory - for example `work/` in its guidelines or
`.gitignore` - that does not exist yet, create it for the copy rather than using the repository
root.

Use the repository root only when no declared or existing temporary directory applies.

Run the copied scripts only against the document being created, edited, or audited.

Remove every copied script after use.

### Skill-Maintenance Tools

Run `validate-skill.py`, `check-references.py`, and `check-update.py` from the Panther repository.

These tools inspect the skill itself and are never copied into a working project.

`check-update.py` reports the git upstream status of the skill repository for the once-per-session
Skill Update Check in `SKILL.md`, and always exits `0` with a `STATUS` verdict line.

They use the Python standard library and do not require PyYAML or a package manager.

## Commands

```text
python detect-encoding.tmp.py <file>
python detect-scope.tmp.py <directory>
python split-sentences.tmp.py <file.md> [--check] [--width N] [--payload-markdown]
python wrap-prose.tmp.py <file.md> [--check] [--width N] [--payload-markdown]
python format-table.tmp.py <file.md> [--check] [--payload-markdown]
python validate-document.tmp.py <file.md> [--width N] [--payload-markdown]
python diff-content.tmp.py <file.md> [--baseline <file>]
python census-document.tmp.py <file.md> [--width N] [--payload-markdown]
python tools/validate-skill.py .
python tools/check-references.py .
python tools/check-update.py
```

`detect-encoding.py` and `detect-scope.py` always exit `0` and print a report.

`split-sentences.py` rewrites the file in place, `--check` only reports lines that pack
multiple sentences.

It emits each paragraph sentence starting on its own logical line and re-wraps the affected
sentences to `--width N`.

It leaves list items and their continuation lines opaque - a packed list item is an
element-level convention, not a defect (see `conventions/markdown-dialects.md`).

Lines ending in `:` are treated as label lines and never absorb following sentences.

Abbreviations such as `e.g.` and `etc.` and periods inside inline code spans do not count as
boundaries.

`wrap-prose.py` rewrites the file in place, `--check` only reports lines that would be
wrapped.

It only splits over-width lines at whitespace - it never joins lines, and it leaves tables,
fenced code blocks, indented code blocks, HTML comments, and frontmatter untouched.

`--payload-markdown` extends `split-sentences.py`, `wrap-prose.py`, `format-table.py`, and
`validate-document.py` into ` ```markdown ` fenced blocks, all other fence languages stay
opaque.

`diff-content.py` compares the normalized token stream of a document against `git show HEAD`
or a `--baseline` file, identical tokens mean a pass changed formatting only.

It exits `0` in every case and prints `WARN` for possible merged lines - review those by hand.

`detect-scope.py` reports a signal census only - the agent maps signals to a scope per
`process/scope-discovery.md`.

Its directory census also lists `docs/` subdirectories, non-document artifacts such as API
specifications and configs, and `.gitignore`-declared directories that are absent on disk.

`census-document.py` reports a structural census of a single document - headings, list
markers, fenced blocks and ` ```markdown ` payloads, special characters, paragraph shape,
tables, task markers, and internal links - and the agent maps counts to findings per
`process/document-audit.md`.

The validators exit `0` when all checks pass and `1` when one or more checks fail.

## Validation Order

Run `detect-scope.py` on the target directory first when the task needs the document scope.

Run checks in this order:

1. Detect encoding before editing an existing file.
2. Check packed sentences with `split-sentences.py --check` when the request covers
   sentence separation.
3. Check wrap convention with `wrap-prose.py --check` when a width rule applies.
4. Format edited tables with `format-table.py`.
5. Validate the written document with `validate-document.py`.
6. Verify formatting-only passes with `diff-content.py`.
7. Run `git diff --check` when inside a repository.
8. Remove temporary `.tmp.` copies from the working repository.

For skill maintenance, run `validate-skill.py` and `check-references.py` first.

## Limitations

`format-table.py` and `validate-document.py` split table rows on every `|` character.

Escaped `\|` sequences and pipes inside inline code spans are not supported, so table cells must
not contain literal pipe characters.

`validate-document.py` skips fenced code blocks when checking tables - example tables inside
code fences, such as AsciiDoc samples, are payload, not Markdown tables.

Pass `--payload-markdown` to apply a curated subset of checks inside ` ```markdown ` blocks:
trailing whitespace, consecutive blank lines, lone list markers, and line width.

`diff-content.py` is a heuristic net, not a proof - its merged-line warnings require manual
review, and a clean report still does not replace reading the diff.

`split-sentences.py` detects boundaries heuristically - review its diff before accepting,
and prefer leaving a questionable line packed over splitting it wrong.

The validators are mechanical checks, not judgment.

A passing validator does not prove that a document is well written or correct.

Use the prompts in `evals/evals.json` for behavioral regression checks.
