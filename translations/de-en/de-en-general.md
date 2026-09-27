# German To English Translation

## Purpose

> **Scope:** Direction contract for rendering a document from German into English
> **Key items:** loading order, style adaptation, abbreviation mapping, terminology
> resolution, untranslated set, output conventions

This file governs the German to English direction of document translation.

Load it together with `languages/en.md` whenever a translate task renders a document into
English, following `process/translate-document.md`.

## Loading Order

Apply the rule files in this order:

1. `languages/en.md` - the English baseline: structure, headings, lists, tables,
   characters, vocabulary, and file naming.
2. `translations/de-en/de-en-general.md` - this file: direction adaptation and
   terminology rules.
3. `translations/de-en/de-en-<category>.md` - every glossary whose domain signals match
   the document.
4. `types/<type>.md` - when the document matches a known type, for its structural deltas.
5. `conventions/` files - only when the source document's dialect requires them.

The English baseline and this file together define the output style.

A glossary supplies vocabulary only - it never overrides the baseline's structure rules.

## Style Adaptation

| Element                | German source                      | English target                             |
|------------------------|------------------------------------|--------------------------------------------|
| Heading capitalization | sentence case                      | Title Case                                 |
| Section names          | `de.md` names or free text         | English type table names, faithful render  |
| Example headings       | `Richtig` / `Falsch`               | `Correct` / `Incorrect`                    |
| Example heading        | `Beispielinhalt`                   | `Example Content`                          |
| Typographic quotes     | low-high double quotes, guillemets | straight ASCII `"`                         |
| Typographic apostrophe | `'`                                | straight ASCII `'`                         |
| Prose dash             | ` - ` or ` – `                     | ` - ` spaced hyphen                        |
| Semicolon in prose     | not used                           | not used                                   |
| Definition pattern     | `**Begriff**: Definition`          | `**Term**: definition`                     |
| Numbered chapters      | `# 1`, `## 1.1` numbering          | numbering kept, caption translated         |
| Diacritics             | umlauts and `ß`                    | none, except inside preserved proper nouns |

Headings keep their level, order, and numbering - only the text and case change.

Proper nouns keep their native spelling - `München`, `Köln`, `Weiß` keep their diacritics
as names.

A German source using straight ASCII quotes already produces straight ASCII quotes - the
document's own convention wins over the conversion row above.

## Abbreviation Mapping

German abbreviations map to their English equivalents:

| German  | English                      |
|---------|------------------------------|
| `z. B.` | `e.g.`                       |
| `d. h.` | `i.e.`                       |
| `usw.`  | `etc.`                       |
| `u. a.` | `among others`               |
| `bzw.`  | `or rather` / `respectively` |
| `sog.`  | `so-called`                  |
| `ca.`   | `approx.`                    |
| `ggf.`  | `if applicable`              |
| `vgl.`  | `cf.`                        |
| `s. o.` | `see above`                  |
| `evtl.` | `possibly`                   |
| `Nr.`   | `no.`                        |
| `Abs.`  | `para.`                      |

Established German acronym glosses reverse to their canonical English forms - `PSP`
becomes `WBS`, `DSGVO` becomes `GDPR` when the matching glossary declares them.

## Locale Conventions

German locale facts - the decimal comma, dot thousands grouping, and `TT.MM.JJJJ` dates -
appear in the source data and stay untouched.

Numeric, date, and code values are preserved verbatim.

Translation changes the language of the document, never its data formats.

## Vocabulary And Register

German loanwords in the source map back to their canonical English forms - `Commit`,
`Pull Request`, `Merge`, `Deployment`, `Endpoint` stay English, never re-englised into
coinages.

German compounds resolve to the glossary's headword before rendering - `Risikoregister`
renders `risk register`, not a per-word literal.

Write plain English per `languages/en.md` - `use`, not `utilize`, `because`, not `due to
the fact that`.

Keep one register per document - the everyday software-engineering register is the
default.

## What Stays Untranslated

The following elements are copied verbatim:

- Fenced and indented code blocks, including their comments.
- Inline code spans, file paths, URLs, commands, and configuration keys.
- Identifiers - record IDs, requirement IDs, API names, version markers in HTML comments.
- Proper nouns, product names, brand names, and architecture element names.
- YAML frontmatter - keys and values stay verbatim as document metadata.
- Machine markers `TBD` and `NOT SPECIFIED`.
- `k. A.` renders `N/A` in English prose and table cells.

## Terminology Resolution

Apply terms in this precedence order:

1. Terminology the document or the project already establishes - a glossary section, a
   sibling English document, or a project dictionary wins over every default and is
   recorded in the report.
2. The matching `translations/de-en/de-en-<category>.md` glossaries.
3. The `en.md` vocabulary table and this file's rules.
4. A faithful literal rendering when no entry exists - never invent an equivalent.

One German term maps to one English rendering inside a document, except entries a glossary
marks as context-dependent.

Record notable choices - project terminology, conflict resolutions, literal renders - for
the delivery report.

## Heading Translation

Translate every heading's text and apply Title Case.

Keep heading depth unchanged - an H2 stays an H2.

Map `de.md` section names back to their English type-table names - `## Zweck` becomes
`## Purpose` for an agent-instruction document.

A section name the tables do not cover is rendered faithfully - `## Hinweise zum
Deployment` becomes `## Deployment Notes`.

## Output Conventions

Write the translated document to a sibling file carrying the language code -
`leitfaden.md` produces `leitfaden-en.md`, `README-de.md` produces `README.md`.

Create the file in UTF-8 without BOM and with LF line endings.

Translate link text but keep link targets - URL, file path, and anchors stay intact unless
they are internal heading anchors.

Recompute internal `#anchor` links against the translated headings using the host
platform's slug convention.

Keep the document's own conventions where they exist - a numbered-chapter source produces
a numbered-chapter English document.

New filenames drop diacritics and spaces per `languages/en.md` naming rules.

## Limitations

The pair covers whole-document rendering.

A mixed-language source gets only its German segments translated - report the rest.

Translate asks for a different language of the same document - improving, restructuring, or
summarizing the content is out of scope.
