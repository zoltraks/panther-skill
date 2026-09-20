# Project Charter

## Purpose

> **Scope:** Project charters and project briefs - the formal documents that authorize a project
> and empower its manager.
>
> **Key items:** SMART objectives, scope boundaries, milestone summary, project-manager
> authority, sponsor approval block.

## When To Use

Use for authorizing documents - a project charter or a project brief. In Polish
projects the charter is `karta projektu`.

Distinguish from `types/proposal-document.md`: the business case argues for
approval before it happens, the charter authorizes the project after it and
empowers the project manager.

**Templates:**

- `templates/en/project-charter-template-en.md`
- `templates/pl/project-charter-template-pl.md`

## Structure

1. H1 title carrying the project name - `# <Project> Charter`, Polish `# Karta projektu <Nazwa>`.
2. Version comment per the project-document convention.
3. Project information block - sponsor, project manager, charter date.
4. Purpose and Justification - why the project exists and what it addresses.
5. Measurable Objectives and Success Criteria - a SMART table with Objective,
   Metric, and Target columns.
6. High-Level Requirements - the project's scope-defining requirements, not
   detail-level specifications.
7. Scope Boundaries - what is in scope and what is explicitly out of scope.
8. Deliverables and Milestones - a summary table of milestones with target
   dates.
9. High-Level Budget - the authorized budget figure or range.
10. Key Stakeholders - sponsor, project manager, team leads, and other key
    parties.
11. Project Manager Role and Authority - what the PM may decide and approve.
12. Assumptions and Constraints - the founding assumptions, each with a source.
13. High-Level Risks - the top risks, pointing to the risk register for the
    maintained list.
14. Exit Criteria - what conditions end the project.
15. Approval - the sponsor sign-off block with name, role, and date.

## Deltas From The Language Baseline

- The charter stays short - one to five pages. Detail lives in plans and
  registers, the charter holds commitments.
- Objectives are SMART - each row carries a metric and a measurable target.
- The project brief is the short variant - objectives, scope summary, timeline,
  budget estimate, and key stakeholders on one page.
- After approval the charter changes only through change control. Update the
  version comment on every approved change, never silently rewrite approved
  sections.
- Reference registers for the maintained lists - the charter names the top
  risks, the risk register tracks them.
- Placement - conventionally `docs/CHARTER.md` uppercase in guided projects or
  where the request names it.

## Section Names

| English                            | Polish                                 |
|------------------------------------|----------------------------------------|
| Purpose and Justification          | Uzasadnienie                           |
| Measurable Objectives              | Mierzalne cele                         |
| Success Criteria                   | Kryteria sukcesu                       |
| High-Level Requirements            | Wymagania ogólne                       |
| Scope Boundaries                   | Granice zakresu                        |
| In Scope                           | W zakresie                             |
| Out of Scope                       | Poza zakresem                          |
| Deliverables                       | Rezultaty                              |
| Milestones                         | Kamienie milowe                        |
| High-Level Budget                  | Budżet                                 |
| Key Stakeholders                   | Kluczowi interesariusze                |
| Project Manager Role and Authority | Rola i uprawnienia kierownika projektu |
| Assumptions and Constraints        | Założenia i ograniczenia               |
| High-Level Risks                   | Ryzyka ogólne                          |
| Exit Criteria                      | Kryteria zakończenia                   |
| Approval                           | Zatwierdzenie                          |
