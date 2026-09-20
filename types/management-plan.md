# Management Plan

## Purpose

> **Scope:** Documents describing how one project domain will be managed - the
> PMBOK plan family.
>
> **Key items:** Methodology, roles, thresholds and tolerances, cadence, tools,
> master plan integration.

## When To Use

Use for the project management plan and its subsidiary plans:

- scope, requirements, schedule, and cost management plans
- quality, resource, and communications management plans
- risk and procurement management plans
- stakeholder engagement and change management plans

An implementation plan that describes how to build a feature is a
`types/technical-document.md`. A management plan describes how a project domain
is governed - that is this type.

**Templates:**

- `templates/en/management-plan-template-en.md`
- `templates/pl/management-plan-template-pl.md`

## Structure

1. H1 title naming the domain - `# Risk Management Plan`, Polish `# Plan
   zarządzania ryzykiem`.
2. Version comment per the project-document convention.
3. Purpose - the domain covered and the relationship to the master plan.
4. Methodology and Approach - how the domain is managed.
5. Roles and Responsibilities - who does what, with a RACI table when several
   parties share the work.
6. Thresholds and Tolerances - the variance that triggers action.
7. Cadence and Process - review frequency, update process, change control.
8. Tools - what the project uses for this domain.
9. Reporting - what gets reported, to whom, and where it is recorded.
10. Related Plans and Registers - pointers to the documents this plan feeds.

## Deltas From The Language Baseline

- The imperative voice matches `types/rules-document.md`, but the plan shape
  adds thresholds, cadences, and named roles.
- Reference registers, never duplicate their entries - the risk management
  plan points at the risk register, it does not contain it.
- Subsidiary plans may live as sections of one master plan. Follow the
  document's existing structure.
- Update the version comment on every change.
- Placement - conventionally `docs/plan/` for subsidiary plans or an uppercase
  `docs/PLAN.md` master plan in guided projects.

## Section Names

| English                    | Polish                   |
|----------------------------|--------------------------|
| Methodology                | Metodyka                 |
| Roles and Responsibilities | Role i odpowiedzialności |
| Thresholds and Tolerances  | Progi i tolerancje       |
| Cadence                    | Częstotliwość przeglądów |
| Process                    | Proces                   |
| Tools                      | Narzędzia                |
| Reporting                  | Raportowanie             |
| Related Plans              | Plany powiązane          |
| Related Registers          | Powiązane rejestry       |
| Change Control             | Kontrola zmian           |
| Master Plan                | Plan główny              |
