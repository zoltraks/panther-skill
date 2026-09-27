# Medical Glossary (Polish-English)

## Purpose

> **Scope:** Polish-English terminology for medical, clinical, and pharmaceutical
> documents
> **Key items:** domain signals, terminology table, context forms, calque traps,
> untranslated terms

Load this glossary for translate tasks on medical and pharmaceutical subjects.

Apply it for Polish to English translate tasks, per `process/translate-document.md`.

## Domain Signals

Apply this glossary when:

- The request names a medical, clinical, pharma, or healthcare subject.
- The document covers trials, products, dosages, patients, or regulatory submissions.
- The document's terminology is dominated by product, dosage, safety, or study
  vocabulary.

## Terminology

The dictionary maps recurring Polish terms to their preferred English forms.

Entries with `/` offer context-dependent forms - pick the form that fits the sentence.

| Polish                               | English                 |
|--------------------------------------|-------------------------|
| badacz                               | investigator            |
| badanie                              | study                   |
| badanie kliniczne                    | clinical trial          |
| bezpieczeństwo                       | safety                  |
| ciężkie zdarzenie niepożądane        | serious adverse event   |
| dawka                                | dose                    |
| dawkowanie                           | dosage                  |
| działanie niepożądane                | side effect             |
| główny punkt końcowy                 | primary endpoint        |
| jakość życia                         | quality of life         |
| kohorta / grupa                      | cohort                  |
| komisja bioetyczna                   | ethics committee        |
| leczenie                             | treatment               |
| lek bez recepty                      | over-the-counter drug   |
| lek generyczny                       | generic drug            |
| lek towarzyszący                     | concomitant medication  |
| monitorowanie                        | monitoring              |
| nadzór nad bezpieczeństwem leków     | pharmacovigilance       |
| niepożądane działanie leku           | adverse drug reaction   |
| odstawienie / wycofanie              | withdrawal              |
| pacjent                              | patient                 |
| placebo                              | placebo                 |
| pozwolenie na dopuszczenie do obrotu | marketing authorization |
| produkt leczniczy                    | medicinal product       |
| protokół                             | protocol                |
| przeciwwskazanie                     | contraindication        |
| przeżycie                            | survival                |
| punkt końcowy                        | endpoint                |
| randomizacja                         | randomization           |
| recepta                              | prescription            |
| rozpowszechnienie                    | prevalence              |
| rozpoznanie                          | diagnosis               |
| seria                                | batch                   |
| skuteczność                          | efficacy                |
| sponsor                              | sponsor                 |
| substancja czynna                    | active substance        |
| substancja pomocnicza                | excipient               |
| śmiertelność                         | mortality               |
| świadoma zgoda                       | informed consent        |
| terapia / leczenie                   | therapy                 |
| termin ważności                      | expiry date             |
| tolerancja / znoszenie               | tolerability            |
| uczestnik badania                    | subject                 |
| ulotka                               | leaflet                 |
| ulotka dołączona do opakowania       | package leaflet         |
| warunki przechowywania               | storage conditions      |
| wskazanie                            | indication              |
| zachorowalność                       | morbidity               |
| zapadalność                          | incidence               |
| zdarzenie niepożądane                | adverse event           |

## Context Forms

Some Polish terms render differently to English by context - do not force one form
everywhere:

- `badanie` renders `study` for a trial and `study` or `paper` for a publication or
  review - `opracowanie` renders `study` or `review`.
- `uczestnik badania` renders `subject` in trial text, while `temat` renders `subject`
  in document metadata.
- `dawka` renders `dose` for an amount - the register follows the document.
- `bezpieczeństwo` renders `safety` for patient safety and `safety profile` inside
  `profil bezpieczeństwa`.
- `zdarzenie niepożądane` renders `adverse event`, never `adverse occurrence` or
  `negative event` - the regulated rendering is required.
- `rozpoznanie` renders `diagnosis` - `diagnoza` is colloquial.

## Calque Traps

| Instead of             | Use                                |
|------------------------|------------------------------------|
| negative event         | adverse event                      |
| product characteristic | Summary of Product Characteristics |
| marketing permission   | marketing authorization            |
| ethical committee      | ethics committee                   |
| medicine product       | medicinal product                  |
| OTC drug               | over-the-counter drug              |
| leaflet for patient    | package leaflet / patient leaflet  |
| examined person        | trial subject / study participant  |
| permission to turnover | marketing authorization            |

## Untranslated

Settled terms render back to their canonical English forms:

- `ChPL` renders `SmPC` (Summary of Product Characteristics), `ulotka dla pacjenta`
  renders `PIL` or `patient leaflet`, `podmiot odpowiedzialny` renders `MAH`.
- `DPK` renders `GCP` (Good Clinical Practice), `DPW` renders `GMP`, `DPL` renders
  `GLP`.
- `EMA`, `FDA`, `WHO`, `MedDRA`, `ATC`, `INN`, `URPL` stay as institution or standard
  names - `URPL` may be glossed as the Polish regulator.
