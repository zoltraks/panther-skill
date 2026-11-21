---
code: es
name: Spanish
native-name: español
---

# Estilo y formato de los documentos Markdown

## Propósito

Este documento define el estilo del texto y las reglas de formato de los documentos
Markdown redactados en español.

Se aplica a toda la documentación del proyecto, incluidas las directrices, las normas,
las plantillas, las notas y los documentos de referencia.

Se dirige a las herramientas que generan contenido y a los agentes de IA, pero sigue
siendo legible para las personas.

Las reglas descritas a continuación se aplican también a este propio documento.

## Tabla de contenidos

| Sección                                    | Línea | Contenido                                               |
|--------------------------------------------|-------|---------------------------------------------------------|
| Estructura del documento                   | 48    | Título, propósito y esquema del documento               |
| Títulos                                    | 67    | Capitalización y calificadores                          |
| Numeración de las secciones                | 101   | Reglas de numeración de las secciones                   |
| Reglas de la tabla de contenidos           | 117   | Cuándo insertar una tabla de contenidos                 |
| Párrafos y frases                          | 135   | Construcción de frases y párrafos                       |
| Salto de línea                             | 150   | Líneas lógicas y saltos de línea forzados               |
| Listas                                     | 184   | Viñetas, numeración y espaciado                         |
| Líneas en blanco y espaciado               | 210   | Reglas de espaciado                                     |
| Bloques de código                          | 224   | Delimitadores, marcadores de lenguaje y código en línea |
| Formato en línea                           | 242   | Comillas, negrita y cursiva                             |
| Punto y coma                               | 263   | Prohibición del punto y coma en el texto                |
| Caracteres especiales                      | 290   | Caracteres de cuadros y emoji                           |
| Vocabulario español                        | 299   | Términos preferidos y calcos                            |
| Nombres de secciones por tipo de documento | 336   | Nombres de secciones y elementos de los tipos           |
| Rasgos tipográficos propios                | 684   | Numeración de capítulos y pseudotítulos                 |
| Tablas                                     | 704   | Alineación según el texto fuente                        |
| Nombres de archivos                        | 845   | Denominación de los nuevos archivos de documentación    |
| Ejemplo                                    | 860   | Ejemplo correcto y ejemplo incorrecto                   |
| Mantenimiento de los archivos              | 894   | Codificación y fines de línea                           |
| Pregunta de actualización                  | 906   | Formulación española de la pregunta de actualización    |
| Frases de activación                       | 914   | Frases españolas y equivalentes ingleses                |

## Estructura del documento

Utilice el mismo esquema en cada documento.

- Un título H1 (`#`) al principio del archivo, uno solo por documento, conciso y descriptivo.
- Una sección de propósito u objetivo, un párrafo que dice qué cubre el documento.
- Secciones principales en el nivel H2 (`##`), subsecciones en el nivel H3 (`###`).

Las secciones **Información del documento**e**Historial de versiones** son opcionales.

No añada estas secciones a un documento existente.

No las inserte tampoco en un documento nuevo,
salvo que la orden de creación lo exija explícitamente.

Si el documento ya las contiene, actualícelas en cada modificación de contenido.

No utilice títulos del nivel H4 ni más profundos.

## Títulos

Escriba los nombres de secciones y subsecciones con una mayúscula inicial y siga para
las demás palabras la ortografía española normal.

No aplique la capitalización de título inglesa, que pone una mayúscula en cada palabra.

Los nombres propios, las siglas y los nombres de tecnologías conservan su ortografía,
por ejemplo "Formato XML", "Integración con Microsoft Fabric", "Capa gold en el Lakehouse".

Mantenga cortos los nombres de las secciones.

No ponga calificadores entre paréntesis en los nombres de las secciones.

Los calificadores como "obligatorio" o "no repetir" van en el cuerpo de la sección.

No termine un título con un signo de puntuación.

### Correcto

```markdown
## Alcance de los datos de origen

### Formato XML
```

### Incorrecto

```markdown
## Alcance De Los Datos De Origen

### Formato XML (obligatorio):
```

## Numeración de las secciones

No numere las secciones por defecto.

La ausencia de numeración simplifica la reorganización de un documento,
porque el desplazamiento de una sección no exige renumerar las demás.

Si el documento editado contiene ya una numeración de secciones,
consérvela y respete el orden correcto de los números.

Tras añadir, eliminar o desplazar una sección, renumere las secciones
de modo que los números sigan siendo continuos y respeten el orden del documento.

El número de una subsección retoma el número de la sección superior,
por ejemplo `3.1.` bajo la sección `3.`.

## Reglas de la tabla de contenidos

No añada una tabla de contenidos por defecto.

Inserte una tabla de contenidos solo cuando se pida y solo
si las secciones del documento están numeradas.

Un archivo de referencia de más de 300 líneas puede contener una tabla de contenidos
incluso sin numeración de secciones.

Colóquela al principio del documento, inmediatamente después de la sección opcional
Información del documento y de la sección opcional Historial de versiones.

Si esas secciones están ausentes, la tabla de contenidos es la primera sección
después del título H1.

Actualice la tabla de contenidos tras cada cambio en la estructura del documento.

## Párrafos y frases

Escriba frases cortas.

Para las descripciones técnicas, utilice una frase por párrafo.

Esta disposición sigue siendo legible en los editores de texto, en la terminal y en
las diferencias de versiones.

Separe cada frase con una línea en blanco.

Una frase puede contener varias partes enlazadas si expresan un mismo pensamiento.

No apriete pensamientos sin relación en un párrafo largo.

## Salto de línea

No corte el texto a un ancho de columna fijo.

Cada frase ocupa una línea lógica.

Una frase puede ser larga cuando el pensamiento es largo,
el editor o el navegador corta el texto al mostrarlo.

