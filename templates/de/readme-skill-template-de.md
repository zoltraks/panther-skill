# Skill-Name

> Ein Satz, der sagt, was der Skill tut und wann er verwendet wird.

## Überblick

Was der Skill ist, was er erzeugt und für welche Agenten-Umgebungen er gedacht ist.

## Funktionen des Skills

- **Fähigkeit eins** - was der Skill bei Aktivierung tut
- **Fähigkeit zwei** - was der Skill bei Aktivierung tut

## Installation

```bash
git clone <repository-url> <skills-verzeichnis>/skill-name
```

### Agenten-Umgebungen

- Agent A - `.agent-a/skills/skill-name/`
- Agent B - `.agent-b/skills/skill-name/`
- Globale Installation - `~/.config/<agent>/skills/skill-name/`

## Verwendung

Der Skill aktiviert sich, wenn eine Anfrage zu einem in `SKILL.md` deklarierten Auslöseschlüssel passt.

## Beispiel-Prompts

> Beispielanfrage, die den Skill aktiviert.

> Eine weitere Beispielanfrage.

## Inhalt

```
skill-name/
├── SKILL.md    # Zentrale Weiterleitung
└── <dir>/      # Ressourcendateien
```

## Lizenz

Lizenzname - siehe `LICENSE`.
