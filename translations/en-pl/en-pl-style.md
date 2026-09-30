# English To Polish Sentence Style

## Purpose

> **Scope:** Sentence-level adaptation rules for rendering a document from English into
> Polish
> **Key items:** aspect and voice, actor verbs, report-register verb choice, fixed
> idioms, correlative frames, enumeration punctuation, hedged verdicts

This file governs how English sentences reshape into natural Polish at the clause level.

`translations/en-pl/en-pl-general.md` covers document-level style adaptation - this
file covers how a single sentence is built.

## When To Load

Load this file on every English to Polish translate task, after
`translations/en-pl/en-pl-general.md` and before the matching industry glossaries, per
`process/translate-document.md`.

Load it on English to Polish translation audits as well, per
`process/translation-audit.md`.

## Aspect And Voice

An English present passive that reports a completed outcome renders as the Polish
perfective resultative - `the variant is rated the weakest` becomes `wariant został
oceniony jako najsłabszy`, not `wariant jest oceniony`.

The stative `jest` + passive participle is reserved for standing or recurring
conditions - `jest wymagany`, `jest zachowana`, `jest opisana` - where the source
describes a state that holds now rather than a finished verdict.

When the English source is ambiguous, the document's frame decides - a report
delivering an evaluation uses the resultative, a specification stating a continuing
rule uses the stative.

The same rule covers other completed outcomes the passive reports - `the file was
removed` and `the entry was added` render `plik został usunięty` and `wpis został
dodany`.

## Actor And Verb Choice

The personification rule in `translations/en-pl/en-pl-general.md` applies - artifacts
do not act, persons and tools do.

An artifact as subject carries only a state verb - `zawiera`, `obejmuje`, `wykazuje`,
`wymaga`, `dostarcza`, `nazywa` - or the passive of a true action.

Report-register verbs map by meaning, not by word shape:

| English verb                 | Polish rendering          |
|------------------------------|---------------------------|
| shows / demonstrates         | `wykazuje`                |
| records / registers an entry | `rejestruje`              |
| notes / remarks              | `odnotowuje` / `zauważa`  |
| documents                    | `dokumentuje`             |
| recommends                   | `zaleca`                  |
| flags / marks                | `oznacza` / `sygnalizuje` |
| classifies                   | `klasyfikuje`             |

`rejestruje` is reserved for writing an entry into a register or a log.

A claim of conformance or a reported result renders `wykazuje` - `the variant records
conformance with the specification` becomes `wariant wykazuje zgodność ze
specyfikacją`, never `rejestruje zgodność`, because nothing is entered into a register.

## Fixed Idioms

Several `pod` phrases are fixed Polish idioms that are never rewritten under the calque
rule - `pod opieką`, `pod kątem`, `pod względem`, `pod warunkiem`, `pod presją`,
`pod kontrolą`, `pod adresem`, `pod hasłem`, `pod nazwą`, `pod postacią`.

The `pod (katalogiem)` row in the `languages/pl.md` vocabulary table covers locative
placement only - `under the directory` rendering `pod katalogiem` is the calque the
rule forbids.

An idiom keeps `pod` even where a different preposition would also be legal -
`assessed under the aspect of` correctly renders `oceniona pod kątem`.

## Correlative Frames

A correlative frame opening a content clause takes a comma before the clause
word - `polega na tym, gdzie`, `sprowadza się do tego, że`, `wynika z tego,
który` - never `polega na tym gdzie`.

The comma belongs after the frame word `tym` or `tego`, not before it.

## Enumeration Punctuation

A comma-separated enumeration of noun phrases is legal Polish - the bare-comma ban in
`languages/pl.md` targets independent clauses only.

An enumeration longer than four members or carrying nested items moves into a bullet
list, per the same baseline.

## Hedged Verdicts

Preserve the hedging level of the source - `the strongest candidate` renders
`najmocniejszy wariant`, `arguably` renders `prawdopodobnie` or `można uznać`, and a
hedged claim is never upgraded into a plain claim.

A comparative verdict keeps its comparative frame - `the fallback option` renders
`wariant zapasowy` or `wariant awaryjny`, not `jedyny wariant`.

## Example

### Correct

```markdown
Wariant eksportu został oceniony jako najmocniejszy kandydat bazowy.

Konfiguracja wykazuje zgodność ze specyfikacją wydania.

Raport ocenia wariant pod kątem ryzyka.
```

### Incorrect

```markdown
Wariant eksportu jest oceniony jako najmocniejszy kandydat bazowy.

Konfiguracja rejestruje zgodność ze specyfikacją wydania.

Raport ocenia wariant w kącie ryzyka.
```