Inserte un salto de línea forzado solo cuando el contenido fuente lo exija,
por ejemplo en un bloque de código o en un diagrama.

Para un documento existente, su propia convención de corte prevalece sobre esta regla.

Detecte si el documento corta la prosa a un ancho fijo o si conserva líneas lógicas,
mantenga esa convención y no la cambie salvo que la orden la cubra.

Las reglas del repositorio, como un `STYLE.md` que exige líneas de como máximo
100 caracteres, fijan la convención para los archivos nuevos y deciden los casos ambiguos.

Utilice `scripts/reflow-prose.py --wrap --width N` para aplicar un ancho fijo
y `scripts/reflow-prose.py --unwrap` para reunir las líneas cortadas en líneas lógicas.

El modo wrap solo corta las líneas, el modo unwrap solo las reúne,
y ambos dejan intactas las tablas, los bloques de código y los bloques de código indentados.

La maquetación de un documento producido sigue `conventions/prose-layout.md` - esta base
describe la convención `separated`, y los parámetros de admisión `line-wrapping`,
`sentence-spacing` y `wrap-width` pueden elegir `flowing`,
`bounded` o `justified` en la creación.

La detección de la maquetación de un documento existente sigue `conventions/prose-layout.md`
y nunca presupone una convención por defecto.

## Listas

Utilice el guion (`-`) para los elementos con viñeta.

No numere los elementos de lista por defecto.

Utilice una numeración para pasos ejecutados en secuencia,
cuando el documento editado ya la emplea en la lista en cuestión o cuando la orden
de modificación lo exige explícitamente.

Si la lista está numerada, mantenga los números continuos tras añadir o eliminar
elementos.

Inserte una línea en blanco antes de la lista y una línea en blanco después.

No inserte líneas en blanco entre elementos cortos.

Inserte una línea en blanco entre elementos largos o que contengan varias frases.

Inserte una línea en blanco entre un elemento padre y su sublista.

Indente la sublista al nivel del elemento padre.

Escriba las listas de tareas como `- [ ]` para un elemento abierto y `- [x]` para
un elemento terminado.

## Líneas en blanco y espaciado

Inserte una línea en blanco entre los párrafos.

Inserte una línea en blanco antes y después de una lista.

Inserte una línea en blanco antes y después de un bloque de código.

Inserte una línea en blanco antes y después de una tabla.

No deje varias líneas en blanco seguidas.

No deje espacios al final de una línea.

## Bloques de código

Delimite cada bloque de código con tres comillas invertidas.

Indique el marcador de lenguaje solo cuando el bloque contenga código en un lenguaje
de programación, de marcado o de datos.

Los bloques de texto plano, de prompts, de salidas de consola o stdout, de árboles de
directorios, de diagramas o de tablas quedan sin marcador - `text` y `txt` también
cuentan como marcadores, y un documento que los emplea de forma coherente conserva su convención.

No deje una línea en blanco en primera ni en última posición dentro del bloque.

Mantenga los bloques de código concisos y ligados al tema descrito.

Escriba los nombres de archivos y de directorios, los comandos, los nombres de columnas
y los valores como código en línea, por ejemplo `docs/directrices`, `SELECT`, `Fact_Sales`.

## Formato en línea

Para el texto normal, utilice los caracteres básicos sin variantes tipográficas.

Utilice las comillas dobles rectas ASCII (`"`)
en lugar de las variantes tipográficas como las comillas latinas.

Utilice el apóstrofo recto ASCII (`'`) en lugar del apóstrofo tipográfico.

La ortografía española abre las interrogaciones y las exclamaciones con los signos
`¿` y `¡`, que son signos ortográficos y no variantes tipográficas.

Si el documento editado sigue de forma coherente otra convención,
conserve la convención de ese documento.

Escriba las definiciones de términos en negrita de la forma **Término**: definición.

Emplee la cursiva con moderación.

No abuse de las marcas de formato.

## Punto y coma

No utilice el punto y coma en el texto corrido.

Enlace dos oraciones estrechamente relacionadas con una coma.

Cuando las oraciones expresan pensamientos distintos, divídalas en frases separadas.

La regla no se aplica a los bloques de código, al código en línea ni a las rutas de
archivos.

### Correcto

```markdown
Los datos brutos llegan a la capa `bronze`, la capa `silver` contiene los datos depurados.

El nombre lleva el sentido, el comentario lleva la justificación.
```

### Incorrecto

```markdown
Los datos brutos llegan a la capa `bronze`; la capa `silver` contiene los datos depurados.

El nombre lleva el sentido; el comentario lleva la justificación.
```

## Caracteres especiales

Los caracteres de dibujo de cuadros están permitidos en los bloques de código, los
diagramas y los esquemas.

No sustituya los caracteres de cuadros por `+`, `-` u otras aproximaciones ASCII.

No utilice emoji salvo que se pida explícitamente.

## Vocabulario español

Escriba un español correcto y evite los calcos aleatorios del inglés.

No añada terminaciones españolas a palabras inglesas
cuando existe un equivalente español natural.

| En lugar de      | Utilice              |
|------------------|----------------------|
| deployar         | desplegar            |
| updatear         | actualizar           |
| fixear           | corregir             |
| customizar       | personalizar         |
| downloadeado     | descargado           |
| mergear          | fusionar             |
| testear          | probar               |
| debuggear        | depurar              |
| checkear         | comprobar            |
| la performance   | el rendimiento       |
| el status report | el informe de estado |
| el deadline      | la fecha límite      |
| soportar         | admitir              |

Los nombres propios establecidos, los nombres de productos y los términos de arquitectura
conservan su forma original, por ejemplo Microsoft Fabric, Lakehouse, Warehouse,
Power BI, Workspace.

