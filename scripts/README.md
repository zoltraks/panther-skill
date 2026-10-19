# Panther Tooling

## Purpose

> **Scope:** Document-production and skill-maintenance scripts
> **Key items:** encoding detection, scope signals, sentence splitting, prose wrapping and
> unwrapping, table formatting, comment alignment, document validation, content diffing,
> structural parity, document census, skill validation, reference integrity,
> contents-table drift, self-update check

These scripts support deterministic production of documents and maintenance of Panther itself.

They do not modify documents beyond the specific task each tool performs.

## Contents

| Section          | Line | What it covers                           |
|------------------|------|------------------------------------------|
| Tool Classes     | 24   | Tool groups and when to run them         |
| Commands         | 95   | Per-tool usage, flags, and output        |
| Validation Order | 453  | Recommended run sequence                 |
| Limitations      | 499  | Known parsing limits and validator scope |

## Tool Classes

### Document-Production Tools

Run `detect-encoding.py`, `detect-scope.py`, `normalize-chars.py`, `split-sentences.py`,
`reflow-prose.py`, `wrap-prose.py`, `format-table.py`, `align-comments.py`,
`validate-document.py`, `check-document.py`, `diff-content.py`, `census-document.py`,
`check-sections.py`, `check-parity.py`, `check-titles.py`, `safe-replace.py`,
`lint-polish.py`, `lint-english.py`, and `check-consistency.py` in place from the
skill repository:

`python <skill-root>/scripts/<tool>.py <file>`.

In-place invocation is the default.

The tools are self-contained, write nothing to the skill repository,
and resolve their rule resources relative to their own location,
so `lint-polish.py` and `lint-english.py` find their rule tables without `--rules` and
`check-sections.py` resolves bare type slugs and language codes.

When the skill root cannot be invoked directly.

For example the skill payload exists only as pasted content - copy the needed tools into the working
repository's `work/` directory under a `.tmp.` name and remove them after use.

In that mode `lint-polish.py` and `lint-english.py` cannot auto-discover their rule
tables - pass them explicitly with `--rules <path>` pointing at the skill's
`languages/pl.md` or `languages/en.md` and the matching glossary files, or set
`PANTHER_SKILL_ROOT` so `check-document.py` locates siblings and rules.

If `work/` does not exist, use an existing `temp` or `temporary` directory.

When the project declares a temporary directory - for example `work/` in its guidelines or
`.gitignore` - that does not exist yet, create it for the copy rather than using the repository
root.

Use the repository root only when no declared or existing temporary directory applies.

Run the tools only against the document being created, edited, or audited.

Ad-hoc helpers created during a session - such as a one-off normalization script - and
baseline snapshots for `diff-content.py` carry the `.tmp.` infix inside that directory.

Remove every copied script and every ad-hoc `.tmp.` helper after use, including on
aborted runs - the working tree must end unchanged outside the target document.

### Skill-Maintenance Tools

Run `validate-skill.py`, `check-references.py`, `check-contents.py`, and `check-update.py` from
the Panther repository.

These tools inspect the skill itself and are never copied into a working project.

Untracked scratch under `work/` is gitignored and excluded from validation.

`check-contents.py` verifies that every `## Contents` table row still points at a real `## `
section - run it after any edit that shifts lines in a file carrying a contents table.

`check-update.py` reports the git upstream status of the skill repository for the once-per-session
Skill Update Check in `SKILL.md`, and always exits `0` with a `STATUS` verdict line.

Its verdicts after upstream resolution carry `tip_sha` and `tip_date` details identifying the
incoming tip commit - the pull path applies no cryptographic verification, so those fields are
the review anchor an agent presents before asking to pull.

`UPDATE-AVAILABLE` also reports `incoming_total` plus one `incoming_<n>=<sha> <subject>` line per
incoming commit (capped at ten, `incoming_truncated=yes` beyond that), `changed_files`, and the
`changed_scripts` / `changed_skill` risk flags so the reviewer sees the payload before approving.

They use the Python standard library and do not require PyYAML or a package manager.

## Commands

The commands below use `python`.

Substitute `python3` when `python` is not on PATH.

