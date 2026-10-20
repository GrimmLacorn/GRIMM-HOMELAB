# Project rules for contributors and coding agents

## Purpose and evidence

- Treat this repository as a personal learning portfolio, not a live inventory or production service catalogue.
- Use the status labels in `ROADMAP.md`. Owner-provided notes without dated evidence are historical reports, not proof of current operation.
- Separate concepts studied, procedures attempted, tests actually run, and work planned. Do not turn a proposed command into a reported result.
- Preserve uncertainties. Do not invent hostnames, IP addresses, domains, dates, credentials, service targets, metrics, screenshots, contacts, or deployment details.
- When a fact changes, record the evidence and verification date in the relevant page.

## Writing and visual design

- Write the primary documentation in professional English. Keep `README.fr.md` as the French entry point.
- Prefer concise explanations, accurate component names, accessible diagrams, and links to primary sources.
- Keep current or previously reported architecture separate from target architecture. Mermaid code fences in the relevant Markdown page are canonical; validate them with `npm run check:diagrams` and use GitHub's native Mermaid rendering.
- Use genuine screenshots only. Redact private addresses, usernames, device identifiers, tokens, passwords, query history, and personal records before adding them.
- Do not add a project-wide license until the owner chooses its terms. Keep third-party licenses attributed to their own projects.

## Security and privacy

- Never commit secrets, private keys, password-vault exports, personal data about third parties, raw logs, or unredacted screenshots.
- For OSINT material, use only the owner's data, synthetic data, or a documented authorized scope. Do not publish lookup results about real people.
- Treat Wi-Fi sensing and identity correlation as privacy-sensitive even when a tool uses public data or no camera.
- Review network exposure, default credentials, API keys, container privileges, and data retention before documenting a deployment as safe.
- Do not run infrastructure-changing commands against the owner's homelab unless they are explicitly requested and the target is clear.

## Changes and review

- Keep the root README useful on its own and maintain the navigation in `docs/README.md`.
- Keep the roadmap consistent with the evidence in project pages.
- Before a pull request, run `npm ci --ignore-scripts`, `npm run check`, and `npm run security:secrets`. Record failures and skipped checks honestly.
- Use least-privilege GitHub Actions permissions. Pin actions to full commit SHAs and tools to exact versions with a lockfile.
- Do not merge changes into `main` without owner approval.
