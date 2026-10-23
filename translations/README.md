# Language Pairs And Glossaries

## Purpose

> **Scope:** Index of the per-direction translation rule files and industry
> glossaries
> **Key items:** pair directories, loading order, glossary slugs

Load on translate tasks per `process/translate-document.md` and on translation-audit tasks
per `process/translation-audit.md`: the direction's `<pair>-general.md`, then
`<pair>-style.md` when it exists, then every matching `<pair>-<category>.md`:

- **`translations/en-pl/`** - English to Polish direction rules and glossaries.
- **`translations/pl-en/`** - Polish to English direction rules and glossaries.
- **`translations/en-de/`** - English to German direction rules and glossaries.
- **`translations/de-en/`** - German to English direction rules and glossaries.
- **`translations/pl-de/`** - Polish to German direction rules and glossaries.
- **`translations/de-pl/`** - German to Polish direction rules and glossaries.
- `general`, `style`, `software`, `project`, `finance`, `legal`, `medical`,
  `electrical`, `construction` - stable slugs across pairs.

A `<pair>-style.md` file carries sentence-level adaptation rules and loads between the
direction contract and the glossaries.
