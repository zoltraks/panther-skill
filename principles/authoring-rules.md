# Authoring Rules

## Purpose

> **Scope:** Non-negotiable rules applied to every document created or edited with this skill
> **Key items:** plain-text readability, one-sentence paragraphs, convention preservation, minimal
> diffs, explicit unknowns

These rules override stylistic preferences and convenience.

Apply them to every section of every document produced by this skill.

If a requested change conflicts with these rules and the user has not explicitly overridden them,
keep the rule and flag the conflict.

## Plain Text First

Write documents that remain readable in a plain text editor, a terminal viewer, and a diff.

The Markdown source is the primary artifact, the rendered output is secondary.

Use short sentences.

Use one sentence per paragraph for technical descriptions.

Separate every sentence with a blank line.

A sentence may contain several related clauses if they express a single thought.

## The Document's Own Conventions Win

When editing an existing document, preserve its conventions.

This covers the Markdown dialect, section numbering, heading style and depth, list style, table
layout, character encoding, line-ending style, and file naming.

Never normalize an existing document silently.

Change an established convention only when the request explicitly covers it, then apply the change
consistently across the whole document.

See `conventions/markdown-dialects.md` for the dialect catalog and detection guidance.

## Minimal Diff

Limit changes to the scope resulting from the request.

Do not reformat untouched sections, rename untouched headings, or fix unrelated typos unless the
request covers it.

Every unrelated edit makes review harder and hides the real change.

## Explicit Unknowns

Never invent content to fill a gap.

When required information is missing, mark it explicitly:

- `NOT SPECIFIED` - the request is silent on this point.
- `TBD` - the value is expected but not yet known.

A clearly marked gap is more valuable than a plausible guess.

## Default Structure

New documents follow this layout unless the matching `types/` file or the request says otherwise:

1. An H1 title (`#`), one per document, concise and descriptive.
2. A purpose section stating what the document covers.
3. Main sections at H2 (`##`), subsections at H3 (`###`).

Do not use H4 or deeper headings in new documents.

Do not add a Document Information or Version History section unless the document type calls for it
or the request requires it.

## Language Authority

The matching `languages/` file is the authoritative style source for the document's language.

Language files are named by ISO 639-1 code (`languages/en.md`, `languages/pl.md`) and identified
by the `code` field in their frontmatter.

Load exactly one language file per document, matching the document language.

The language file governs headings, lists, spacing, inline formatting, tables, file naming, and the
language vocabulary rules.

A `types/` file may add or override rules for its document type, it never replaces the language
file.

## Characters And Formatting

Use straight ASCII double quotes (`"`) and apostrophes (`'`) in prose, unless the edited document
consistently follows another convention.

Do not use the semicolon character in running prose, join related clauses with a comma or split
them into sentences.

Do not use emoji unless explicitly requested.

When a request requires ASCII-only text and the document contains em or en dashes, replace
them with ` - `.

Use ` -- ` only when the edited document already uses the double-minus form or when the
request explicitly asks for it.

A repository style document that prescribes ` -- ` makes it an eligible option - ask for
confirmation before applying it.

Write file names, commands, column names, and values in inline code.

Write term definitions with bold in the form **Term**: definition.

## Encoding And Bytes

Create new files in UTF-8 encoding without a byte order mark.

Preserve the encoding and line-ending style of every existing file you edit.

Never transcode or change line endings silently.

See `conventions/file-encoding.md` for the full encoding rules and `tools/detect-encoding.py` for
detection.
