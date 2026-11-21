# Título del manual de procedimientos

## Propósito

Qué regula este manual y qué destinatarios atiende.

Para el lector humano: cómo este manual sirve de referencia.

Para el operador o el agente: qué operación ejecutar y cuándo.

## Modos de operación

- **Primera operación** - qué hace, cuándo se elige.
- **Segunda operación** - qué hace, cuándo se elige.

## Puntos de decisión

Antes de empezar, el operador decide cada punto y registra la respuesta.

**Nombre de la pregunta**

"Pregunta literal presentada al usuario?"

- Primera opción - valor por defecto recomendado
- Segunda opción
- El usuario puede dar otra respuesta.

## Roles y ubicaciones

Los roles lógicos se asignan a ubicaciones concretas.

Cada rol se resuelve de forma independiente, y las convenciones ya establecidas
en el destino se conservan.

| Rol            | Ubicación              | Requerido        |
|----------------|------------------------|------------------|
| Nombre del rol | `ruta/` o `ARCHIVO.md` | Sí o condicional |
| Otro rol       | `otra/ruta/`           | No               |

## Procedimientos

### Primera operación

1. Primer paso - qué hace el operador.
2. Segundo paso - qué hace a continuación el operador.

### Segunda operación

1. Primer paso - qué hace el operador.

## Validación

Confirme todos los puntos siguientes antes de concluir:

- [ ] Cada artefacto requerido existe.
- [ ] Cada regla definida en este manual se respeta.

## Apéndice

### Árbol de estructura

```
docs/
  DIRECTRICES.md     (rol: titular de reglas, existente)
  PROPUESTA.md       (rol: nuevo titular, propuesto)
```

### Biblioteca de plantillas

```markdown
# Esqueleto incrustado

Una plantilla lista para copiar que el operador rellena.
```
