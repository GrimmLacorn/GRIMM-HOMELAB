# Target observability architecture

## Status

Prometheus, Grafana, and Alertmanager are planned projects. No exporters, dashboards, retention policy, or notification route are configured or tested in the supplied evidence.

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Inter, Segoe UI, sans-serif","primaryColor":"#e8f5f7","primaryTextColor":"#18323d","primaryBorderColor":"#197f91","lineColor":"#49616e","secondaryColor":"#eef1f6","tertiaryColor":"#ffffff"}}}%%
flowchart LR
  HOSTS["Proxmox host and selected guests"] --> EXPORTERS["Node / application exporters<br/>selection not designed"]
  EXPORTERS --> PROM["Prometheus<br/>planned"]
  PROM --> GRAFANA["Grafana dashboards<br/>planned"]
  PROM --> ALERT["Alertmanager<br/>planned"]
  ALERT --> DEST["Notification channel<br/>not selected"]
  RULES["Retention, access, and alert rules<br/>to design"] -.-> PROM
  classDef target fill:#fff9e8,stroke:#c38a19,color:#4a3812,stroke-dasharray:5 4;
  class HOSTS,EXPORTERS,PROM,GRAFANA,ALERT,DEST,RULES target;
```

- [Uptime Kuma previous setup](../services/uptime-kuma.md)
- [Proxmox resource constraints](../infrastructure/proxmox.md)

## Proposed scope

Start with a small set of host and guest health signals: CPU, memory, swap, disk capacity, filesystem usage, and service reachability. Avoid collecting personal activity or high-cardinality labels. Keep Prometheus scrape access and Grafana administration on a trusted network.

## Design questions

- Which host and guest metrics are useful enough to retain?
- What retention limit fits the NVMe and backup budget?
- Which metrics distinguish hypervisor pressure from one guest's pressure?
- Which alerts have a clear action and a known owner?
- Which notification channel can be tested without exposing credentials?
- How will configuration and dashboards be backed up and restored?

## Validation plan

In a disposable VM, verify one exporter scrape, one Grafana panel, one intentional test alert, and alert recovery. Record versions, resource use, retention, and access controls. Do not label this target operational until those checks pass on the actual lab.
