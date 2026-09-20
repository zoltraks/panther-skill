# Changelog Document

## Purpose

> **Scope:** Conventions for `CHANGELOG.md` files - version-grouped records of what changed in a
> project and why
> **Key items:** version sections, newest first, change categories, user-facing language

A changelog tells a reader what changed between versions.

It is written for the user of the project, not for the developer who made the change.

Typical shape: one section per released version, newest first, with a summary sentence and
change-kind bullets.

## When To Use

Use for `CHANGELOG.md` files and for release-notes sections inside other documents.

A project change-request register is a different document - use `types/register-log.md` for it.

**Templates**

- `templates/en/changelog-file-template-en.md`
- `templates/pl/changelog-file-template-pl.md`

The filename is `CHANGELOG.md` - a type-conventional name that overrides the lowercase naming
rule.

## Structure

1. H1 title - `# Changes` or `# Changelog`.
2. One H2 section per version, newest first (`## Version X.Y.Z`).
3. A one-sentence summary under each version heading.
4. Bullet items grouped by change kind: added, improved, fixed, removed.

Write bullets that describe the effect for the user, name the feature and say what changed and
why it matters.

## Deltas From The Language Baseline

- Keep each entry to one sentence where possible.
- Bold the feature or component name at the start of the bullet when the existing file does so.
- Keep versions in newest-first order and never edit a released version section except to fix an
  error, add new sections at the top.
- The version numbering scheme belongs to the project - read `VERSIONING.md` or the project
  guidelines before inventing a version number, and ask when the scheme is unclear.

## Section Names

- Changes
- Version
- Added
- Improved
- Fixed
- Removed

Polish section names for this document type are declared in `languages/pl.md`.