```bash
python <skill-root>/scripts/detect-encoding.py <file>
python <skill-root>/scripts/detect-scope.py <directory>
python <skill-root>/scripts/normalize-chars.py <file.md> [--check] [--payload-markdown]
python <skill-root>/scripts/split-sentences.py <file.md> [--check] [--paragraphs | --flow] [--width N] [--payload-markdown]
python <skill-root>/scripts/reflow-prose.py <file.md> (--wrap | --unwrap | --justify) [--check] [--width N] [--payload-markdown]
python <skill-root>/scripts/format-table.py <file.md> [--check] [--payload-markdown] [--drop-empty-columns]
python <skill-root>/scripts/align-comments.py <file.md> [--check] [--compact] [--payload-markdown]
python <skill-root>/scripts/validate-document.py <file.md> [--width N] [--payload-markdown]
python <skill-root>/scripts/check-document.py <file.md> [--width N] [--payload-markdown] [--layout wrap|unwrap] [--split] [--polish] [--english] [--consistency] [--type <slug>] [--language <code>] [--baseline <file>] [--normalize-chars] [--parity <source.md>] [--terms <glossary.md> ...] [--expect-map <file> ...] [--eol lf|crlf] [--title-agreement] [--skill-root <dir>]
python <skill-root>/scripts/check-parity.py <source.md> <target.md> [--terms <glossary.md> ...] [--expect-map <file> ...] [--eol lf|crlf]
python <skill-root>/scripts/check-titles.py <file.md> [--verbose]
python <skill-root>/scripts/safe-replace.py <file.md> <old> <new> [--raw] [--check]
python <skill-root>/scripts/diff-content.py <file.md> [--baseline <file>] [--normalize-chars]
python <skill-root>/scripts/census-document.py <file.md> [--width N] [--payload-markdown]
python <skill-root>/scripts/check-sections.py <file.md> --type <slug-or-path> [--language <code-or-path>]
python <skill-root>/scripts/lint-polish.py <file.md> [--rules <rulefile.md> ...] [--group-by-form] [--payload-markdown]
python <skill-root>/scripts/lint-english.py <file.md> [--rules <rulefile.md> ...] [--group-by-form] [--payload-markdown]
python <skill-root>/scripts/check-consistency.py <file.md> [--group-by-form] [--payload-markdown]
python scripts/validate-skill.py .
python scripts/check-references.py .
python scripts/check-contents.py .
python scripts/check-update.py
```

`detect-encoding.py` and `detect-scope.py` always exit `0` and print a report.

`normalize-chars.py` rewrites typographic characters to ASCII equivalents - quotes,
dashes, arrows, ellipsis, Unicode spaces, and the soft hyphen - and rewrites the file in
place, `--check` only reports the lines that would change.

Fences and frontmatter stay opaque while prose, inline code spans, table cells, and link
targets are normalized - run it before sentence and table passes so those passes see the
final characters.

`split-sentences.py` rewrites the file in place, `--check` only reports lines or blocks that pack
multiple sentences.

By default it emits each paragraph sentence starting on its own logical line and re-wraps the
affected sentences to `--width N`.

With `--paragraphs` it emits the house convention instead: every sentence becomes its own
paragraph, separated by one empty line, and sentences are never re-wrapped.

With `--flow` it repacks each paragraph block's sentences onto shared logical lines -
a sentence joins the current line while it still fits `--width` (default 80 in this mode)
or starts a new line when it does not, and sentences are never split.

This produces the `flowing` layout from `conventions/prose-layout.md`.

It leaves list items and their continuation lines opaque.

A packed list item is an element-level convention,
not a defect (see `conventions/markdown-dialects.md`).

Lines ending in `:` are treated as label lines and never absorb following sentences.

Abbreviations such as `e.g.` and `etc.` and periods inside inline code spans do not count as
boundaries.

`reflow-prose.py` rewrites the file in place, `--check` only reports the lines or blocks
the chosen direction would change.

Its `--wrap` mode splits over-width lines at whitespace - the same algorithm as
`wrap-prose.py`.

`--wrap` is width-only and does not place sentences on their own lines - run
`split-sentences.py --paragraphs` first when the convention also requires one sentence per
line.

Its `--unwrap` mode joins hard-wrapped continuation lines inside paragraphs, list items,
and blockquotes back into single logical lines.

Unwrap joins a line only when the accumulated text does not end with sentence-final
punctuation or a label colon, so separate sentences sharing a paragraph block stay on
their own lines - combine it with `split-sentences.py --paragraphs` when the task also asks
for one sentence per paragraph.

Its `--justify` mode wraps like `--wrap` and additionally stretches inter-word spacing on
every line of a block except its last, so both edges sit flush - the `justified` layout
from `conventions/prose-layout.md`.

