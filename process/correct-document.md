# Correct Document

## Purpose

> **Scope:** The standalone procedure for correcting a document in place
> **Key items:** target resolution, governing rules, source resolution,
> correction classes, check pass, translation-quality layer, plan confirmation,
> correction pass, fidelity proposals, validation, report

A correction repairs a document in place - it finds what violates the governing
rules and fixes it.

It modifies the target document, never a resolved source.

Use it when the request asks to correct, fix, or proofread a document's
formatting, sections, language, or style.

## When This Applies

The correction task activates on requests such as "correct this document", "fix
the errors in this document", "proofread this file", "correct the grammar", "fix
the typos", or their localized equivalents declared in the matching `languages/`
file.

Neighboring tasks stay distinct:

- Analysis without changes is a document audit - follow
  `process/document-audit.md`.
- A scoped change the request names - "add a section", "update the glossary" -
  is an Edit task.
- A formatting-only pass the request names - "align this table", "unwrap the
  document" - is a Reformat task.
- A fresh render of a source is a Translate task - follow
  `process/translate-document.md`.
- A request that names the translation itself - "fix this translation", "correct
  the translated document", "apply the review findings" - is a Revise task per
  `process/translation-revision.md`.

A document-named correction request whose target resolves to a translation
source is still one Correct task - the translation-quality layer below runs
inside this procedure.

## Target Resolution

The target is the document named by the request.

When the request names none, the target is the file the request centers on.

Markdown documents get the full procedure.

Other text formats get the character and spacing surface only - encoding,
typographic characters, spacing, and blank lines - and the report records the
partial coverage as a `Note`.

## Governing Rules

Read the target repository's own rule documents first, per
`process/document-audit.md` - `README.md`, `AGENTS.md`, and declared rule files
such as `GUIDELINES.md` or `STYLE.md`.

The document's own conventions win over skill defaults.

Where the repository is silent, the matching `languages/` baseline and `types/`
file supply the defaults.

Directories the repository marks frozen or excluded stay out of scope unless the
request names them.

## Detection And Source Resolution

Run the detection pass from `process/document-workflow.md` before planning any
edit - `scripts/detect-encoding.py`, the Markdown dialect, the prose layout,
quote and apostrophe style, list markers, table alignment, and embedded payload
regions.

Then resolve whether the target is a translation, per the Pair Resolution in
`process/translation-revision.md`: the request pairs it to a source, or a
sibling file without the language code exists - `guide-pl.md` pairs with
`guide.md`.

A resolved source turns on the translation-quality layer below and loads the
pair's rule set per `process/translate-document.md` - the target-language
baseline, `<pair>-general.md`, `<pair>-style.md` when it exists, the resolved
format-contract mapping, and every matching industry glossary.

When no source resolves, the correction runs monolingual and the report says so.

## Correction Classes

Every issue the checks surface belongs to one class.

| Class                  | Handling | Covers                                                        |
|------------------------|----------|---------------------------------------------------------------|
| `formatting`           | applied  | table alignment, comment columns, spacing and blank lines,    |
|                        |          | trailing whitespace, packed sentences, typographic characters |
| `structure`            | applied  | missing required or recommended sections, heading depth and   |
|                        |          | case, contents drift, dead internal anchors                   |
| `language`             | applied  | grammar, agreement, punctuation, typos, doubled words,        |
|                        |          | misspellings, vocabulary-table violations                     |
| `style`                | applied  | overloaded sentences, register drift, heading case,           |
|                        |          | discouraged forms                                             |
| `consistency`          | applied  | terminology drift, unresolved quoted references, variant      |
|                        |          | spellings                                                     |
| `translation-fidelity` | proposed | calques, modality and condition drift, meaning drift,         |
|                        |          | concordance breaks, untranslated-set corruption               |

The `proposed` class requires a resolved source - a monolingual run has no
fidelity findings.

A request that narrows scope - "correct only the typos", "fix the tables" -
limits the run to the named classes, and the report names the scope it ran.

## Check Pass

Run the mechanical battery through `scripts/check-document.py`, exactly as the
document audit does:

```bash
python3 <skill-root>/scripts/check-document.py <file> --width <convention> --layout <wrap-or-unwrap>
```

Select the optional gates by target:

- `--split` - packed-sentence findings feed the `formatting` class.
- `--english` on `en` targets, `--polish` on `pl` targets - lint findings feed
  the `language` and `style` classes.
- `--consistency` - reference and terminology findings feed the `consistency`
  class.
- `--type <slug>` and `--language <code>` when the document type resolves -
  section findings feed the `structure` class.
- `--parity <source.md> --terms <glossary>` when a source resolved - the delta
  set feeds the translation-quality layer.
- `--payload-markdown` whenever the document embeds ` ```markdown ` blocks.

Run `scripts/census-document.py` for the structural picture the audit procedure
describes.

A German target has no language linter - the `language` and `style` classes run
as a manual review against `languages/de.md`, and the report states that
limitation.

## Translation-Quality Layer

This layer runs only when a source resolved in Detection.

Run the checks of `process/translation-audit.md` internally - the audit's
analysis-only contract is preserved because the deliverable here is the
corrected document plus a proposal list, not an audit report:

- `scripts/check-parity.py <source.md> <target.md>` with `--terms <glossary>`
  for every loaded glossary - the structure map, the inline-code diff, the
  untranslated-set verification, and the concordance hints.
- `scripts/lint-polish.py` on `pl` targets, with `--payload-markdown` when the
  document embeds ` ```markdown ` blocks.
