# Polish To German Translation

## Purpose

> **Scope:** Direction contract for rendering a document from Polish into German
> **Key items:** loading order, style adaptation, abbreviation mapping, locale
> conventions, vocabulary and register, untranslated set, terminology resolution,
> output conventions

This file governs the Polish to German direction of document translation.

Load it together with `languages/de.md` whenever a translate task renders a document into
German, following `process/translate-document.md`.

## Loading Order

Apply the rule files in this order:

1. `languages/de.md` - the German baseline: structure, headings, lists, tables, characters,
   vocabulary, file naming, and per-type section names.
2. `translations/pl-de/pl-de-general.md` - this file: direction adaptation and
   terminology rules.
3. `translations/pl-de/pl-de-<category>.md` - every glossary whose domain signals match
   the document, for example `translations/pl-de/pl-de-construction.md`.
4. `types/<type>.md` - when the document matches a known type, for its structural deltas.
5. `conventions/` files - only when the source document's dialect requires them.

The German baseline and this file together define the output style.

A glossary supplies vocabulary only - it never overrides the baseline's structure rules.

## Style Adaptation

| Element                | Polish source                | German target                                          |
|------------------------|------------------------------|--------------------------------------------------------|
| Heading capitalization | sentence case                | sentence case with German noun capitalization          |
| Section names          | `pl.md` names or free text   | `de.md` section-name mapping, faithful render          |
| Example headings       | `Poprawnie` / `Niepoprawnie` | `Richtig` / `Falsch`                                   |
| Example heading        | `Przykład zawartości`        | `Beispielinhalt`                                       |
| Prose quotes           | straight ASCII `"`           | straight ASCII `"` - typographic quotes not introduced |
| Prose dash             | ` - ` spaced hyphen          | ` - ` spaced hyphen                                    |
| Semicolon in prose     | not used                     | not used                                               |
| Definition pattern     | `**Termin**: definicja`      | `**Begriff**: Definition`                              |
| Numbered chapters      | `# 1`, `## 1.1` numbering    | numbering kept, caption translated                     |
| Diacritics             | full Polish set              | umlauts and `ß` in composed form                       |

Headings keep their level, order, and numbering - only the text changes.

Map Polish section names to the matching German entry of the same type-table row -
`## Przeznaczenie` becomes `## Zweck` for an agent-instruction document.

A section name neither table covers gets a faithful German rendering in sentence case.

A Polish source already using typographic quotes keeps straight ASCII `"` in the German
output - the conversion applies to language, not to punctuation conventions.

Proper nouns keep their native spelling - `Łódź`, `Kraków` stay unchanged in German text.

## Abbreviation Mapping

Polish abbreviations map to their German equivalents in rendered prose:

| Polish  | German           |
|---------|------------------|
| `np.`   | `z. B.`          |
| `tj.`   | `d. h.`          |
| `itd.`  | `usw.`           |
| `itp.`  | `usw.`           |
| `m.in.` | `u. a.`          |
| `tzw.`  | `sog.`           |
| `ok.`   | `ca.`            |
| `wg`    | `nach` / `gemäß` |
| `por.`  | `vgl.`           |
| `nr`    | `Nr.`            |

Established Polish acronym glosses map to their German counterparts - `SPP` becomes `PSP`,
`RODO` becomes `DSGVO` when the matching glossary declares them.

## Locale Conventions

Polish locale facts - the decimal comma, thin-space thousands grouping, and `DD.MM.RRRR`
dates - appear in the source data and stay untouched.

Numeric, date, and code values are preserved verbatim.

Translation changes the language of the document, never its data formats.

## Vocabulary And Register

Prefer the German form from the matching glossary and the `de.md` vocabulary table.

Settled loanwords stay untranslated: `Commit`, `Pull Request`, `Merge`, `Branch`,
`Repository`, `Deployment`, `Pipeline`, `Cache`, `Endpoint`, `Backend`, `Frontend`,
`Framework`.

Avoid Denglish calques the way `de.md` and the glossaries describe - `bereitstellen`, not
`deployen`, `aktualisieren`, not `updaten`.

Keep one register per document - everyday German technical usage is the default, the
formal `Sie` register is applied only when the source or the request establishes it.

Direct instructions use the imperative - `Verwende`, `Schreibe` - matching the baseline
files, unless the source's register calls for `Sie` forms.

## What Stays Untranslated

The following elements are copied verbatim:

- Fenced and indented code blocks, including their comments.
- Inline code spans, file paths, URLs, commands, and configuration keys.
- Identifiers - record IDs, requirement IDs, API names, version markers in HTML comments.
- Proper nouns, product names, brand names, and architecture element names.
- YAML frontmatter - keys and values stay verbatim as document metadata.
- Machine markers `TBD` and `NOT SPECIFIED`.
- `N/D` renders `k. A.` in German prose and table cells.

## Terminology Resolution

Apply terms in this precedence order:

1. Terminology the document or the project already establishes - a glossary section, a
   sibling German document, or a project dictionary wins over every default and is
   recorded in the report.
2. The matching `translations/pl-de/pl-de-<category>.md` glossaries.
3. The `de.md` vocabulary table and this file's rules.
4. A faithful literal rendering when no entry exists - never invent an equivalent.

One Polish term maps to one German rendering inside a document, except entries a glossary
marks as context-dependent.

Record notable choices - project terminology, conflict resolutions, literal renders - for
the delivery report.

## Heading Translation

Translate every heading's text and apply sentence case with normal German noun
capitalization.

Keep heading depth unchanged - an H2 stays an H2.

Map `pl.md` section names to the German names of the same type-table rows - `## Cel
dokumentu` becomes `## Zweck des Dokuments` for a project-document document.

A section name the tables do not cover is rendered faithfully - `## Uwagi wdrożeniowe`
becomes `## Hinweise zum Deployment`.

## Output Conventions

Write the translated document to a sibling file carrying the language code -
`przewodnik.md` produces `przewodnik-de.md`, `README.md` produces `README-de.md`.

Create the file in UTF-8 without BOM and with LF line endings.

Translate link text but keep link targets - URL, file path, and anchors stay intact unless
they are internal heading anchors.

Recompute internal `#anchor` links against the translated headings using the host
platform's slug convention - GitHub keeps Unicode letters, so `## Überschriften` anchors
to `#überschriften`.

Keep the document's own conventions where they exist - a numbered-chapter source produces
a numbered-chapter German document.

## Limitations

The pair covers whole-document rendering.

A mixed-language source gets only its Polish segments translated - report the rest.

Translate asks for a different language of the same document - improving, restructuring, or
summarizing the content is out of scope.
