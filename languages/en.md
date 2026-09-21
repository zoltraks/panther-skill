---
code: en
name: English
native-name: English
---

# Document Style and Markdown Formatting

## Purpose

This document defines text style and formatting rules for Markdown documents written in English.

It applies across all project documentation, including guidelines, standards, templates, notes, and reference materials.

It is intended for content-generating tools and AI agents, but must remain readable to humans.

The rules described below apply to this document itself as well.

## Contents

| Section                  | Line | What it covers                      |
|--------------------------|------|-------------------------------------|
| Document Structure       | 41   | Titles, purpose blocks, and layout  |
| Headings                 | 59   | Capitalization and qualifiers       |
| Section Numbering        | 91   | Numbered section policy             |
| Table of Contents        | 103  | When to add a contents section      |
| Paragraphs and Sentences | 117  | Sentence structure                  |
| Line Wrapping            | 131  | Logical lines and hard breaks       |
| Lists                    | 145  | Bullets, numbering, and spacing     |
| Blank Lines and Spacing  | 167  | Whitespace rules                    |
| Code Blocks              | 181  | Fences, tags, and inline code       |
| Inline Formatting        | 195  | Quotes, bold, and italics           |
| Semicolons               | 211  | Semicolon prohibition in prose      |
| Special Characters       | 237  | Box-drawing and emoji               |
| English Vocabulary       | 245  | Preferred terms and calques         |
| Tables                   | 268  | Source-width alignment rules        |
| File Names               | 381  | Naming new documentation files      |
| Example                  | 391  | Correct and incorrect sample        |
| File Maintenance         | 425  | Encoding and line-ending preserving |

## Document Structure

Use the same layout in every document.

- An H1 title (`#`) at the top of the file, one per document, concise and descriptive.
- A purpose section, one paragraph stating what the document covers.
- Main sections at H2 (`##`), subsections at H3 (`###`).

The **Document Information** and **Version History** sections are optional.

Do not add these sections to an existing document.

Do not add them to a new document either, unless the request to create the document explicitly requires it.

If a document already contains them, update them with every content change.

Do not use H4 headings or deeper.

## Headings

Section and subsection names may use Title Case, in which each major word starts with a capital letter.

Keep the capitalization convention consistent within a document.

Proper nouns, abbreviations, and technology names keep their own spelling, for example "XML Formatting", "Integration with Microsoft Fabric", "Gold Layer in Lakehouse".

Keep section names short.

Do not place parenthesized qualifiers in a section name.

Qualifiers such as "mandatory" or "do not repeat" belong in the section body.

Do not end a heading with a punctuation mark.

### Correct

```markdown
## Source Data Scope

### XML Formatting
```

### Incorrect

```markdown
## source data scope

### XML Formatting (mandatory):
```

## Section Numbering

By default, do not number sections.

The absence of numbering simplifies reorganizing the document, because moving a section does not require renumbering the others.

If the document being edited already uses section numbering, keep it and maintain the correct sequence of numbers.

After adding, removing, or moving a section, renumber the sections so that the numbers are continuous and follow the document order.

Subsection numbering reflects the parent section number, for example `3.1.` inside section `3.`.

## Table of Contents

By default, do not add a table of contents.

Add a table of contents only on request and only when the document sections are numbered.

A reference file longer than 300 lines may include a contents table even when its sections are not numbered.

Place it at the beginning of the document, directly after the optional document information section and the optional version history section.

If those sections are absent, the table of contents is the first section after the H1 title.

Update the table of contents after changing the document structure.

## Paragraphs and Sentences

Write short sentences.

For technical descriptions, use one sentence per paragraph.

This layout stays readable in text editors, in the terminal, and in version diffs.

Separate each sentence with a blank line.

A sentence may contain several related parts if they express a single thought.

Do not pack unrelated thoughts into one long paragraph.

## Line Wrapping

Do not hard-wrap text at a fixed column width.

Each sentence occupies one logical line.

