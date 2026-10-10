# Translation Revision

## Purpose

> **Scope:** The standalone procedure for correcting an existing translated document
> **Key items:** pair resolution, review input, passage alignment, issue classes,
> minimal-diff correction, same-class sweep, validation, report

A translation revision corrects an existing translation against its source and the
pair's rules.

It modifies the target document, never the source.

Use it when the request asks to fix, correct, or improve an existing translation, or
to apply review findings to one.

## When This Applies

The revision task activates on requests such as "fix this translation", "correct the
translated document", "apply the review findings to the translation", or their
localized equivalents declared in the matching `languages/` file.

Three neighboring tasks stay distinct:

- A fresh render of a source is a Translate task - follow
  `process/translate-document.md`.
- An analysis of translation quality without changes is a translation audit - follow
  `process/translation-audit.md`.
- A content change unrelated to translation fidelity is an Edit task.

A request that combines analysis with correction is one Revision task - the audit's
checks run internally, and the deliverable is the corrected document.

## Pair Resolution

Resolve the translated document and its source the request pairs.

When the request names only the translation, the source is the sibling file without
the language code - `guide-pl.md` pairs with `guide.md` - or the file the request
names as the source.

Detect the direction from the pair and load the rules that direction declares, per
`process/translate-document.md` - the target-language baseline, the pair's
`-general` file, its `-style` file when it exists, the resolved format-contract
mapping when the source is governed-format, and every matching industry glossary.

When no source can be resolved, proceed in grammar-and-terminology mode: apply
mechanical and glossary findings only, and state in the report that no source
alignment was possible.

## Review Input

The request arrives with or without a review.

A supplied review may be a findings table, a free-text list, or inline markers in the
document - parse each entry into a target passage plus its recommended change.

When no review is supplied, or the request asks to find the problems first, run the
checks of `process/translation-audit.md` internally to build the findings list -
the audit's analysis-only contract is preserved because the deliverable here is the
corrected document, not an audit report.

## Passage Alignment

Every finding is located in the target document and aligned with its source passage
before any edit.

Locate the passage the finding names - by heading, quote, or description - then map
it to the corresponding source passage through the structure map.

Never correct a passage by its Polish wording alone - the source sentence decides
what the correct rendering is, so a stylistic polish never drifts the meaning.

A finding whose passage cannot be located is reported as unapplied, not guessed.

## Issue Classes

Classify each finding before correcting it:

- `grammar` - syntax, agreement, or punctuation error.
- `terminology` - a glossary term rendered inconsistently or against the table.
- `calque` - a literal English construction the Calque Traps or vocabulary table
  names.
- `meaning drift` - the translation changes what the source says.
- `modality` - `must`/`should`/`may` strength altered, or a condition (`only`,
  `unless`, `when`, `if`, `otherwise`) blurred.
- `identifier` - a filename, path, command, key, or marker translated or broken.
- `structure` - a heading, anchor, or link text out of sync with the translation.
- `style` - register, voice, or phrasing inconsistent with the baseline.

## Correction

Apply the minimal edit that resolves the finding.

A correction is never a wholesale retranslation - passages the review does not flag
and the rules do not fail stay untouched.

One term keeps one form - a term corrected in one place is corrected in every place
the source uses it, so the document stays concordant.

Fix a finding and sweep the document for the same class of issue - a review row is
an example of the rule, not the whole of it.

Preserve the target document's own conventions - encoding, line endings, wrap,
tables, and every structure element the source carries.

Recompute an internal anchor or link text only when a heading it targets changes.

## Validation

Run the mechanical checks on the corrected file:

- `scripts/format-table.py` - mandatory when the document contains tables.
- `scripts/validate-document.py` - with `--payload-markdown` when the document
  embeds ` ```markdown ` blocks.
- `scripts/lint-polish.py` - on `pl` output - every finding is fixed or reported.

Self-review against `process/document-checklist.md` plus the translation items:

- Modality strength is preserved - `must` renders `musi` or `należy`, `must not`
  renders `nie wolno`, `should` renders `powinien`, `may` renders `może`.
- Conditions and exceptions survive exactly - `only`, `unless`, `when`, `if`,
  `otherwise` map one-to-one.
- Gender, number, and case still agree after every term substitution.
- Second-person pronouns stay lowercase - `cię`, `tobie`, `twój`.
- Localized markers stay coherent with the example commands that reference them.
- The corrected passages read naturally in Polish without consulting the source.

## Report

Deliver the report inline unless the request asks for a file.

Structure it as:

1. **Summary** - what was corrected and the revision's scope.
2. **Document Facts** - source path, translation path, direction, glossaries
   applied.
3. **Findings** - every finding with its source location, target location, issue
   class, and `applied` or `rejected` status with reason.
4. **Checks** - every check run or skipped and its result.

## Non-Goals

The revision never edits the source document.

It never silently retranslates the whole document - when the translation diverges
pervasively rather than locally, recommend a fresh translation instead.

It does not review the source document's own quality or restructure content the
source does not carry.