- The Calque Traps tables of the loaded glossaries and the baseline's
  vocabulary table.

Classify each finding per the Issue Classes in
`process/translation-revision.md`.

Findings that name `language` or `style` defects in the target - grammar,
typos, register, heading case - join the Correction Pass like any document
issue.

Findings that can shift meaning - `calque`, `terminology`, `meaning drift`, `modality`,
`identifier`, and `structure` fidelity - are never applied by this procedure.

Each is written up as a proposal per `When a corrected defect class appears in a generated or template-derived
document, the same class is checked against the producing template and its
sibling outputs, so the fix covers the source of the pattern, not only the file
that surfaced it.

## Fidelity Proposals` below.

## Plan Confirmation

The standard gate from `process/document-workflow.md` runs before the
Correction Pass.

The plan names the target, the governing rule set, the detected conventions,
the correction classes in scope with their finding counts, and whether the
translation-quality layer ran.

The `plan-confirmation` choice offers `Proceed` (recommended), `Adjust`, and
`Cancel`.

Under the shared `autonomous` flag the gate resolves to `Proceed` without
waiting, and `verbose` adds the offered options with their rationale, per the
Autonomous Surfaces section of `process/json-exchange.md`.

## Correction Pass

Apply the `applied` classes in place, minimal diff.

Run the scripted fixes first, in the mutating-pass order of
`process/document-workflow.md` - `scripts/normalize-chars.py`,
`scripts/split-sentences.py`, `scripts/reflow-prose.py`,
`scripts/align-comments.py`, and `scripts/format-table.py` last, because any
later text edit inside a cell re-breaks the source alignment.

Missing sections feed the `section-add` selection surface before insertion -
inserted sections land at their canonical positions per the type's
`## Structure` order and carry `NOT SPECIFIED` markers, no content is invented.

Language, style, and typo fixes are hand edits per the language baseline - an
overloaded sentence is split by rewriting it into two sentences, never by a
mechanical split that reorders the wording.

A fix applied to one instance sweeps the document for the same class of issue,
per `process/translation-revision.md` - scripted bulk replacements run through
`scripts/safe-replace.py` word-boundary matching, never bare substrings.

A systematic in-document convention stays untouched and is reported as a
convention, per `process/document-audit.md` - the correction never normalizes a
deliberate convention silently.

The document's encoding, byte order mark, line endings, dialect markers, and
payload regions are preserved per the File Handling Contract in `SKILL.md`.

## Fidelity Proposals

Every `translation-fidelity` finding is written up as a proposal, never
applied.

A proposal names the target passage, the aligned source passage, the
recommended rendering, and the rule source that judges it - the same alignment
evidence `process/translation-revision.md` requires before any edit.

Approving the proposals converts them into a Revise task per
`process/translation-revision.md`, which applies them minimal-diff against the
source.

Under JSON exchange the approval question emits as the `fidelity-proposals`
`choice` parameter.

## Validation

Re-run the battery on the corrected file with the same gates - every check that
covers an applied class must pass or be reported:

- `scripts/validate-document.py`, with `--payload-markdown` when the document
  embeds payloads.
- `scripts/format-table.py --check` on every document that contains tables.
- `scripts/lint-english.py` on `en` output and `scripts/lint-polish.py` on `pl`
  output - every finding fixed or reported.
- `scripts/reflow-prose.py --wrap --check --width N` or `--unwrap --check` per
  the detected convention.
- `scripts/check-sections.py` when the document type is known.
- `scripts/check-consistency.py` - the correction introduced no unresolved
  references.
- `scripts/check-parity.py` re-run when the quality layer ran - the residual
  deltas are the proposed set.
- `scripts/diff-content.py --baseline <snapshot>` verifies an unchanged token
  stream only when the request scoped the correction to formatting - language
  fixes change tokens by design.
- `git diff --check` inside a repository.

A failing check is fixed or explicitly reported with a reason.

## Report

Deliver the report inline unless the request asks for a file.

Structure it as:

1. **Summary** - what was corrected and the scope that ran.
2. **Document Facts** - path, type, language, dialect, detected conventions,
   and the resolved source and direction when present.
3. **Corrections** - every applied fix with its class, location, old text, new
   text, and the rule source.
4. **Proposals** - fidelity findings with the aligned source passage and the
   recommended rendering, each marked `proposed`, `approved - revised`, or
   `rejected` with reason.
5. **Checks** - every check run or skipped and its result.
6. **Conventions And Limitations** - in-document conventions left untouched and
   what was not covered, for example the missing German language lint.

## Non-Goals

The correction never edits a resolved source document.

It never invents content - inserted sections carry `NOT SPECIFIED` markers.

It is not a wholesale rewrite or retranslation - when a translation diverges
pervasively rather than locally, recommend a fresh translation instead.

Fidelity proposals are never applied inside this procedure - their execution is
a Revise task.

A systematic in-document convention is reported, never normalized.
