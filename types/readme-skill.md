# Skill Repository README

## Purpose

> **Scope:** Conventions for the `README.md` of an Agent Skill repository - a directory
> containing a `SKILL.md` router and bundled resource files
> **Key items:** activation contract, agent-environment installation, example prompts,
> directory tree

| Out of scope                    | See instead                   |
|---------------------------------|-------------------------------|
| General repository README       | `types/readme-general.md`     |
| Software product README         | `types/readme-application.md` |
| Package and library README      | `types/readme-library.md`     |
| Command-line tool README        | `types/readme-cli.md`         |
| Documentation repository README | `types/readme-docs.md`        |
| Collection and monorepo README  | `types/readme-collection.md`  |

A skill repository README is both a human document and a sales pitch for the skill.

It tells a reader what the skill does, shows the prompts that activate it, and gives the exact
paths where an agent loads it.

## When To Use

Use for the root `README.md` of a repository that ships an Agent Skill - one or more `SKILL.md`
routers with their resource files - like this skill's own `README.md`.

For a repository that collects several independent skills as a catalog, prefer
`types/readme-collection.md` instead.

**Templates**

- `templates/en/readme-skill-template-en.md`
- `templates/pl/readme-skill-template-pl.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the skill name, optionally with a short tag line.
2. Purpose - a paragraph or blockquote stating what the skill does.
3. Contents - table of sections for long READMEs.
4. Overview - what the skill is and what it produces.
5. What The Skill Does - a capability walkthrough in feature order.
6. Installation - how to add the skill to an agent environment.
7. Usage - how agents activate the skill and what happens next.
8. Example Prompts - a list of real trigger phrases as blockquotes.
9. What's Inside - a directory tree of the skill's resource files.
10. Verification - the skill's own maintenance checks when they exist.
11. License and credits.

## Deltas From The Language Baseline

- The Installation section names the concrete skills directory per agent environment, for
  example `.devin/skills/`, `.claude/skills/`, or `.agents/skills/`, plus a global or personal
  install path and a `git clone` command when the skill ships as a repository.
- Example Prompts list real requests as blockquoted phrases - they double as activation
  examples and must stay in sync with the `SKILL.md` trigger phrases.
- The What's Inside tree lists the skill's own resource directories - keep it in sync with the
  actual layout.
- A Verification section documents the skill's maintenance commands when the skill defines
  them, for example its own validators.
- Keep the README honest about activation: describe what the skill does when triggered, not
  aspirational behavior.

## Section Names

- Contents
- Overview
- What The Skill Does
- Installation
- Agent Environments
- Usage
- Example Prompts
- What's Inside
- Verification
- License
- Credits

Polish section names for this document type are declared in `languages/pl.md`.
