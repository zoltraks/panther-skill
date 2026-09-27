# Software Engineering Glossary (English-Polish)

## Purpose

> **Scope:** English-Polish terminology for software engineering and the software
> development lifecycle
> **Key items:** domain signals, terminology table, context forms, calque traps,
> untranslated terms

Load this glossary for translate tasks on software and software-documentation subjects.

Apply it for English to Polish translate tasks, per `process/translate-document.md`.

## Domain Signals

Apply this glossary when:

- The request names a software, IT, or SDLC subject.
- The document type is technical, specification, README, contributing, changelog, agent
  instruction, format specification, or rules document for a software project.
- The document's terminology is dominated by code, API, build, deploy, test, or
  infrastructure vocabulary.

## Terminology

The dictionary maps recurring English terms to their preferred Polish forms.

Entries with `/` offer context-dependent forms - pick the form that fits the sentence.

| English                        | Polish                                    |
|--------------------------------|-------------------------------------------|
| acceptance criteria            | kryteria akceptacji                       |
| access token                   | token dostępu                             |
| API contract                   | kontrakt API                              |
| application                    | aplikacja                                 |
| architecture decision record   | rejestr decyzji architektonicznych        |
| artifact                       | artefakt                                  |
| attack surface                 | powierzchnia ataku                        |
| availability                   | dostępność                                |
| backlog                        | backlog                                   |
| baseline                       | baza                                      |
| branch                         | gałąź                                     |
| breadcrumb                     | nawigacja okruszkowa                      |
| breaking change                | zmiana niezgodna wstecz                   |
| bug                            | błąd                                      |
| build                          | proces budowania                          |
| build artifact                 | artefakt wynikowy / artefakt wdrożeniowy  |
| cache                          | pamięć podręczna                          |
| changelog                      | dziennik zmian                            |
| code review                    | przegląd kodu                             |
| codebase                       | baza kodu                                 |
| concurrency                    | współbieżność                             |
| configuration                  | konfiguracja                              |
| container                      | kontener                                  |
| continuous delivery            | ciągłe dostarczanie                       |
| continuous deployment          | ciągłe wdrażanie                          |
| continuous integration         | ciągła integracja                         |
| contribution                   | wkład / współpraca                        |
| credentials                    | poświadczenia                             |
| dashboard                      | panel                                     |
| data flow                      | przepływ danych                           |
| dead code                      | martwy kod                                |
| default value                  | wartość domyślna                          |
| dependency                     | zależność                                 |
| deploy / deployment            | wdrażać / wdrożenie                       |
| deprecated                     | wycofany / przestarzały                   |
| design pattern                 | wzorzec projektowy                        |
| documentation                  | dokumentacja                              |
| endpoint                       | endpoint / punkt końcowy                  |
| environment                    | środowisko                                |
| error handling                 | obsługa błędów                            |
| feature                        | funkcja                                   |
| fork                           | fork / rozwidlenie                        |
| framework                      | framework / szkielet                      |
| guideline                      | wytyczna                                  |
| hotfix                         | poprawka pilna                            |
| idempotent                     | idempotentny                              |
| infrastructure                 | infrastruktura                            |
| issue                          | problem / zgłoszenie                      |
| library                        | biblioteka                                |
| license                        | licencja                                  |
| lockfile                       | plik blokady zależności                   |
| logging                        | rejestrowanie zdarzeń / logowanie         |
| maintainability                | utrzymywalność                            |
| middleware                     | middleware / oprogramowanie pośredniczące |
| migration                      | migracja                                  |
| module                         | moduł                                     |
| monitoring                     | monitorowanie                             |
| observability                  | obserwowalność                            |
| owner                          | właściciel                                |
| pipeline / CI pipeline         | proces / proces CI / proces CI/CD         |
| preview                        | podgląd                                   |
| production                     | środowisko produkcyjne                    |
| pull request                   | pull request                              |
| quality gate                   | kryterium jakości / warunek jakości       |
| rate limiting                  | ograniczenie częstotliwości żądań         |
| refactoring                    | refaktoryzacja                            |
| release                        | wydanie                                   |
| release candidate              | kandydat do wydania                       |
| repository                     | repozytorium                              |
| requirement                    | wymaganie                                 |
| rollback                       | wycofanie / powrót do poprzedniej wersji  |
| runtime                        | środowisko uruchomieniowe                 |
| scalability                    | skalowalność                              |
| screenshot                     | zrzut ekranu                              |
| security                       | bezpieczeństwo                            |
| software development lifecycle | cykl wytwarzania oprogramowania           |
| specification                  | specyfikacja                              |
| sprint                         | sprint                                    |
| staging                        | środowisko przejściowe / staging          |
| stakeholder                    | interesariusz                             |
| tag                            | tag / znacznik                            |
| technical debt                 | dług techniczny                           |
| template                       | szablon                                   |
| test coverage                  | pokrycie testami                          |
| testability                    | testowalność                              |
| thread                         | wątek                                     |
| toolchain                      | łańcuch narzędzi                          |
| tooltip                        | podpowiedź                                |
| use case                       | przypadek użycia                          |
| user story                     | historyjka użytkownika                    |
| version pinning                | zamrożenie wersji                         |
| versioning                     | wersjonowanie                             |
| vulnerability                  | podatność                                 |
| wizard                         | kreator                                   |
| workflow                       | przepływ pracy / proces                   |
| workload                       | obciążenie robocze                        |

