# Panther Tooling

## Purpose

> **Scope:** Document-production and skill-maintenance scripts
> **Key items:** encoding detection, scope signals, sentence splitting, prose wrapping and
> unwrapping, table formatting, comment alignment, document validation, content diffing,
> document census, skill validation, reference integrity, contents-table drift, self-update
> check

These scripts support deterministic production of documents and maintenance of Panther itself.

They do not modify documents beyond the specific task each tool performs.

## Tool Classes

### Document-Production Tools

Copy `detect-encoding.py`, `detect-scope.py`, `split-sentences.py`, `reflow-prose.py`,
`wrap-prose.py`, `format-table.py`, `align-comments.py`, `validate-document.py`,
`diff-content.py`, `census-document.py`, and `lint-polish.py` into the working
repository's `work/` directory under a `.tmp.` name before use.

When `lint-polish.py` is copied out of the skill repository it cannot auto-discover its
rule tables - pass them explicitly with `--rules <path>` pointing at the skill's
`languages/pl.md` and the matching glossary files.

If `work/` does not exist, use an existing `temp` or `temporary` directory.

When the project declares a temporary directory - for example `work/` in its guidelines or
`.gitignore` - that does not exist yet, create it for the copy rather than using the repository
root.

Use the repository root only when no declared or existing temporary directory applies.

Run the copied scripts only against the document being created, edited, or audited.

Remove every copied script after use.

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

The commands below use `python` - substitute `python3` when `python` is not on PATH.

```bash
python detect-encoding.tmp.py <file>
python detect-scope.tmp.py <directory>
python split-sentences.tmp.py <file.md> [--check] [--paragraphs] [--width N] [--payload-markdown]
python reflow-prose.tmp.py <file.md> (--wrap | --unwrap) [--check] [--width N] [--payload-markdown]
python wrap-prose.tmp.py <file.md> [--check] [--width N] [--payload-markdown]
python format-table.tmp.py <file.md> [--check] [--payload-markdown]
python align-comments.tmp.py <file.md> [--check] [--compact] [--payload-markdown]
python validate-document.tmp.py <file.md> [--width N] [--payload-markdown]
python diff-content.tmp.py <file.md> [--baseline <file>]
python census-document.tmp.py <file.md> [--width N] [--payload-markdown]
python lint-polish.tmp.py <file.md> [--rules <rulefile.md> ...]
python scripts/validate-skill.py .
python scripts/check-references.py .
python scripts/check-contents.py .
python scripts/check-update.py
```

`detect-encoding.py` and `detect-scope.py` always exit `0` and print a report.

`split-sentences.py` rewrites the file in place, `--check` only reports lines or blocks that pack
multiple sentences.

By default it emits each paragraph sentence starting on its own logical line and re-wraps the
affected sentences to `--width N`.

With `--paragraphs` it emits the house convention instead: every sentence becomes its own
paragraph, separated by one empty line, and sentences are never re-wrapped.

It leaves list items and their continuation lines opaque - a packed list item is an
element-level convention, not a defect (see `conventions/markdown-dialects.md`).

Lines ending in `:` are treated as label lines and never absorb following sentences.

Abbreviations such as `e.g.` and `etc.` and periods inside inline code spans do not count as
boundaries.

`reflow-prose.py` rewrites the file in place, `--check` only reports the lines the chosen
direction would change.

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

Both directions leave tables, fenced code blocks, indented code blocks, HTML comments, and
frontmatter untouched.

`wrap-prose.py` is deprecated, use `reflow-prose.py --wrap` instead.

It stays in `scripts/` for compatibility with documents that already reference it.

`--payload-markdown` extends `split-sentences.py`, `reflow-prose.py`, `wrap-prose.py`,
`format-table.py`, `align-comments.py`, and `validate-document.py` into ` ```markdown `
fenced blocks, all other fence languages stay opaque.

`align-comments.py` aligns trailing `#` comments inside untagged fenced blocks and
shell-tagged blocks to one shared column per block - the established column when most
comments already share one, otherwise the longest entry plus two spaces.

