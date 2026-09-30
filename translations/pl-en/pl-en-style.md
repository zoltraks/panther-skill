# Polish To English Sentence Style

## Purpose

> **Scope:** Sentence-level adaptation rules for rendering a document from Polish into
> English
> **Key items:** aspect and voice, report-register verb choice, fixed idioms,
> enumeration punctuation, hedged verdicts

This file governs how Polish sentences reshape into natural English at the clause level.

`translations/pl-en/pl-en-general.md` covers document-level style adaptation - this
file covers how a single sentence is built.

## When To Load

Load this file on every Polish to English translate task, after
`translations/pl-en/pl-en-general.md` and before the matching industry glossaries, per
`process/translate-document.md`.

Load it on Polish to English translation audits as well, per
`process/translation-audit.md`.

## Aspect And Voice

A Polish perfective resultative reporting a completed evaluation - `została oceniona`,
`został usunięty`, `zostało dodane` - renders as the English past passive `was rated`,
`was removed`, `was added`.

The English present passive `is rated`, `is required` is reserved for standing
conditions the source describes as currently holding - `jest wymagany`, `jest
zachowana`, `jest opisana`.

When the Polish source is ambiguous, the document's frame decides - a report delivering
an evaluation uses the past passive, a specification stating a continuing rule uses the
present passive.

## Actor And Verb Choice

Polish artifact state verbs map to natural English equivalents:

| Polish verb               | English rendering    |
|---------------------------|----------------------|
| `zawiera` / `obejmuje`    | contains / covers    |
| `wykazuje`                | demonstrates / shows |
| `wymaga`                  | requires             |
| `rejestruje`              | records / registers  |
| `odnotowuje`              | notes                |
| `dokumentuje`             | documents            |
| `zaleca`                  | recommends           |
| `oznacza` / `sygnalizuje` | flags / marks        |
| `klasyfikuje`             | classifies           |

A conformance claim `wykazuje zgodność z` renders `demonstrates conformance with` or
`is compliant with`, never `registers compliance` - the claim is a verdict, not a
registry write.

Reports and reviewers may act in English the way the Polish source allows - `raport
wskazuje` renders `the report states` or `the report notes`.

## Fixed Idioms

Fixed Polish idioms map to natural English phrases - they are never rendered word by
word:

| Polish idiom    | English rendering             |
|-----------------|-------------------------------|
| `pod kątem`     | in terms of                   |
| `pod względem`  | in terms of / regarding       |
| `pod opieką`    | under the stewardship of      |
| `pod warunkiem` | provided that                 |
| `pod presją`    | under pressure                |
| `pod kontrolą`  | under control / governed by   |
| `pod adresem`   | at the address / addressed to |
| `pod hasłem`    | under the heading of          |
| `pod nazwą`     | under the name                |
| `pod postacią`  | in the form of                |

`pod kątem` is never "under the angle" and `pod względem` is never "under the respect".

## Enumeration Punctuation

A Polish comma-separated enumeration keeps its commas in English, and the final
conjunction renders per `languages/en.md` - `A, B i C` becomes `A, B and C` or
`A, B, and C` per the document's own convention.

## Hedged Verdicts

Preserve the hedging level of the source - `najmocniejszy wariant` renders `the
strongest candidate`, `prawdopodobnie` renders `probably` or `arguably`, and a hedged
verdict is never upgraded into a plain claim.

A comparative verdict keeps its comparative frame - `wariant zapasowy` renders `the
fallback option`, not `the only option`.

## Example

### Correct

```markdown
The export variant was rated the strongest base candidate.

The configuration demonstrates conformance with the release specification.

The report assesses the variant in terms of risk.
```

### Incorrect

```markdown
The export variant is rated the strongest base candidate.

The configuration registers compliance with the release specification.

The report assesses the variant under the angle of risk.
```