Los términos técnicos establecidos como préstamos también quedan inalterados, por
ejemplo commit, pull request, merge, branch, repository, pipeline, cache, backend,
frontend, framework, endpoint, backlog y ticket.

Escriba los nombres técnicos procedentes del sistema fuente exactamente como aparecen
en él.

En los títulos de los ejemplos, utilice los nombres de secciones españoles,
por ejemplo "Contenido de ejemplo", "Correcto" e "Incorrecto".

## Nombres de secciones por tipo de documento

Los nombres de secciones españoles se declaran exclusivamente en esta sección.

Los archivos en `types/` solo nombran los nombres ingleses.

Elija el nombre de sección español según el tipo de documento en la tabla siguiente.

| Tipo de documento        | Sección inglesa                    | Sección española                          |
|--------------------------|------------------------------------|-------------------------------------------|
| agent-instruction        | Purpose                            | Propósito                                 |
| agent-instruction        | Audiences                          | Destinatarios                             |
| agent-instruction        | Use Cases                          | Casos de uso                              |
| agent-instruction        | Decision Points                    | Puntos de decisión                        |
| agent-instruction        | Procedures                         | Procedimientos                            |
| agent-instruction        | Validation                         | Validación                                |
| agent-instruction        | Example Content                    | Contenido de ejemplo                      |
| agent-instruction        | Best Practices                     | Buenas prácticas                          |
| agent-instruction        | References                         | Referencias                               |
| article-text             | Introduction                       | Introducción                              |
| article-text             | Summary                            | Resumen                                   |
| article-text             | Further Reading                    | Lecturas adicionales                      |
| article-text             | References                         | Referencias                               |
| change-request           | Document Information               | Información del documento                 |
| change-request           | Summary                            | Resumen                                   |
| change-request           | Description                        | Descripción                               |
| change-request           | Justification                      | Justificación                             |
| change-request           | Impact                             | Impacto                                   |
| change-request           | Alternatives                       | Alternativas                              |
| change-request           | Approval                           | Aprobación                                |
| changelog-file           | Changes                            | Cambios                                   |
| changelog-file           | Version                            | Versión                                   |
| changelog-file           | Added                              | Añadido                                   |
| changelog-file           | Improved                           | Mejorado                                  |
| changelog-file           | Fixed                              | Corregido                                 |
| changelog-file           | Removed                            | Eliminado                                 |
| contributing-file        | Purpose                            | Propósito                                 |
| contributing-file        | Ways To Contribute                 | Formas de contribuir                      |
| contributing-file        | Reporting Issues                   | Notificación de problemas                 |
| contributing-file        | Development Setup                  | Entorno de desarrollo                     |
| contributing-file        | Pull Requests                      | Pull Requests                             |
| contributing-file        | AI-Assisted Contributions          | Contribuciones asistidas por IA           |
| contributing-file        | License                            | Licencia                                  |
| contributing-file        | Code Of Conduct                    | Código de conducta                        |
| contributing-file        | Getting Help                       | Obtener ayuda                             |
| daily-plan               | Priorities                         | Prioridades                               |
| daily-plan               | Schedule                           | Cronograma                                |
| daily-plan               | Tasks                              | Tareas                                    |
| daily-plan               | Notes                              | Observaciones                             |
| daily-plan               | Carry Over                         | Arrastre                                  |
| daily-plan               | Document Information               | Información del documento                 |
| daily-plan               | Version History                    | Historial de versiones                    |
| daily-plan               | Contents                           | Tabla de contenidos                       |
| decision-record          | Status                             | Estado                                    |
| decision-record          | Context and Problem Statement      | Contexto y problema                       |
| decision-record          | Decision Drivers                   | Factores de decisión                      |
| decision-record          | Considered Options                 | Opciones consideradas                     |
| decision-record          | Decision Outcome                   | Resultado de la decisión                  |
| decision-record          | Consequences                       | Consecuencias                             |
| decision-record          | Positive Consequences              | Consecuencias positivas                   |
| decision-record          | Negative Consequences              | Consecuencias negativas                   |
| decision-record          | Pros and Cons of the Options       | Ventajas e inconvenientes de las opciones |
| decision-record          | Links                              | Enlaces                                   |
| decision-record          | Supersedes                         | Sustituye                                 |
| engineering-standard     | Purpose                            | Propósito                                 |
| engineering-standard     | Scope                              | Alcance                                   |
| engineering-standard     | How To Use This Standard           | Uso de esta norma                         |
| engineering-standard     | Order Of Operations                | Orden de aplicación                       |
| engineering-standard     | Precedence                         | Precedencia                               |
| engineering-standard     | Non-Negotiable Rules               | Reglas no negociables                     |
| engineering-standard     | Agent Intake Protocol              | Protocolo de admisión del agente          |
| engineering-standard     | Detection First                    | Detección primero                         |
| engineering-standard     | Existing Project                   | Proyecto existente                        |
| engineering-standard     | New Project                        | Proyecto nuevo                            |
| engineering-standard     | Documentation                      | Documentación                             |
| engineering-standard     | Language Version                   | Versión del lenguaje                      |
| engineering-standard     | Core Technologies                  | Tecnologías principales                   |
| engineering-standard     | Project Structure                  | Estructura del proyecto                   |
| engineering-standard     | Naming Conventions                 | Convenciones de nomenclatura              |
| engineering-standard     | Code Conventions                   | Convenciones de código                    |
| engineering-standard     | Formatting and Linting             | Formato y linting                         |
| engineering-standard     | Testing                            | Pruebas                                   |
| engineering-standard     | Build                              | Build                                     |
| engineering-standard     | Dependencies                       | Dependencias                              |
| engineering-standard     | Security                           | Seguridad                                 |
| engineering-standard     | Observability                      | Observabilidad                            |
| engineering-standard     | Logging                            | Registro                                  |
| engineering-standard     | Comments                           | Comentarios                               |
| engineering-standard     | Error Handling                     | Gestión de errores                        |
| engineering-standard     | Verification                       | Verificación                              |
| engineering-standard     | Definition of Done                 | Definition of Done                        |
| engineering-standard     | Correctness                        | Corrección                                |
| engineering-standard     | Structure                          | Estructura                                |
| engineering-standard     | Quality                            | Calidad                                   |
| engineering-standard     | Hygiene                            | Higiene                                   |
| engineering-standard     | General Principles                 | Principios generales                      |
| engineering-standard     | Sources                            | Fuentes                                   |
| format-specification     | Document Information               | Información del documento                 |
| format-specification     | Version History                    | Historial de versiones                    |
| format-specification     | Quick Overview                     | Resumen rápido                            |
| format-specification     | Design Principles                  | Principios de diseño                      |
| format-specification     | Structure                          | Estructura                                |
| format-specification     | Implementation Notes               | Notas de implementación                   |
| management-plan          | Purpose                            | Propósito                                 |
| management-plan          | Methodology                        | Metodología                               |
| management-plan          | Methodology and Approach           | Metodología y enfoque                     |
| management-plan          | Roles and Responsibilities         | Roles y responsabilidades                 |
| management-plan          | Thresholds and Tolerances          | Umbrales y tolerancias                    |
| management-plan          | Cadence                            | Cadencia                                  |
| management-plan          | Process                            | Proceso                                   |
| management-plan          | Cadence and Process                | Cadencia y proceso                        |
| management-plan          | Tools                              | Herramientas                              |
| management-plan          | Reporting                          | Informes                                  |
| management-plan          | Related Plans                      | Planes relacionados                       |
| management-plan          | Related Registers                  | Registros relacionados                    |
| management-plan          | Related Plans and Registers        | Planes y registros relacionados           |
| management-plan          | Change Control                     | Control de cambios                        |
| management-plan          | Master Plan                        | Plan maestro                              |
| meeting-minutes          | Meeting Details                    | Detalles de la reunión                    |
| meeting-minutes          | Attendees                          | Asistentes                                |
| meeting-minutes          | Absentees                          | Ausentes                                  |
| meeting-minutes          | Agenda                             | Orden del día                             |
| meeting-minutes          | Discussion                         | Discusión                                 |
| meeting-minutes          | Decisions                          | Acuerdos                                  |
| meeting-minutes          | Action Items                       | Acciones a realizar                       |
| meeting-minutes          | Open Questions                     | Preguntas abiertas                        |
| meeting-minutes          | Next Meeting                       | Próxima reunión                           |
| meeting-minutes          | Facilitator                        | Moderador                                 |
| meeting-minutes          | Minute Taker                       | Redactor del acta                         |
| meeting-minutes          | Due Date                           | Fecha de vencimiento                      |
| meeting-minutes          | Owner                              | Responsable                               |
| message-document         | Background                         | Contexto                                  |
| message-document         | Details                            | Detalles                                  |
| message-document         | Action Required                    | Acción requerida                          |
| message-document         | Next Steps                         | Próximos pasos                            |
| message-document         | Contact                            | Contacto                                  |
| message-document         | Document Information               | Información del documento                 |
| message-document         | Version History                    | Historial de versiones                    |
| message-document         | Contents                           | Tabla de contenidos                       |
| project-charter          | Purpose and Justification          | Propósito y justificación                 |
| project-charter          | Measurable Objectives              | Objetivos medibles                        |
| project-charter          | Success Criteria                   | Criterios de éxito                        |
| project-charter          | High-Level Requirements            | Requisitos generales                      |
| project-charter          | Scope Boundaries                   | Límites del alcance                       |
| project-charter          | In Scope                           | Dentro del alcance                        |
| project-charter          | Out of Scope                       | Fuera del alcance                         |
| project-charter          | Deliverables and Milestones        | Entregables e hitos                       |
| project-charter          | Deliverables                       | Entregables                               |
| project-charter          | Milestones                         | Hitos                                     |
| project-charter          | High-Level Budget                  | Presupuesto general                       |
| project-charter          | Key Stakeholders                   | Partes interesadas clave                  |
| project-charter          | Project Manager Role and Authority | Rol y autoridad del director de proyecto  |
| project-charter          | Assumptions and Constraints        | Supuestos y restricciones                 |
| project-charter          | High-Level Risks                   | Riesgos generales                         |
| project-charter          | Exit Criteria                      | Criterios de salida                       |
| project-charter          | Approval                           | Aprobación                                |
| project-document         | Document Purpose                   | Propósito del documento                   |
| project-document         | Document Navigation                | Navegación del documento                  |
| project-document         | Glossary                           | Glosario                                  |
| project-document         | Abbreviations                      | Abreviaturas                              |
| project-document         | Vision                             | Visión                                    |
| project-document         | Goals                              | Objetivos                                 |
| project-document         | Non-Goals                          | No objetivos                              |
| project-document         | Quality Requirements               | Requisitos de calidad                     |
| project-document         | System Architecture                | Arquitectura del sistema                  |
| project-document         | Component Diagram                  | Diagrama de componentes                   |
| project-document         | Functional Requirements            | Requisitos funcionales                    |
| project-document         | Non-Functional Requirements        | Requisitos no funcionales                 |
| project-document         | Use Cases                          | Casos de uso                              |
| project-document         | Design Decisions                   | Decisiones de diseño                      |
| project-document         | Implementation Phases              | Fases de implementación                   |
| project-document         | Testing Strategy                   | Estrategia de pruebas                     |
| project-document         | Naming Conventions                 | Convenciones de nomenclatura              |
| project-document         | Version Control                    | Control de versiones                      |
| project-document         | Documentation                      | Documentación                             |
| proposal-document        | Status                             | Estado                                    |
| proposal-document        | Summary                            | Resumen                                   |
| proposal-document        | Background                         | Contexto                                  |
| proposal-document        | Background and Context             | Contexto y antecedentes                   |
| proposal-document        | Proposal                           | Propuesta                                 |
| proposal-document        | Alternatives Considered            | Alternativas consideradas                 |
| proposal-document        | Risks and Mitigations              | Riesgos y mitigaciones                    |
| proposal-document        | Open Questions                     | Preguntas abiertas                        |
| proposal-document        | Decision                           | Decisión                                  |
| proposal-document        | Reviewers                          | Revisores                                 |
| procedure-manual         | Purpose                            | Propósito                                 |
| procedure-manual         | Audiences                          | Destinatarios                             |
| procedure-manual         | Operating Modes                    | Modos de operación                        |
| procedure-manual         | Decision Points                    | Puntos de decisión                        |
| procedure-manual         | Roles and Locations                | Roles y ubicaciones                       |
| procedure-manual         | Procedures                         | Procedimientos                            |
| procedure-manual         | Validation                         | Validación                                |
| procedure-manual         | Examples                           | Ejemplos                                  |
| procedure-manual         | Template Library                   | Biblioteca de plantillas                  |
| procedure-manual         | Appendix                           | Apéndice                                  |
| readme-application       | Contents                           | Tabla de contenidos                       |
| readme-application       | Overview                           | Descripción general                       |
| readme-application       | Download                           | Descarga                                  |
| readme-application       | Installation                       | Instalación                               |
| readme-application       | Project Status                     | Estado del proyecto                       |
| readme-application       | Technical Stack                    | Pila tecnológica                          |
| readme-application       | Features                           | Funcionalidades                           |
| readme-application       | Quick Start                        | Inicio rápido                             |
| readme-application       | Usage                              | Uso                                       |
| readme-application       | Configuration                      | Configuración                             |
| readme-application       | Repository Structure               | Estructura del repositorio                |
| readme-application       | Documentation                      | Documentación                             |
| readme-application       | Changelog                          | Registro de cambios                       |
| readme-application       | License                            | Licencia                                  |
| readme-application       | Credits                            | Créditos                                  |
| readme-cli               | Overview                           | Descripción general                       |
| readme-cli               | Install                            | Instalación                               |
| readme-cli               | Commands                           | Comandos                                  |
| readme-cli               | Options                            | Opciones                                  |
| readme-cli               | Examples                           | Ejemplos                                  |
| readme-cli               | Configuration                      | Configuración                             |
| readme-cli               | License                            | Licencia                                  |
| readme-collection        | Overview                           | Descripción general                       |
| readme-collection        | About This Repository              | Acerca de este repositorio                |
| readme-collection        | Contents                           | Tabla de contenidos                       |
| readme-collection        | Usage                              | Uso                                       |
| readme-collection        | Notices                            | Avisos                                    |
| readme-collection        | License                            | Licencia                                  |
| readme-collection        | Credits                            | Créditos                                  |
| readme-docs              | Overview                           | Descripción general                       |
| readme-docs              | Documentation                      | Documentación                             |
| readme-docs              | Project Guidelines                 | Directrices del proyecto                  |
| readme-docs              | Repository Layout                  | Estructura del repositorio                |
| readme-docs              | License                            | Licencia                                  |
| readme-general           | Contents                           | Tabla de contenidos                       |
| readme-general           | Overview                           | Descripción general                       |
| readme-general           | Installation                       | Instalación                               |
| readme-general           | Usage                              | Uso                                       |
| readme-general           | Project Layout                     | Estructura del proyecto                   |
| readme-general           | Documentation                      | Documentación                             |
| readme-general           | License                            | Licencia                                  |
| readme-general           | Credits                            | Créditos                                  |
| readme-library           | Install                            | Instalación                               |
| readme-library           | Usage                              | Uso                                       |
| readme-library           | API Reference                      | Referencia de la API                      |
| readme-library           | Configuration                      | Configuración                             |
| readme-library           | Contributing                       | Contribución                              |
| readme-library           | License                            | Licencia                                  |
| readme-skill             | Contents                           | Tabla de contenidos                       |
| readme-skill             | Overview                           | Descripción general                       |
| readme-skill             | What The Skill Does                | Funciones de la habilidad                 |
| readme-skill             | Installation                       | Instalación                               |
| readme-skill             | Agent Environments                 | Entornos de agentes                       |
| readme-skill             | Usage                              | Uso                                       |
| readme-skill             | Example Prompts                    | Prompts de ejemplo                        |
| readme-skill             | What's Inside                      | Contenido                                 |
| readme-skill             | Verification                       | Verificación                              |
| readme-skill             | License                            | Licencia                                  |
| readme-skill             | Credits                            | Créditos                                  |
| register-log             | Purpose                            | Propósito                                 |
| register-log             | Scoring Definitions                | Definiciones de la escala de puntuación   |
| register-log             | Notes                              | Observaciones                             |
| register-log             | Register                           | Registro                                  |
| register-log             | Probability                        | Probabilidad                              |
| register-log             | Impact                             | Impacto                                   |
| register-log             | Score                              | Puntuación                                |
| register-log             | Response Strategy                  | Estrategia de respuesta                   |
| register-log             | Owner                              | Responsable                               |
| register-log             | Status                             | Estado                                    |
| register-log             | Review Date                        | Fecha de revisión                         |
| register-log             | Raised Date                        | Fecha de registro                         |
| register-log             | Due Date                           | Fecha de vencimiento                      |
| register-log             | Resolution                         | Resolución                                |
| register-log             | Priority                           | Prioridad                                 |
| register-log             | Description                        | Descripción                               |
| register-log             | Category                           | Categoría                                 |
| register-log             | Assumption                         | Supuesto                                  |
| register-log             | Constraint                         | Restricción                               |
| register-log             | Validated By                       | Validado por                              |
| register-log             | Submitted By                       | Registrado por                            |
| register-log             | Decision                           | Decisión                                  |
| register-log             | Authority                          | Instancia decisoria                       |
| register-log             | Recommendation                     | Recomendación                             |
| rules-document           | Purpose                            | Propósito                                 |
| rules-document           | Sources Of Truth                   | Fuentes de referencia                     |
| rules-document           | Scope                              | Alcance                                   |
| rules-document           | General Rules                      | Reglas generales                          |
| rules-document           | Exceptions                         | Excepciones                               |
| rules-document           | Correct                            | Correcto                                  |
| rules-document           | Incorrect                          | Incorrecto                                |
| rules-document           | Example Content                    | Contenido de ejemplo                      |
| rules-document           | File Maintenance                   | Mantenimiento de archivos                 |
| rules-document           | Verification                       | Verificación                              |
| status-report            | Reporting Period                   | Período del informe                       |
| status-report            | Overall Status                     | Estado general                            |
| status-report            | Status by Area                     | Estado por área                           |
| status-report            | Schedule                           | Cronograma                                |
| status-report            | Budget                             | Presupuesto                               |
| status-report            | Scope                              | Alcance                                   |
| status-report            | Risk                               | Riesgo                                    |
| status-report            | Summary                            | Resumen                                   |
| status-report            | Accomplishments                    | Logros                                    |
| status-report            | Milestones                         | Hitos                                     |
| status-report            | Metrics                            | Métricas                                  |
| status-report            | Top Risks and Issues               | Principales riesgos y problemas           |
| status-report            | Planned Next Period                | Plan para el próximo período              |
| status-report            | Decisions Needed                   | Decisiones requeridas                     |
| summary-document         | Purpose                            | Propósito                                 |
| summary-document         | Abstract                           | Compendio                                 |
| summary-document         | Summary                            | Resumen                                   |
| summary-document         | Detailed Abstract                  | Compendio detallado                       |
| summary-document         | Omitted Material                   | Material omitido                          |
| supplement-document      | Purpose                            | Propósito                                 |
| supplement-document      | Continuation Scope                 | Alcance de la continuación                |
| supplement-document      | Extended Content                   | Contenido ampliado                        |
| supplement-document      | Continued Entries                  | Entradas continuadas                      |
| supplement-document      | Updated Conclusions                | Conclusiones actualizadas                 |
| technical-document       | Purpose                            | Propósito                                 |
| technical-document       | Overview                           | Descripción general                       |
| technical-document       | Prerequisites                      | Requisitos previos                        |
| technical-document       | Configuration                      | Configuración                             |
| technical-document       | Usage                              | Uso                                       |
| technical-document       | Examples                           | Ejemplos                                  |
| technical-document       | Troubleshooting                    | Resolución de problemas                   |
| technical-document       | Limitations                        | Limitaciones                              |
| technical-document       | References                         | Referencias                               |
| work-breakdown-structure | Structure                          | Estructura                                |
| work-breakdown-structure | Work Packages                      | Paquetes de trabajo                       |
| work-breakdown-structure | WBS Dictionary                     | Diccionario de la EDT                     |
| work-breakdown-structure | Acceptance Criteria                | Criterios de aceptación                   |
| work-breakdown-structure | Owner                              | Responsable                               |
| work-breakdown-structure | Estimate                           | Estimación                                |
| work-breakdown-structure | Dependencies                       | Dependencias                              |
| work-breakdown-structure | RACI Matrix                        | Matriz RACI                               |
| work-breakdown-structure | Baseline                           | Línea base                                |

