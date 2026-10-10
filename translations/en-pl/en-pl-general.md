# English To Polish Translation

## Purpose

> **Scope:** Direction contract for rendering a document from English into Polish
> **Key items:** loading order, style adaptation, locale conventions, vocabulary and
> register, untranslated set, terminology resolution, output conventions

This file governs the English to Polish direction of document translation.

Load it together with `languages/pl.md` whenever a translate task renders a document into
Polish, following `process/translate-document.md`.

## Loading Order

Apply the rule files in this order:

1. `languages/pl.md` - the Polish baseline: structure, headings, lists, tables, characters,
   vocabulary, file naming, and per-type section names.
2. `translations/en-pl/en-pl-general.md` - this file: direction adaptation and
   terminology rules.
3. `translations/en-pl/en-pl-style.md` - sentence-level adaptation: aspect and voice,
   actor verbs, verb choice, fixed idioms, hedged verdicts.
4. The resolved format-contract mapping per `process/translate-document.md` - the
   producer's own Polish rendering rules, when the source is a governed-format document.
5. `translations/en-pl/en-pl-<category>.md` - every glossary whose domain signals match
   the document, for example `translations/en-pl/en-pl-software.md`.
6. `types/<type>.md` - when the document matches a known type, for its structural deltas.
7. `conventions/` files - only when the source document's dialect requires them.

The Polish baseline and this file together define the output style.

A glossary supplies vocabulary only - it never overrides the baseline's structure rules.

## Style Adaptation

| Element                | English source                | Polish target                                                     |
|------------------------|-------------------------------|-------------------------------------------------------------------|
| Heading capitalization | Title Case                    | sentence case                                                     |
| Section names          | type table names or free text | contract mapping first, then `pl.md` mapping or a faithful render |
| Example headings       | `Correct` / `Incorrect`       | `Poprawnie` / `Niepoprawnie`                                      |
| Example heading        | `Example Content`             | `Przykład zawartości`                                             |
| Prose quotes           | straight ASCII `"`            | straight ASCII `"` - typographic quotes not introduced            |
| Prose dash             | ` - ` spaced hyphen           | ` - ` spaced hyphen                                               |
| Semicolon in prose     | not used                      | not used                                                          |
| Definition pattern     | `**Term**: definition`        | `**Termin**: definicja`                                           |
| Numbered chapters      | `# 1`, `## 1.1` numbering     | numbering kept, caption translated                                |
| Diacritics             | none                          | full Polish diacritics in composed form                           |

Headings keep their level, order, and numbering - only the text and case change.

When the document type is known, map section names per the "Nazwy sekcji według typu
dokumentu" table in `languages/pl.md`.

A heading the table does not cover gets a faithful Polish rendering in sentence case.

A Polish source document already using typographic quotes keeps that convention - the
document's own conventions win over this table.

The character convention is a per-task decision resolved in this order: an explicit
request, the source document's own convention, then the nature of the deliverable -
plain ASCII is the default for every output, and typographic quotes, pauza or półpauza
dashes, and `→` arrows are used only when one of those sources establishes them.

## Locale Conventions

Polish locale facts - dates as `DD.MM.RRRR`, the decimal comma, thin-space thousands
grouping, and the `sierotki` rule keeping single-letter words off a line end - apply only
to prose the translation newly generates.

Numeric, date, and code values are preserved verbatim.

Translation changes the language of the document, never its data formats.

## Vocabulary And Register

Prefer the Polish form from the matching glossary and the `pl.md` vocabulary table.

Settled loanwords stay untranslated: `endpoint`, `frontend`, `backend`, `CI/CD`, `commit`,
`pull request`, `merge`, `lint`, `due diligence`, `roadmapa`.

Never combine both forms of one term in a single phrase - write `środowisko uruchomieniowe`
or `runtime`, never `środowisko uruchomieniowe runtime`.

