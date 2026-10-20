---
name: homelab-documentation
description: Turn verified HomeLab notes, commands, configurations, and screenshots into clear technical records. Use when documenting a service, infrastructure change, incident, learning lab, or lessons learned in this repository.
---

# HomeLab documentation

## Workflow

1. Read the repository's `AGENTS.md`, the relevant project page, and `ROADMAP.md`.
2. List the facts available and label each as owner-reported, source-documented, directly tested, or planned. Do not infer current operation from an old note.
3. Identify missing evidence that changes the reader's understanding: date, version, hardware, resource limit, topology, test action, expected result, or observed result.
4. Write or update the page in professional English. Keep `README.fr.md` aligned when a portfolio-level claim changes.
5. Include architecture, requirements, configuration, security, validation, problems, lessons, and next steps when relevant. Mark proposed procedures as proposed.
6. Add only genuine screenshots. Review each image for hostnames, addresses, usernames, browser tabs, query data, secrets, and metadata before linking it.
7. Update navigation, roadmap status, and Mermaid diagrams affected by the change.
8. Run `npm run check` and `npm run security:secrets`; report exact failures and skipped checks.

## Evidence rules

- Use `Completed Learning Lab` only for a completed study phase; it does not imply a persistent service.
- Use `Previously configured` when an owner reports past deployment but current state is unknown.
- Use `Research only` when reading sources without running the software.
- Use `Planned` for work without implementation evidence.
- Record dates and versions only when supplied or measured. Do not fabricate command output, uptime, test results, screenshots, or contact links.
- Keep passwords, private keys, vault data, unredacted logs, and third-party personal data out of public documentation.

## Quality criteria

- A reader can distinguish design, actual work, and proposed next steps.
- Commands state their working context and are not described as run unless they were run.
- Service claims have a path to dated evidence and a relevant validation result.
- Internal links and diagrams are updated with the page.
- The page follows `templates/project-record.md` where that structure fits.