### Elementos propios de los tipos

Algunos tipos de documento fijan también títulos, esquemas de títulos y claves de
campos españoles.

| Tipo de documento        | Elemento                                | Forma española                                                                      |
|--------------------------|-----------------------------------------|-------------------------------------------------------------------------------------|
| changelog-file           | título H1                               | `# Cambios`                                                                         |
| management-plan          | esquema del título H1                   | `# Plan de gestión de <área>`                                                       |
| project-charter          | nombre del tipo y esquema del título H1 | `acta de constitución del proyecto`, `# Acta de constitución del proyecto <nombre>` |
| project-document         | títulos de documento típicos            | `diseño de la solución`, `especificación del proyecto`                              |
| project-document         | grupo de requisitos H3                  | `Hito I: ...`                                                                       |
| project-document         | línea de mecanismos del caso de uso     | `**Mecanismos utilizados:**`                                                        |
| project-document         | claves de la tabla de metadatos         | `Nombre del proyecto`, `Versión`                                                    |
| register-log             | título H1 del registro de riesgos       | `# Registro de riesgos`                                                             |
| work-breakdown-structure | nombre del tipo y abreviatura           | `estructura de desglose del trabajo` (EDT)                                          |

## Rasgos tipográficos propios

Los documentos formales españoles numeran a menudo los capítulos y los subcapítulos,
por ejemplo `# 1 Datos generales` y `## 1.1 Objeto`.