Avoid literal calques the way `pl.md` and the glossaries describe - `rozbieżność`, not
`rozjazd`, `zamrożenie wersji`, not `przypięcie wersji`.

Check the loaded glossary's Calque Traps table and the `pl.md` vocabulary table before
writing any flagged form - a form listed there is always wrong regardless of how
natural it sounds in the source.

Never join two independent Polish clauses with a bare comma - the English comma-splice
habit does not transfer.

Use a full stop, a colon, or a conjunction (`więc`, `natomiast`, `ponieważ`).

Do not personify artifacts - files, sections, and branches do not act - persons and
tools do.

Render `the file removes X` as `plik usuwa X` only when the file is a program.

Otherwise use the passive or an action noun (`plik został usunięty`, `usunięcie X`).

A rendering never adds or drops meaning - no invented negation, quantifier, condition,
or exception, and no silently changed entity kind (`file` stays `plik`, never
`katalog`) - and a source ambiguity or contradiction is reported in the delivery
report, never silently resolved in the rendering.

Expand abbreviations at first use and record them in the document's glossary -
`merge request (MR)`, not a bare `MR`.

Product and technology names keep their canonical spelling and decline normally -
`Git`, `SemVer`, `w plikach Dockera` - filenames, commands, and identifiers never
decline and take a generic noun (`plik AGENTS.md`, `system GitLab`).

A verbatim foreign-language quotation stays in quotes with a Polish gloss beside it -
never weave quoted English into Polish syntax.

A translator's own rendering is marked as such or paraphrased without quotes.

Decline adjectives in gender agreement with the governed noun - `ważność WYSOKA`,
`wpływ WYSOKI`, `ryzyko WYSOKIE`, `następstwa NEGATYWNE`.

Render countable items with countable nouns - `wpisy .gitignore`, not
`ignorowanie` - a nominalized verb names the mechanism, not the item.

Use neuter gender for acronyms treated as nouns - `czyste PWA`, not `czysta PWA`.

Keep one register per document - everyday Polish software-engineering usage is the default,
formal standards-register spellings are applied only when the source or the request
establishes them.

Recognized industry terms stay in English with a Polish gloss at first use - `Promise`,
`frontmatter`, `pull request`, `commit` - when a literal rendering would read as a
calque.

Never render them literally - `obietnica pływająca` is a calque, `obiekt Promise
pozostawiony bez obsługi` is the rendering.

Address the reader with lowercase second-person pronouns - `cię`, `tobie`, `twój` -
or drop the pronoun, never `Cię` or `Twój` mid-sentence.

Agent and people terms stay uniform per the glossary - `agent AI do programowania`,
`agenci AI`, `opiekun projektu`, `osoby współtworzące projekt` - never mixed with
`agenci kodowania`, `maintainerzy`, or `współpracownicy`.

Do not decline English words with Polish endings when a natural Polish equivalent exists -
`właściciele biznesowi`, not `ownerzy biznesowi`.

Settled technical loanwords without a common Polish equivalent decline normally in
expert register - `hooka`, `scorecardy`, `commitami`, `niezacommitowany` - the
glossary's Untranslated list carries them.

## What Stays Untranslated

The following elements are copied verbatim:

- Fenced and indented code blocks - code, commands, keys, and values. The comments and
  natural-language strings inside them follow the Reader-Facing Text In Examples rule
  below.
- Inline code spans, file paths, URLs, commands, and configuration keys.
- Identifiers - record IDs, requirement IDs, API names, version markers in HTML comments.
- Proper nouns, product names, brand names, and architecture element names.
- Cited section names, field labels, and verdict vocabularies of referenced
  documents and tools - `Evidence Ledger`, `Finding Disposition`, `Journey
  Traces` stay verbatim wherever the prose cites them.
