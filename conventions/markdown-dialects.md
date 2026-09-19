# Markdown Dialects

## Purpose

> **Scope:** Catalog of Markdown dialects observed in real documents, detection signals, and the
> preserve-on-edit rule
> **Key items:** ATX, setext headings, numbered chapters, pandoc artifacts, per-document
> conventions

Documents in the wild do not all look the same.

This file catalogs the dialects the skill recognizes, and defines how to handle them.

The core rule: the document's own dialect wins over the default style. Detect it, preserve it,
normalize only on explicit request.

## Standard ATX

The default dialect for new documents.

- ATX headings (`#`, `##`, `###`), never deeper than H3.
- Hyphen (`-`) bullets.
- Pipe tables aligned by source width.
- Fenced code blocks with language tags.

This is the dialect the `languages/` files define.

## Setext Headings

Some documents underline headings instead of using `#` markers:

```text
Title
=====

Section
-------
```

Signals: lines of `=` or `-` directly below a text line.

Seen in older prose documents and documents produced by converters.

Rule: when editing a setext document, keep using setext for existing headings. For added
headings, match the document's dominant style.

## Closed ATX

A variant of ATX with trailing markers:

```text
### Gitara elektryczna ###
```

Signals: `###` at both ends of the heading line.

Rule: keep the closing markers when editing such a document, match the style for added headings.

## Numbered Chapters

Formal documents may number chapters and sections:

```markdown
# 1 Podstawowe informacje

## 1.1 Cel

### Podział konfiguracji
```

Signals: heading text starting with a chapter or section number, one H1 per chapter.

Seen in formal project documents, especially Polish specifications.

Additional traits that may accompany this dialect:

- H4 headings (`####`) or deeper, used sparingly for enumeration detail. Preserve them when
  established, even though the standard dialect stops at H3.
- Double-backtick inline code for filenames and identifiers: `` ``config.yaml`` ``.
- Bold pseudo-headings such as `**Uwaga**`, `**Ważne**`, or `**Opis:**` standing in for headings.
- Spaced table separator cells (`| ------ |`) instead of compact ones (`|------|`).

Rule: keep the numbering scheme, renumber continuously after adding, removing, or moving a
section. Subsection numbers reflect the parent (`3.1.` inside `3.`). Preserve the additional
traits above when editing. Apply them to new content when the document uses them consistently.

## Pandoc And Export Artifacts

Documents produced by converters or exports may carry:

- HTML blocks such as `<div style="page-break-after: always;"></div>`
- `*` or `+` bullet markers
- Tables without a closing pipe
- Trailing whitespace at line ends
- Long lines without sentence-per-line layout

Seen in documents produced by converters or written outside the skill's conventions.

Rule: these artifacts are part of the document's conventions. Do not clean them up during an
unrelated edit - the minimal-diff rule applies. Normalize them only when the request is about
reformatting or cleanup.

## Mixed And Unknown Dialects

A document may mix dialects, for example ATX headings with a numbered chapter scheme.

When signals conflict, the dominant pattern wins.

When no pattern is clear, apply the standard ATX dialect to new content and leave existing
content untouched.

## Detection Procedure

1. Read the document, or its outline when it is long.
2. Note the heading style, section numbering, list markers, table shape, and embedded HTML.
3. Classify the dialect or dialects.
4. Record the classification in the working notes, and apply it consistently for the rest of the
   edit.
