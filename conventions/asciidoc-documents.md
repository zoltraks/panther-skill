# AsciiDoc Documents

## Purpose

> **Scope:** Handling of AsciiDoc files encountered inside projects the skill works on
> **Key items:** title markers, document attributes, admonitions, includes, tables, minimal-edit
> contract

The skill authors Markdown.

Some projects keep content in AsciiDoc, for example Antora documentation sites and enterprise
manuals built with Asciidoctor.

This file defines how to read and minimally edit `.adoc` files in that situation.

Load it when the task touches an `.adoc` file, or when a scope file delegates to it.

## The Minimal-Edit Contract

Author document content in Markdown files only.

Edit an `.adoc` file only for structural changes the task requires, such as adding or removing
an entry in a navigation outline or an include list.

Never convert an `.adoc` file to Markdown or a Markdown file to `.adoc` as a side effect of a
document task.

Never reformat, restyle, or normalize an `.adoc` file.

The skill's document tools `tools/format-table.py` and `tools/validate-document.py` do not apply
to `.adoc` files, verify edits by reading the file instead.

## Title Markers

AsciiDoc marks headings with equals signs preceding the title:

```text
= Document Title

== Section

=== Subsection

==== Detail
```

The number of `=` characters chooses the level - one for the document title, two for sections,
three for subsections.

When editing, keep the document's existing marker-to-level mapping and match it for added
headings.

## Document Header And Attributes

The document header sits between the title and the first section and carries attribute lines:

```text
= Document Title
Author Name <author@example.com>
:toc: left
:icons: font
:source-highlighter: pygments
```

Attribute lines start with a colon and end with a colon, they configure the renderer.

Treat the header and its attributes as opaque - preserve them exactly, change a value only when
the task explicitly asks for it.

## Admonitions

AsciiDoc marks admonitions with a keyword prefix:

```text
NOTE: A single-line remark for the reader.

TIP: A helpful suggestion.
```

Block admonitions use a delimited form:

```text
[WARNING]
====
Multi-line warning text.
====
```

The keywords are `NOTE`, `TIP`, `WARNING`, `IMPORTANT`, and `CAUTION`.

Preserve the single-line or block form the document uses, match it for added admonitions.

## Includes And Cross-References

Directives pull in other files and cross-link sections:

```text
include::shared/header.adoc[]

xref:installation[see the installation section]

link:https://example.com[external link]
```

An `include::` path resolves relative to the including file or to the base directory the build
defines - check the project's build configuration before moving a file that includes others.

Treat `xref:`, `link:`, and `<<anchor>>` references as opaque content, preserve them exactly
when editing.

## Tables

AsciiDoc tables use delimited blocks:

```text
[cols="1,1"]
|===
| Header one | Header two
| Cell       | Cell
|===
```

The `|===` lines open and close the table, `cols=` sets the column specification, and cells
separate with `|`.

Treat table blocks as opaque - do not realign cells, do not convert them to Markdown tables,
and do not run the table formatter on them.

## Inline Markup

AsciiDoc inline markup differs from Markdown:

- `*bold*` and `_italic_` use single delimiters.
- `` `literal` `` marks monospace.
- `` `+passthrough+` `` guards content from interpretation.
- `{attribute}` inserts a document attribute value.

Treat all of it as opaque content - preserve it exactly when editing.

## Detection Signals

A file is likely AsciiDoc when it has an `.adoc` extension, or when it opens with a `= Title`
line, carries `:attribute:` lines, or contains `include::` directives or `|===` table
delimiters.

An `.txt` file may also contain AsciiDoc inside a documentation project, check the project's
build configuration when unsure.
