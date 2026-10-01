# Translation Audit

## Purpose

> **Scope:** The standalone procedure for auditing a translated document against its source
> **Key items:** target resolution, rule loading, fidelity classification, structure map,
> untranslated-set verification, terminology concordance, style conformance, findings, report

A translation audit answers "how faithfully does this rendering reproduce its source".

It is analysis only - it changes nothing in either document.

Use it when the request asks to audit, verify, check, or compare a translation against its
source, or asks how a document was translated.

## Target Resolution

Resolve the source document and the translated document the request pairs.

When the request names only the translation, the source is the sibling file without the
language code - `guide-pl.md` pairs with `guide.md` - or the file the request names as the
source.

Ask when no source can be resolved - under JSON exchange this emits as the `source-resolution`
`text` parameter with `open: true`.

Detect the direction from the pair - an English source and a Polish rendering is an
`en-pl` audit - and report it.

## Rule Loading

Load the same rule set a translate task for the pair would have used, per
`process/translate-document.md`:

1. `languages/<dst>.md` - the target baseline.
2. `translations/<pair>/<pair>-general.md` - the direction contract.
3. `translations/<pair>/<pair>-style.md` - the pair's sentence-level adaptation rules,
   when the pair provides one.
4. `translations/<pair>/<pair>-<category>.md` - every glossary the document's domain
   signals.
5. `types/<type>.md` - when the source matches a known type.

The audited pair is judged against the rules that were in force for the translation -
when the translation predates this skill, the current rules still supply the audit's
vocabulary and severities, and the report notes the timing.

## Fidelity Classification

Classify the expected fidelity before judging deltas:

- `faithful` - the default: structure preserved one-to-one.
- `adapted` - the translation declares an adaptation contract, or evidence shows an
  intentional abridgment: compressed length, merged sections, reordered blocks.

A structural delta matching a declared or evident adaptation contract is reported as an
`Adaptation`, not a defect - an adaptation without a visible contract is reported as a
`Major` finding because the delta is unauditable.

## Audit Checks

Run the checks in order and record each result for the report:

1. **Structure map** - align the two documents heading by heading and classify every
   source heading as `faithful`, `reworded`, `dropped`, `merged`, `reordered`, plus every
   target-only heading as `added` - a faithful translation yields only `faithful` and
   `reworded` classes.
2. **Untranslated set** - verify byte-identity of code block content, inline code
   spans, file paths, URLs, commands, identifiers, frontmatter, and the `TBD` and
   `NOT SPECIFIED` markers against the pair file's untranslated list - comments and
   natural-language string values inside examples follow the pair's reader-facing
   rule and may differ.
3. **Terminology concordance** - map every glossary-covered source term to its target
   rendering and flag a term rendered by several different forms (a split rendering), a
   glossary form ignored, an invented equivalent, and every calque the pair file or
   baseline names.
4. **Style conformance** - heading capitalization per the target baseline, section names
   mapped through the type table, quote and dash conventions, diacritics completeness, and
   one register throughout.
5. **Embedded payloads** - ` ```markdown ` interiors are translated or declared verbatim,
   applied consistently across the document.
6. **Language naturalness** - run `scripts/lint-polish.py` for `pl` targets and review
   flagged lines. Scan for calques the pair's Calque Traps table names, clauses spliced
   by a bare comma, a participial opener missing its comma, personified files or
   branches, completed verdicts rendered against the pair style file's aspect rule,
   report-register verbs mismatched to its verb-choice mapping, modality drift
   (`must`/`should`/`may` strength altered), condition drift (`only`, `unless`,
   `when`, `if`, `otherwise` blurred), mixed quote or dash conventions, mixed
   second-person register, and the same English term rendered by several Polish
   forms.

## Findings

Structure every finding per `process/document-audit.md` - `FINDING-001` IDs, `Critical`,
`Major`, `Minor`, or `Note` severity, one-sentence finding, line evidence plus the rule
source.

Severity guidance:

- `Critical` - content mistranslated so the meaning changed, or large untranslated blocks
  the rules required translated.
- `Major` - a structural delta without a declared adaptation, untranslated-set corruption,
  a glossary term ignored document-wide, or a modality or condition drift that changes
  the instruction's strength.
- `Minor` - heading-case violations, inconsistent term renderings, style-adaptation
  misses, calques and unnatural phrasing that do not shift the meaning.
- `Note` - evident adaptations worth surfacing, register choices, timing notes.

## Report

Deliver the report inline unless the request asks for a file.

Structure it as:

1. **Verdict** - `faithful`, `declared adaptation`, or `defective`, with the one-line
   basis.
2. **Document Facts** - source path, translation path, direction, glossaries applied,
   fidelity classification.
3. **Structure Map** - the delta counts by class and every non-faithful entry.
4. **Findings** - the findings table.
5. **Limitations** - what could not be verified, for example a source version that no
   longer exists.

## Non-Goals

The audit never retranslates or fixes the target document - applying its findings is a
Revision task per `process/translation-revision.md`, run only when the user asks.

It does not grade the source document's own quality.

It does not audit machine-translation output line by line - it verifies conformance to the
pair's rules, not linguistic elegance.
