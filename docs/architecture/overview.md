# Physical architecture overview

## Overview

This diagram combines the physical path and virtualized services described in owner-provided notes. It is a historical record, not a live network map. The direct Ethernet route is a proposal. The Raspberry Pi's exact network attachment, the current host status, and individual VM/LXC assignments beyond the named services have not been independently verified.

- [View the physical architecture diagram in the main README](../../README.md#infrastructure-overview).
- [Network topology detail](../networking/topology.md)
- [Proxmox inventory](../infrastructure/proxmox.md)

## Reported components

| Component | Owner-provided note | Evidence still needed |
| --- | --- | --- |
| Proxmox host | Recycled desktop, 16 GB DDR4, 500 GB NVMe, GTX 1660 Super | Dated `pveversion`, storage summary, current memory and guest inventory |
| Guest systems | Multiple Debian and Ubuntu VMs and Linux containers | Redacted VM/LXC inventory and resource allocations |
| Vaultwarden | Debian 12 VM with Vaultwarden and Caddy; local HTTPS tested previously | Version, proxy topology, certificate scope, backup and recovery evidence |
| Uptime Kuma | Debian-based LXC and first monitoring setup | Version, configured monitors, test results, alert channel |
| Raspberry Pi | Pi 4 Model B, 4 GB RAM, Debian 13 ARM64, Pi-hole | Dated OS/service versions and redacted connectivity checks |

## Legend

- **Reported / historical:** supplied in project notes, not checked on a live device during this update.
- **Unrecorded:** an attachment or implementation detail is unknown; the dashed line does not imply a fault.
- **Planned:** an intended change that has not been implemented or validated.

## Next evidence capture

Capture the host and guest inventory described in the [Proxmox page](../infrastructure/proxmox.md), then update the diagram only when guest placement and network links are supported by evidence. Keep public diagrams free of LAN addresses, public IPs, hostnames, serial numbers, usernames, and authentication details.
