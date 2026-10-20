# Raspberry Pi and Pi-hole

## Overview

Owner-provided notes describe a Raspberry Pi 4 Model B with 4 GB RAM, Debian 13 ARM64, and Pi-hole as a local DNS filtering service. They also report SSH key authentication, UFW, Fail2ban, Wake-on-LAN, and a local dashboard. Current versions, service reachability, DNS upstream, firewall rules, and the Pi's exact network attachment have not been checked.

### Raspberry Pi service map

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Inter, Segoe UI, sans-serif","primaryColor":"#e8f5f7","primaryTextColor":"#18323d","primaryBorderColor":"#197f91","lineColor":"#49616e","secondaryColor":"#eef1f6","tertiaryColor":"#ffffff"}}}%%
flowchart TB
  CLIENT["LAN DNS clients<br/>client inventory not supplied"] -->|DNS query| PI
  subgraph PI["Raspberry Pi 4 Model B · owner-reported"]
    OS["Debian 13 ARM64<br/>4 GB RAM"] --> DNS["Pi-hole<br/>local DNS filtering reported"]
    SSH["SSH key authentication reported"]
    FW["UFW and Fail2ban reported"]
    DASH["Local dashboard reported"]
    WOL["Wake-on-LAN reported"]
  end
  PI -. "physical network link not recorded" .-> LAN["Home LAN"]
  classDef reported fill:#e8f5f7,stroke:#197f91,color:#18323d;
  classDef unknown fill:#fff3e3,stroke:#b76819,color:#4a301c,stroke-dasharray:3 3;
  class CLIENT,OS,DNS,SSH,FW,DASH,WOL reported;
  class LAN unknown;
```

## DNS flow

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Inter, Segoe UI, sans-serif","primaryColor":"#e8f5f7","primaryTextColor":"#18323d","primaryBorderColor":"#197f91","lineColor":"#49616e","secondaryColor":"#eef1f6","tertiaryColor":"#ffffff"}}}%%
flowchart LR
  CLIENT["LAN client"] -->|DNS query| PI["Pi-hole on Raspberry Pi<br/>service reported"]
  PI -->|Allowed query · upstream not recorded| UPSTREAM["Upstream DNS resolver<br/>not documented"]
  UPSTREAM -->|DNS response| PI
  PI -->|Filtered or forwarded answer| CLIENT
  PI -. "blocking lists and resolver configuration not supplied" .-> UNKNOWN["Configuration evidence needed"]
  classDef reported fill:#e8f5f7,stroke:#197f91,color:#18323d;
  classDef unknown fill:#fff3e3,stroke:#b76819,color:#4a301c,stroke-dasharray:3 3;
  class CLIENT,PI reported;
  class UPSTREAM,UNKNOWN unknown;
```

- [Network topology](../networking/topology.md)
- [Hardening record](../security/hardening.md)

## Objectives

- Provide a local DNS filtering service for authorized home clients.
- Practice administration of a small ARM64 Linux node.
- Document the DNS path, service health, security controls, and restore process without exposing local identifiers.

## Configuration and evidence status

The owner reports a Pi-hole installation and previous service tests. No Pi-hole version, upstream resolver, blocklist configuration, DHCP role, query sample, uptime result, or backup was supplied. The diagram marks those details as unknown rather than filling them in.

## Proposed validation

When the device is available, record its service version and test one synthetic domain query from a LAN client. A future runbook may use a placeholder form such as `dig example.org @<PIHOLE_LAN_ADDRESS>`; replace the placeholder locally and redact the address and client identity from public evidence. Confirm both an allowed response and a deliberately blocked test domain from a maintained test list before describing filtering as verified.

No such command was run for this portfolio.

## Security and recovery

- Restrict the DNS and administration interfaces to the intended LAN segments.
- Confirm whether the Pi provides DHCP before changing DNS settings elsewhere.
- Keep SSH keys, dashboard credentials, query logs, and client inventories private.
- Back up Pi-hole configuration through its supported method and test restore to a separate instance before claiming recovery.
- Review update cadence, local firewall rules, and Fail2ban status as described in [Linux hardening](../security/hardening.md).

## Problems and lessons

No Pi-hole incident or measured DNS availability was supplied. The key documentation improvement is to retain a redacted before/after DNS test and identify the upstream resolver and DHCP owner in private notes, then publish only non-sensitive configuration facts.

## Screenshots

No screenshot was supplied. Follow the [capture checklist](../media/capture-checklist.md) before adding any dashboard image.

## References

- [Pi-hole documentation repository](https://github.com/pi-hole/docs)
- [Pi-hole project](https://github.com/pi-hole/pi-hole)
