# Linux hardening notes

## Scope

The owner reports SSH key authentication, UFW, and Fail2ban on the Raspberry Pi, along with basic Linux hardening. These controls were not checked on a live device during this update. This page records the claims and the evidence needed to make them reproducible; it does not certify the current host as hardened.

- [Raspberry Pi service record](../services/raspberry-pi-pihole.md)

## Reported controls

| Control | Reported practice | Evidence needed |
| --- | --- | --- |
| Remote access | SSH key authentication | Effective `sshd` settings, allowed users, key rotation/revocation process |
| Host firewall | UFW | Dated ruleset and confirmation that required services remain reachable only from intended clients |
| Login protection | Fail2ban | Active jail list, log source, ban behavior, and safe recovery procedure |
| Updates | Not described | OS release, supported update channel, last update date |
| Backup | Not described | Encrypted backup scope, retention, off-device copy, restore result |

## Proposed read-only checks

On the owner-managed Pi, review the following locally before sharing any output:

```bash
sudo sshd -T
sudo ufw status verbose
sudo fail2ban-client status
systemctl --failed
```

These commands were not run for this portfolio. Redact usernames, source addresses, hostnames, and service-specific paths before publishing excerpts.

## Security review rules

- Never publish private SSH keys, recovery codes, local account names, or full firewall exports containing public addresses.
- Do not disable the firewall or password authentication as a troubleshooting shortcut without an out-of-band recovery plan.
- Record exact changes and a rollback path for future hardening experiments.
- Add a dated status to the relevant service page after tests are actually completed.