También pueden emplear pseudotítulos en negrita como `**Nota**`,
`**Importante**` o `**Descripción:**` en lugar de títulos de secciones.

Una tabla de metadatos con encabezado vacío puede sustituir al comentario de versión
en la convención española del documento de proyecto.

```markdown
|                      |                          |
|----------------------|--------------------------|
| Nombre del proyecto  | Data Integration Service |
| Versión              | 1.0.7                    |
```

Conserve estos rasgos al editar según `conventions/markdown-dialects.md`.

## Tablas

Las tablas deben seguir siendo legibles en la vista de texto antes de que un lector
Markdown las procese.

La alineación de las columnas y el relleno uniforme de las celdas son el objetivo
principal del formateo.

### Delimitadores

Separe las columnas con la barra vertical (`|`).

Ponga un espacio después de la barra que abre una celda y un espacio antes de la barra
que la cierra.

No añada más espacios alrededor de las barras que el único requerido.

Comience cada línea - encabezado, línea de separación y línea de datos - con una sola
barra vertical.

Una doble barra al principio de la línea (`||`) se interpreta como una primera celda vacía.

La herramienta de formateo la convierte entonces en una columna vacía adicional,
lo que daña la estructura de la tabla sin limitarse a desplazarla.

Escriba una primera celda deliberadamente vacía como `| |` y solo
cuando la tabla la necesite de verdad.

