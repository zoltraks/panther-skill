# Rules Document

## Purpose

> **Scope:** Conventions for documents that define rules - guidelines, standards, conventions,
> and workflow definitions other documents or agents must follow
> **Key items:** imperative voice, scope statement, correct/incorrect examples, sources of truth

A rules document instructs the reader.

It exists to be applied, not just read - every rule must be unambiguous and checkable.

Typical shape: a document made of short imperative rules grouped by topic, with paired
correct/incorrect examples - like this skill's own `STYLE.md`.

## When To Use

Use for coding standards, documentation guidelines, workflow rules, review checklists, and agent
instruction documents.

Templates: `templates/en/rules-document.md` and `templates/pl/rules-document.md`.

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the ruled domain (`# Markdown Text Style`, `# Project Guidelines`).
2. Purpose - what the rules apply to, who must follow them.
3. Sources of truth - which files are authoritative when several exist.
4. Rule sections - one H2 per topic, one H3 per subtopic.
5. Examples - `Correct` / `Incorrect` pairs in fenced `markdown` blocks.

## Writing Rules

Write rules as imperative sentences.

State the rule first, then the reason when the reason is not obvious.

Put qualifiers like "mandatory" or "do not repeat" in the section body, never in the heading.

One rule per sentence, one sentence per line.

Keep rules general - describe the principle, not a single instance.

## Examples

Illustrate non-obvious rules with paired examples:

````markdown
### Correct

```markdown
## Source Data Scope
```

### Incorrect

```markdown
## source data scope
```
````

Use the language-specific example headings: `Correct`/`Incorrect` in English,
`Poprawnie`/`Niepoprawnie` in Polish.

Show the smallest example that demonstrates the rule.

## Deltas From The Language Baseline

- The document may address an AI agent directly, rules phrased as commands are acceptable.
- A `Sources Of Truth` section near the top declares which files outrank this one on conflict.
- Rule sentences stay short even at the cost of elegance, a rule must be checkable mechanically
  where possible.

## Section Names

| English          | Polish              |
|------------------|---------------------|
| Purpose          | Przeznaczenie       |
| Sources Of Truth | Źródła prawdy       |
| Scope            | Zakres              |
| General Rules    | Zasady ogólne       |
| Exceptions       | Wyjątki             |
| Correct          | Poprawnie           |
| Incorrect        | Niepoprawnie        |
| Example Content  | Przykład zawartości |
| File Maintenance | Utrzymanie plików   |
| Verification     | Weryfikacja         |
