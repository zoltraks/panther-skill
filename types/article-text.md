# Article

## Purpose

> **Scope:** Conventions for prose documents - articles, tutorials, and educational material read
> for understanding rather than scanned for rules
> **Key items:** prose flow, illustrative tables and figures, looser structure, dialect tolerance

An article is a narrative document.

It explains a topic through connected prose, examples, and figures rather than through rules or
requirements.

Typical shape: a themed essay built from prose sections, illustrative tables, and embedded
media.

## When To Use

Use for articles, tutorials, course material, blog posts, and explanatory essays.

**Templates**

- `templates/en/article-text-template-en.md`
- `templates/pl/article-text-template-pl.md`

## Structure

The canonical skeleton, adjusted to the request:

1. H1 title - the article topic.
2. Lead - a short opening that states the subject.
3. Themed sections - H2 per theme, H3 for subtopics when needed.
4. Closing section - summary, references, or further reading.

Articles may keep connected prose paragraphs.

The one-sentence-per-paragraph rule relaxes here: a paragraph may hold a small number of related
sentences when the text is narrative.

Keep sentences short even inside paragraphs.

## Deltas From The Language Baseline

- Existing articles may use the setext heading dialect (underlined `===`/`---`), closed ATX
  headings (`### Title ###`), or embedded HTML such as page-break divs. Preserve the dialect when
  editing, see `conventions/markdown-dialects.md`.
- Images and media are referenced relative to the document (`![](media/figure.png)`), keep media
  paths consistent with the existing layout.
- Illustrative tables are allowed to be small and loose in older documents, apply the table rules
  to any table you create or touch.
- A closing `---` horizontal rule may separate major parts in narrative documents that already
  use it.

## Diataxis Mapping

In Diataxis terms, this type covers the tutorial quadrant - learning-oriented, step-by-step
lessons - and shares the explanation quadrant with `types/technical-document.md`.

When a project organizes docs into Diataxis quadrants, tutorials and explanations land in this
type, how-to guides and reference pages land in the `technical-document` type.

## Section Names

- Introduction
- Summary
- Further Reading
- References

Polish section names for this document type are declared in `languages/pl.md`.
