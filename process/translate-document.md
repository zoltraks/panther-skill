# Translate Document

## Purpose

> **Scope:** The standalone procedure for rendering a document into another supported
> language while preserving its structure and adapting its style
> **Key items:** language pair resolution, industry glossary selection, single-pass
> translation, structure preservation, validation, delivery

This file defines the translate procedure.

Follow it whenever the request asks to translate, render, or produce a document in
another language.

## When This Applies

The translate task activates on requests such as "translate this document", "translate to
Polish", "translate this file to English", or their equivalents declared in the matching
`languages/` file.

Classify the request as Translate when it asks for the same document in a different
language.

A request that scopes the change to a fragment - "translate this section", "translate the
table" - is an Edit task that applies the translation rules to the edited fragment only.

A request to create a new document directly in a target language is a Create task - the
language baseline alone covers it, no translation files load.

A request to correct or fix an existing translation is a Revise task - follow
`process/translation-revision.md` instead.

## Parameter Resolution

Resolve these parameters before translating:

| Parameter       | Default                                                          |
|-----------------|------------------------------------------------------------------|
| Source language | Detected from the document, ask when ambiguous                   |
| Target language | Named by the request, ask when absent                            |
| Industry        | Detected from request, type, or terminology - ask when ambiguous |
| Output location | Sibling file `<basename>-<code>.md`                              |
| Fidelity        | faithful - one-to-one structure                                  |
| Encoding        | UTF-8 without BOM                                                |
| Line endings    | LF                                                               |

Confirm the parameters with the user per `process/document-workflow.md` - ask whether to
accept the defaults or configure them.

Under JSON exchange the gate emits as `parameters-acceptance`, and the per-parameter asks emit as
`source-language`, `target-language`, `translation-industry`, `translation-fidelity`,
`filename`, `encoding`, and `line-endings` per `process/json-exchange.md`.

Fidelity resolves to `adapted` only when the request explicitly asks for an adapted,
abridged, loose, or audience-adapted translation - it is never inferred from the source or
the target audience.

An in-place overwrite of the source file happens only when the request explicitly asks for
it and the user confirms, per the File Handling Contract.

Under JSON exchange the overwrite confirmation emits as `overwrite-confirmation`.

A language pair without a `translations/<pair>/<pair>-general.md` file is unsupported -
report it and ask whether to proceed with the language baselines only or to stop.

Under JSON exchange that question emits as the `unsupported-pair` `choice` parameter.

A source document already in the target language is a no-op - report it and stop.

## Detection

Read the whole source document before writing anything.

Identify the document language and its dialect per `conventions/markdown-dialects.md`.

Identify the document type - the matching `types/` file controls which section names the
translation maps through the language file's type table.

Identify the industry in this order:

1. The request names an industry or a glossary file.
2. The document type implies one - PMBOK types map to the `project` glossary, for
   example `translations/en-pl/en-pl-project.md` on an English to Polish task.
3. Terminology density inside the document.
4. Ask when still ambiguous, otherwise translate with no glossary - under JSON exchange the ask
   emits as the `translation-industry` `selection` parameter, since several glossaries may apply.

Several glossaries may apply to one document.

On a term conflict between glossaries, precedence runs request-named, then type-matched,
then alphabetical - record the conflict in the delivery report.

## Rule Loading

Load the rule files in this order:

1. `languages/<dst>.md` - the target baseline, mandatory for every translation.
2. `translations/<pair>/<pair>-general.md` - the direction contract: style adaptation,
   locale conventions, untranslated set, terminology resolution, output conventions.
3. `translations/<pair>/<pair>-style.md` - the pair's sentence-level adaptation rules,
   when the pair provides one.
4. `translations/<pair>/<pair>-<category>.md` - every matching industry glossary in the
   same pair directory. Category slugs are stable across pair directories - `project`
   means project management in every pair.
5. `types/<type>.md` - when the document matches a known type.
6. `conventions/` files - only when the source dialect requires them.

## Translation Pass

Render the document in a single pass - one terminology convention applies uniformly to the
whole output.

