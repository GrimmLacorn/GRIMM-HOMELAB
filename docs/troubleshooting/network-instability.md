# Network instability investigation

## Incident summary

Owner-provided notes describe intermittent packet loss toward the local gateway and Internet connectivity. Ping checks were used, a Wi-Fi repeater was in the historical path, and possible Proxmox impact was considered. The dates, commands, outputs, host state, and results were not supplied.

**Status:** historical investigation; cause unknown. The repeater and Proxmox are hypotheses to evaluate, not confirmed causes.

- [Historical and proposed network diagram](../networking/topology.md)

## Evidence table

| Observation | What it establishes | What it does not establish |
| --- | --- | --- |
| Loss toward the gateway was reported | A local-path symptom was observed at some time | Which device or link caused it |
| Internet connectivity loss was reported | An external-path symptom occurred | Whether the LAN, router, ISP, DNS, or target caused it |
| A repeater was present in the path | One wireless segment existed in the historical topology | That the repeater caused packet loss |
| Proxmox impact was investigated | Host load was considered | That Proxmox or a guest caused the symptom |

## Future test record

Use one test client and the same probe count/interval in each comparison. Record the date, approximate load, link mode, loss percentage, latency range, gateway reachability, and whether DNS resolution was separately tested. A modest set of probes is sufficient; avoid high-rate traffic.

| Comparison | Local gateway | Public IP | DNS | Notes |
| --- | --- | --- | --- | --- |
| Repeater path | Not recorded | Not recorded | Not recorded | Historical symptoms only |
| Direct Ethernet path | Planned | Planned | Planned | Run only after the cabling change is actually complete |

If gateway loss occurs on both paths, inspect cable, switch, NIC counters, and router LAN state. If gateway tests pass but public IP tests fail, investigate the WAN path. If IP reachability passes but names fail, examine DNS separately. Correlate with host load before attributing the fault to Proxmox.

## Privacy

Redact gateway addresses, public IPs, device names, MAC addresses, ISP account details, and timestamps that could reveal when the home is unattended. Do not publish raw packet captures.
