# Software Engineering Glossary (Polish-English)

## Purpose

> **Scope:** Polish-English terminology for software engineering and the software
> development lifecycle
> **Key items:** domain signals, terminology table, context forms, calque traps,
> untranslated terms

Load this glossary for translate tasks on software and software-documentation subjects.

Apply it for Polish to English translate tasks, per `process/translate-document.md`.

## Domain Signals

Apply this glossary when:

- The request names a software, IT, or SDLC subject.
- The document type is technical, specification, README, contributing, changelog, agent
  instruction, format specification, or rules document for a software project.
- The document's terminology is dominated by code, API, build, deploy, test, or
  infrastructure vocabulary.

## Terminology

The dictionary maps recurring Polish terms to their preferred English forms.

Entries with `/` offer context-dependent forms - pick the form that fits the sentence.

| Polish                                    | English                        |
|-------------------------------------------|--------------------------------|
| aplikacja                                 | application                    |
| artefakt                                  | artifact                       |
| artefakt wynikowy / artefakt wdrożeniowy  | build artifact                 |
| backlog                                   | backlog                        |
| baza                                      | baseline                       |
| baza kodu                                 | codebase                       |
| bezpieczeństwo                            | security                       |
| biblioteka                                | library                        |
| błąd                                      | bug                            |
| ciągła integracja                         | continuous integration         |
| ciągłe dostarczanie                       | continuous delivery            |
| ciągłe wdrażanie                          | continuous deployment          |
| cykl wytwarzania oprogramowania           | software development lifecycle |
| dług techniczny                           | technical debt                 |
| dokumentacja                              | documentation                  |
| dostępność                                | availability                   |
| dziennik zmian                            | changelog                      |
| endpoint / punkt końcowy                  | endpoint                       |
| fork / rozwidlenie                        | fork                           |
| framework / szkielet                      | framework                      |
| funkcja                                   | feature                        |
| gałąź                                     | branch                         |
| historyjka użytkownika                    | user story                     |
| idempotentny                              | idempotent                     |
| infrastruktura                            | infrastructure                 |
| interesariusz                             | stakeholder                    |
| kandydat do wydania                       | release candidate              |
| konfiguracja                              | configuration                  |
| kontener                                  | container                      |
| kontrakt API                              | API contract                   |
| kreator                                   | wizard                         |
| kryteria akceptacji                       | acceptance criteria            |
| kryterium jakości / warunek jakości       | quality gate                   |
| licencja                                  | license                        |
| łańcuch narzędzi                          | toolchain                      |
| martwy kod                                | dead code                      |
| middleware / oprogramowanie pośredniczące | middleware                     |
| migracja                                  | migration                      |
| moduł                                     | module                         |
| monitorowanie                             | monitoring                     |
| nawigacja okruszkowa                      | breadcrumb                     |
| obciążenie robocze                        | workload                       |
| obserwowalność                            | observability                  |
| obsługa błędów                            | error handling                 |
| ograniczenie częstotliwości żądań         | rate limiting                  |
| pamięć podręczna                          | cache                          |
| panel                                     | dashboard                      |
| plik blokady zależności                   | lockfile                       |
| podatność                                 | vulnerability                  |
| podgląd                                   | preview                        |
| podpowiedź                                | tooltip                        |
| pokrycie testami                          | test coverage                  |
| poprawka pilna                            | hotfix                         |
| poświadczenia                             | credentials                    |
| powierzchnia ataku                        | attack surface                 |
| problem / zgłoszenie                      | issue                          |
| proces / proces CI / proces CI/CD         | pipeline / CI pipeline         |
| proces budowania                          | build                          |
| przegląd kodu                             | code review                    |
| przepływ danych                           | data flow                      |
| przepływ pracy / proces                   | workflow                       |
| przypadek użycia                          | use case                       |
| pull request                              | pull request                   |
| refaktoryzacja                            | refactoring                    |
| rejestr decyzji architektonicznych        | architecture decision record   |
| rejestrowanie zdarzeń / logowanie         | logging                        |
| repozytorium                              | repository                     |
| skalowalność                              | scalability                    |
| specyfikacja                              | specification                  |
| sprint                                    | sprint                         |
| szablon                                   | template                       |
| środowisko                                | environment                    |
| środowisko produkcyjne                    | production                     |
| środowisko przejściowe / staging          | staging                        |
| środowisko uruchomieniowe                 | runtime                        |
| tag / znacznik                            | tag                            |
| testowalność                              | testability                    |
| token dostępu                             | access token                   |
| utrzymywalność                            | maintainability                |
| wartość domyślna                          | default value                  |
| wątek                                     | thread                         |
| wdrażać / wdrożenie                       | deploy / deployment            |
| wersjonowanie                             | versioning                     |
| wkład / współpraca                        | contribution                   |
| właściciel                                | owner                          |
| współbieżność                             | concurrency                    |
| wycofanie / powrót do poprzedniej wersji  | rollback                       |
| wycofany / przestarzały                   | deprecated                     |
| wydanie                                   | release                        |
| wymaganie                                 | requirement                    |
| wytyczna                                  | guideline                      |
| wzorzec projektowy                        | design pattern                 |
| zależność                                 | dependency                     |
| zamrożenie wersji                         | version pinning                |
| zmiana niezgodna wstecz                   | breaking change                |
| zrzut ekranu                              | screenshot                     |

## Context Forms

Some Polish terms render differently to English by context - do not force one form
everywhere:

- `funkcja` renders `feature` in product documentation and `function` in code and API text.
- `błąd` renders `bug` for a tracked defect and `error` for runtime and message text.
- `problem` renders `issue` for a tracked item and `problem` in prose.
- `wydanie` renders `release` for a software version and `issue` for a published document.
- `środowisko` renders `environment` generally and `runtime` inside
  `środowisko uruchomieniowe`.
- `proces` renders `process` for automation and `pipeline` inside `proces CI`.
- `wydajność` renders `performance`, never `efficiency` in software text.
- `poprawka` renders `hotfix` for an urgent release and `fix` for a routine correction.

## Calque Traps

| Instead of          | Use                   |
|---------------------|-----------------------|
| interested persons  | stakeholders          |
| register of risks   | risk register         |
| user history        | user story            |
| code overview       | code review           |
| diary of changes    | changelog             |
| running environment | runtime environment   |
| final point         | endpoint              |
| demand              | requirement           |
| work flow           | workflow              |
| turn back           | rollback              |
| reparation          | fix / hotfix          |
| cover by tests      | test coverage         |
| personalization     | customization         |
| actualization       | update                |
| implement (wdrażać) | deploy                |
| programmer's note   | quick note / dev note |

## Untranslated

Polish loanwords and identifiers render back to their canonical English forms:

- `endpoint`, `commit`, `merge`, `pull request`, `lint`, `fork`, `framework`,
  `middleware`, `staging`, `backlog`, `sprint`, `roadmapa` renders `roadmap`,
  `due diligence`, `copyleft`, `SBOM`, `open source`
- Acronyms: `API`, `SDK`, `CLI`, `UI`, `URL`, `HTTP`, `JSON`, `YAML`, `XML`, `SQL`,
  `REST`, `IDE`, `CI/CD`, `ASCII`, `UTF-8`, `CRLF`, `npm`, `git`
- Product and technology names: `Docker`, `Kubernetes`, `Microsoft Fabric`, `Power BI`
