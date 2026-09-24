# Document Checklist

## Purpose

> **Scope:** The mechanical pre-delivery checklist applied to every document
> **Key items:** structure checks, spacing, characters, tables, file properties

Run this checklist before delivering any created or edited document.

Items marked **existing** apply only to documents being edited - they verify that the document's
own conventions were preserved rather than normalized.

Fix every failure, or report it to the user with a reason.

## Structure

- The document has exactly one H1 title, unless the type or the existing convention says
  otherwise (for example, notes may omit it, numbered-chapter documents use one H1 per chapter).
- Headings do not exceed H3 in new documents, and do not exceed the existing depth in edited ones.
- Headings carry no parenthesized qualifiers and no trailing punctuation.
- The purpose section is present and matches the document's actual content.
- Optional sections (Document Information, Version History) were not added without a request.
- A Contents table exists when required by the document's own convention or the skill's style
  rules.

## Spacing

- One blank line separates paragraphs, and surrounds every list, code block, and table.
- No two consecutive blank lines exist anywhere.
- No line ends with a whitespace character.
- No blank line sits as the first or last line inside a fenced code block.
- No line carries a lone list marker without content.
- **Existing:** lines respect the document's width convention when one exists - verified with
  `tools/wrap-prose.py --check --width N`, otherwise one logical line per sentence applies.
- **Existing:** character substitutions that change line length were re-verified against the
  document's width convention - for example `—` replaced by `--` adds one character per dash.

## Characters

- Prose uses straight ASCII double quotes (`"`) and apostrophes (`'`).
- No semicolon appears in running prose outside code blocks, inline code, and file paths.
- No emoji appears unless explicitly requested.
- Box-drawing characters appear only inside code blocks, diagrams, and schematics.
- Diacritics are written in composed form, one Unicode character per letter.
- **Existing:** quote and apostrophe style matches the document's established convention when it
  deliberately differs.
- **Existing:** non-ASCII punctuation in prose (dashes, ellipsis, non-breaking spaces) was
  surfaced and checked against the document's convention.

## Lists And Code

- Bullet items use the hyphen (`-`), or the marker the edited document already uses.
- Numbered lists appear only for sequential steps or where the document already numbers items.
- Task lists use `- [ ]` and `- [x]`.
- Every fenced code block carrying code in a programming, markup, or data language has a language
  tag.
- Fenced blocks carrying plain text, directory trees, diagrams, console output, or tables have no
  language tag.
- Trailing `#` comments inside a plain-text or shell-tagged block share one column - the
  established column, or the longest entry plus two spaces - aligned with
  `tools/align-comments.py` or an equivalent script, not by hand.

## Tables

- Columns align in plain-text view, every cell is padded to the column width.
- Every table row starts with a single pipe - a leading `||` produces a spurious empty first
  column.
- The separator row matches each column width plus two hyphens.
- Column widths were measured on source text, including backticks and emphasis markers.
- The table is compacted to the minimum widths that fit the widest cell per column.
- Tables were formatted with `tools/format-table.py` or an equivalent script, not by hand.

## Language

- Heading capitalization follows the document language (Title Case for English, sentence case for
  Polish, or the rule in the matching `languages/` file).
- The vocabulary table of the language file was applied, no discouraged terms remain.
- Technical names and proper nouns keep their original spelling.

## Consistency

- Every enumeration of a governed set - canonical files, owners, options, steps - lists the
  same members wherever it appears in tables, menus, checklists, and examples.
- No reference to a renamed or removed section, file, or owner remains.
- Numbered lists renumber correctly after inserted or removed items.
- A document serving both human readers and AI agents states each shared rule consistently
  for both audiences.
- Embedded ` ```markdown ` example documents match the normative text they illustrate.
- Version markers and contents tables reflect the current change when the document's own
  convention maintains them.

## File Properties

- The filename follows the language file naming rules, or a type-conventional name.
- **Existing:** the file keeps its original encoding, byte order mark, and line-ending style.
- **Existing:** the diff is limited to the requested scope.

## Embedded Payloads

- ` ```markdown ` payload blocks were treated as separate dialect regions - the payload's own
  style was preserved.
- Payload content stayed opaque unless the request covered it - tables and prose inside
  payloads were reformatted only through the `--payload-markdown` tools on explicit request.
- Indented code blocks inside payloads, such as directory trees, kept their original line
  structure.
- **Existing:** a formatting-only pass changed no words - `tools/diff-content.py` reports a
  token stream identical to the baseline, and every merged-line warning was reviewed.

## Project Scope

- The detected or named scope was reported, `unstructured-layout` when nothing matched.
- A new file sits in the directory the scope assigns to its role.
- The filename follows the scope's naming convention when it overrides the language default.
- Every registration or index file the scope requires was updated, for example a `SKILL.md`
  router entry or an `index.rst` toctree entry.
- Validators the scope mandates ran, for example the skill repository's own checkers.

## Final Pass

- `tools/validate-document.py` reports no failures on the written file, run with
  `--payload-markdown` when the document embeds ` ```markdown ` blocks.
- `tools/diff-content.py` reports an identical token stream after formatting-only passes.
- `git diff --check` reports no whitespace errors when inside a repository.
- Temporary `.tmp.` tool copies are removed from the working repository.