A sentence may be long when the thought is long, the editor or viewer wraps it on display.

Insert a hard line break only when the source content itself requires it, for example in a code block or a diagram.

Exception: when the repository's own rules set a hard limit, for example a `STYLE.md` that requires lines no longer than 100 characters, detect that convention before formatting and apply `tools/wrap-prose.py --width N`.

The wrapper only splits lines - it never joins them, and it leaves tables, code fences, and indented code blocks untouched.

## Lists

Use a hyphen (`-`) for bullet items.

By default, do not number list items.

Use numbering for steps performed in sequence, when the edited document already uses it in a given list, or when the change request explicitly requires it.

If a list is numbered, keep the numbers continuous after adding or removing items.

Insert one blank line before a list and one blank line after it.

Do not insert blank lines between short list items.

Insert a blank line between items when the items are long or contain several sentences.

Insert one blank line between a parent item and its nested list.

Indent a nested list to the level of its parent item.

Write task lists as `- [ ]` for an open item and `- [x]` for a completed item.

## Blank Lines and Spacing

Use one blank line between paragraphs.

Use one blank line before a list and one after it.

Use one blank line before a code block and one after it.

Use one blank line before a table and one after it.

Do not leave several blank lines in a row.

Do not leave whitespace characters at the end of a line.

## Code Blocks

Fence every code block with three backticks.

Provide a language tag only when the block contains code in a programming, markup, or data language.

Leave blocks that contain plain text, directory trees, diagrams, console output, or tables untagged.

Do not leave a blank line as the first or the last line inside the block.

Keep code blocks concise and related to the described topic.

Write file names, directory names, commands, column names, and values in inline code, for example `docs/guidelines`, `SELECT`, `Fact_Sales`.

## Inline Formatting

Use plain characters for regular text, without decorative equivalents.

Use the straight ASCII double quote (`"`) instead of typographic quotes.

Use the straight ASCII apostrophe (`'`) instead of a typographic apostrophe.

If the edited document consistently follows another convention, keep that document's convention.

Write term definitions with bold in the form **Term**: definition.

Use italics sparingly.

Do not overuse emphasis.

## Semicolons

Do not use the semicolon character in running text.

Join two closely related clauses with a comma.

When the clauses express separate thoughts, split them into separate sentences.

The rule does not apply to code blocks, inline code, or file paths.

### Correct

```markdown
Raw data lands in the `bronze` layer, the `silver` layer holds cleansed data.

The name carries the meaning, the comment carries the justification.
```

### Incorrect

```markdown
Raw data lands in the `bronze` layer; the `silver` layer holds cleansed data.

The name carries the meaning; the comment carries the justification.
```

## Special Characters

Box-drawing characters are allowed in code blocks, diagrams, and schematics.

Do not replace box-drawing characters with `+`, `-`, or other ASCII approximations.

Do not use emoji unless explicitly requested.

## English Vocabulary

Write correct English and avoid accidental calques from other languages.

Prefer plain, established terms over corporate jargon or ad-hoc coinages.

| Instead of            | Use     |
|-----------------------|---------|
| utilize               | use     |
| leverage (as a verb)  | use     |
| in order to           | to      |
| due to the fact that  | because |
| at this point in time | now     |
| prior to              | before  |
| in the event that     | if      |
| perform an update     | update  |

Keep established proper nouns, product names, and architecture element names in their original form, for example Microsoft Fabric, Lakehouse, Warehouse, Power BI, workspace.

Write technical names taken from a source system exactly as they appear in that system.

In example headings, use English section names such as "Example Content", "Correct", and "Incorrect".

## Tables

Tables must remain readable in plain-text view, before processing by a Markdown renderer.

Column alignment and uniform cell padding are the main formatting goals.

### Delimiters

Separate columns with a pipe character (`|`).

Insert one space after the pipe opening a cell and one space before the pipe closing a cell.

Do not add extra spaces around pipes beyond the one required.

