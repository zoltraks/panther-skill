# English To Polish Sentence Style

## Purpose

> **Scope:** Sentence-level adaptation rules for rendering a document from English into
> Polish
> **Key items:** aspect and voice, actor verbs, report-register verb choice, fixed
> idioms, correlative frames, enumeration punctuation, hedged verdicts, meaning over
> word order, metaphors resolved to function, modality, conditions, enumeration logic,
> imperative voice, verbs before nominalizations, participial openers

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

Verbs that make an artifact an actor are always wrong - `reguły rządzą plikami`,
`plik orkiestruje proces`, `dowody wygrywają`, `blok wtóruje nawigacji` -
render them as `reguły obowiązują w tych plikach`, `plik określa przebieg procesu`,
`pierwszeństwo mają informacje ustalone na podstawie repozytorium`, and
`blok powtarza odnośniki nawigacyjne`.

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

A document's stated purpose renders as a function description, not a service verb -
`this document serves two audiences` becomes `dokument jest przeznaczony dla dwóch
grup odbiorców` or `dokument stanowi przewodnik dla`, never `dokument obsługuje
odbiorców`.

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

## Dash Splices

A spaced hyphen joining two independent clauses in the English source does not
transfer - split the pair into two sentences.

`The file must exist - a missing file stops the run` splits into `Plik musi
istnieć.` and `Brak pliku przerywa uruchomienie.` - never `Plik musi istnieć - brak
pliku przerywa uruchomienie`.

The same split applies when the second half is an imperative or an apposition the
reader must act on - `check the marker - it carries the date` splits into `Sprawdź
znacznik.` and `Znacznik zawiera datę.`

The spaced hyphen stays legal for the functions `languages/pl.md` assigns it - an
apposition or enumeration introducer, a paired parenthetical, a label definition in
the `- **Term** - value` pattern, a cross-reference such as `- zobacz "Rozdział 4"`,
and table cells.

A standalone second clause after ` - ` is never one of those - when in doubt, read the
right half aloud as a sentence and split on the period.

## Hedged Verdicts

Preserve the hedging level of the source - `the strongest candidate` renders
`najmocniejszy wariant`, `arguably` renders `prawdopodobnie` or `można uznać`, and a
hedged claim is never upgraded into a plain claim.

A comparative verdict keeps its comparative frame - `the fallback option` renders
`wariant zapasowy` or `wariant awaryjny`, not `jedyny wariant`.

## Meaning Over Word Order

Translate the meaning of the whole sentence, not the English syntax.

English word order carried into Polish produces calques like `rozstrzygnij rolę do
ścieżki` or `nazwany po zapisie zmiany`.

Render the intent instead - `przypisz rolę do rzeczywistej ścieżki`, `o nazwie
odpowiadającej dokumentowi zmiany`.

An English adjective is not a Polish adjective guarantee - `phases are revisitable`
renders `do poszczególnych faz można powracać`, not `fazy są odtwarzalne`, and
`stretched to target length` renders `nie wydłużaj pliku na siłę`, not
`plik jest dopychany do docelowej długości`.

An English `for` does not always render `dla` - `rules for testing` renders `zasady
testowania` or `reguły dotyczące testów`, matching the relation the noun carries.

An English `with` resolves the same way - `complete the run with zero warnings`
renders `zakończ przebieg bez ostrzeżeń`, not `z zerową liczbą ostrzeżeń`.

After replacing a noun with a different Polish term, propagate gender, number, and
case through the whole phrase - swapping `przyrost` for `partia` re-genders every
adjective and pronoun that refers to it (`spójna partia`, not `spójny partia`).

## Metaphors Translate By Function

An English metaphor renders its Polish function, not its image - `clean seams` becomes
`jasno określone punkty rozszerzeń`, `thin router` becomes `krótki plik kierujący
do zasad`, and `frame budget` becomes `czas jednej ramki`.

