# Tytuł podręcznika procedur

## Przeznaczenie

Czym zarządza ten podręcznik i jakim odbiorcom służy.

Dla czytelnika: jak korzystać z tego podręcznika jako z odniesienia.

Dla operatora lub agenta: którą operację wykonać i kiedy.

## Tryby działania

- **Pierwsza operacja** - co robi, kiedy jest wybierana.
- **Druga operacja** - co robi, kiedy jest wybierana.

## Punkty decyzyjne

Przed rozpoczęciem operator rozstrzyga każdą decyzję i zapisuje odpowiedź.

**Nazwa pytania**

"Dosłowna treść pytania przedstawiana użytkownikowi?"

- Pierwsza opcja - zalecana wartość domyślna
- Druga opcja
- Pozwól użytkownikowi podać inną odpowiedź.

## Role i lokalizacje

Role logiczne są przypisane do konkretnych lokalizacji.

Każdą rolę rozstrzygaj niezależnie i zachowaj konwencje już ustalone w obiekcie docelowym.

| Rola       | Lokalizacja              | Wymagana          |
|------------|--------------------------|-------------------|
| Nazwa roli | `ścieżka/` lub `PLIK.md` | Tak lub warunkowo |
| Inna rola  | `inna/ścieżka/`          | Nie               |

## Procedury

### Pierwsza operacja

1. Pierwszy etap - co robi operator.
2. Drugi etap - co robi operator dalej.

### Druga operacja

1. Pierwszy etap - co robi operator.

## Weryfikacja

Przed zakończeniem potwierdź wszystkie poniższe:

- [ ] Każdy wymagany artefakt istnieje.
- [ ] Każda zasada zdefiniowana w tym podręczniku jest przestrzegana.

## Dodatek

### Drzewo struktury

```
docs/
  WYTYCZNE.md        (rola: właściciel zasad, istniejący)
  PROPOZYCJA.md      (rola: nowy właściciel, proponowany)
```

### Biblioteka szablonów

```markdown
# Osadzony szkielet

Gotowy do skopiowania szablon, który operator wypełnia.
```
