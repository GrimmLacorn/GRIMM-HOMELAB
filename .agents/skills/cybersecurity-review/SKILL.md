---
name: cybersecurity-review
description: Review HomeLab documentation, infrastructure examples, dependencies, screenshots, and GitHub workflows for secrets, sensitive data, unsafe exposure, privacy issues, and unsupported security claims. Use before publishing or changing security-sensitive material.
---

# Cybersecurity and privacy review

## Workflow

1. Read `AGENTS.md` and identify the files, history, workflows, diagrams, and images in scope.
2. Classify sensitive material: credentials, private keys, personal records, internal addresses, hostnames, device identifiers, logs, URLs with tokens, and screenshots with hidden context.
3. Run `npm run security:secrets` and inspect its result. Never paste a detected secret into a report. If a finding is real, stop publication and recommend rotation/removal from history through an owner-approved process.
4. Review network exposure, default credentials, service binding addresses, container privileges, update sources, API key handling, data retention, backup scope, and recovery evidence.
5. Review third-party project identity and license from its repository, then distinguish upstream claims from features tested in this HomeLab.
6. For OSINT or sensing material, require owner/synthetic/authorized data, consent, minimal retention, and a clear publication boundary.
7. Review GitHub Actions permissions, action pinning, triggers, secret use, and deployment side effects.
8. Record findings with evidence, severity, and a concrete remediation. Re-run affected checks after changes.

## Guardrails

- Do not claim a host or service is hardened from a list of tools alone.
- Do not publish personal information about third parties or real OSINT output.
- Do not execute third-party OSINT or sensing tools as part of documentation review.
- Do not suppress a scanner finding without evidence and an explicit, narrow explanation.
- Do not place credentials in skills, CI configuration, samples, or screenshots.

## Quality criteria

- Findings are reproducible and distinguish observed risk from speculation.
- User data is minimized and redaction is reviewed before commit.
- Only least-privilege CI permissions are used.
- Any remaining limitation is named plainly with the required next evidence or control.
