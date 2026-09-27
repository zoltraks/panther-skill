# English To German Translation

## Purpose

> **Scope:** Direction contract for rendering a document from English into German
> **Key items:** loading order, style adaptation, abbreviation mapping, locale
> conventions, vocabulary and register, untranslated set, terminology resolution,
> output conventions

This file governs the English to German direction of document translation.

Load it together with `languages/de.md` whenever a translate task renders a document into
German, following `process/translate-document.md`.

## Loading Order

Apply the rule files in this order:

1. `languages/de.md` - the German baseline: structure, headings, lists, tables, characters,
   vocabulary, file naming, and per-type section names.
2. `translations/en-de/en-de-general.md` - this file: direction adaptation and
   terminology rules.
3. `translations/en-de/en-de-<category>.md` - every glossary whose domain signals match
   the document, for example `translations/en-de/en-de-construction.md`.
4. `types/<type>.md` - when the document matches a known type, for its structural deltas.
5. `conventions/` files - only when the source document's dialect requires them.

The German baseline and this file together define the output style.

A glossary supplies vocabulary only - it never overrides the baseline's structure rules.

## Style Adaptation

| Element                | English source                | German target                                          |
|------------------------|-------------------------------|--------------------------------------------------------|
| Heading capitalization | Title Case                    | sentence case with German noun capitalization          |
| Section names          | type table names or free text | `de.md` section-name mapping, faithful render          |
| Example headings       | `Correct` / `Incorrect`       | `Richtig` / `Falsch`                                   |
| Example heading        | `Example Content`             | `Beispielinhalt`                                       |
| Prose quotes           | straight ASCII `"`            | straight ASCII `"` - typographic quotes not introduced |
| Prose dash             | ` - ` spaced hyphen           | ` - ` spaced hyphen                                    |
| Semicolon in prose     | not used                      | not used                                               |
| Definition pattern     | `**Term**: definition`        | `**Begriff**: Definition`                              |
| Numbered chapters      | `# 1`, `## 1.1` numbering     | numbering kept, caption translated                     |
| Diacritics             | none                          | umlauts and `ß` in composed form                       |

Headings keep their level, order, and numbering - only the text and case change.

When the document type is known, map section names per the "Abschnittsnamen nach
Dokumenttyp" table in `languages/de.md`.

A heading the table does not cover gets a faithful German rendering in sentence case.

A German document already using typographic quotes - German low-high double quotes or
guillemets - keeps that convention.

The document's own conventions win over this table.

## Abbreviation Mapping

English abbreviations map to their German equivalents in rendered prose:

| English     | German  |
|-------------|---------|
| `e.g.`      | `z. B.` |
| `i.e.`      | `d. h.` |
| `etc.`      | `usw.`  |
| `a.m.`      | `u. a.` |
| `et al.`    | `u. a.` |
| `approx.`   | `ca.`   |
| `cf.`       | `vgl.`  |
| `no.`       | `Nr.`   |
| `so-called` | `sog.`  |

Do not abbreviate where the source writes the phrase out - write `zum Beispiel` out when
the source says "for example" in prose.

## Locale Conventions

German locale facts - dates as `TT.MM.JJJJ`, the decimal comma, and dot thousands
grouping - apply only to prose the translation newly generates.

Numeric, date, and code values are preserved verbatim.

Translation changes the language of the document, never its data formats.

## Vocabulary And Register

Prefer the German form from the matching glossary and the `de.md` vocabulary table.

Settled loanwords stay untranslated: `Commit`, `Pull Request`, `Merge`, `Branch`,
`Repository`, `Deployment`, `Pipeline`, `Cache`, `Endpoint`, `Backend`, `Frontend`,
`Framework`, `Workspace`.

Avoid Denglish calques the way `de.md` and the glossaries describe - `bereitstellen`, not
`deployen`, `aktualisieren`, not `updaten`, `beheben`, not `fixen`, `leistungsfähig`, not
`performant`.

Write compounds the German way - one word or a hyphenated joiner on a loanword, never a
bare concatenation of separate words - `Repository-Struktur`, not `Repository Struktur`.

Keep one register per document - everyday German software-engineering usage is the
default, formal `Sie` register and standards-register spellings are applied only when the
source or the request establishes them.

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
- `N/A` renders `k. A.` in German prose and table cells.

## Terminology Resolution

Apply terms in this precedence order:

1. Terminology the document or the project already establishes - a glossary section, a
   sibling German document, or a project dictionary wins over every default and is
   recorded in the report.
2. The matching `translations/en-de/en-de-<category>.md` glossaries.
3. The `de.md` vocabulary table and this file's rules.
4. A faithful literal rendering when no entry exists - never invent an equivalent.

One English term maps to one German rendering inside a document, except entries a glossary
marks as context-dependent.

Record notable choices - project terminology, conflict resolutions, literal renders - for
the delivery report.

## Heading Translation

Translate every heading's text and apply sentence case with normal German noun
capitalization.

Keep heading depth unchanged - an H2 stays an H2.

Map known-type section names through the `de.md` table - `## Purpose` becomes `## Zweck`
for an agent-instruction document.

A section name the table does not cover is rendered faithfully - `## Deployment Notes`
becomes `## Hinweise zum Deployment`, not a forced table match.

## Output Conventions

Write the translated document to a sibling file carrying the language code -
`guide.md` produces `guide-de.md`, `README.md` produces `README-de.md`.

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

A mixed-language source gets only its English segments translated - report the rest.

Translate asks for a different language of the same document - improving, restructuring, or
summarizing the content is out of scope.
