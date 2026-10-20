# Screenshot and evidence capture checklist

No genuine screenshots were supplied for this portfolio. No synthetic dashboards or mock screenshots have been created.

## Candidate screenshots

- **Proxmox:** node summary and a sanitized VM/LXC inventory. Hide hostnames, guest IDs if not public, storage labels, IPs, and browser URLs.
- **Raspberry Pi / Pi-hole:** Pi-hole version/about or status page and one synthetic DNS test. Hide client names, query history, local domains, and IP addresses.
- **Vaultwarden / Caddy:** browser certificate summary for a local test hostname and redacted service status. Never show vault contents, login names, URL tokens, or certificate private keys.
- **Uptime Kuma:** one sanitized monitor status page. Hide target URLs, headers, ping payloads, and notification destinations.
- **Wazuh:** one version page or synthetic alert in a disposable lab, with agent identities and local host data redacted.
- **Network troubleshooting:** a small table of date, path, probe count, loss, and latency. Do not publish packet captures or public IP details.

## Before adding an image

1. Capture it from the real application or device; do not redraw a UI as if it were evidence.
2. Remove browser tabs, names, addresses, user identifiers, real query data, tokens, and secrets.
3. Preserve a private original and publish only the reviewed redacted export.
4. Add alt text, date, software version, test scope, and a short note about what the image demonstrates.
5. Verify the export contains no hidden metadata or private identifiers.