`--compact` moves the column to the minimum.

A block whose opening fence is preceded by `<!-- align-comments: off -->` - optionally with one
blank line between the marker and the fence - is skipped entirely, so the marker exempts
deliberate examples of misalignment from both fixing and `--check`.

The convention lives in `conventions/plain-text-comments.md`.

`diff-content.py` compares the normalized token stream of a document against `git show HEAD`
or a `--baseline` file, identical tokens mean a pass changed formatting only.

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

Flagged commas inside a series closed by a conjunction (`X, Y i Z`) count as an
enumeration and raise no spliced-clause warning - the heuristic stays silent on
conjunction-closed coordination, which is legal Polish.

A line opened by a subordinate or participial clause (`Gdy ...`, `Jeśli ...`,
`Odwołując ...`) has its first flaggable comma exempt - it closes the opener clause -
and a comma followed by an `-ąc`/`-wszy`/`-łszy` participle is an adverbial phrase,
not a splice.

It targets Polish deliverable documents - the skill's own rule files contain the
forbidden forms by definition and will report them.

The validators exit `0` when all checks pass and `1` when one or more checks fail.

`validate-document.py` warns on `text` and `txt` fence tags - plain-text blocks default to
untagged fences in new content, while an existing document may carry the tag as its own
convention.

## Validation Order

Run `detect-scope.py` on the target directory first when the task needs the document scope.

Run checks in this order:

1. Detect encoding before editing an existing file.
2. Check packed sentences with `split-sentences.py --check` when the request covers
   sentence separation.
3. Check the wrap convention with `reflow-prose.py --wrap --check` for fixed-width
   documents or `reflow-prose.py --unwrap --check` for logical-line documents, matching
   the detected convention.
4. Format edited tables with `format-table.py`.
5. Align comments in plain-text blocks with `align-comments.py` when the document contains
   them.
6. Validate the written document with `validate-document.py`.
7. Lint Polish output with `lint-polish.py`.
8. Verify formatting-only passes with `diff-content.py`.
9. Run `git diff --check` when inside a repository.
10. Remove temporary `.tmp.` copies from the working repository.

For skill maintenance, run `validate-skill.py`, `check-references.py`, and `check-contents.py`
first.

## Limitations

`format-table.py` and `validate-document.py` split table rows on every `|` character.

Escaped `\|` sequences and pipes inside inline code spans are not supported, so table cells must
not contain literal pipe characters.

`validate-document.py` skips fenced code blocks when checking tables - example tables inside
code fences, such as AsciiDoc samples, are payload, not Markdown tables.

Pass `--payload-markdown` to apply a curated subset of checks inside ` ```markdown ` blocks:

trailing whitespace, consecutive blank lines, lone list markers, and line width.

`diff-content.py` is a heuristic net, not a proof - its merged-line warnings require manual
review, and a clean report still does not replace reading the diff.

`split-sentences.py` detects boundaries heuristically - review its diff before accepting,
and prefer leaving a questionable line packed over splitting it wrong.

`reflow-prose.py --unwrap` joins a line when the accumulated text does not end with
sentence-final punctuation, and treats a label line ending in `:` as a boundary - review
the joins on documents that mix several layouts.

`lint-polish.py` suppresses splice warnings inside conjunction-closed enumerations by
design - a genuinely spliced pair of clauses that happens to end with `i`, `oraz`,
`lub`, or `albo` can pass silently.

The leading-clause exemption and the participle exemption can likewise hide a real
splice - a comma joining two clauses after an opener clause or before a participle
stays silent.

Console output never fails on a legacy encoding - every script reconfigures `sys.stdout`
and `sys.stderr` with `errors="backslashreplace"` under its `__main__` guard, so characters
the console cannot encode print as `\uXXXX` escapes instead of raising.

Subprocess text output decodes as UTF-8 with an explicit error handler - `surrogateescape`
where byte fidelity matters, `replace` for display payloads.

The validators are mechanical checks, not judgment.

A passing validator does not prove that a document is well written or correct.

Use the prompts in `evals/evals.json` for behavioral regression checks.
