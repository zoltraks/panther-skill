# Daily Plan

## Purpose

> **Scope:** Conventions for single-day planning documents - the day's priorities, scheduled
> blocks, and notes kept or thrown away at day's end
> **Key items:** date-first title, top priorities, time blocks, carry-over

A daily plan organizes one working day.

It is a working artifact - written fast, consulted during the day, superseded tomorrow.

Typical shape: a dated title, a short priority list, an optional schedule, and a notes or
carry-over section.

## When To Use

Use for daily plans, day journals, and per-day checklists.

For recurring project planning use `types/management-plan.md`.

For formal meeting records use `types/meeting-minutes.md`.

**Templates**

- `templates/en/daily-plan-template-en.md`
- `templates/pl/daily-plan-template-pl.md`
- `templates/de/daily-plan-template-de.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title carrying the date - `# Daily Plan - 2026-10-07`.
2. Priorities - the one to three items that define a successful day.
3. Schedule - time-blocked entries when the day is planned hour by hour.
4. Tasks - the unscheduled work items, as a checklist.
5. Notes - observations captured during the day.
6. Carry Over - items deliberately moved to the next day's plan.

## Deltas From The Language Baseline

- Keep it operational - a plan that takes longer to write than to read fails its purpose.
- Task items use `- [ ]` checkboxes so the plan doubles as a tracking document.
- Priorities stay few - a daily plan with ten priorities has none.
- A carry-over item moves to the next day's plan by reference, not by duplication.

## Section Names

| Section              | Requirement |
|----------------------|-------------|
| Priorities           | recommended |
| Schedule             | optional    |
| Tasks                | recommended |
| Notes                | optional    |
| Carry Over           | optional    |
| Document Information | unusual     |
| Version History      | unusual     |
| Contents             | unusual     |

Section names for other languages are declared in the matching `languages/<code>.md` file.
