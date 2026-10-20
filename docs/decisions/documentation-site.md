# Documentation site decision

## Decision

Keep GitHub Markdown as the publishing surface for this stage. The README already provides the project overview, and the repository's small documentation set renders Markdown and Mermaid directly on GitHub. A separate site would add a second build and publishing surface before navigation needs justify it.

The README must remain complete and useful without a site. No GitHub Pages workflow or external site deployment is configured.

## Options reviewed

| Option | Fit | Decision |
| --- | --- | --- |
| GitHub Markdown | Native rendering, pull-request review, no build service | Use now |
| MkDocs Material | Mature documentation theme, search, navigation, and GitHub Pages workflows | Revisit when the docs grow or need a separate versioned site |
| Zensical | Newer documentation project from the Material ecosystem | Revisit after its ecosystem and migration path fit the portfolio's maintenance needs |

Sources: [MkDocs Material](https://github.com/squidfunk/mkdocs-material) and [Zensical](https://github.com/zensical/zensical).

## Reconsider when

- The number of pages makes the GitHub document index hard to use.
- Search, versioned documentation, or custom responsive navigation materially improves a reader's task.
- There is a tested site build and a reviewed publishing workflow with least-privilege permissions.
