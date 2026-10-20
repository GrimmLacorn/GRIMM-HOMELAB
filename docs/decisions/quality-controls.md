# Documentation quality controls

## Adopted checks

| Concern | Check | Reason |
| --- | --- | --- |
| Markdown | `scripts/validate_markdown.py` uses the Python standard library to check whitespace, heading spacing, and fenced-block balance | Keeps basic source hygiene checks without adding runtime dependencies. |
| Links | `scripts/validate_docs.py` checks local paths, heading fragments, and external HTTPS links | Broken navigation is a portfolio defect. |
| Mermaid | The pinned Mermaid parser validates every fenced diagram in Markdown; GitHub renders those sources natively | Catches syntax failures without a copied diagram or browser-rendering dependency. |
| YAML | The pinned `yaml` package parses GitHub workflow YAML and Agent Skill frontmatter | Catches syntax and duplicate-key errors. |
| SVG | Python XML validation checks dimensions, `viewBox`, and active/external content | Keeps diagrams portable and safe to render. |
| Secrets | Gitleaks CLI in an upstream container pinned by immutable digest | Scans the checkout history without using a license-restricted GitHub Action. |
| Toolchain advisories | `npm audit` against the committed lockfile | Covers the small documentation toolchain. |

GitHub Actions use full commit SHAs, `contents: read`, no deployment secrets, and no infrastructure-changing steps.

## Deferred checks

- **Trivy:** no application containers, deployment manifests, or IaC exist in this repository. Revisit when those artifacts are added; scan their actual image/configuration scope then.
- **Documentation site build:** GitHub renders the current Markdown and Mermaid portfolio adequately. No site or publishing workflow is enabled; see the [site decision](documentation-site.md).
- **Action schema linting:** YAML syntax is checked locally and in CI. Add a GitHub workflow semantic linter if the workflow set grows beyond the current documentation pipeline.

## Agent Skills recognition

The four skills use the repository-local `.agents/skills/<skill-name>/SKILL.md` structure and the official Agent Skills frontmatter format. The installed skill catalog for this current session exposes only environment skills; repository-local skills are packaged and validated here, but this session does not report them as activated Codex capabilities. Reopen the repository in a new Codex task to confirm runtime discovery.