- YAML frontmatter - keys and values stay verbatim as document metadata.
- Machine markers `TBD` and `NOT SPECIFIED`.
- Verdict, option, and status labels fixed as contract vocabulary - `CONFORMING`,
  `GAP`, `DRIFT`, enumerated choice names such as `Adopt` or `Distributed` - stay
  verbatim in prose and embedded payloads alike, unless the producing contract maps
  them: a resolved format contract's Polish forms apply instead.
- `N/A` renders `N/D` in Polish prose and table cells.

## Reader-Facing Text In Examples

Text a reader reads gets translated even when it sits inside an example or a fenced
block.

Translate explanatory comments inside code blocks, example prompts and request
payloads, and the natural-language values of fields such as `question` or
`description`.

In a menu or option label, translate the descriptive part and keep every required
technical value verbatim.

An example table that demonstrates a machine-readable contract keeps its fixed values
verbatim - the cells show the output format, not reader prose.

A prompt intended as executable input to an English-language tool may stay verbatim
when the project convention shows it - record the choice in the report.

Never translate code, commands, configuration keys, file paths, protocol values, or
the surrounding syntax - only the reader-facing prose they carry.

## Terminology Resolution

Apply terms in this precedence order:

1. Terminology the document or the project already establishes - a glossary section, a
   sibling Polish document, or a project dictionary wins over every default and is recorded
   in the report.
2. The resolved format-contract mapping - the producer's own Polish renderings for every
   element it covers.
3. The matching `translations/en-pl/en-pl-<category>.md` glossaries.
4. The `pl.md` vocabulary table and this file's rules.
5. Established usage in authoritative Polish sources - translated standards such as
   ISTQB and ISO, the Polish Scrum Guide, Polish Pro Git, and official vendor
   documentation.
6. A faithful literal rendering when no entry exists - never invent an equivalent.

The Calque Traps tables and the `pl.md` "Zamiast / Używaj" table act as a veto at every
precedence level - a form they forbid is never a candidate, even for a literal render.

One English term maps to one Polish rendering inside a document, except entries a glossary
marks as context-dependent.

Record notable choices - project terminology, conflict resolutions, literal renders - for
the delivery report.

## Heading Translation

Translate every heading's text and apply sentence case.

Keep heading depth unchanged - an H2 stays an H2.

Map known-type section names through the `pl.md` table - `## Purpose` becomes
`## Przeznaczenie` for an agent-instruction document.

A section name the table does not cover is rendered faithfully - `## Deployment Notes`
becomes `## Uwagi wdrożeniowe`, not a forced table match.

Prefer a short verb-noun heading that names what the section does - `## Ustalanie
lokalizacji wytycznych` reads naturally where `## Strategie lokalizacji wytycznych`
mirrors the English noun phrase.

A heading also drops a qualifier the section body already states - `## Zestaw
kanoniczny`, not `## Zestaw kanoniczny według profilu`.

## Output Conventions

Write the translated document to a sibling file carrying the language code -
`guide.md` produces `guide-pl.md`, `README.md` produces `README-pl.md`.

Create the file in UTF-8 without BOM and with LF line endings.

Translate link text but keep link targets - URL, file path, and anchors stay intact unless
they are internal heading anchors.

Recompute internal `#anchor` links against the translated headings using the host
platform's slug convention - GitHub keeps Unicode letters, so `## Nazwy plików` anchors to
`#nazwy-plików`.

Keep the document's own conventions where they exist - a numbered-chapter source produces
a numbered-chapter Polish document.

A localized marker stays coherent with the examples that reference it - when the header
comment uses `Wersja:`, an example command searching for the marker searches `Wersja:`
too, or the marker stays untranslated. A localized marker paired with an example that
still greps the English form is a defect.

Link text stays consistent with the translated heading it points at - when a heading is
retranslated, its anchor link text follows.

## Limitations

The pair covers whole-document rendering.

A mixed-language source gets only its English segments translated - report the rest.

Translate asks for a different language of the same document - improving, restructuring, or
summarizing the content is out of scope.