Preserve the structure one-to-one: heading depth, list shape and numbering, table geometry,
fenced blocks, links, frontmatter, and comments.

### Terminology Lock

Before rendering the first chunk of a chunked document, fix the recurring vocabulary once:

- Translate every heading text first - prose cross-references then have a fixed target
  and section names do not drift between chunks.
- Extract the repeated domain terms the loaded glossaries cover and pick one rendering per
  term *per sense* - `owner` the person and `owner` the document carrying the governing
  rules are different entries in the lock - a term rendered two ways across chunk
  boundaries is a defect the parity check reports.

The locked map may live in a `.tmp.` file inside the working repository's temporary
directory, removed at delivery per the File Handling Contract.

### Chunked Rendering

A document too long for one render pass is translated in chunks, each covering an
assigned source span bounded at heading boundaries.

Render sequentially: for each chunk, read its source span immediately before writing the
rendering, so the source text is in context while it is translated - never render a span
recalled from earlier context, and re-read the span when in doubt.

After writing a chunk, run `scripts/lint-polish.py` on the file-so-far for `pl` output - a
systematic calque habit caught on the first chunk costs one fix instead of repeating in
every remaining chunk.

When the document embeds ` ```markdown ` payload blocks, pass `--payload-markdown` - a
payload interior is translated prose and the same rules apply.

Verify the chunk boundaries against the source before concatenation - a dropped or
doubled span surfaces in the Validation parity checks.

Working notes, drafts, and meta-commentary never enter the output file - only translated
document content is written.

Translate the document title, every heading, prose, list items, table cell text, link
text, and label text.

Never translate code block contents, inline code, file paths, URLs, commands, identifiers,
record and requirement IDs, version markers, proper nouns, frontmatter, or the machine
markers `TBD` and `NOT SPECIFIED` - the pair file lists the complete untranslated set.

Apply the pair file's style-adaptation table to every element - heading case, section-name
mapping, quote and dash conventions, example headings.

Keep one sentence per logical line in the output, same as the baselines require - the
`separated` prose layout from `conventions/prose-layout.md` applies unless the request
names another layout.

Apply the untranslated-set rules and the terminology precedence the pair file declares -
project-established terms first, then glossaries, then the baseline, then a faithful
literal render, never an invented equivalent.

Treat ` ```markdown ` payload blocks as embedded documents - translate their interiors.

On `.adoc` and `.rst` documents, translate prose while preserving the marker syntax, after
loading the matching `conventions/` file.

Refuse non-Markdown, binary, or non-textual input with a stated reason.

## Adapted Translation

This section applies only when Fidelity resolved to `adapted`.

Explicit request phrases include "adapted translation", "adapt it", "translate loosely",
"shorten for a <language> audience", "adapt for a <language> audience", and their localized
equivalents declared in the matching `languages/` file.

An adapted translation may drop, merge, or reorder sections, compress prose, and render the
title adaptively.

Retained content obeys every rule of this procedure - style adaptation, terminology
precedence, and the untranslated set apply unchanged.

Nothing may be invented - every retained statement must exist in the source document.

The delivery report must list every structural delta - dropped, merged, and reordered
sections - so the adaptation is auditable.

A silent compression or reordering is a defect, not an adaptation.

## Validation

Run `scripts/check-parity.py <source.md> <output.md>` first - it mechanically verifies
the structural parity the faithful contract requires: heading level sequence, fence
count and language tags, table geometry, list counts, HTML comments, inline-code spans,
internal `#anchor` resolution, and file-level whitespace and byte conventions.

With `--terms <glossary.md>` it also prints concordance hints - source terms whose
preferred target variants never appear - for every glossary loaded in Rule Loading.

Then run the mechanical checks on the written file - `scripts/check-document.py` covers
them in one invocation (`--polish` on `pl` output, `--payload-markdown` on embedded
payloads, `--parity <source.md>` to fold the parity run in):

- `scripts/format-table.py` - mandatory on output with tables, translated cells change
  column widths.
