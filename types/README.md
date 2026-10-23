# Document Type Rules

## Purpose

> **Scope:** Index of the per-type rule files loaded during document creation
> **Key items:** type selection, deltas on the language baseline

Load the file matching the document type, it adds deltas on top of the language baseline:

- **`types/technical-document.md`** - Guides, architecture notes, API docs, reference material.
  The default type when nothing more specific matches.
- **`types/project-document.md`** - Project specifications and designs: version comment,
  document navigation, glossary, requirements tables, numbered-chapter variant.
- **`types/rules-document.md`** - Guidelines, standards, and workflow rules: imperative voice,
  sources of truth, Correct/Incorrect examples.
- **`types/agent-instruction.md`** - Documents an AI coding agent executes: dual audiences,
  activation routing, staged procedures, validation checklists, embedded templates.
- **`types/procedure-manual.md`** - Long procedural guides with a self-defined section
  vocabulary: operating modes, decision gates, role mappings, structure trees.
- **`types/engineering-standard.md`** - Coding standards by stack: precedence, intake, verification.
- **`types/format-specification.md`** - File format and protocol specifications: document
  information, version history, field tables, value enumerations.
- **`types/article-text.md`** - Prose documents, tutorials, course material: narrative paragraphs,
  dialect tolerance, media references.
- **`types/quick-note.md`** - Quick notes and drafts: minimal structure, informal lists.
- **`types/message-document.md`** - Announcements and memos: subject-first title, one clear ask.
- **`types/daily-plan.md`** - Single-day planning documents: date-first title, priorities,
  scheduled blocks, carry-over.
- **`types/readme-general.md`** - Repository and package READMEs, the default variant when no
  more specific type applies: entry-point structure, layout trees.
- **`types/readme-skill.md`** - Agent Skill repository READMEs: activation contract,
  agent-environment installation, example prompts.
- **`types/readme-application.md`** - Software product READMEs: install and download paths,
  features, technical stack, changelog pointer.
- **`types/readme-library.md`** - Package and library READMEs: install command, minimal usage
  example, API pointer.
- **`types/readme-cli.md`** - Command-line tool READMEs: commands/options tables, examples.
- **`types/readme-docs.md`** - Documentation-repo READMEs: document locations, rules pointer.
- **`types/readme-collection.md`** - Collection and monorepo READMEs: entry catalog, notices.
- **`types/changelog-file.md`** - Version-grouped change records: newest first, user-facing.
- **`types/contributing-file.md`** - `CONTRIBUTING.md` contributor guides: ways to
  contribute, issue reporting, development setup, pull-request rules, license.
- **`types/decision-record.md`** - Architecture decision records: status lifecycle, numbered
  filenames, immutable once accepted, supersede chain.
- **`types/proposal-document.md`** - RFC and design proposals: review states, alternatives,
  open questions.
- **`types/project-charter.md`** - Project charters and briefs: SMART objectives, scope
  boundaries, PM authority, sponsor approval block.
- **`types/change-request.md`** - Formal change requests to a governed baseline: request
  metadata, justification, impact assessment, approval block.
- **`types/register-log.md`** - Risk, issue, stakeholder, and similar registers: ID prefixes,
  status lifecycles, append-only entry tables.
- **`types/status-report.md`** - Periodic status and quality reports: RAG ratings, metrics.
- **`types/meeting-minutes.md`** - Meeting minutes and agendas: attendees, decisions, action items.
- **`types/management-plan.md`** - Management and subsidiary plans: methodology, cadence, roles.
- **`types/work-breakdown-structure.md`** - WBS and dictionaries: decimal outline, packages, RACI.
- **`types/summary-document.md`** - Summaries, briefs, abstracts: declared source,
  compression tiers, carried verdict.
- **`types/supplement-document.md`** - Supplements: continued ID sequences, extended matrices.
- **`types/yaml-document.md`** - YAML data files: indentation, quoting, comments, minimal edits.
