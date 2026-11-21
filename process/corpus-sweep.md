# Corpus Sweep

## Purpose

> **Scope:** The bulk-formatting procedure that applies the mechanical battery across a repository
> or directory of documents
>
> **Key items:** baseline snapshot, battery run, dialect classification before repair,
> mechanical classes only, attribution by snapshot compare

A corpus sweep normalizes mechanical formatting across many documents at once - the bulk form of the
per-file correction pass in `process/correct-document.md`.

Use it when the request asks to sweep, normalize, or reformat an entire docs tree,
repository, or directory set.

A single named document follows the correction procedure instead.

## Snapshot First

Before any repair runs, record the corpus state.

A clean git tree or a recorded `HEAD` anchors a versioned corpus.

An untracked or dirty corpus gets a `.tmp.` snapshot copy of every file in scope first.

The snapshot is the attribution anchor for the closing compare - without it the sweep cannot prove
it changed formatting only.

## Run The Battery For The FAIL List

Run `scripts/check-document.py <dir>` over the sweep scope.

It sweeps every `*.md` recursively, skipping `.git` and `work` trees,
and prints one verdict line per tool per file with an aggregate verdict at the end.

The gated findings form the work list.

`validate-document.py`, `format-table.py --check`,
and `align-comments.py --check` gate a first sweep.

Add `--split`, `--layout`, `--polish`, or `--english` only when the request names those surfaces.

## Classify Dialect Artifacts Before Fixing

Read the corpus's own style documents first - `STYLE.md`, `AGENTS.md`,
contributor guides - and run a dialect census on a sample of files before treating any
finding class as a defect.

A finding class that reproduces a documented convention is a dialect artifact,
not a defect - a flush-left lazy-continuation list, a packed consecutive-sentence layout,
or spaced table separators are conventions to preserve.

Declare each dialect in a `panther.json` at the corpus root, per `conventions/markdown-dialects.md`.

`lazy_continuation` suppresses the blank-line findings and repairs a flush-left list style attracts.

`sentence_layout` steers the `--split` check.

`findings` covers any class the dialect keys do not - record every suppression in the sweep report.

## Fix Mechanical Classes Only

Run `scripts/fix-document.py` per flagged file.

It repairs the mechanical finding classes in place - blank lines, semicolons, literal pipes,
table alignment, merged blockquote rows - and leaves structural and judgment findings untouched.

`--only <text>` scopes a run to one class for a controlled single-class pass across the corpus.

Findings outside the mechanical set - headings, fences, links, wrap conventions - stay manual.

Batch them into the report as a plan, never an applied edit.

## Attribution By Snapshot Compare

After the repairs, prove the sweep touched formatting only.

`scripts/diff-content.py <file> --baseline <snapshot>` compares token streams per file - identical
tokens mean a pass changed formatting alone.

A token delta is a content change - attribute it to a named repair or revert it.

The closing report counts findings per class, names the dialect declarations applied,
and lists every finding class left standing for a follow-up pass.