- `scripts/validate-document.py` - on the written file, with `--payload-markdown` when the
  document embeds ` ```markdown ` blocks.
- `scripts/lint-polish.py` - on `pl` output, with `--payload-markdown` when the document
  embeds ` ```markdown ` blocks - every finding is fixed or reported.

Self-review against `process/document-checklist.md` plus the translation items:

- Heading capitalization follows the target language.
- Section names map through the language file's type table when the type is known.
- Polish output carries full diacritics in composed form.
- No typographic quotes were introduced where the target baseline requires ASCII.
- The resolved character convention is recorded - explicit request, source convention,
  or the ASCII default.
- Internal `#anchor` links resolve against the translated headings - `check-parity.py`
  reports every unresolved one.
- Code, identifiers, and the untranslated set are byte-identical to the source.
- Heading counts per depth match the source - a chunked render loses sections
  silently.
- The fence count and language-tag distribution match the source.
- Every backticked span in the source appears unchanged in the output - the
  `check-parity.py` inline-code diff lists each missing technical span - and a label
  fixed as contract vocabulary is identical in every occurrence.
- One English term renders one Polish term consistently, except declared context forms -
  the terminology lock fixes renderings before the first chunk and the `--terms`
  concordance hints surface terms the locked rendering missed.
- No agent working notes, draft markers, or meta-commentary appear anywhere in the
  output file.
- No form forbidden by a Calque Traps table or the language file's vocabulary table
  appears in the output.
- No independent clauses are joined by a bare comma, and no file, section, or branch is
  personified as an actor.
- Completed verdicts and report-register verbs follow the pair's `<pair>-style.md`
  rules when the pair provides one - a finished evaluation renders per its aspect
  rule, and conformance claims follow its verb-choice mapping.
- Normative strength survives - `must` renders `musi`/`należy`, `must not` renders
  `nie wolno`, `should` renders `powinien`, `may` renders `może`.
- Conditions and exceptions map one-to-one - `only`, `unless`, `when`, `if`,
  `otherwise` - `chyba że` never stands in for `jeśli`.
- Enumeration logic matches the source - a positive `or` list renders `lub` and
  `ani` appears only under a source negation, no quantifier, negation, condition,
  or exception is added or dropped, and a named entity keeps its kind (`file`
  renders `plik`, never `katalog`).
- For every sentence carrying an obligation, prohibition, condition, or enumeration,
  compare the meaning representation against the source - actor, action, object,
  modality, negation, ordering, and quantity all match.
- Metaphors and personifications render their Polish function, and named technical
  patterns keep the canonical name with a gloss - `God Class`, never `klasa boska`.
- Source ambiguities and contradictions are reported in the delivery report, never
  silently resolved in the rendering.
- Instructions use one imperative register throughout. Descriptions use the
  indicative.
- Gender, number, and case agree after every terminology substitution.
- Second-person pronouns stay lowercase - `cię`, `tobie`, `twój`.
- A localized marker stays coherent with the example commands that reference it.
- Reader-facing text inside examples - comments, prompts, `question`/`description`
  values - is translated while code, keys, and technical values stay verbatim.
- The Polish output was proofread once without the source - every sentence reads
  naturally on its own.
- Abbreviations are expanded at first use and a verbatim foreign-language quote carries
  a Polish gloss beside it.
- Embedded example payloads follow the declared payload rule consistently.
- An adapted output reports every structural delta in the delivery report.

`scripts/diff-content.py` does not apply - the token stream changes by design across
languages, state the skip in the report.

## Delivery

Write the output file at the resolved location - UTF-8 without BOM, LF line endings.

Report inline: the source and target language, the glossaries applied, notable term
choices and conflict resolutions, any literal renders, every source ambiguity or
contradiction left as-is, and every check run or skipped.

Remove every ad-hoc `.tmp.` helper and any `.tmp.` tool copies from the working
repository.

## Non-Goals

A faithful translation does not review, improve, restructure, or summarize the content -
restructuring happens only under the declared adapted mode.

It does not produce bilingual documents unless the request asks for them.

It does not convert locale data formats - dates, decimals, and machine values stay
verbatim.
