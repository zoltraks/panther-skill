# Status Report

## Purpose

> **Scope:** Periodic project health reports that compare the project to its
> baselines.
>
> **Key items:** RAG ratings, variance metrics, decisions needed, fixed
> structure, period identification.

## When To Use

Use for the PMBOK report family - status, variance, forecasting, and quality
reports on a weekly, biweekly, or monthly cadence.

**Templates:**

- `templates/en/status-report-template-en.md`
- `templates/pl/status-report-template-pl.md`

## Structure

1. H1 title identifying the period - `# Status Report - 2026-09-20` or a week
   or sprint number.
2. Reporting period block - project name, period covered, author.
3. Overall Status - the RAG rating with a one-line explanation.
4. Status by Area - a table rating Schedule, Budget, Scope, and Risk.
5. Summary - a short executive paragraph.
6. Accomplishments - three to five bullets.
7. Milestones - a table with completed, on track, and delayed states.
8. Budget and Metrics - approved, spent, forecast, and variance figures in a
   table.
9. Top Risks and Issues - one line each, referencing the register IDs.
10. Planned Next Period - the work scheduled for the next report.
11. Decisions Needed - each decision as a question with a deadline and the
    consequence of delay.

## Deltas From The Language Baseline

- The structure stays fixed across periods. Readers compare reports, so
  sections keep their names and order.
- Newest period first when one file aggregates several reports, one file per
  period otherwise - `docs/report/<date>/` in guided projects.
- Define the RAG legend once per project and reference it. Do not re-explain
  the colors in every report.
- Reference register IDs instead of restating entries - `R-03`, `I-12`.
- Keep every section short. The audience is executive.
- RAG values as fixed words - `Green`, `Amber`, `Red` - matching the project's
  existing reports.

## Section Names

| English              | Polish                          |
|----------------------|---------------------------------|
| Reporting Period     | Okres raportowania              |
| Overall Status       | Status ogólny                   |
| Status by Area       | Status według obszaru           |
| Schedule             | Harmonogram                     |
| Budget               | Budżet                          |
| Scope                | Zakres                          |
| Risk                 | Ryzyko                          |
| Summary              | Podsumowanie                    |
| Accomplishments      | Osiągnięcia                     |
| Milestones           | Kamienie milowe                 |
| Metrics              | Mierniki                        |
| Top Risks and Issues | Najważniejsze ryzyka i problemy |
| Planned Next Period  | Plan na kolejny okres           |
| Decisions Needed     | Wymagane decyzje                |
