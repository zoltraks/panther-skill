# Titel des Prozedurhandbuchs

## Zweck

Was dieses Handbuch regelt und welche Zielgruppen es bedient.

Für den menschlichen Leser: wie dieses Handbuch als Referenz verwendet wird.

Für den Operator oder Agenten: welche Operation wann auszuführen ist.

## Betriebsmodi

- **Erste Operation** - was sie tut, wann sie gewählt wird.
- **Zweite Operation** - was sie tut, wann sie gewählt wird.

## Entscheidungspunkte

Vor Beginn entscheidet der Operator jeden Punkt und hält die Antwort fest.

**Fragename**

"Wörtliche Fragestellung, die dem Benutzer präsentiert wird?"

- Erste Option - empfohlener Standard
- Zweite Option
- Der Benutzer kann eine andere Antwort angeben.

## Rollen und Speicherorte

Logische Rollen werden konkreten Speicherorten zugeordnet. Jede Rolle wird
unabhängig aufgelöst, und im Ziel bereits etablierte Konventionen bleiben
erhalten.

| Rolle         | Speicherort             | Erforderlich    |
|---------------|-------------------------|-----------------|
| Rollenname    | `pfad/` oder `DATEI.md` | Ja oder bedingt |
| Weitere Rolle | `anderer/pfad/`         | Nein            |

## Verfahren

### Erste Operation

1. Erste Stufe - was der Operator tut.
2. Zweite Stufe - was der Operator als Nächstes tut.

### Zweite Operation

1. Erste Stufe - was der Operator tut.

## Validierung

Bestätige vor dem Abschluss alle folgenden Punkte:

- [ ] Jedes erforderliche Artefakt existiert.
- [ ] Jede in diesem Handbuch definierte Regel wird eingehalten.

## Anhang

### Strukturbaum

```
docs/
  RICHTLINIEN.md     (Rolle: Regelinhaber, vorhanden)
  VORSCHLAG.md       (Rolle: neuer Inhaber, vorgeschlagen)
```

### Vorlagenbibliothek

```markdown
# Eingebettetes Gerüst

Eine kopierfertige Vorlage, die der Operator ausfüllt.
```