The marker prefix of a list item or blockquote stays fixed, and the mode is idempotent on
an already justified document.

Both directions leave tables, fenced code blocks, indented code blocks, HTML comments, and
frontmatter untouched.

`wrap-prose.py` is deprecated, use `reflow-prose.py --wrap` instead.

It stays in `scripts/` for compatibility with documents that already reference it.

`check-document.py` runs the standard non-mutating battery against one file in a
single invocation - `detect-encoding.py`, `validate-document.py`,
`format-table.py --check`, `align-comments.py --check`, and both `reflow-prose.py`
direction checks - and prints one verdict line per tool.

`--layout wrap` or `--layout unwrap` promotes the matching reflow check to a gated
verdict - without it both report as advisory, since the document's convention decides
which applies.

`--split`, `--polish`, `--english`, `--consistency`, `--type`, `--language`,
`--baseline`, `--parity`, and `--title-agreement` add the `split-sentences.py`,
`lint-polish.py`, `lint-english.py`, `check-consistency.py`, `check-sections.py`,
`diff-content.py`, `check-parity.py`, and `check-titles.py` checks to the battery,
and a missing sibling reports `SKIP` instead of failing.

`--parity <source.md>` compares the checked file's structure against its source
document - the translate and revision validation gate - and `--terms <glossary.md>`
(repeatable) forwards glossary files to the parity concordance report and the
expected-translation map, while `--expect-map <file>` and `--eol` forward to
`check-parity.py`.

The script exits `1` when a gated check reports findings and `0` otherwise.

`--payload-markdown` extends `split-sentences.py`, `reflow-prose.py`, `wrap-prose.py`,
`format-table.py`, `align-comments.py`, `validate-document.py`, `check-document.py`,
`check-sections.py`, `lint-english.py`, and `check-consistency.py` into ` ```markdown `
fenced blocks, all other fence languages stay opaque.

`align-comments.py` aligns trailing `#` comments inside untagged fenced blocks and
shell-tagged blocks to one shared column per block - the established column when most
comments already share one, otherwise the longest entry plus two spaces.

`--compact` moves the column to the minimum.

A block whose opening fence is preceded by `<!-- align-comments: off -->` - optionally with one
blank line between the marker and the fence.

Is skipped entirely, so the marker exempts deliberate examples of misalignment from both fixing and
`--check`.

The convention lives in `conventions/plain-text-comments.md`.

`check-parity.py` diffs the structural fingerprint of a rendered document against its
source - heading level sequence, fence count and language tags, table geometry, list
counts, HTML comments, inline-code spans, internal `#anchor` resolution, and file-level
whitespace and byte conventions - printing `PARITY`, `DELTA`, `DECLARED`, or `NOTE`
lines and exiting `1` on any `DELTA`.

Heading *text* is never compared - a faithful render legitimately rewords it.

A missing inline-code span that looks like prose (multiple plain words) reports as a
`NOTE` - translated label text is legal - while identifier- or path-like missing spans
report as `DELTA`, and each diff line names the source or target lines the span
occupies.

`--expect-map <file>` (repeatable) declares intentional source-to-target changes: each
`SRC -> TGT` line - `#` comments and blank lines allowed, ` / ` separating alternative
targets - downgrades a matching inline-code delta to a `DECLARED` line, and
`link:#anchor -> -N` or `+N` declares an expected change in that anchor's link count.

`--terms <glossary.md>` (repeatable) cross-counts each glossary's Terminology table: an
English term appearing at least twice in the source but whose Polish variants never
appear in the target reports a `NOTE` concordance hint - context forms stay legal, so a
hint is a review prompt, not a verdict - and the same pairs seed the expected map, so a
span rendered as a declared variant reports `DECLARED`.

Target-side variants are matched by stem prefix, so inflected forms of a preferred
rendering still count.

A line-ending delta that matches the convention declared by `--eol lf|crlf` - or by the
nearest `.gitattributes` `eol=` attribute found walking up from the target - reports
`NOTE` instead of `DELTA`, while a delta contradicting a declared convention still
fails.

`diff-content.py` compares the normalized token stream of a document against `git show HEAD`
or a `--baseline` file, identical tokens mean a pass changed formatting only.

A document outside version control has no `git show HEAD` anchor - snapshot it to a
`.tmp.` file before the first edit and pass that snapshot as `--baseline`.

`--normalize-chars` maps both sides through the `normalize-chars.py` table first, so a
sanctioned character-normalization pass reports no token differences while word-level
edits still surface.

