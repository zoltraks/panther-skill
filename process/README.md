# Process Files

## Purpose

> **Scope:** Index of the procedures under `process/` and the per-operation behavior summary
> **Key items:** load triggers, workflow, standalone procedures, operations summary

Load a procedure only when the task reaches it - progressive disclosure stays lazy,
nothing here is bulk-read.

## Operations Summary

On request it discovers a location's document layout - signals, best-matching scope,
exceptions - and audits a document against its governing rules with an optional fix plan.

On describe or summarize requests it produces consolidated inline descriptions - impersonal,
compact, with "shortly" caps and a hundred-sentence floor.

On derivation requests it produces documents derived from an existing one - summaries and briefs at
declared compression tiers, supplements continuing the source's numbering.

On translate requests it renders into the target language in one pass with the pair's style
adaptation and glossaries - structure, code, and identifiers preserved,
every adaptation delta reported.

On translation-audit requests it maps a rendered document against its source - structure map,
untranslated set, terminology concordance - then reports a fidelity verdict.

On translation-revision requests it corrects an existing translation - aligning findings with source
passages and applying minimal-diff fixes and same-class sweeps.

On correction requests it repairs the document in place - formatting, structure, grammar,
and typos - and surfaces fidelity findings as proposals on translation targets.

On "work on panther-skill" requests it presents the maintenance menu - document work,
skill adjustment, or session review - then reads the governing set and applies
`docs/MAINTENANCE.md`.

On bare activation it enables for editorial support: the update check runs,
and the answer describes the skill, names its version, and shows the operations table.

## Index

| File                         | Load when                                                      |
|------------------------------|----------------------------------------------------------------|
| `document-workflow.md`       | Every document task - intake, parameters, plan, draft, deliver |
| `document-checklist.md`      | The mechanical pre-delivery checklist                          |
| `decision-modes.md`          | Any operation run - the interaction-mode matrix                |
| `parameter-configuration.md` | Creation parameter surfaces, defaults, question shapes         |
| `scope-discovery.md`         | Discover or detect a location's document layout                |
| `document-audit.md`          | Audit a document against its governing rules                   |
| `correct-document.md`        | Correct, fix, or proofread a document                          |
| `humanize-document.md`       | Humanize or rewrite a document's voice, facts preserved        |
| `describe-response.md`       | Describe or summarize inline                                   |
| `derived-documents.md`       | Derive a summary, brief, or supplement from a source           |
| `translate-document.md`      | Translate a document                                           |
| `translation-audit.md`       | Audit, verify, or compare a translation against its source     |
| `translation-revision.md`    | Correct an existing translation or apply review findings       |
| `json-exchange.md`           | JSON parameter requests or diagnostic surfaces                 |
| `operation-timing.md`        | Timing under the four mode keywords                            |
| `operations-catalog.md`      | "List all operations" requests                                 |
| `skill-activation.md`        | Bare activation - the request names the skill but no task      |
| `skill-maintenance.md`       | The request targets this repository's own files                |
| `session-review.md`          | "Improve the skill from this session" requests                 |
| `parallel-execution.md`      | Large work surfaces split across delegated scouts              |
| `housekeeping.md`            | Self-repository upkeep: registration, coverage, validation     |
| `self-healing.md`            | The evidence-gated self-repair loop for this skill             |
| `development.md`             | Standby-for-specification development mode                     |
