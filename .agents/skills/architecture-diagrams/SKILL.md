---
name: architecture-diagrams
description: Create and maintain readable Mermaid diagrams and SVG exports for HomeLab networks, Proxmox guests, services, monitoring, and automation. Use when a topology, data flow, or target architecture changes.
---

# Architecture diagrams

## Workflow

1. Read `AGENTS.md` and the source page. Separate confirmed, owner-reported historical, unknown, and target components before drawing.
2. Choose a single flow direction and a small number of nodes. Use short labels and avoid real IP addresses, domains, credentials, serials, or user names.
3. Keep the Mermaid source as a fenced block in the relevant Markdown page. Use the shared palette and line styles: solid for reported/known relationships, dashed for unknown or planned relationships.
4. Label unknown links explicitly. Do not use placement or arrows to imply an unverified network path.
5. Run `npm run check:diagrams` to parse every source block. Review the GitHub native render for text overlap, contrast, line direction, and separation of current and target state.
6. Run `npm run check`. Export a standalone SVG only when a concrete use case needs one; review its dimensions, contrast, and accessibility separately.
7. Update the page and navigation in the same change.

## Diagram rules

- Mark target components as planned and keep them out of the current architecture.
- Use only relationships supported by project evidence or official component documentation.
- Prefer diagrams that answer a specific reader question over decorative detail.
- Ensure SVG exports have a `viewBox`, descriptive title, no scripts, and no external assets.
- Keep one canonical Mermaid source; avoid copying the same diagram into several Markdown pages.

## Quality criteria

- A reader can identify each component and understand the direction of each flow.
- Reported facts and uncertainties are visually distinct.
- Mermaid parser validation succeeds and GitHub renders the fenced source.
- Diagram context and labels explain the status of reported, unknown, and planned components.
