# Panther Tooling

## Purpose

> **Scope:** Document-production and skill-maintenance scripts
> **Key items:** encoding detection, scope signals, table formatting, document validation,
> skill validation, reference integrity

These scripts support deterministic production of documents and maintenance of Panther itself.

They do not modify documents beyond the specific task each tool performs.

## Tool Classes

### Document-Production Tools

Copy `detect-encoding.py`, `detect-scope.py`, `format-table.py`, and `validate-document.py`
into the working repository's `work/` directory under a `.tmp.` name before use.

If `work/` does not exist, use an existing `temp` or `temporary` directory.

When the project declares a temporary directory - for example `work/` in its guidelines or
`.gitignore` - that does not exist yet, create it for the copy rather than using the repository
root.

Use the repository root only when no declared or existing temporary directory applies.

Run the copied scripts only against the document being created or edited.

Remove every copied script after use.

### Skill-Maintenance Tools

Run `validate-skill.py` and `check-references.py` from the Panther repository.

These tools inspect the skill itself and are never copied into a working project.

They use the Python standard library and do not require PyYAML or a package manager.

## Commands

```text
python detect-encoding.tmp.py <file>
python detect-scope.tmp.py <directory>
python format-table.tmp.py <file.md>
python validate-document.tmp.py <file.md>
python tools/validate-skill.py .
python tools/check-references.py .
```

`detect-encoding.py` and `detect-scope.py` always exit `0` and print a report.

`detect-scope.py` reports a signal census only - the agent maps signals to a scope per
`process/scope-discovery.md`.

Its directory census also lists `docs/` subdirectories, non-document artifacts such as API
specifications and configs, and `.gitignore`-declared directories that are absent on disk.

The validators exit `0` when all checks pass and `1` when one or more checks fail.

## Validation Order

Run `detect-scope.py` on the target directory first when the task needs the document scope.

Run checks in this order:

1. Detect encoding before editing an existing file.
2. Format edited tables with `format-table.py`.
3. Validate the written document with `validate-document.py`.
4. Run `git diff --check` when inside a repository.
5. Remove temporary `.tmp.` copies from the working repository.

For skill maintenance, run `validate-skill.py` and `check-references.py` first.

## Limitations

`format-table.py` and `validate-document.py` split table rows on every `|` character.

Escaped `\|` sequences and pipes inside inline code spans are not supported, so table cells must
not contain literal pipe characters.

`validate-document.py` skips fenced code blocks when checking tables - example tables inside
code fences, such as AsciiDoc samples, are payload, not Markdown tables.

The validators are mechanical checks, not judgment.

A passing validator does not prove that a document is well written or correct.

Use the prompts in `evals/evals.json` for behavioral regression checks.
