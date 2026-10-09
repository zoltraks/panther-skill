# Engineering Standard

## Purpose

> **Scope:** Conventions for coding standards consumed by AI coding agents - per-language,
> per-framework, and cross-cutting documents that stack into a project's governing rules
> **Key items:** version comment, scope, precedence table, agent intake protocol, executable
> verification table, definition of done, self-contained layers

An engineering standard states the rules a codebase follows for one technology stack or
concern.

It is written for two audiences: humans who review the rules, and AI coding agents that
apply them during code generation.

Standards stack in layers: a general language standard applies first, a category standard
extends or overrides it for a framework or purpose, and project rules outrank both.

## When To Use

Use for language, framework, or cross-cutting standards that must stay portable across
projects and composable in layers.

A document belongs to this type when it names a stack or concern in its title, pins
toolchain versions, and ends with checks an agent can run.

**Templates**

- `templates/en/engineering-standard-template-en.md`
- `templates/pl/engineering-standard-template-pl.md`
- `templates/de/engineering-standard-template-de.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the stack and layer (`# Python Web Engineering Standard`).
2. Version comment - an HTML comment directly under the H1 carrying version and date.
3. Purpose - which stack and artifacts the standard governs.
4. Scope - what the rules apply to and what stays out.
5. How To Use This Standard - order of operations, precedence table, non-negotiable rules.
6. Agent Intake Protocol - what the agent detects before applying rules.
7. Documentation - the authoritative references the standard defers to.
8. Language Version - pinned runtime and toolchain versions.
9. Project Structure - required layout and file placement.
10. Naming Conventions.
11. Code Conventions - required constructs and forbidden patterns.
12. Formatting and Linting - tool setup and enforced gates.
13. Testing - framework, placement, and coverage floor.
14. Build - build and packaging commands.
15. Dependencies - version policy and audit requirements.
16. Verification - executable check table.
17. Definition of Done - the gates a change must pass.
18. General Principles - the ideas the detailed rules implement.
19. Sources - authoritative external links.

## Layering

Name files after the stack and layer, for example `python-general-development.md` for the
base layer and `python-web-development.md` for the category layer.

Keep every standard self-contained - usable on its own after being copied into a project.

Never name or link another standard file inside a standard.

Refer to other layers by role, such as the language standard or the project rules.

A category standard assumes the general layer for the same stack already applies and states
only its deltas.

Record the stacking in a precedence table - wider rules first, narrower rules override.

## Writing Rules

Write rules as imperative, checkable sentences - the agent must be able to obey or violate
each one.

Keep each rule in exactly one place.

Pin toolchain and runtime versions to concrete releases.

Phrase divergences found in an existing project as defects to fix, never as style choices
to tolerate.

## Verification Table

End the standard with a verification table of commands the agent can run.

One row per check - a short name, the literal command, and what it proves.

Commands must be copy-paste runnable in the target environment.

## Definition Of Done

Close with the gates a change must pass before it counts as done - correctness, structure,
quality, and hygiene - written as checkable statements.

## Deltas From The Language Baseline

- The version comment is required directly under the H1 and is bumped on every change.
- Imperative rules addressed to an executing agent are the norm, as in
  `types/agent-instruction.md`.
- Verification commands and URLs may exceed the prose wrap width - never break them.
- A Contents table appears only when the document grows long enough to need one.

## Section Names

| Section                  | Requirement |
|--------------------------|-------------|
| Purpose                  | required    |
| Scope                    | required    |
| How To Use This Standard | recommended |
| Order Of Operations      | recommended |
| Precedence               | recommended |
| Non-Negotiable Rules     | recommended |
| Agent Intake Protocol    | recommended |
| Detection First          | optional    |
| Existing Project         | optional    |
| New Project              | optional    |
| Documentation            | recommended |
| Language Version         | recommended |
| Core Technologies        | optional    |
| Project Structure        | recommended |
| Naming Conventions       | recommended |
| Code Conventions         | recommended |
| Formatting and Linting   | recommended |
| Testing                  | recommended |
| Build                    | recommended |
| Dependencies             | recommended |
| Security                 | optional    |
| Observability            | optional    |
| Logging                  | optional    |
| Comments                 | optional    |
| Error Handling           | optional    |
| Verification             | required    |
| Definition of Done       | required    |
| Correctness              | optional    |
| Structure                | optional    |
| Quality                  | optional    |
| Hygiene                  | optional    |
| General Principles       | recommended |
| Sources                  | required    |

Section names for other languages are declared in the matching `languages/<code>.md` file.