Una celda vacía solo está permitida en una columna que la línea de separación declara -
su celda de separación debe contener al menos un guion.

Una columna vacía en todas las líneas, incluido el encabezado, no está nunca permitida -
retírela.

### Línea de separación

Coloque la línea de separación inmediatamente después del encabezado.

La línea de separación contiene únicamente guiones y barras verticales.

Cada celda de la línea de separación contiene al menos un guion - una celda de espacios
no declara la columna.

Los guiones llegan hasta las barras verticales sin espacio.

La anchura de un separador de columna equivale a la anchura de la columna más dos guiones.

Los dos guiones adicionales representan el espacio antes del valor de la celda y
el espacio después.

La anchura mínima de una columna es de tres caracteres.

### Relleno de las celdas

Rellene cada celda por la izquierda con espacios hasta la anchura de la columna.

Rellene las celdas vacías con espacios hasta la anchura de la columna.

No rellene las celdas más allá de la anchura de la columna.

No trunque nunca el contenido de una celda.

Utilice la alineación a la izquierda en todas las celdas.

### Anchura de las columnas

La anchura de una columna es el mayor número de caracteres de todas las celdas de esa
columna, incluida la celda de encabezado.

Mida la anchura como la longitud del **texto fuente** de la celda,
no del texto mostrado.

