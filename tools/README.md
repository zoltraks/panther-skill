# Panther Tooling

## Purpose

> **Scope:** Document-production and skill-maintenance scripts
> **Key items:** encoding detection, table formatting, document validation, skill validation,
> reference integrity

These scripts support deterministic production of documents and maintenance of Panther itself.

They do not modify documents beyond the specific task each tool performs.

## Tool Classes

### Document-Production Tools

Copy `detect-encoding.py`, `format-table.py`, and `validate-document.py` into the working
repository's `work/` directory under a `.tmp.` name before use.

If `work/` does not exist, use an existing `temp` or `temporary` directory.

Use the repository root only when none of those directories exists.

Run the copied scripts only against the document being created or edited.

Remove every copied script after use.

### Skill-Maintenance Tools

Run `validate-skill.py` and `check-references.py` from the Panther repository.

These tools inspect the skill itself and are never copied into a working project.

They use the Python standard library and do not require PyYAML or a package manager.

## Commands

```text
python detect-encoding.tmp.py <file>
python format-table.tmp.py <file.md>
python validate-document.tmp.py <file.md>
python tools/validate-skill.py .
python tools/check-references.py .
```

`detect-encoding.py` always exits `0` and prints a report.

The validators exit `0` when all checks pass and `1` when one or more checks fail.

## Validation Order

Run checks in this order:

1. Detect encoding before editing an existing file.
2. Format edited tables with `format-table.py`.
3. Validate the written document with `validate-document.py`.
4. Run `git diff --check` when inside a repository.
5. Remove temporary `.tmp.` copies from the working repository.

For skill maintenance, run `validate-skill.py` and `check-references.py` first.

## Limitations

The validators are mechanical checks, not judgment.

A passing validator does not prove that a document is well written or correct.

Use the prompts in `evals/evals.json` for behavioral regression checks.
