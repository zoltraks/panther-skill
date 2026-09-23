# Agent Instruction

## Purpose

> **Scope:** Conventions for documents an AI coding agent executes - preparation procedures,
> operational specifications, and instruction documents that also serve human readers
> **Key items:** dual audience, activation routing, decision menus, staged procedures,
> validation checklists, embedded templates

An agent instruction document tells an AI coding agent what to do.

It is written to be executed, not only read - it carries triggers, mandatory questions,
staged procedures, and a done-condition the agent must satisfy.

Many such documents serve two audiences: human readers who review or maintain the document,
and agents who execute it.

## When To Use

Use for preparation and bootstrap documents, agent-operational procedures, and self-contained
specifications that instruct an agent to set up, transform, or verify a project.

A document belongs to this type when it defines executable machinery - trigger phrases,
routing between procedures, decision menus, validation checklists, or embedded templates
the agent must instantiate.

**Templates**

- `templates/en/agent-instruction-template-en.md`
- `templates/pl/agent-instruction-template-pl.md`

## Audiences

Declare the audiences near the top when the document serves both humans and agents.

State what each audience uses the document for - for example the human reads it as a
reference, while the agent treats one named section as an executable instruction.

Write agent-facing parts as imperative, checkable instructions.

Write human-facing parts as explanations.

A rule that applies to both audiences is stated once and referenced, never restated in two
diverging forms.

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the governed domain or procedure (`# Repository Preparation`).
2. Purpose - what the document does and which audiences it serves.
3. Use cases or applicability - when the document applies, one line per scenario.
4. Activation and routing - the conditions that select each procedure.
5. Decision points - mandatory questions with literal wording, options, and defaults.
6. Procedures - one section per scenario, staged numbered steps.
7. Validation - the checklist the agent must pass before finishing.
8. Example content - embedded copy-ready templates when the document instructs file
   creation.

## Writing Rules

Give every decision question literal wording in quotes, an explicit option list, a
recommended default, and an escape hatch such as accepting all defaults.

Keep the document self-contained - the agent should not need external files to execute it.

When the document defines a governed set - canonical files, directories, rule owners, or
options - keep every enumeration of that set identical across tables, lists, menus,
checklists, and embedded examples.

Keep each rule in exactly one place - other sections reference the owning section instead of
repeating the rule.

Keep embedded templates consistent with the normative text they implement.

## Embedded Templates

A ` ```markdown ` fenced block that carries a complete document skeleton is a payload
region with its own conventions.

Preserve payload interiors on edit - reformat them only when the request covers them, see
`conventions/markdown-dialects.md`.

## Deltas From The Language Baseline

- The document may address an AI agent directly, rules phrased as commands are acceptable.
- Quoted decision wording and embedded ` ```markdown ` templates are payload regions -
  preserve them on edit.
- A document long enough to need navigation carries a Contents table.
- A version marker such as an HTML version comment is updated only when the request or the
  document's own versioning rule requires it.

## Section Names

- Purpose
- Audiences
- Use Cases
- Decision Points
- Procedures
- Validation
- Example Content
- Best Practices
- References

Polish section names for this document type are declared in `languages/pl.md`.
