# Nazwa skilla

> Jedno zdanie mówiące, co skill robi i kiedy go używać.

## Przegląd

Czym jest skill, co produkuje i w jakich środowiskach agentów działa.

## Możliwości

- **Możliwość pierwsza** - co skill robi po aktywacji
- **Możliwość druga** - co skill robi po aktywacji

## Instalacja

```bash
git clone <adres-repozytorium> <katalog-skilli>/nazwa-skilla
```

### Środowiska agentów

- Agent A - `.agent-a/skills/nazwa-skilla/`
- Agent B - `.agent-b/skills/nazwa-skilla/`
- Instalacja globalna - `~/.config/<agent>/skills/nazwa-skilla/`

## Użycie

Skill aktywuje się, gdy żądanie pasuje do frazy wyzwalającej zadeklarowanej w `SKILL.md`.

## Przykładowe polecenia

> Przykładowe żądanie aktywujące skilla.

> Kolejne przykładowe żądanie.

## Zawartość

```
nazwa-skilla/
├── SKILL.md    # Główny router
└── <dir>/      # Pliki zasobów
```

## Licencja

Nazwa licencji - patrz `LICENSE`.
