# Derived Documents

## Purpose

> **Scope:** The standalone procedure for producing a document derived from an
> existing document - a summary, a brief or abstract, or a supplement.
> **Key items:** derivation contract, compression tiers, continuation contract,
> naming, freshness, validation, delivery.

This file defines the derive procedure.

Follow it whenever the request asks to produce a new file that compresses or
extends an existing document.

## When This Applies

The derive task activates on requests such as "summarize this document to a
file", "write a brief of this document", "abridge this document", "write a
supplement", or their equivalents declared in the matching `languages/` file.

Classify the request as Derive when it names a source document and asks for a
new file derived from it.

A request that names no file output - "summarize this", "give an overview" - is
a Describe task producing an inline response per `process/describe-response.md`.

A request to rework the source file itself is an Edit task - no derived file is
created.

A rendering into another language is a Translate task - derivation compresses
or extends within one language.

## Derivation Roles

Two roles exist, distinguished by what the derived document does to the source:

| Role       | Relation to the source                                   |
|------------|----------------------------------------------------------|
| Summary    | Compresses the source into a shorter standalone document |
| Supplement | Extends the source with new material and continued IDs   |

A brief, abstract, or abridgment is a summary at a declared compression tier -
it is not a separate role.

When the request does not make the role obvious, ask - under JSON exchange the
question emits as the `derived-role` `choice` parameter per
`process/json-exchange.md`.

## Parameter Resolution

Resolve these parameters before writing:

| Parameter       | Default                                                 |
|-----------------|---------------------------------------------------------|
| Source document | Named by the request, ask when absent                   |
| Role            | Detected from the request, ask when ambiguous           |
| Tiers           | The tiers named by the request, `summary` when unstated |
| Language        | The source document's language                          |
| Output location | Sibling file per the Naming rules below                 |
| Encoding        | UTF-8 without BOM                                       |
| Line endings    | LF                                                      |

Confirm the parameters with the user per `process/document-workflow.md` - ask
whether to accept the defaults or configure them.

Under JSON exchange the gate emits as `parameters-acceptance`, and the
per-parameter asks emit as `derived-role` and `summary-tiers` per
`process/json-exchange.md`.

## Source Reading

Read the whole source document before writing anything.

For a summary, identify the source's type - the matching `types/` file controls
which sections exist to compress and which section names the derived document
inherits.

For a supplement, identify the source's numbering schemes - finding, risk,
requirement, and entry IDs - and record the highest used value per scheme.

A derivation chain is allowed - a brief may derive from a summary, which itself
derives from a report.

The declared source is always the direct parent - a document derived from a
derived document names that document, not the root.

## Derivation Contract

Every derived document opens with a Purpose section that declares:

- The source document by its current filename.
- The role - summary or supplement.
- The derivation rules - the tiers and their caps for a summary, the
  continuation scope for a supplement.

A reader of the derived document alone must be able to tell what it was derived
from and under which contract.

## Compression Tiers

A summary document carries one or more tiers:

| Tier       | Cap                                                   |
|------------|-------------------------------------------------------|
| `abstract` | At most ten sentences - verdict and key facts only    |
| `summary`  | At most fifty sentences - conclusions plus reasoning  |
| `detailed` | No fixed cap - mirrors the source's section structure |

Tier selection is an intake parameter - under JSON exchange it emits as the
`summary-tiers` `selection` parameter.

A document carrying only the `abstract` tier is a brief - the naming rules give
it the brief marker.

The `detailed` tier reproduces the source's section structure at reduced depth,
tables included.

## Compression Rules

- Preserve identifiers, paths, versions, and verdicts verbatim - compression
  changes prose, never facts.
- Impersonal narration, one sentence per paragraph - the language baseline's
  prose rules apply unchanged.
- Carry the source's conclusion or recommendation into every tier - a summary
  that drops the verdict is a defect.
- Add nothing - every statement in the derived document must exist in the
  source.
- Add no statement about the skill, rules, or procedure that rendered the derived
  document - that is production metadata, not source content.
- Name omitted material - a `detailed` tier that drops a source section lists
  the omission in an Omitted Material section.

## Continuation Contract

A supplement extends its parent without replacing it:

- Continue every numbering scheme from the parent's highest used value - never
  restart or collide with parent IDs.
- Extend matrices and registers by adding rows or columns - do not rewrite the
  parent's entries.
- Mark every restated parent claim as declared, not re-verified, unless the
  supplement verifies it again - say which applies.
- Update the parent's conclusions only in an Updated Conclusions section -
  state plainly which conclusions change and which stand.
- Record the reference point - a supplement written against a new source
  version says so in its Document Information block or scope section.

## Naming

The output filename is `<stem>-<marker>` next to the source, where `<stem>` is
the source filename without its extension.

The marker follows the output language:

| Document role | Marker en    | Marker pl      | Marker de         |
|---------------|--------------|----------------|-------------------|
| Summary       | `Summary`    | `Podsumowanie` | `Zusammenfassung` |
| Brief         | `Brief`      | `Skrót`        | `Kurzfassung`     |
| Supplement    | `Supplement` | `Suplement`    | `Ergänzung`       |

A version or context tag named by the request appends after the marker -
`<stem>-<marker>-<tag>`.

When the source filename already carries a role marker, the derived stem drops
it - a brief derived from `report-Summary` is `report-Brief`, never
`report-Summary-Brief`.

## Freshness And Renames

A derived document references the source by its current filename.

When a request renames a source, offer to propagate the rename into the Purpose
sections of its derived documents.

A stale source reference in a delivered derived document is a defect - it is
fixed under an Edit task.

## Validation

Run the mechanical checks on the written file - `scripts/check-document.py` covers them
in one invocation (`--polish` on `pl` output, `--payload-markdown` on embedded payloads):

- `scripts/format-table.py` - mandatory on output with tables.
- `scripts/validate-document.py` - on the written file, with
  `--payload-markdown` when the document embeds ` ```markdown ` blocks.
- `scripts/lint-polish.py` - on `pl` output - every finding is fixed or
  reported.

Self-review against `process/document-checklist.md` plus the derivation items:

- The Purpose section names the source by its current filename.
- The declared tier caps hold - count the sentences.
- Every identifier, version marker, and verdict in the derived document matches
  the source verbatim.
- A supplement's new IDs continue the parent's sequences with no gaps or
  collisions.
- Parent claims restated in a supplement are marked declared or re-verified.
- The source's verdict or recommendation appears in every tier.

## Delivery

Write the output file at the resolved location - UTF-8 without BOM, LF line
endings.

Report inline: the role, the tiers written, the source filename declared, any
omitted material, and every check run or skipped.

Remove every ad-hoc `.tmp.` helper and any `.tmp.` tool copies from the working
repository.

## Non-Goals

A summary does not review, extend, or correct the source - compression never
adds claims.

A supplement does not restate the parent - unchanged material stays in the
parent and is referenced, not repeated.

Derivation never translates - a language change is a Translate task, and a
derived document in another language is two separate tasks, never blended
silently.
