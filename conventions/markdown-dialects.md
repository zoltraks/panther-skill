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
- Fenced code blocks with language tags for code in a programming, markup, or data language, untagged for plain text.

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
# 1 Basic Information

## 1.1 Purpose

### Configuration Split
```

Signals: heading text starting with a chapter or section number, one H1 per chapter.

Seen in formal project documents.

The Polish variant of this dialect is described in `languages/pl.md`.

Additional traits that may accompany this dialect:

- H4 headings (`####`) or deeper, used sparingly for enumeration detail. Preserve them when
  established, even though the standard dialect stops at H3.
- Double-backtick inline code for filenames and identifiers: `` ``config.yaml`` ``.
- Bold pseudo-headings such as `**Note**`, `**Important**`, or `**Description:**` standing in
  for headings.
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

## YAML Frontmatter

Many documents open with a metadata block between fence lines:

```yaml
---
title: Installation Guide
sidebar_position: 3
---
```

Signals: the file opens with a `---` line, followed by `key: value` lines, and closed by a
second `---` line.

Seen in MkDocs, Docusaurus, VitePress, and GitBook sites, and in blog engines.

Rule: the frontmatter belongs to the document's conventions.

- Preserve every existing key on edit, keep the original key order.
- Never remove or rename a key silently, report a key that seems wrong instead of fixing it.
- Add or change a key only when the task requires it, for example `sidebar_position` when
  reordering pages.
- The block is metadata, not prose - the sentence-per-paragraph and wrapping rules do not apply
  inside it.
- Keep values in their existing scalar style, quoted or bare.
- Common keys: `title`, `description`, `slug`, `sidebar_position`, `sidebar_label`, `layout`,
  `nav_order`, `order`, `weight`, `draft`.

## Mixed And Unknown Dialects

A document may mix dialects, for example ATX headings with a numbered chapter scheme.

When signals conflict, the dominant pattern wins.

When no pattern is clear, apply the standard ATX dialect to new content and leave existing
content untouched.

## Embedded Payload Documents

Some documents carry complete documents inside ` ```markdown ` fenced blocks - embedded
templates, examples, and prompt payloads that readers copy into other files.

The host document and its payloads can legitimately follow different conventions, treat each
payload as its own dialect region.

Recognize a payload by context: the fence language is `markdown`, the content forms a
complete document (own headings, lists, tables, sometimes indented code blocks such as
directory trees), and surrounding prose says the content is copied elsewhere or defines a
target file.

Inside a payload:

- The payload's own established style is authoritative, not the host document's and not this
  skill's defaults.
- Content is opaque unless the user asks for changes inside payloads. In particular,
  reformat tables inside payloads only on explicit request -
  `tools/format-table.py --payload-markdown` exists for that case.
- Wrap payload prose only when the host convention requires it or the user asks, via
  `tools/wrap-prose.py --payload-markdown`.
- Payload content can carry real formatting defects (trailing whitespace, lone list markers,
  merged indented lines). Surface them with `tools/validate-document.py --payload-markdown`.
- Other fence languages (` ```bash `, ` ```python `, ` ```text `, bare ` ``` `) and indented
  code blocks are always opaque - they may contain table-like `|` text or prose-like lines
  that must never be reformatted.

When a document embeds another fenced block inside a payload, the inner fence must use a
longer marker than the outer one (four backticks inside a three-backtick fence).

Nested fences never nest at the same marker length.

## Detection Procedure

1. Read the document, or its outline when it is long.
2. Note the heading style, section numbering, list markers, table shape, and embedded HTML.
3. Classify the dialect or dialects.
4. Record the classification in the working notes, and apply it consistently for the rest of the
   edit.