It exits `0` for identical token streams and `1` when tokens differ.

It prints `WARN` for possible merged lines - review those by hand.

`detect-scope.py` reports a signal census only - the agent maps signals to a scope per
`process/scope-discovery.md`.

Its directory census also lists `docs/` subdirectories, non-document artifacts such as API
specifications and configs, and `.gitignore`-declared directories that are absent on disk.

`census-document.py` reports a structural census of a single document - headings, list
markers, fenced blocks and ` ```markdown ` payloads, special characters, paragraph shape,
tables, task markers, and internal links - and the agent maps counts to findings per
`process/document-audit.md`.

Its paragraph report includes a prose-layout classification per element type -
`separated`, `flowing`, `bounded`, `justified`, or `mixed` - following the conventions
in `conventions/prose-layout.md`.

`check-sections.py` compares a document's headings against the `## Section Names` table of a
`types/<name>.md` rule file - the table marks each section `required`, `recommended`,
`optional`, or `unusual`.

Missing `required` sections print `MISSING required` and fail the run.

Missing `recommended` sections, `unusual` sections found in the document, and headings the
type does not list print warnings or `NOTE` lines and stay advisory.

A type file without a section table reports an open set and exits `0`.

`--language` points at a `languages/<code>.md` file so localized headings match the
canonical English names - a Polish `Decyzje` heading satisfies the `Decisions` section.

Headings match a canonical name by prefix when the remainder looks like a version or
placeholder - `## Version 1.2` and `## Version X.Y.Z` satisfy `Version`, and the same
prefix rule applies to localized names such as `## Wersja 1.2`.

`--type` also accepts a bare type slug resolved against `types/`, and `--language` a bare
language code resolved against `languages/`.

`lint-polish.py` lints a Polish document against the forbidden-form tables declared in
the loaded rule files (the `Zamiast`/`Używaj` table in `languages/pl.md` and the Calque
Traps tables of the matching glossaries).

It reports calques, clauses spliced by a bare comma, `per X` constructions, `tylko, gdy`,
a correlative `na tym` clause opened without a comma, a leading participial clause
missing its closing comma, typographic characters under the
ASCII convention, and `w.` abbreviations with line-level
findings - errors exit `1`, warnings are advisory and never fail the run.

Fixed idioms such as `pod kątem`, `pod względem`, or `pod opieką` are allowlisted - a
calque-flagged stem inside one of them produces no finding.

Each word of a forbidden form matches by declinable stem, so inflected variants hit the
form - `instrukcją wykonywalną` matches `instrukcja wykonywalna`.

Pass `--payload-markdown` to lint prose inside ` ```markdown ` fenced payload blocks,
whose interiors are translated text - other fence languages stay skipped.

Flagged commas inside a series closed by a conjunction (`X, Y i Z`) count as an
enumeration and raise no spliced-clause warning - the heuristic stays silent on
conjunction-closed coordination, which is legal Polish.

Parentheses, brackets, and braces also close a series, so `F-01, F-02 (wymagane)` or
`a, b (c, d)` raise no warning, and a comma before an identifier token such as `F-02` or
`ADR-3` counts as a list separator.

A line opened by a subordinate or participial clause (`Gdy ...`, `Jeśli ...`,
`Odwołując ...`) has its first flaggable comma exempt - it closes the opener clause -
and a comma followed by an `-ąc`/`-wszy`/`-łszy` participle is an adverbial phrase,
not a splice.

A calque stem inside an all-uppercase token - a status enum, an option name, an acronym -
raises no error, because replacing it would break a fixed label the document does not own.

A quoted span - `"..."`, `„..."`, or `«...»` - is verbatim cited material and raises no
calque finding, so quoted titles and foreign-language citations stay legal.

A parenthesized qualifier on a banned form - `trasa (routing)`, `rozjazd (drift)` -
bounds the ban to the named sense: every hit reports a warning naming that sense, never
an error, because the form is legal outside it.

`--group-by-form` replaces the line-by-line output with one line per matched form or
rule - hit count, line numbers, and the suggested replacement - the shape a bulk
fix pass needs.

Rerun without the flag for per-line detail.

It targets Polish deliverable documents - the skill's own rule files contain the
forbidden forms by definition and will report them.

`lint-english.py` lints an English document against the rule tables declared in
`languages/en.md` - the "Instead of / Use" vocabulary table and the Dialect
Consistency variant-pair table - plus built-in checks for common misspellings,
doubled words, `then`/`than` misuse, and `its'` errors.