## Context Forms

Some English terms render differently by context - do not force one form everywhere:

- `weakness` renders `błąd bezpieczeństwa` or `podatność bezpieczeństwa` in security text.
- `drift` renders `rozbieżność` for configuration and `dezaktualizacja` for documentation.
- `gate` renders `warunek` or `kontrola`, never `brama`.
- `workflow` renders `przepływ pracy` for user processes and `proces` for automation.
- `fallback` renders `mechanizm awaryjny` or `obsługa zastępcza`.
- `fail-closed` renders `odmowa dostępu` or `zamknięcie w przypadku błędu`.
- `deploy` compounds translate in full - `środowisko wdrożeniowe`, `zadanie wdrożeniowe`.

## Calque Traps

| Instead of        | Use                                   |
|-------------------|---------------------------------------|
| deployować        | wdrażać                               |
| requestować       | zgłaszać                              |
| update'ować       | aktualizować                          |
| fixować           | poprawiać                             |
| kastomizacja      | dostosowanie                          |
| performance       | wydajność                             |
| paczka            | pakiet                                |
| potok             | proces / proces CI                    |
| triaż podatności  | weryfikacja i klasyfikacja podatności |
| joiny             | łączenia                              |
| lookupy           | wyszukiwania                          |
| brama             | warunek / kontrola                    |
| bramy weryfikacji | warunki weryfikacyjne                 |
| rozjazd           | rozbieżność                           |
| dryf dokumentacji | dezaktualizacja dokumentacji          |
| designer wizualny | projektowanie wizualne                |
| stakeholderzy     | interesariusze                        |
| ownerzy biznesowi | właściciele biznesowi                 |
| status report     | raport o statusie                     |
| meeting minutes   | protokół zebrania                     |
| dane skrapane     | dane skrapowane                       |

## Untranslated

Settled loanwords and identifiers stay in English form in Polish output:

- `endpoint`, `frontend`, `backend`, `commit`, `merge`, `pull request`, `lint`,
  `roadmapa`, `due diligence`, `copyleft`, `SBOM`, `open source`
- Acronyms: `API`, `SDK`, `CLI`, `UI`, `URL`, `HTTP`, `JSON`, `YAML`, `XML`, `SQL`,
  `REST`, `IDE`, `CI/CD`, `ASCII`, `UTF-8`, `CRLF`, `npm`, `git`
- Product and technology names: `Docker`, `Kubernetes`, `Microsoft Fabric`, `Power BI`