Esta es la regla más importante del formateo de tablas.

Cuente cada carácter presente en la fuente Markdown, incluidos todos los caracteres
de formato.

No retire, no interprete ni agrupe ningún carácter antes de medir.

El lector Markdown oculta las comillas invertidas y los asteriscos,
esos caracteres están sin embargo presentes en la fuente y deben contarse.

Los elementos siguientes forman parte del contenido de la celda y entran en la medida
de la anchura.

- Las comillas invertidas del código en línea, por ejemplo la celda `` `nombre.valor` `` a 13 caracteres, no 11.
- Las dobles comillas invertidas alrededor de valores como códigos y números,
  por ejemplo la celda `` `` 00 `` `` a 6 caracteres, no 2.
- Los asteriscos de la cursiva, por ejemplo la celda `*cursiva*` a 9 caracteres, no 7.
- Los dobles asteriscos de la negrita, por ejemplo la celda `**negrita**` a 11 caracteres, no 7.
- Los guiones bajos del formato, por ejemplo la celda `_texto_` a 7 caracteres, no 5.
- Los espacios, la puntuación y todos los demás caracteres visibles en la fuente.

Las letras acentuadas y la ñ cuentan cada una como un carácter,
por ejemplo la palabra `Frecuencia` tiene 10 caracteres.

Escriba las letras acentuadas en forma compuesta, como un único carácter Unicode,
para que la medida de la anchura coincida con el número de caracteres visibles.

El error de formateo más frecuente consiste en medir la anchura del texto mostrado
en lugar de la del texto fuente.

La celda `` ` api/configuracion ` `` tiene 21 caracteres en la fuente,
el lector sin embargo solo muestra 19.

El uso de 19 en lugar de 21 produce una columna demasiado estrecha y barras verticales
desplazadas en la vista de texto.

### Compactado

Compacte la tabla tras el cálculo de las anchuras de columna.

Retire el relleno que sobrepasa la celda más ancha de cada columna.

Recalcule tras el compactado la línea de separación y el relleno de todas las celdas.

Una tabla compactada tiene las menores anchuras de columna que bastan para mostrar
correctamente todas las celdas.

La versión compactada es la versión correcta.

### Celdas multilínea

Evite las celdas multilínea.

Si una celda debe cortarse,
aplique las mismas reglas de formateo en todas las líneas de la tabla.

### Contenido de ejemplo

La tabla siguiente está compactada y alineada.

Las anchuras de columna son de 10, 8 y 13 caracteres.

```markdown
| Columna     | Valor    | Descripción   |
|-------------|----------|---------------|
| `cliente_id` | ``0001`` | Código cliente |
| `nombre`    | ``ABC``  | Nombre corto  |
```

## Nombres de archivos

Escriba los nombres de los nuevos archivos de documentación en minúsculas y separe las
palabras con guiones bajos, por ejemplo `especificacion_tecnica.md`.

No utilice letras acentuadas ni espacios en los nombres de los archivos nuevos.

Conserve los nombres convenidos en su forma original, por ejemplo `README.md`,
`CHANGELOG.md` o `ESPECIFICACION.md`.

Prefiera las palabras completas a las abreviaturas que la petición no emplea,
por ejemplo `informe_de_fusion.md` en lugar de `idf_informe.md`.

El nombre del archivo debe corresponder al tema del documento.

## Ejemplo

### Correcto

```markdown
# Plan de vistas de datos

## Propósito

Este documento describe las vistas de datos previstas en la capa `gold`.

Cada frase está separada por una línea en blanco.

## Reglas de edición

- Escriba frases cortas.
- Utilice una frase por párrafo.
- Mantenga cortos los nombres de las secciones.
```

### Incorrecto

```markdown
# Plan de vistas de datos

## Propósito
Este documento describe las vistas de datos previstas en la capa gold. Cada frase se encuentra en el mismo párrafo; el texto se vuelve difícil de comparar en diff.

## Reglas de edición (obligatorias):
- Escriba frases cortas.
- Utilice una frase por párrafo.
- Mantenga cortos los nombres de las secciones.
```

