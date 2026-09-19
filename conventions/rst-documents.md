# reStructuredText Documents

## Purpose

> **Scope:** Handling of reStructuredText files encountered inside projects the skill works on
> **Key items:** heading underlines, directives, toctrees, indentation sensitivity, minimal-edit
> contract

The skill authors Markdown.

Some projects keep structural files in reStructuredText while content lives in Markdown, for
example Sphinx documentation projects.

This file defines how to read and minimally edit `.rst` files in that situation.

Load it when the task touches an `.rst` file, or when a scope file delegates to it.

## The Minimal-Edit Contract

Author document content in Markdown files only.

Edit an `.rst` file only for structural changes the task requires, such as adding or removing an
entry in a `toctree` directive.

Never convert an `.rst` file to Markdown or a Markdown file to `.rst` as a side effect of a
document task.

Never reformat, restyle, or normalize an `.rst` file.

The skill's document tools `tools/format-table.py` and `tools/validate-document.py` do not apply
to `.rst` files, verify edits by reading the file instead.

## Heading Underlines

reStructuredText marks headings by underlining the title, optionally with an overline:

```text
Document Title
==============

Section
-------

Subsection
~~~~~~~~~
```

The character chooses the level: `=` for the document title, `-` for sections, `~` or `^` for
deeper levels.

The underline must be at least as long as the title text.

When editing, keep the document's existing character-to-level mapping.

## Directives

Directives are block elements starting with `.. ` followed by a name and two colons:

```text
.. toctree::
   :maxdepth: 2
   :titlesonly:

   introduction
   base-text
   standard/index

.. image:: ../media/logo.png
   :width: 400px
   :align: center

.. note:: A remark for the reader.
```

Directive bodies are indented, conventionally by three spaces.

reStructuredText is whitespace-sensitive - wrong indentation breaks the directive.

When editing a directive, match the file's existing indentation exactly.

Common directives in documentation projects: `toctree` (navigation), `image`, `raw`, `note`,
`warning`, `code-block`.

## Toctree Entries

A `toctree` lists document names without file extension, one per line, relative to the file that
contains the directive.

Entries may point into subdirectories, for example `standard/index`.

Add a new entry in the position the document structure suggests - toctree order defines the
reading order of the built documentation.

Remove the entry when its document is removed.

## Inline Markup

reStructuredText inline markup differs from Markdown:

- `*emphasis*` and `**strong**` work like Markdown.
- ````literal```` uses double backticks for code.
- `` `Link text <https://example.com>`_ `` is an external link.
- `:role:` prefixes mark semantic roles such as `:ref:`, `:doc:`, or `:math:`.

Treat all of it as opaque content - preserve it exactly when editing.

## Detection Signals

A file is likely reStructuredText when it has an `.rst` extension, or when it contains `.. `
directives, underline-only headings, or directive options such as `:maxdepth:`.

A `.txt` file may also contain reStructuredText inside a documentation project, check the
project's build configuration when unsure.
