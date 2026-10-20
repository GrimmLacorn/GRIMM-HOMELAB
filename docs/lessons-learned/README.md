# Lessons learned

These lessons are drawn from the owner's reported activities and from gaps found while preparing the portfolio. They are not claims that every listed control or service remains active.

## Resource planning

The Proxmox host is reported to have 16 GB RAM shared by several virtual machines and containers. The Wazuh learning lab encountered RAM and swap pressure. A useful next experiment measures guest allocation, available memory, swap, indexing workload, and service health together before scaling the stack.

## Troubleshooting

Packet loss is a symptom, not a root cause. Compare local gateway, public IP, DNS, link path, and host load independently. A suspected repeater or hypervisor should remain a hypothesis until a controlled comparison supports it.

## Security documentation

SSH keys, UFW, Fail2ban, local HTTPS, and service names are useful context, but they do not by themselves demonstrate safe configuration. A credible record also includes scope, versions, reachable interfaces, update state, backup/restore evidence, and a dated validation result.

## Evidence discipline

- Keep the source of each claim visible: owner report, upstream documentation, observed command output, or planned work.
- Do not publish screenshots before checking browser tabs, usernames, query history, network labels, certificate names, and device identifiers.
- Document a failure and the uncertainty around it; do not invent a clean result to make a portfolio look complete.
- Save reproducible commands and redacted output only after they have been run on the intended device.

## Follow-up

Use the [project record template](../../templates/project-record.md) for future deployments and experiments. Update the [roadmap](../../ROADMAP.md) when evidence changes a project's status.
