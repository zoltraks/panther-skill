# Encoding And Dialects

## Purpose

> **Scope:** Index of the convention rule files loaded for encoding, dialect, and
> format-contract requirements
> **Key items:** encodings, Markdown dialects, foreign formats, fenced and diagram
> conventions, prose layouts

- **`conventions/file-encoding.md`** - UTF-8 default, BOM handling, UTF-16/UCS-2 and code-page
  (CP1250) preservation, conversion rules, line endings, composed diacritics.
- **`conventions/markdown-dialects.md`** - Dialect catalog (ATX, setext, closed ATX, numbered
  chapters, export artifacts) with detection signals and preserve-on-edit rules.
- **`conventions/rst-documents.md`** - reStructuredText dialect and the minimal-edit contract.
- **`conventions/asciidoc-documents.md`** - AsciiDoc dialect and the minimal-edit contract for
  `.adoc` files: title markers, admonitions, includes, opaque tables.
- **`conventions/plain-text-comments.md`** - `#` comment alignment inside untagged fenced blocks
  and shell-tagged blocks: one shared column per block, longest entry plus two spaces.
- **`conventions/ascii-diagrams.md`** - Box-drawing node-and-edge diagrams: fixed border
  columns per box, one shared axis, centered boxes and prose lines, `┬`/`▼` vertical
  edges, gap-filling `▶` side branches, `┌`/`┬`/`┼`/`┐` fan-out junctions.
- **`conventions/prose-layout.md`** - Prose-layout conventions `flowing`, `separated`,
  `bounded`, `justified`: detection signals, the no-assumed-default and mixed-document
  rules, the `line-wrapping`/`sentence-spacing`/`wrap-width` parameters, and the tooling map.
