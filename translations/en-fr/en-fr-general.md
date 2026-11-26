# English To French Translation

## Purpose

> **Scope:** Direction contract for rendering a document from English into French

> **Key items:** loading order, style adaptation, abbreviation mapping, locale conventions,
> vocabulary and register, untranslated set, terminology resolution, output conventions

This file governs the English to French direction of document translation.

Load it together with `languages/fr.md` whenever a translate task renders a document into French,
following `process/translate-document.md`.

## Loading Order

Apply the rule files in this order:

1. `languages/fr.md` - the French baseline: structure, headings, lists, tables, characters,
   vocabulary, file naming, and per-type section names.
2. `translations/en-fr/en-fr-general.md` - this file: direction adaptation and terminology rules.
3. `translations/en-fr/en-fr-<category>.md` - every glossary whose domain signals match the
   document, for example `translations/en-fr/en-fr-software.md`.
4. `types/<type>.md` - when the document matches a known type, for its structural deltas.
5. `conventions/` files - only when the source document's dialect requires them.

The French baseline and this file together define the output style.

A glossary supplies vocabulary only.

It never overrides the baseline's structure rules.

## Style Adaptation

| Element                | English source                | French target                                              |
|------------------------|-------------------------------|------------------------------------------------------------|
| Heading capitalization | Title Case                    | sentence case with normal French capitalization            |
| Section names          | type table names or free text | `fr.md` section-name mapping, faithful render              |
| Example headings       | `Correct` / `Incorrect`       | `Correct` / `Incorrect`                                    |
| Example heading        | `Example Content`             | `Contenu d'exemple`                                        |
| Prose quotes           | straight ASCII `"`            | straight ASCII `"` - guillemets not introduced             |
| Prose dash             | ` - ` spaced hyphen           | ` - ` spaced hyphen                                        |
| Semicolon in prose     | not used                      | not used                                                   |
| Definition pattern     | `**Term**: definition`        | `**Terme** : définition`                                   |
| Numbered chapters      | `# 1`, `## 1.1` numbering     | numbering kept, caption translated                         |
| Diacritics             | none                          | accented letters and `ç` in composed form                  |
| Double punctuation     | `?`, `!`, `:`                 | preceded by an ordinary space - never a non-breaking space |

Headings keep their level, order, and numbering - only the text and case change.

When the document type is known, map section names per the "Noms de sections par type de document"
table in `languages/fr.md`.

A heading the table does not cover gets a faithful French rendering in sentence case.

A French document already using guillemets keeps that convention.

The document's own conventions win over this table.

## Abbreviation Mapping

English abbreviations map to their French equivalents in rendered prose:

| English   | French         |
|-----------|----------------|
| `e.g.`    | `p. ex.`       |
| `i.e.`    | `c.-à-d.`      |
| `etc.`    | `etc.`         |
| `a.m.`    | `entre autres` |
| `et al.`  | `et al.`       |
| `approx.` | `env.`         |
| `cf.`     | `cf.`          |
| `no.`     | `n°`           |
| `ibid.`   | `ibid.`        |

Do not abbreviate where the source writes the phrase out - write `par exemple` out when the source
says "for example" in prose.

## Locale Conventions

French locale facts - dates as `JJ/MM/AAAA`, the decimal comma,
and space thousands grouping - apply only to prose the translation newly generates.

Numeric, date, and code values are preserved verbatim.

Translation changes the language of the document, never its data formats.

## Vocabulary And Register

Prefer the French form from the matching glossary and the `fr.md` vocabulary table.

Settled loanwords stay untranslated: `commit`, `pull request`, `merge`, `branch`, `repository`,
`pipeline`, `cache`, `endpoint`, `backend`, `frontend`, `framework`, `workspace`.

Avoid anglicism calques the way `fr.md` and the glossaries describe - `mettre à jour`,
not `updater`, `corriger`, not `fixer`, `personnaliser`, not `customiser`,
`enregistrer`, not `sauver`.

Write multi-word terms the French way - a noun joined by a preposition or a hyphen,
never a bare noun stack - `registre des risques`, not `risques registre`.

Keep one register per document.

Everyday French software-engineering usage is the default,
formal register and standards-register spellings are applied only when the source or the
request establishes them.

Direct instructions use the `vous`-imperative - `Utilisez`, `Écrivez` - matching the baseline files,
unless the source's register calls for a different form.

## What Stays Untranslated

The following elements are copied verbatim:

- Fenced and indented code blocks, including their comments.
- Inline code spans, file paths, URLs, commands, and configuration keys.
- Identifiers - record IDs, requirement IDs, API names, version markers in HTML comments.
- Proper nouns, product names, brand names, and architecture element names.
- YAML frontmatter - keys and values stay verbatim as document metadata.
- Machine markers `TBD` and `NOT SPECIFIED`.
- `N/A` renders `s. o.` in French prose and table cells.

## Terminology Resolution

Apply terms in this precedence order:

1. Terminology the document or the project already establishes - a glossary section,
   a sibling French document, or a project dictionary wins over every default and is
   recorded in the report.
2. The matching `translations/en-fr/en-fr-<category>.md` glossaries.
3. The `fr.md` vocabulary table and this file's rules.
4. A faithful literal rendering when no entry exists - never invent an equivalent.

One English term maps to one French rendering inside a document,
except entries a glossary marks as context-dependent.

Record notable choices - project terminology, conflict resolutions,
literal renders - for the delivery report.

## Heading Translation

Translate every heading's text and apply sentence case with normal French capitalization.

Keep heading depth unchanged - an H2 stays an H2.

Map known-type section names through the `fr.md` table - `## Purpose` becomes `## Objet` for an
agent-instruction document.

A section name the table does not cover is rendered faithfully - `## Deployment Notes` becomes
`## Notes de déploiement`, not a forced table match.

## Output Conventions

Write the translated document to a sibling file carrying the language code - `guide.md` produces
`guide-fr.md`, `README.md` produces `README-fr.md`.

Create the file in UTF-8 without BOM and with LF line endings.

Translate link text but keep link targets - URL, file path,
and anchors stay intact unless they are internal heading anchors.

Recompute internal `#anchor` links against the translated headings using the host platform's slug
convention - GitHub keeps Unicode letters, so `## Procédures` anchors to `#procédures`.

Keep the document's own conventions where they exist.

A numbered-chapter source produces a numbered-chapter French document.

## Limitations

The pair covers whole-document rendering.

A mixed-language source gets only its English segments translated - report the rest.

Translate asks for a different language of the same document - improving, restructuring,
or summarizing the content is out of scope.