Heuristic checks report warnings instead of errors: a/an agreement (with
acronym and vowel-sound exceptions), spaced hyphens joining clauses, and
dialect-minority spellings measured against the document's dominant variant -
the document's own convention wins, so dialect findings never name a fixed
dialect as mandatory.

A vocabulary form qualified in its table entry - `leverage (as a verb)` -
bounds the ban to the named sense and reports warnings, and a "verb + article +
noun" form demotes to a warning when the noun modifies a following word
("performs an update check").

Fully uppercase tokens are treated as constants, quoted verbatim spans are
exempt, and inline code spans stand in as placeholders so adjacent prose words
do not collapse into phantom findings - errors exit `1`, warnings stay
advisory.

`--group-by-form` groups findings per matched form like `lint-polish.py`, and
`--rules` overrides rule-table discovery, which defaults to the skill's
`languages/en.md`.

`check-consistency.py` verifies a document's internal references and managed
terminology.

A quoted Title-Case name in a reference context - a connector word like `in`,
`see`, `per`, `the`, or `of` before the quote, or a noun like `section` after
it must resolve against the document's own anchors: every heading, plus
`**Term**:` definition rows and bare `**Term**` pseudo-headings.

Quoted literals are not references.

Names inside code spans, paths, and lowercase or single-word quotes without a strong connector stay
ignored, and a path-qualified name like `"Appendix - Template Library"` resolves through its final
segment.

Unresolved references print `UNRESOLVED` and fail the run.

Similar names that appear to denote one thing print `VARIANT` warnings - advisory only - detected by
interior token gaps or a shared prefix and suffix.

Two plain headings are deliberately parallel and never pair,
and contiguous prefix or suffix extensions are legitimate scoping, not drift.

`check-titles.py` verifies that a document's `## ID: title` headings match the
title their summary-table row declares - the ID anchors the row whichever column holds
it, the title comes from the `Title`/`Tytuł` header column or the column after the ID,
and the comparison strips links, backticks, and emphasis so a heading that omits the
cell's glossary link still matches.

It prints `MISMATCH`, `MISSING-ROW`, and `MISSING-HEADING` findings and exits `1` when
any exist - `check-document.py --title-agreement` folds it into the battery.

`safe-replace.py` replaces text with whole-word boundaries by default - `niesie` to
`wnosi` never rewrites `odniesienia` into `odwnosinia` - and reports the residue after
every run: words still containing the pattern as a fragment and words containing the
replacement inside a longer token.

`--raw` performs a deliberate substring replacement with the same residue report,
`--check` is a dry run that exits `1` when the pattern also occurs inside longer words,
and the file's encoding and line endings are preserved.

`format-table.py` rebuilds tables with source-width alignment and normalizes every separator-row
cell to the correct hyphen count.

A separator cell without hyphens does not declare its column and is repaired, not preserved.

It warns on rows starting with `||` and on columns empty in every non-separator row -
`--drop-empty-columns` removes such columns instead of only warning.

`validate-document.py` fails on a table without a separator row, a separator row that is not
the second row, a separator cell lacking hyphens, a column empty in every row, a row
starting with `||`, a literal `|` inside an inline code span, and an escaped `\|` in a
table row - the last two silently inflate the column count, so the cell must use
`&#124;` or a different layout.

The validators exit `0` when all checks pass and `1` when one or more checks fail.

`validate-document.py` warns on `text` and `txt` fence tags - plain-text blocks default to
untagged fences in new content, while an existing document may carry the tag as its own
convention.

## Validation Order

Run `detect-scope.py` on the target directory first when the task needs the document scope.

Run checks in this order:

1. Detect encoding before editing an existing file.
2. Snapshot a `.tmp.` baseline for `diff-content.py` when the document is untracked and
   `git show HEAD` has no version to compare against.
3. Normalize typographic characters with `normalize-chars.py` when the document's
   convention is ASCII.
4. Check packed sentences with `split-sentences.py --check` when the request covers
   sentence separation.
5. Check the wrap convention with `reflow-prose.py --wrap --check` for fixed-width
   documents or `reflow-prose.py --unwrap --check` for logical-line documents, matching
   the detected convention.
6. Lint Polish output with `lint-polish.py` and apply every content fix it requires,
   or lint English output with `lint-english.py` for an English document.
7. Format edited tables with `format-table.py` - the last content-changing pass, so any
   later text edit requires re-running it and re-validating.
