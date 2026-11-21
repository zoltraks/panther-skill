# Nombre de la habilidad

> Una frase que dice qué hace la habilidad y cuándo se usa.

## Descripción general

Qué es la habilidad, qué produce y para qué entornos de agentes está pensada.

## Funciones de la habilidad

- **Función una** - qué hace la habilidad al activarse
- **Función dos** - qué hace la habilidad al activarse

## Instalación

```bash
git clone <url-del-repositorio> <directorio-de-habilidades>/nombre-habilidad
```

### Entornos de agentes

- Agente A - `.agent-a/skills/nombre-habilidad/`
- Agente B - `.agent-b/skills/nombre-habilidad/`
- Instalación global - `~/.config/<agent>/skills/nombre-habilidad/`

## Uso

La habilidad se activa cuando una petición coincide con una clave de activación
declarada en `SKILL.md`.

## Prompts de ejemplo

> Petición de ejemplo que activa la habilidad.

> Otra petición de ejemplo.

## Contenido

```
nombre-habilidad/
├── SKILL.md    # Enrutado central
└── <dir>/      # archivos de recursos
```

## Licencia

Nombre de la licencia - vea `LICENSE`.
