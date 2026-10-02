# Supplement Document

## Purpose

> **Scope:** Documents that extend an existing document with new material
> while continuing its numbering and verdicts.
>
> **Key items:** declared parent, continued ID sequences, extended matrices,
> declared versus re-verified marking, updated conclusions.

## When To Use

Use when the request asks to extend an existing document into a new file -
"write a supplement", "extend this report", "continue this document with the
new data".

A rewrite that replaces the source is an Edit task, not this type.

The procedure is `process/derived-documents.md` - it governs the continuation
contract, naming, and freshness.

**Templates**

- `templates/en/supplement-document-template-en.md`
- `templates/pl/supplement-document-template-pl.md`
- `templates/de/supplement-document-template-de.md`

## Structure

1. H1 title - `<source title> - <role marker>` in the output language.
2. Document Information - a block naming the parent document, the parent's
   reference point, and the reference point this supplement is written
   against.
3. Purpose - declares the parent and the continuation scope.
4. Continuation Scope - what the supplement adds and what it deliberately
   leaves to the parent.
5. Extended Content - the new material, organized like the parent's matching
   sections - matrices gain a row or column rather than a rewrite.
6. Continued Entries - new findings, risks, or records continuing the
   parent's ID sequences.
7. Updated Conclusions - which parent conclusions change, which stand.

## Deltas From The Language Baseline

- New IDs continue the parent's sequences - never restart, never collide.
- Parent claims restated here are marked declared or re-verified.
- The parent is referenced, never re-litigated - unchanged content stays in
  the parent.
- Impersonal narration, one sentence per paragraph.
- The supplement does not stand alone - it names the parent and depends on
  it.

## Section Names

| Section              | Requirement |
|----------------------|-------------|
| Document Information | required    |
| Purpose              | required    |
| Continuation Scope   | recommended |
| Extended Content     | required    |
| Continued Entries    | optional    |
| Updated Conclusions  | recommended |

Section names for other languages are declared in the matching
`languages/<code>.md` file.
