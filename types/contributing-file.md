# Contributing File

## Purpose

> **Scope:** Conventions for `CONTRIBUTING.md` - the root-level contributor guide in open
> source and collaborative projects
> **Key items:** welcome paragraph, ways to contribute, issue reporting, development setup,
> pull request rules, AI-assisted contributions, license note

A contributing file tells people how to participate in a project.

It exists to be followed - every instruction must be concrete enough for a first-time
contributor to act on.

Typical shape: a welcoming document at the repository root that explains how to report
issues, set up the project, and submit changes.

## When To Use

Use for `CONTRIBUTING.md` at a repository root in open source or collaborative projects.

For contribution sections inside a `README.md`, use the matching `readme-*` type instead.

**Templates**

- `templates/en/contributing-file-template-en.md`
- `templates/pl/contributing-file-template-pl.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - `Contributing to <Project>`.
2. Welcome paragraph - one or two sentences thanking the reader and stating the document's
   purpose.
3. `Ways To Contribute` - reporting bugs, requesting features, improving documentation,
   submitting code.
4. `Reporting Issues` - search first, one issue per problem, what to include.
5. `Development Setup` - clone, install, and check commands in fenced `bash` blocks.
6. `Pull Requests` - focused changes, commit conventions, tests, CI expectations.
7. `AI-Assisted Contributions` - the project's policy on AI-generated reports and code.
8. `License` - contributions are licensed under the project's license.
9. `Code Of Conduct` - pointer to the conduct document when the project has one.
10. `Getting Help` - the community channels for questions.

## Writing Rules

Address the contributor directly - second person and a welcoming tone are expected.

State rules as checkable instructions, one per sentence.

Link to deeper documentation - style guides, development guides, security policies - instead
of duplicating their content.

Put runnable commands in fenced `bash` blocks that a contributor can copy and run.

Keep the document focused on the contributor's path - maintainer-only internals belong
elsewhere.

## AI-Assisted Contributions

Cover AI use explicitly - contributors increasingly submit AI-generated issues, reports, and
code.

The section states the project's position and at minimum these rules:

- Disclose when a report or change was produced with AI assistance.
- Verify every AI-generated finding personally before reporting it - never paste raw AI
  output into an issue or pull request.
- The submitter must understand and own the submitted code - AI-assisted changes follow the
  same style, testing, documentation, and licensing requirements as any other contribution.

Adjust the strictness to the project - anything from a permissive disclosure rule to a full
ban is valid, as long as the document states it unambiguously.

## Deltas From The Language Baseline

- The document addresses the reader as "you" - second person is acceptable.
- Checklists for issue and pull request preparation may use `- [ ]` task items.
- Links to external community resources - chat, forums, wikis - are expected.
- The welcome paragraph may bend the one-sentence-per-paragraph rule into two sentences for
  warmth.

## Section Names

- Purpose
- Ways To Contribute
- Reporting Issues
- Development Setup
- Pull Requests
- AI-Assisted Contributions
- License
- Code Of Conduct
- Getting Help

Polish section names for this document type are declared in `languages/pl.md`.
