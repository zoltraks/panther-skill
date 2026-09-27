# German To Polish Translation

## Purpose

> **Scope:** Direction contract for rendering a document from German into Polish
> **Key items:** loading order, style adaptation, abbreviation mapping, locale
> conventions, vocabulary and register, untranslated set, terminology resolution,
> output conventions

This file governs the German to Polish direction of document translation.

Load it together with `languages/pl.md` whenever a translate task renders a document into
Polish, following `process/translate-document.md`.

## Loading Order

Apply the rule files in this order:

1. `languages/pl.md` - the Polish baseline: structure, headings, lists, tables,
   characters, vocabulary, file naming, and per-type section names.
2. `translations/de-pl/de-pl-general.md` - this file: direction adaptation and
   terminology rules.
3. `translations/de-pl/de-pl-<category>.md` - every glossary whose domain signals match
   the document.
4. `types/<type>.md` - when the document matches a known type, for its structural deltas.
5. `conventions/` files - only when the source document's dialect requires them.

The Polish baseline and this file together define the output style.

A glossary supplies vocabulary only - it never overrides the baseline's structure rules.

## Style Adaptation

| Element                | German source                      | Polish target                                 |
|------------------------|------------------------------------|-----------------------------------------------|
| Heading capitalization | sentence case                      | sentence case                                 |
| Section names          | `de.md` names or free text         | `pl.md` section-name mapping, faithful render |
| Example headings       | `Richtig` / `Falsch`               | `Poprawnie` / `Niepoprawnie`                  |
| Example heading        | `Beispielinhalt`                   | `Przykład zawartości`                         |
| Typographic quotes     | low-high double quotes, guillemets | straight ASCII `"`                            |
| Prose dash             | ` - ` or ` – `                     | ` - ` spaced hyphen                           |
| Semicolon in prose     | not used                           | not used                                      |
| Definition pattern     | `**Begriff**: Definition`          | `**Termin**: definicja`                       |
| Numbered chapters      | `# 1`, `## 1.1` numbering          | numbering kept, caption translated            |
| Diacritics             | umlauts and `ß`                    | full Polish diacritics in composed form       |

Headings keep their level, order, and numbering - only the text changes.

Map German section names to the matching Polish entry of the same type-table row -
`## Zweck` becomes `## Przeznaczenie` for an agent-instruction document.

A section name neither table covers gets a faithful Polish rendering in sentence case.

Proper nouns keep their native spelling - `München`, `Köln` keep their diacritics in
Polish text, `ß` renders as `ß` or `ss` per the name's accepted spelling.

A German source using straight ASCII quotes produces straight ASCII quotes - the
document's own convention wins over the conversion row above.

## Abbreviation Mapping

German abbreviations map to their Polish equivalents in rendered prose:

| German  | Polish  |
|---------|---------|
| `z. B.` | `np.`   |
| `d. h.` | `tj.`   |
| `usw.`  | `itd.`  |
| `u. a.` | `m.in.` |
| `sog.`  | `tzw.`  |
| `ca.`   | `ok.`   |
| `vgl.`  | `por.`  |
| `ggf.`  | `ew.`   |
| `Nr.`   | `nr`    |

Established German acronym glosses map to their Polish counterparts - `PSP` becomes `SPP`,
`DSGVO` becomes `RODO` when the matching glossary declares them.

## Locale Conventions

German locale facts - the decimal comma, dot thousands grouping, and `TT.MM.JJJJ` dates -
appear in the source data and stay untouched.

Numeric, date, and code values are preserved verbatim.

Translation changes the language of the document, never its data formats.

## Vocabulary And Register

Prefer the Polish form from the matching glossary and the `pl.md` vocabulary table.

Settled loanwords stay untranslated: `endpoint`, `frontend`, `backend`, `CI/CD`, `commit`,
`pull request`, `merge`, `lint`.

Do not decline English words with Polish endings when a natural Polish equivalent exists -
`właściciele biznesowi`, not `ownerzy biznesowi`.

Keep one register per document - everyday Polish software-engineering usage is the
default, formal standards-register spellings are applied only when the source or the
request establishes them.

## What Stays Untranslated

The following elements are copied verbatim:

- Fenced and indented code blocks, including their comments.
- Inline code spans, file paths, URLs, commands, and configuration keys.
- Identifiers - record IDs, requirement IDs, API names, version markers in HTML comments.
- Proper nouns, product names, brand names, and architecture element names.
- YAML frontmatter - keys and values stay verbatim as document metadata.
- Machine markers `TBD` and `NOT SPECIFIED`.
- `k. A.` renders `N/D` in Polish prose and table cells.

## Terminology Resolution

Apply terms in this precedence order:

1. Terminology the document or the project already establishes - a glossary section, a
   sibling Polish document, or a project dictionary wins over every default and is
   recorded in the report.
2. The matching `translations/de-pl/de-pl-<category>.md` glossaries.
3. The `pl.md` vocabulary table and this file's rules.
4. A faithful literal rendering when no entry exists - never invent an equivalent.

One German term maps to one Polish rendering inside a document, except entries a glossary
marks as context-dependent.

Record notable choices - project terminology, conflict resolutions, literal renders - for
the delivery report.

## Heading Translation

Translate every heading's text and apply sentence case.

Keep heading depth unchanged - an H2 stays an H2.

Map `de.md` section names to the Polish names of the same type-table rows - `## Zweck des
Dokuments` becomes `## Cel dokumentu` for a project-document document.

A section name the tables do not cover is rendered faithfully - `## Hinweise zum
Deployment` becomes `## Uwagi wdrożeniowe`.

## Output Conventions

Write the translated document to a sibling file carrying the language code -
`leitfaden.md` produces `leitfaden-pl.md`, `README.md` produces `README-pl.md`.

Create the file in UTF-8 without BOM and with LF line endings.

Translate link text but keep link targets - URL, file path, and anchors stay intact unless
they are internal heading anchors.

Recompute internal `#anchor` links against the translated headings using the host
platform's slug convention - GitHub keeps Unicode letters, so `## Nazwy plików` anchors
to `#nazwy-plików`.

Keep the document's own conventions where they exist - a numbered-chapter source produces
a numbered-chapter Polish document.

## Limitations

The pair covers whole-document rendering.

A mixed-language source gets only its German segments translated - report the rest.

Translate asks for a different language of the same document - improving, restructuring, or
summarizing the content is out of scope.