Where a metaphor names the result a check requires, take the criteria from the
document's own instructions - `until the increment is clean` renders `aż dana partia
zmian nie będzie powodowała błędów ani ostrzeżeń` when the document defines clean as
zero errors and warnings - never invent criteria the source does not state.

A named technical pattern keeps its canonical name with a Polish gloss - `god classes`
renders `klasy skupiające zbyt wiele zadań (God Class)` and `feature envy` renders
`metody nadmiernie korzystające z danych innych klas (Feature Envy)` - a literal image
such as `klasy boskie` erases the recognized name.

## Modality

Preserve the strength of normative language exactly:

| English  | Polish            |
|----------|-------------------|
| must     | `musi` / `należy` |
| must not | `nie wolno`       |
| should   | `powinien`        |
| may      | `może`            |

Never upgrade a recommendation into an obligation, a permission into a requirement,
or a ban into a suggestion.

Word order follows Polish grammar, not the English model - `the document must not be
used` renders `nie wolno wykorzystywać tego dokumentu`, not
`dokument ten nie wolno wykorzystywać`.

## Conditions And Exceptions

Conditions and exceptions map one-to-one - `only` renders `tylko` or `wyłącznie`,
`unless` renders `chyba że`, `when` renders `gdy`, `if` renders `jeśli`, and
`otherwise` renders `w przeciwnym razie`.

`chyba że` and `jeśli` are not interchangeable - `chyba że` introduces the sole
exception that flips the rule, `jeśli` introduces a condition.

## Enumeration Logic

An `or` enumeration under no negation renders `lub` - `ani` is legal only where the
source already negates the scope (`nie … ani`, `neither … nor`).

`A source, configuration, test, or toolchain change invalidates the result` renders
`zmiana kodu źródłowego, konfiguracji, testów lub zestawu narzędzi unieważnia wynik` -
never `zmiana … testów, zależności ani łańcucha narzędzi`, where the stray `ani`
reads as if the last item were exempted or the list were under negation.

The Polish rendering never gains a negation the source lacks and never loses one the
source carries - check every `nie` and `ani` in the output against the source's
polarity.

A named entity keeps its kind - a `file` renders `plik`, never `katalog`, and a
`directory` renders `katalog`, never `plik` - substituting the container kind changes
what the instruction tells the reader to produce or inspect.

Quantifier scope is preserved - `each` and `every` render `każdy`, `all` renders
`wszystkie`, `at least`/`at most` render `co najmniej`/`co najwyżej` - a dropped or
weakened quantifier silently widens or narrows the rule.

## Imperative Voice

Instruction sentences use the imperative mood consistently - `przeczytaj`,
`utwórz`, `sprawdź`, `zapisz`.

Description sentences use the indicative.

A step or stage label names the step rather than instructing, so it takes the nominal
form - `Spójny przyrost`, not `Zrealizuj spójny przyrost` - while the instruction
sentences inside the step keep the imperative.

Never alternate between the infinitive, the imperative, and impersonal constructions
inside one instruction set.

Prefer verb-first imperative order, mirroring the English `verb + object` flow -
`Zapisuj skonfigurowane szczegóły w dokumencie nadrzędnym` over the object-fronted
`Skonfigurowane szczegóły zapisuj w dokumencie nadrzędnym`.

Object fronting stays acceptable when it gives deliberate emphasis or marks a topic
shift.

Second-person pronouns stay lowercase inside a sentence - `cię`, `tobie`, `twój`,
never `Cię` or `Twój`.

## Verbs Before Nominalizations

Prefer a verb over a stacked nominalization - `ustal lokalizację`,
`przypisz rolę`, `zapisz wynik`, `sprawdź zgodność`, not `dokonaj ustalenia
lokalizacji` or `zestaw określony wstępnie przez wybory`.

An English `the set determined by X` renders `zestaw wynikający z X`.

The same preference covers copula nominalizations - `X is not proof that Y` renders
`X nie dowodzi tego, że Y`, not `X nie jest dowodem, że Y`.

Prefer explicit `nie` negation over a heavier negative adjective where both work -
`weryfikacja nie jest potrzebna` reads cleaner than `weryfikacja jest zbędna` and keeps
the source's negation visible.

A clause opened by an adverbial participle takes a comma after it -
`Wnosząc wkład, zgadzasz się`, `Odwołując się do standardu, utwórz sekcję`.

The comma belongs after the participle clause, before the main clause verb.

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
