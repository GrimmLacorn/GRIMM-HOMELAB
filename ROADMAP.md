# Roadmap

This roadmap separates learning completed in the past from services previously configured and work that is only planned. Dates and deployment evidence were not included in the source notes. Items marked **owner-reported** need a dated runbook, screenshot, or command output before they can be presented as currently operational.

## Completed learning labs

- **Wazuh SIEM fundamentals and initial Ubuntu Server deployment experiments** — owner-reported as a completed learning phase. This does not mean a permanent Wazuh deployment is running.

## Configured or previously tested

These items are described in owner-provided notes. Their present state has not been checked against the homelab during this work.

- Proxmox VE host with Debian/Ubuntu virtual machines and Linux containers.
- Raspberry Pi 4 running Debian 13 ARM64, with Pi-hole and reported SSH key, UFW, Fail2ban, Wake-on-LAN, and local dashboard work.
- Vaultwarden on a Debian 12 VM behind Caddy with local HTTPS.
- Uptime Kuma in a Debian-based LXC for initial service monitoring.
- Intermittent network troubleshooting involving gateway and Internet packet loss; the Wi-Fi repeater is a suspected link, not a confirmed cause.

## Research and experiments

- **Eye of God** — repository research only. The exact phrase maps to multiple unrelated projects; this portfolio reviews `RykerWilder/eye-of-god` as one self-hosted dashboard candidate and does not claim it is the canonical Telegram service.
- **RuView** — repository and hardware-prerequisite research only. No sensor or software experiment is claimed.

## Planned

1. Capture a redacted, dated inventory of the Proxmox host, Raspberry Pi, VM/LXC placement, and service health.
2. Replace the historical Wi-Fi repeater path with a direct Ethernet path if the physical migration is completed; measure packet loss before and after.
3. Record a small, reproducible Wazuh experiment with VM memory limits, swap measurements, logs, and teardown notes.
4. Add Prometheus, Grafana, and Alertmanager as a separately labelled observability target.
5. Build a disposable Ansible lab and a Docker Compose service example with secrets kept outside Git.
6. Add centralized logging, Home Assistant, NAS, and further security detection experiments when there is evidence and a bounded test plan.
7. Select a repository license and confirm which professional contact links may be published.

## Status vocabulary

| Status | Meaning |
| --- | --- |
| Completed learning lab | The owner reports that the named study phase is complete; it does not imply a service remains deployed. |
| Previously configured | The owner reports a past setup or test; present state is unverified until dated evidence is recorded. |
| Research only | Sources or requirements were reviewed; software was not installed or exercised. |
| Planned | Future work with no implementation or test result claimed. |
