# English To Spanish Translation

## Purpose

> **Scope:** Direction contract for rendering a document from English into Spanish

> **Key items:** loading order, style adaptation, abbreviation mapping, locale conventions,
> vocabulary and register, untranslated set, terminology resolution, output conventions

This file governs the English to Spanish direction of document translation.

Load it together with `languages/es.md` whenever a translate task renders a document into Spanish,
following `process/translate-document.md`.

## Loading Order

Apply the rule files in this order:

1. `languages/es.md` - the Spanish baseline: structure, headings, lists, tables, characters,
   vocabulary, file naming, and per-type section names.
2. `translations/en-es/en-es-general.md` - this file: direction adaptation and terminology rules.
3. `translations/en-es/en-es-<category>.md` - every glossary whose domain signals match the
   document, for example `translations/en-es/en-es-software.md`.
4. `types/<type>.md` - when the document matches a known type, for its structural deltas.
5. `conventions/` files - only when the source document's dialect requires them.

The Spanish baseline and this file together define the output style.

A glossary supplies vocabulary only.

It never overrides the baseline's structure rules.

## Style Adaptation

| Element                | English source                | Spanish target                                         |
|------------------------|-------------------------------|--------------------------------------------------------|
| Heading capitalization | Title Case                    | sentence case with normal Spanish capitalization       |
| Section names          | type table names or free text | `es.md` section-name mapping, faithful render          |
| Example headings       | `Correct` / `Incorrect`       | `Correcto` / `Incorrecto`                              |
| Example heading        | `Example Content`             | `Contenido de ejemplo`                                 |
| Prose quotes           | straight ASCII `"`            | straight ASCII `"` - typographic quotes not introduced |
| Prose dash             | ` - ` spaced hyphen           | ` - ` spaced hyphen                                    |
| Semicolon in prose     | not used                      | not used                                               |
| Definition pattern     | `**Term**: definition`        | `**Término**: definición`                              |
| Numbered chapters      | `# 1`, `## 1.1` numbering     | numbering kept, caption translated                     |
| Diacritics             | none                          | accented letters and `ñ` in composed form              |
| Question marks         | `?` closing only              | `¿...?` opening and closing marks                      |
| Exclamation marks      | `!` closing only              | `¡...!` opening and closing marks                      |

Headings keep their level, order, and numbering - only the text and case change.

When the document type is known, map section names per the "Nombres de secciones por tipo de
documento" table in `languages/es.md`.

A heading the table does not cover gets a faithful Spanish rendering in sentence case.

A Spanish document already using typographic quotes keeps that convention.

The document's own conventions win over this table.

## Abbreviation Mapping

English abbreviations map to their Spanish equivalents in rendered prose:

| English   | Spanish       |
|-----------|---------------|
| `e.g.`    | `p. ej.`      |
| `i.e.`    | `es decir`    |
| `etc.`    | `etc.`        |
| `a.m.`    | `entre otros` |
| `et al.`  | `et al.`      |
| `approx.` | `aprox.`      |
| `cf.`     | `cf.`         |
| `no.`     | `n.º`         |
| `ibid.`   | `ibíd.`       |

Do not abbreviate where the source writes the phrase out - write `por ejemplo` out when the source
says "for example" in prose.

## Locale Conventions

Spanish locale facts - dates as `DD/MM/AAAA`, the decimal comma,
and dot thousands grouping - apply only to prose the translation newly generates.

Numeric, date, and code values are preserved verbatim.

Translation changes the language of the document, never its data formats.

## Vocabulary And Register

Prefer the Spanish form from the matching glossary and the `es.md` vocabulary table.

Settled loanwords stay untranslated: `commit`, `pull request`, `merge`, `branch`, `repository`,
`pipeline`, `cache`, `endpoint`, `backend`, `frontend`, `framework`, `backlog`, `sprint`.

Avoid anglicism calques the way `es.md` and the glossaries describe - `desplegar`,
not `deployar`, `actualizar`, not `updatear`, `corregir`, not `fixear`,
`probar`, not `testear`.

Write multi-word terms the Spanish way - a noun joined by a preposition,
never a bare noun stack - `registro de riesgos`, not `riesgos registro`.

Keep one register per document.

Everyday Spanish software-engineering usage is the default,
formal register and standards-register spellings are applied only when the source or the
request establishes them.

Direct instructions use the `usted`-imperative - `Utilice`, `Escriba` - matching the baseline files,
unless the source's register calls for a different form.

## What Stays Untranslated

The following elements are copied verbatim:

- Fenced and indented code blocks, including their comments.
- Inline code spans, file paths, URLs, commands, and configuration keys.
- Identifiers - record IDs, requirement IDs, API names, version markers in HTML comments.
- Proper nouns, product names, brand names, and architecture element names.
- YAML frontmatter - keys and values stay verbatim as document metadata.
- Machine markers `TBD` and `NOT SPECIFIED`.
- `N/A` renders `N/D` in Spanish prose and table cells.

## Terminology Resolution

Apply terms in this precedence order:

1. Terminology the document or the project already establishes - a glossary section,
   a sibling Spanish document, or a project dictionary wins over every default and is
   recorded in the report.
2. The matching `translations/en-es/en-es-<category>.md` glossaries.
3. The `es.md` vocabulary table and this file's rules.
4. A faithful literal rendering when no entry exists - never invent an equivalent.

One English term maps to one Spanish rendering inside a document,
except entries a glossary marks as context-dependent.

Record notable choices - project terminology, conflict resolutions,
literal renders - for the delivery report.

## Heading Translation

Translate every heading's text and apply sentence case with normal Spanish capitalization.

Keep heading depth unchanged - an H2 stays an H2.

Map known-type section names through the `es.md` table - `## Purpose` becomes `## Propósito` for an
agent-instruction document.

A section name the table does not cover is rendered faithfully - `## Deployment Notes` becomes
`## Notas de despliegue`, not a forced table match.

## Output Conventions

Write the translated document to a sibling file carrying the language code - `guide.md` produces
`guide-es.md`, `README.md` produces `README-es.md`.

Create the file in UTF-8 without BOM and with LF line endings.

Translate link text but keep link targets - URL, file path,
and anchors stay intact unless they are internal heading anchors.

Recompute internal `#anchor` links against the translated headings using the host platform's slug
convention - GitHub keeps Unicode letters, so `## Propósito` anchors to `#propósito`.

Keep the document's own conventions where they exist.

A numbered-chapter source produces a numbered-chapter Spanish document.

## Limitations

The pair covers whole-document rendering.

A mixed-language source gets only its English segments translated - report the rest.

Translate asks for a different language of the same document - improving, restructuring,
or summarizing the content is out of scope.
