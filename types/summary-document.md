# Summary Document

## Purpose

> **Scope:** Documents derived from an existing document by compression -
> summaries, briefs, and abstracts.
>
> **Key items:** declared source, compression tiers, carried verdict, verbatim
> identifiers, localized role marker.

## When To Use

Use when the request asks for a document that compresses an existing document
into a file - "summarize this report to a file", "write a brief of this
document", "abridge this document".

An inline summary without a file is a Describe response, not this type.

The procedure is `process/derived-documents.md` - it governs derivation,
tiers, naming, and freshness.

**Templates**

- `templates/en/summary-document-template-en.md`
- `templates/pl/summary-document-template-pl.md`
- `templates/de/summary-document-template-de.md`

## Structure

1. H1 title - `<source title> - <role marker>` in the output language, for
   example `# Quarterly Review - Summary`.
2. Purpose - declares the source file, the role, and the tier contract with
   its caps.
3. Abstract - the top tier, at most ten sentences, verdict and key facts only.
4. Summary - the middle tier, at most fifty sentences, conclusions plus key
   reasoning.
5. Detailed Abstract - mirrors the source's section structure at reduced
   depth, tables included.
6. Omitted Material - the source sections consciously dropped, when any.

The request selects the tiers - a brief carries only the Abstract section.

## Deltas From The Language Baseline

- Identifiers, paths, versions, and verdicts copy verbatim from the source.
- Every tier carries the source's conclusion - never compress it away.
- Nothing is invented - each statement exists in the source.
- Impersonal narration, one sentence per paragraph.
- The document is standalone - it reads correctly without opening the source.

## Section Names

- Purpose
- Abstract
- Summary
- Detailed Abstract
- Omitted Material

Section names for other languages are declared in the matching
`languages/<code>.md` file.
