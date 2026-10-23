# Parameter Configuration

## Purpose

> **Scope:** The document-creation parameter surfaces, their defaults, and the
> resolution rules applied before drafting
> **Key items:** core parameters table, question shapes, plan confirmation, edit-case
> resolution

When creating a new standalone document, the agent runs the Parameter Resolution step in
`process/document-workflow.md`, asking whether to accept or configure the core parameters.

Defaults are:

| Parameter         | Default                                                             |
|-------------------|---------------------------------------------------------------------|
| Document type     | Inferred from the request, ask when ambiguous                       |
| Document language | Language of the user's request, English when unclear                |
| Document scope    | Detected from the project layout, unstructured when nothing matches |
| Filename          | Per the language file naming rules, or the scope's convention       |
| Encoding          | UTF-8 without BOM                                                   |
| Line endings      | LF, or the dominant style of the target directory                   |
| Delivery          | File in the location named by the request                           |

Every question offers at most four answers - up to three candidates guessed from detection
evidence plus `Cancel`, which aborts the task.

Format questions are asked before the document-type question, which is always its own surface.

A section-plan question then selects the required, recommended, and optional sections.

Before executing, the agent describes the plan and asks to proceed, adjust, or cancel.

For edits to existing documents, the document's own conventions and the minimal-diff rule answer.
