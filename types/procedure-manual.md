# Procedure Manual

## Purpose

> **Scope:** Conventions for long procedural guides that define their own section
> vocabulary - preparation guides, operational runbooks, and multi-mode handbooks an
> agent or operator executes against a repository or environment
> **Key items:** open heading set, operating modes, decision gates, role-to-path
> mappings, structure trees, embedded templates, appendices

A procedure manual is a long procedural guide with a self-defined section vocabulary.

It describes how to evaluate, prepare, repair, supplement, or reorganize a target -
usually a repository, environment, or governed document set - through staged
operations, decision gates, and validation steps.

Unlike a generic `technical-document`, its headings are invented for the domain it
governs, so the type's section vocabulary is open: no heading is required or
unexpected.

## When To Use

Use for documents like preparation and governance guides, multi-operation runbooks,
environment-readiness procedures, and any manual that an agent or operator executes
in more than one mode or against more than one target shape.

A document belongs to this type when it defines its own section names instead of the
generic Purpose/Overview/Usage/Examples set, and when it carries procedural
machinery such as operating modes, decision gates, role mappings, or embedded
templates.

**Templates**

- `templates/en/procedure-manual-template-en.md`
- `templates/pl/procedure-manual-template-pl.md`
- `templates/de/procedure-manual-template-de.md`

## Audiences

Declare the audiences near the top when the document serves both humans and agents.

State which audience reads the document as reference and which executes it.

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the governed domain (`# Repository Preparation`).
2. Purpose - what the document does and which audiences it serves.
3. Contents - a table of contents, which long manuals always carry.
4. Operating modes - the named modes or operations the manual supports, with the
   trigger or selection rule for each.
5. Decision points - mandatory questions or approval gates with literal wording,
   options, and defaults.
6. Roles and locations - logical roles (documents, directories, artifacts) mapped to
   concrete paths or owners.
7. Procedures - one procedure per operation, staged numbered steps.
8. Validation - the checklist the operator must pass before finishing.
9. Appendices - examples, standards, and copy-ready templates.

## Writing Rules

Keep the manual self-contained - the operator should not need external files to
execute a procedure.

Give every decision gate literal wording in quotes, an explicit option list, a
recommended default, and an escape hatch such as accepting all defaults.

Define every logical role once and reference it by name everywhere else - the
role-to-path mapping is the single place names and locations meet.

Keep every enumeration of a governed set identical across tables, lists, menus,
checklists, and embedded examples.

Reference other sections by quoted heading name ("see \"Decision Points\"") and
keep those names resolving - `check-consistency.py` verifies them against the
document's own headings and `**Term**` definitions.

## Structure Trees

A manual that creates or inspects file structure shows the planned or observed
document tree as a fenced `text` block, limited to the structures the manual
governs.

Show existing, proposed, retained, moved, and retired paths distinctly, and mark
each node's logical role.

## Embedded Templates

A ` ```markdown ` fenced block that carries a complete document skeleton is a
payload region with its own conventions.

Preserve payload interiors on edit - reformat them only when the request covers
them, see `conventions/markdown-dialects.md`.

## Deltas From The Language Baseline

- Section names are open - the manual invents its headings, and `check-sections.py`
  treats every listed name as optional and every unlisted heading as informational.
- Operating modes may address the operator directly, and imperative phrasing is
  acceptable inside procedures.
- Quoted decision wording, structure trees, and embedded ` ```markdown ` templates
  are payload regions - preserve them on edit.
- `check-consistency.py` is part of the edit gate - quoted section references must
  resolve and managed terms must not drift.

## Section Names

| Section             | Requirement |
|---------------------|-------------|
| Purpose             | optional    |
| Audiences           | optional    |
| Operating Modes     | optional    |
| Decision Points     | optional    |
| Roles and Locations | optional    |
| Procedures          | optional    |
| Validation          | optional    |
| Examples            | optional    |
| Template Library    | optional    |
| Appendix            | optional    |

All section names are optional - the manual defines its own vocabulary, and
headings outside this table are informational notes, never failures.

Section names for other languages are declared in the matching
`languages/<code>.md` file.
