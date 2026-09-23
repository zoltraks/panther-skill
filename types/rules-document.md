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

When the document carries executable machinery - trigger routing, decision menus, staged
procedures, validation checklists, or embedded templates - it follows the `agent-instruction`
type instead.

**Templates**

- `templates/en/rules-document-template-en.md`
- `templates/pl/rules-document-template-pl.md`

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

## Audiences

A rules document may address human readers, AI agents, or both.

When it serves both, the purpose section declares the audiences and what each uses the
document for.

Agent-facing rules stay imperative and mechanically checkable where possible.

A rule that applies to both audiences is stated once and referenced, never restated in two
diverging forms.

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
the equivalents declared in `languages/pl.md` for other languages.

Show the smallest example that demonstrates the rule.

## Deltas From The Language Baseline

- The document may address an AI agent directly, rules phrased as commands are acceptable -
  see `## Audiences`.
- A `Sources Of Truth` section near the top declares which files outrank this one on conflict.
- Rule sentences stay short even at the cost of elegance, a rule must be checkable mechanically
  where possible.

## Section Names

- Purpose
- Sources Of Truth
- Scope
- General Rules
- Exceptions
- Correct
- Incorrect
- Example Content
- File Maintenance
- Verification

Polish section names for this document type are declared in `languages/pl.md`.
