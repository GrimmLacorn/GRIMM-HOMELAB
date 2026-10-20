![GRIMM HOMELAB — laboratoire d'infrastructure auto-hébergée, réseau et cybersécurité](assets/branding/hero-banner.svg)

# GRIMM HOMELAB

> Laboratoire personnel d'infrastructure auto-hébergée, de réseaux et de cybersécurité

![Monogramme GRIMM](assets/branding/logo.svg)

[English version](README.md) · [Index documentaire](docs/README.md) · [Feuille de route](ROADMAP.md)

GRIMM HOMELAB est un portfolio personnel d'ingénierie consacré à la construction, à la sécurisation, à la supervision et à la documentation d'un homelab aux ressources limitées. Il suit des travaux pratiques sur Linux, Proxmox VE, les réseaux, les services auto-hébergés, la supervision de sécurité et l'automatisation.

> **État des preuves :** les caractéristiques du matériel et des services ci-dessous proviennent de notes historiques fournies par le propriétaire. Elles n'ont pas été vérifiées sur les équipements actifs pendant cette mise à jour. Chaque page distingue les travaux rapportés, les recherches vérifiées et les expérimentations futures. Aucun mot de passe, clé privée, adresse réseau ou résultat OSINT réel ne doit être publié.

## En bref

- **Hôte de virtualisation :** ordinateur de bureau recyclé, Proxmox VE, 16 Go DDR4, NVMe de 500 Go, NVIDIA GTX 1660 Super.
- **Nœud périphérique :** Raspberry Pi 4 Model B, 4 Go de RAM, Debian 13 ARM64 et Pi-hole rapportés.
- **Services précédemment configurés :** Vaultwarden derrière Caddy en HTTPS local; Uptime Kuma dans un conteneur LXC.
- **Apprentissage terminé :** fondamentaux du SIEM Wazuh et premières expérimentations de déploiement sous Ubuntu Server. Aucun Wazuh permanent n'est déclaré.
- **Recherche uniquement :** étude du dépôt Eye of God et de l'architecture/matériel RuView. Aucun des deux outils n'a été exécuté.

## Domaines techniques

| Domaine | Technologies et sujets |
| --- | --- |
| Virtualisation | Proxmox VE, machines virtuelles KVM, conteneurs LXC |
| Systèmes | Debian, Ubuntu Server, administration Linux, ARM64 |
| Réseaux | Routage domestique, Ethernet, DNS, dépannage Wi-Fi, analyse des pertes de paquets |
| Sécurité | Clés SSH, UFW, Fail2ban, HTTPS, contrôle d'accès, protection de la vie privée |
| Supervision | Uptime Kuma; Prometheus, Grafana et Alertmanager prévus |
| Automatisation | Ansible, Docker Compose et Infrastructure as Code prévus |
| Auto-hébergement | Vaultwarden, Caddy, Pi-hole |
| Opérations de sécurité | Architecture Wazuh, collecte de journaux, triage d'alertes, concepts FIM et détection de vulnérabilités |

## Vue de l'infrastructure

La documentation reprend le chemin réseau historique rapporté : routeur Internet → répéteur Wi-Fi → switch Ethernet → ordinateur Proxmox. Une liaison Ethernet directe est une amélioration envisagée pour la fiabilité. Le raccordement physique exact du Raspberry Pi et l'accès actuel à ses services ne sont pas documentés.

Le schéma principal apparaît dans la section correspondante de la [version anglaise](README.md#infrastructure-overview). Voir aussi la [vue d'ensemble](docs/architecture/overview.md), la [topologie réseau](docs/networking/topology.md) et l'[inventaire Proxmox](docs/infrastructure/proxmox.md). Les sources Mermaid sont conservées dans les pages Markdown qui les affichent.

## Projets

| Projet | Statut | Documentation |
| --- | --- | --- |
| Proxmox VE | Configuré auparavant, selon le propriétaire | [Infrastructure et virtualisation](docs/infrastructure/proxmox.md) |
| Raspberry Pi et Pi-hole | Configurés auparavant, selon le propriétaire | [Services du Raspberry Pi](docs/services/raspberry-pi-pihole.md) |
| Vaultwarden et Caddy | Déploiement antérieur rapporté; état actuel non vérifié | [Flux HTTPS et points de contrôle](docs/services/vaultwarden-caddy.md) |
| Uptime Kuma | Première configuration de supervision rapportée | [Compte rendu de supervision](docs/services/uptime-kuma.md) |
| Durcissement Linux | Clés SSH, UFW et Fail2ban rapportés sur le Pi | [Notes de sécurité](docs/security/hardening.md) |
| SIEM Wazuh | Apprentissage terminé; pas de service permanent déclaré | [Architecture, essais et leçons](docs/wazuh-lab/README.md) |
| Recherche OSINT | Recherche uniquement; aucun outil exécuté | [Étude d'Eye of God et RuView](docs/osint-lab/README.md) |
| Observabilité et automatisation | Prévues | [Observabilité](docs/future/observability.md) · [Automatisation](docs/future/automation.md) |

## Sécurité et dépannage

Le portfolio distingue les contrôles rapportés par le propriétaire des configurations vérifiées. Les notes actuelles décrivent des clés SSH, UFW et Fail2ban sur le Raspberry Pi, ainsi que HTTPS local pour Vaultwarden. Les règles de pare-feu, les mises à jour, la restauration des sauvegardes, TLS, l'exposition réseau et les alertes doivent encore être étayés par des preuves datées avant d'être présentés comme actuels.

Des investigations antérieures ont relevé des pertes de paquets vers la passerelle et Internet. Le répéteur est une hypothèse à tester, pas une cause établie. Le [compte rendu de dépannage](docs/troubleshooting/network-instability.md) conserve cette distinction et propose des mesures pour comparer une future liaison Ethernet.

## Apprentissage Wazuh

La page Wazuh explique le chemin agent → manager → indexer → tableau de bord, les concepts SIEM, le contrôle d'intégrité des fichiers, la détection de vulnérabilités et le triage d'alertes. Le propriétaire rapporte une première expérimentation sous Ubuntu Server avec une pression sur la RAM et le swap. La version Wazuh, les composants utilisés, les mesures et les sorties de tests n'ont pas été fournis; aucune fonctionnalité exécutée n'est donc revendiquée.

## Recherche OSINT

Le nom « Eye of God » est ambigu. Le dépôt GitHub étudié, `RykerWilder/eye-of-god`, est un tableau de bord OSINT auto-hébergé dont les fonctionnalités sont décrites par son auteur; rien ne permet de confirmer qu'il s'agit du même service que le bot Telegram russe parfois traduit par « L'Œil de Dieu ». Le code et la documentation ont été examinés, mais pas exécutés. Toute expérience future devra porter sur des données synthétiques, les comptes du propriétaire ou un périmètre autorisé documenté. RuView est présenté comme une recherche de détection Wi-Fi sensible à la vie privée, pas comme un service déployé.

## Leçons et feuille de route

Les principales leçons d'ingénierie sont de mesurer avant d'attribuer une cause, de prévoir les ressources avant d'exécuter une pile SIEM, de maîtriser l'exposition des services et de documenter des preuves reproductibles sans divulguer de données privées. La [feuille de route](ROADMAP.md) sépare apprentissages terminés, configurations antérieures, recherches et travaux prévus.

## À propos

Le propriétaire est diplômé d'un BUT Informatique, parcours administration, déploiement et sécurité des systèmes, et poursuit une formation supérieure en administration d'infrastructures sécurisées et cybersécurité. Ce portfolio documente son apprentissage personnel et sa pratique technique. Aucun lien de contact public n'a été fourni.

## Documentation et qualité

Commencer par l'[index documentaire](docs/README.md). Les consignes réutilisables pour Codex figurent dans [AGENTS.md](AGENTS.md) et `.agents/skills/`. Les contrôles documentaires locaux utilisent les versions exactes enregistrées dans `package-lock.json`; les workflows GitHub disposent uniquement d'un accès en lecture au dépôt.

## Licence

Aucune licence générale n'a été choisie pour ce dépôt. Les projets cités conservent leurs licences propres; les dépôts Eye of God retenu et RuView déclarent actuellement MIT. Une licence devra être choisie avant d'autoriser la réutilisation du code ou les contributions externes.