Start every row - header, separator, and data - with a single pipe.

A leading double pipe (`||`) parses as an empty first cell.

An automated formatter materializes that cell into a spurious empty column, which silently
corrupts the table structure instead of only misaligning it.

Write an intentionally empty first cell as `| |`, and only when the table truly needs one.

### Separator Row

Place the separator row directly after the header row.

The separator row contains only hyphens and pipes.

Hyphens touch the pipes, with no spaces between them.

The column separator width equals the column width increased by two hyphens.

The extra two hyphens correspond to the space before the cell value and the space after it.

The minimum column width is three characters.

### Cell Padding

Pad every cell with spaces on the right side up to the column width.

Pad empty cells with spaces up to the column width.

Do not pad cells beyond the column width.

Never shorten cell content.

Use left alignment in all cells.

### Column Widths

The column width is the largest character count among all cells of that column, including the header cell.

Measure width as the length of the cell's **source** text, not the rendered text.

This is the most important table formatting rule.

Count every character present in the Markdown source, including all formatting characters.

Do not remove, interpret, or collapse any characters before measuring.

A Markdown renderer hides backticks and asterisks, but those characters are still present in the source and must be counted.

The following elements are part of the cell content and enter the width measurement.

- Backticks around inline code, for example the cell `` `db.table_name` `` has 15 characters, not 13.
- Double backticks around values such as codes and numbers, for example the cell `` ``00`` `` has 6 characters, not 2.
- Emphasis asterisks, for example the cell `*italics*` has 9 characters, not 7.
- Bold double asterisks, for example the cell `**bold text**` has 13 characters, not 9.
- Emphasis underscores, for example the cell `_text_` has 6 characters, not 4.
- Spaces, punctuation, and all other characters visible in the source.

Diacritical letters count as one character each, for example the word `Częstotliwość` has 13 characters.

Write diacritical letters in composed form as a single Unicode character, so that the width measurement matches the number of characters visible in the text.

The most common formatting error is measuring the rendered text width instead of the source text width.

The cell `` `api/configuration` `` has 19 characters in the source, while the renderer displays only 17.

Using 17 instead of 19 produces a column that is too narrow and misaligned pipes in text view.

### Compacting

Compact the table after computing the column widths.

Remove padding that exceeds the widest cell in a given column.

After compacting, recompute the separator row and the padding of all cells.

A compacted table has the smallest column widths sufficient to display all cells correctly.

The compacted version is the correct version.

### Multiline Cells

Avoid multiline cells.

If a cell must be wrapped, apply the same formatting rules across all rows of the table.

### Example Content

The table below is compacted and aligned.

The column widths are 11, 7, and 17 characters.

```markdown
| Column      | Value   | Description       |
|-------------|---------|-------------------|
| `client_id` | ``001`` | Client identifier |
| `name`      | ``ABC`` | Short name        |
```

## File Names

Write names of new documentation files in lowercase, separating words with underscores, for example `user_guide.md`.

Do not use diacritical letters or spaces in new file names.

Keep conventionally established names in their original form, for example `README.md`.

The file name should match the document topic.

## Example

### Correct

```markdown
# Data Views Plan

## Purpose

This document describes the planned data views in the `gold` layer.

Each sentence is separated by a blank line.

## Editing Rules

- Write short sentences.
- Use one sentence per paragraph.
- Keep section names short.
```

### Incorrect

```markdown
# Data views plan

## Purpose
This document describes the planned data views in the gold layer. Each sentence is in the same paragraph; the text becomes hard to diff.

## Editing rules (mandatory):
- Write short sentences.
- Use one sentence per paragraph.
- Keep section names short.
```

## File Maintenance

Preserve the existing line-ending convention and encoding of the document you edit.

Create new files in UTF-8 encoding.

Do not change an existing document's conventions for section numbering, list numbering, and optional sections, unless the change request covers it.

When editing, limit changes to the scope resulting from the request.
