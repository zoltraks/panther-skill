# Format Specification

## Purpose

> **Scope:** Conventions for file format specifications and protocol documents that describe a
> binary or textual structure field by field
> **Key items:** document information, version history, overview, structure tables, value
> references

A format specification describes a file format or protocol precisely enough to implement a reader
or writer.

Typical shape: a specification with a version history, a chunked or sectioned structure
description, and per-variant field or register tables.

## When To Use

Use for file format specifications, protocol descriptions, and structured data layout documents.

**Templates**

- `templates/en/format-specification-template-en.md`
- `templates/pl/format-specification-template-pl.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - `<Format> Format Specification`.
2. `Document Information` - version, date, state.
3. `Version History` - table of dated versions, newest first.
4. `Quick Overview` - one-paragraph summary of what the format is and how it differs from
   neighbors.
5. `Design Principles` - the rules that shaped the format.
6. Structure sections - one section per structural element (chunk, block, record), each with its
   field tables.
7. Reference tables - value enumerations, register maps, type codes.
8. Implementation notes - reader/writer guidance.

## Document Information And Version History

Format specifications always carry both optional sections, placed directly after the H1:

```markdown
## Document Information

**Version**: 1.7

**Date**: 2026-07-07

**State**: Release Candidate 7

## Version History

| Date           | Version     |
|----------------|-------------|
| **2026-07-07** | Version 1.7 |
```

Bump the document version on every content change and append a row to the history.

## Structure Tables

Describe every structural element with a field table.

Keep field tables narrow: field name, offset or size, type, meaning.

Use inline code for field names, hex values, magic bytes, and type codes.

Write multi-byte values with explicit endianness notes in prose under the table.

## Deltas From The Language Baseline

- The `Document Information` and `Version History` sections are required for this type, not
  optional.
- Enumerated values get their own subsections or tables (for example one register map per chip).
- Binary diagrams may use box-drawing or ASCII art inside code blocks.
- Precision beats brevity: a field description may run longer than one line when the semantics
  require it, keep the prose below the table instead.
