# Medical Glossary (English-Polish)

## Purpose

> **Scope:** English-Polish terminology for medical, clinical, and pharmaceutical
> documents
> **Key items:** domain signals, terminology table, context forms, calque traps,
> untranslated terms

Load this glossary for translate tasks on medical and pharmaceutical subjects.

Apply it for English to Polish translate tasks, per `process/translate-document.md`.

## Domain Signals

Apply this glossary when:

- The request names a medical, clinical, pharma, or healthcare subject.
- The document covers trials, products, dosages, patients, or regulatory submissions.
- The document's terminology is dominated by product, dosage, safety, or study
  vocabulary.

## Terminology

The dictionary maps recurring English terms to their preferred Polish forms.

Entries with `/` offer context-dependent forms - pick the form that fits the sentence.

| English                 | Polish                               |
|-------------------------|--------------------------------------|
| active substance        | substancja czynna                    |
| adverse drug reaction   | niepożądane działanie leku           |
| adverse event           | zdarzenie niepożądane                |
| batch                   | seria                                |
| clinical trial          | badanie kliniczne                    |
| cohort                  | kohorta / grupa                      |
| concomitant medication  | lek towarzyszący                     |
| contraindication        | przeciwwskazanie                     |
| diagnosis               | rozpoznanie                          |
| dosage                  | dawkowanie                           |
| dose                    | dawka                                |
| efficacy                | skuteczność                          |
| endpoint                | punkt końcowy                        |
| ethics committee        | komisja bioetyczna                   |
| excipient               | substancja pomocnicza                |
| expiry date             | termin ważności                      |
| generic drug            | lek generyczny                       |
| incidence               | zapadalność                          |
| indication              | wskazanie                            |
| informed consent        | świadoma zgoda                       |
| investigator            | badacz                               |
| leaflet                 | ulotka                               |
| marketing authorization | pozwolenie na dopuszczenie do obrotu |
| medicinal product       | produkt leczniczy                    |
| mortality               | śmiertelność                         |
| morbidity               | zachorowalność                       |
| monitoring              | monitorowanie                        |
| over-the-counter drug   | lek bez recepty                      |
| package leaflet         | ulotka dołączona do opakowania       |
| patient                 | pacjent                              |
| pharmacovigilance       | nadzór nad bezpieczeństwem leków     |
| placebo                 | placebo                              |
| prescription            | recepta                              |
| prevalence              | rozpowszechnienie                    |
| primary endpoint        | główny punkt końcowy                 |
| protocol                | protokół                             |
| quality of life         | jakość życia                         |
| randomization           | randomizacja                         |
| safety                  | bezpieczeństwo                       |
| serious adverse event   | ciężkie zdarzenie niepożądane        |
| side effect             | działanie niepożądane                |
| sponsor                 | sponsor                              |
| storage conditions      | warunki przechowywania               |
| study                   | badanie                              |
| subject                 | uczestnik badania                    |
| survival                | przeżycie                            |
| therapy                 | terapia / leczenie                   |
| tolerability            | tolerancja / znoszenie               |
| treatment               | leczenie                             |
| withdrawal              | odstawienie / wycofanie              |

## Context Forms

Some English terms render differently by context - do not force one form everywhere:

- `study` renders `badanie` for a trial and `opracowanie` for a publication or review.
- `subject` renders `uczestnik badania` in trial text and `temat` in document metadata.
- `dose` renders `dawka` for an amount and `porcja` colloquially - the register follows the
  document.
- `safety` renders `bezpieczeństwo` for patient safety and `profil bezpieczeństwa` for the
  product profile.
- `adverse event` renders `zdarzenie niepożądane`, never `zdarzenie negatywne` - the
  regulated EMA rendering is required.

## Calque Traps

| Instead of               | Use                                  |
|--------------------------|--------------------------------------|
| zdarzenie negatywne      | zdarzenie niepożądane                |
| charakterystyka produktu | Charakterystyka Produktu Leczniczego |
| pozwolenie marketingowe  | pozwolenie na dopuszczenie do obrotu |
| komitet etyczny          | komisja bioetyczna                   |
| substancja aktywna       | substancja czynna                    |
| lek OTC                  | lek bez recepty                      |

## Untranslated

Settled terms stay in their canonical form in Polish output:

- `SmPC` renders `ChPL` (Charakterystyka Produktu Leczniczego), `PIL` renders `ulotka dla
  pacjenta`, `MAH` renders `podmiot odpowiedzialny`
- `GCP` renders `Dobra Praktyka Kliniczna` (DPK), `GMP` renders `Dobra Praktyka
  Wytwarzania` (DPW), `GLP` renders `Dobra Praktyka Laboratoryjna` (DPL)
- `EMA`, `FDA`, `WHO`, `MedDRA`, `ATC`, `INN`, `URPL` stay as institution or standard
  names