8. Align comments in plain-text blocks with `align-comments.py` when the document contains
   them.
9. Validate the written document with `validate-document.py`.
10. Check sections against the type file with `check-sections.py` when the document has a
    known type.
11. Check internal references and terminology with `check-consistency.py` when the
    document names its own sections by quote or defines managed terms.
12. Verify formatting-only passes with `diff-content.py` - add `--normalize-chars` when
    step 3 ran so the sanctioned character map does not surface as token differences.
13. Run `git diff --check` when inside a repository.
14. Remove every ad-hoc `.tmp.` helper and baseline snapshot - and any `.tmp.` tool
    copies made under the fallback convention - from the working repository.

`check-document.py` covers steps 4-5, 7-9, and 12 in one call - `--layout` selects the
wrap convention, `--polish` and `--english` cover step 6, `--type` covers step 10,
`--consistency` covers step 11, and `--baseline` covers step 12.

For a translation or revision task, `check-parity.py <source.md> <output.md>` runs as an
additional gate after the content-changing passes - `check-document.py --parity
<source.md>` folds it into the battery, `--expect-map` silences declared translation
deltas, and `--title-agreement` adds the summary-table and heading title check for
ID-keyed documents.

For skill maintenance, run `validate-skill.py`, `check-references.py`, and `check-contents.py`
first.

## Limitations

`format-table.py` and `validate-document.py` split table rows on every `|` character.

Escaped `\|` sequences and pipes inside inline code spans are not supported, so table cells must
not contain literal pipe characters - `validate-document.py` fails both forms on sight so
the miscount surfaces instead of passing silently.

`validate-document.py` skips fenced code blocks when checking tables - example tables inside
code fences, such as AsciiDoc samples, are payload, not Markdown tables.

Pass `--payload-markdown` to apply a curated subset of checks inside ` ```markdown ` blocks:

trailing whitespace, consecutive blank lines, lone list markers, and line width.

`diff-content.py` is a heuristic net, not a proof - its merged-line warnings require manual
review, and a clean report still does not replace reading the diff.

`check-parity.py` compares structure only - it cannot judge whether a target paragraph
translates its source faithfully, and its `--terms` hints flag missing preferred
variants, not wrong ones, so a hint can be a legitimate context form.

`split-sentences.py` detects boundaries heuristically - a capitalized word after a
period inside parentheses, such as `(np. Wartość)`, can be split wrongly - review its
diff before accepting, and prefer leaving a questionable line packed over splitting it
wrong.

`reflow-prose.py --unwrap` joins a line when the accumulated text does not end with
sentence-final punctuation, and treats a label line ending in `:` as a boundary - review
the joins on documents that mix several layouts.

`lint-polish.py` suppresses splice warnings inside conjunction-closed enumerations by
design - a genuinely spliced pair of clauses that happens to end with `i`, `oraz`,
`lub`, or `albo` can pass silently.

The leading-clause, participle, parenthesized-series, and identifier-token exemptions
can likewise hide a real splice - a comma joining two clauses under any of them stays
silent.

The all-uppercase calque exemption can hide a real calque inside a deliberately shouted
word - uppercase warnings deserve a manual glance when the document uses emphasis
capitals.

`lint-english.py` article and spaced-hyphen checks are heuristics by design - acronym
pronunciation is decided by a curated letter-by-letter set, and a code span standing in
as a placeholder can hide a genuine article error adjacent to it.

Its dialect census measures surface forms only - a variant inside a quoted citation
counts toward the minority, so deliberate quotes deserve a manual glance.

`check-consistency.py` treats a quoted name as a reference only under connector-word
context - a section named by bare quote without a connector stays unchecked, and a
Title-Case literal under a weak connector can read as an `UNRESOLVED` reference.

Its variant detection stays advisory.

Two names may be deliberately parallel even when one is not a heading,
and a drift that never leaves the heading set stays invisible by design.

Console output never fails on a legacy encoding - every script reconfigures `sys.stdout`
and `sys.stderr` with `errors="backslashreplace"` under its `__main__` guard, so characters
the console cannot encode print as `\uXXXX` escapes instead of raising.

Subprocess text output decodes as UTF-8 with an explicit error handler - `surrogateescape`
where byte fidelity matters, `replace` for display payloads.

The validators are mechanical checks, not judgment.

A passing validator does not prove that a document is well written or correct.

Use the prompts in `evals/evals.json` for behavioral regression checks.