## Mantenimiento de los archivos

Conserve el estilo de los fines de línea y la codificación del documento que edite.

Cree los archivos nuevos con codificación UTF-8.

No cambie las convenciones de un documento existente para la numeración de secciones,
la numeración de listas y las secciones opcionales, salvo que la orden de modificación
las cubra.

Al editar, limite los cambios al alcance de la orden.

## Pregunta de actualización

Cuando haya cambios entrantes listos para recuperarse en el repositorio de la habilidad,
la pregunta de actualización es
`Hay una actualización de la habilidad disponible (<n> commits nuevos). ¿Actualizar ahora u omitir en esta sesión?`.

Las opciones de respuesta son `Actualizar ahora` y `Omitir en esta sesión`.

## Frases de activación

Las peticiones dirigidas a esta habilidad pueden formularse en español.

Las frases siguientes activan la habilidad del mismo modo que sus equivalentes
ingleses en `languages/en.md`.

Trate una petición que coincida con una frase de la tabla como su equivalente inglés.

| Frase                                               | Equivalente inglés                       |
|-----------------------------------------------------|------------------------------------------|
| crea un documento                                   | create a document                        |
| redacta un documento                                | create a document                        |
| especificación                                      | draft a specification                    |
| diseño de la solución                               | project document                         |
| documentación técnica                               | technical documentation                  |
| documentación del proyecto                          | project documentation                    |
| artículo                                            | write an article                         |
| nota                                                | quick note                               |
| documento yaml                                      | yaml document                            |
| escribe una configuración yaml                      | write a yaml config                      |
| edita este archivo yaml                             | edit this yaml file                      |
| corrige esta tabla                                  | fix this table                           |
| formatea esta tabla                                 | format this table                        |
| actualiza este documento                            | update this document                     |
| traduce este documento                              | translate this document                  |
| traduce al alemán                                   | translate to German                      |
| traduce al inglés                                   | translate to English                     |
| traduce al polaco                                   | translate to Polish                      |
| traducción de documento                             | translate this document                  |
| nuevo documento en este proyecto                    | new document in this project             |
| documento de funcionalidad                          | add a feature document                   |
| plan de implementación                              | write an implementation plan             |
| redacta un adr                                      | write an ADR                             |
| propuesta de diseño                                 | design proposal                          |
| acta de constitución del proyecto                   | project charter                          |
| registro de riesgos                                 | risk register                            |
| registro de partes interesadas                      | stakeholder register                     |
| informe de estado                                   | status report                            |
| acta de reunión                                     | meeting minutes                          |
| plan de gestión                                     | management plan                          |
| estructura de desglose del trabajo                  | work breakdown structure                 |
| plan del día                                        | daily plan                               |
| mensaje                                             | write a message                          |
| anuncio                                             | write a message                          |
| solicitud de cambio                                 | change request                           |
| detecta la disposición del documento                | detect document layout                   |
| analiza la estructura del documento                 | analyze document structure               |
| auditoría del documento                             | audit this document                      |
| comprueba el formato del documento                  | check document formatting                |
| planifica las correcciones de los hallazgos         | plan fixes for findings                  |
| auditoría de traducción                             | audit this translation                   |
| comprueba la traducción                             | check the translation                    |
| verifica la traducción                              | verify the translation                   |
| corrige la traducción                               | fix this translation                     |
| mejora la traducción                                | fix this translation                     |
| aplica las correcciones de revisión a la traducción | apply review findings to the translation |
| traducción adaptada                                 | adapted translation                      |
| documento de instrucciones de agente                | agent instruction document               |
| documento de preparación                            | preparation document                     |
| guía de contribución                                | contributing guide                       |
| guía del colaborador                                | contributing guide                       |
| describe                                            | describe                                 |
| describe brevemente                                 | describe shortly                         |
| redacta una descripción                             | make a description                       |
| resume                                              | summarize                                |
| escribe un resumen                                  | write a summary                          |
| da una visión general                               | give an overview                         |
| descripción corta                                   | short description                        |
| descripción detallada                               | detailed description                     |
| describe en detalle                                 | describe in detail                       |
| descripción completa                                | full description                         |
| resume este documento en un archivo                 | summarize this document to a file        |
| compendio del documento                             | write an abstract of this document       |
| redacta un compendio de este documento              | write a brief of this document           |
| abrevia este documento                              | abridge this document                    |
| escribe un suplemento                               | write a supplement                       |
| amplía este informe                                 | extend this report                       |
| trabaja en panther                                  | work on panther                          |
| trabaja en esta habilidad                           | work on this skill                       |
| repara esta habilidad                               | fix this skill                           |
| ajusta la habilidad                                 | adjust the skill                         |
| actualiza los documentos de la habilidad            | update the skill documents               |
| ejecuta panther                                     | run panther                              |
| usa panther                                         | use panther                              |
| usa la habilidad                                    | use skill                                |
| usa esta habilidad                                  | use this skill                           |
| activa la habilidad                                 | activate the skill                       |
| trabaja con la habilidad                            | work with skill                          |
| lista todas las operaciones                         | list all operations                      |
| muestra todas las capacidades                       | show all capabilities                    |
| corrige este documento                              | correct this document                    |
| corregir este documento                             | correct this document                    |
| revisa este documento                               | proofread this document                  |
| humaniza este documento                             | humanize this document                   |
| como si lo hubiera escrito una persona              | make it read like a person wrote it      |
| reescribe la voz del documento                      | rewrite the voice                        |
| corrige la gramática                                | correct the grammar                      |
| corrige las erratas                                 | fix the typos                            |
| corrige los errores del documento                   | fix the errors in this document          |
