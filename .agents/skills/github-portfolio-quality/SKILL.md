---
name: github-portfolio-quality
description: Improve this repository's GitHub portfolio presentation, README navigation, documentation consistency, links, SVG accessibility, roadmap, and CI checks. Use when preparing a portfolio change or pull request.
---

# GitHub portfolio quality

## Workflow

1. Read `AGENTS.md`, `README.md`, `README.fr.md`, `docs/README.md`, and `ROADMAP.md`.
2. Check every project status against its page. Keep completed learning, previous configuration, research, and planned work distinct.
3. Confirm the first screen explains the project, its technical focus, and how to reach key documentation.
4. Review headings, tables, links, image alt text, mobile readability, dark/light contrast, and Mermaid source/export parity.
5. Add badges only when they represent a real, current workflow or license. Do not add counters, false percentages, invented test status, or decorative technology claims.
6. Check repository licensing and third-party attributions. Do not choose legal terms for the owner.
7. Run `npm run check` and `npm run security:secrets`. Confirm the workflow uses read-only permissions and immutable action references.
8. Review the final diff and summarize what changed, which validations ran, and what remains unverified.

## Quality criteria

- A recruiter can reach infrastructure, service, security, learning, and research pages in a few clicks.
- The English and French entry points agree on status and evidence.
- No unsupported current-state or contact claims are present.
- All linked assets render and have descriptive alt text.
- The README remains useful without an optional documentation website.
