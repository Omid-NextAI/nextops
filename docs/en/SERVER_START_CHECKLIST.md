# Server start checklist

**Status: existing controlled deployment; not production acceptance or permission for a new
change.** The four guests and controlled application, AI, connector and Zabbix services already
exist. The [release manifest](../status/current-release.yaml), [project state](../PROJECT_STATE.md)
and [next task](../NEXT_TASK.md) identify the serving releases and open gates. This checklist is
for an approved change to those existing guests or a separately authorized rebuild. It does not
authorize target access, package installation, network changes, reboot, VM creation or storage work.

## What to do first

Start with the **private approved change record for the existing `nextops-app` guest**: exact
candidate, change ID and window, named operator and rollback owner, verified rollback access and
last-known-good artifact, then fresh preflight. The corrected `d973785` application wheel passed
a desktop Ubuntu 24.04.5 package-install/import check; it is unsigned and **not deployed**. The
serving `01755d1` application failed the held-out answer-semantic gate. Do not promote the
candidate or run a live qualification solely because its source and local tests pass.

The four-guest profile below is the **existing controlled baseline**, not a VM-creation order:

| Existing guest | vCPU | RAM | Disk | Controlled role |
|---|---:|---:|---:|---|
| `nextops-app` | 8 | 32 GiB | 200 GiB | TLS/UI/API, durable audit, restricted NextOps PostgreSQL |
| `nextops-ai` | 24 | 128 GiB | 500 GiB | Local CPU inference only |
| `nextops-connectors-ro` | 4 | 8 GiB | 80 GiB | Isolated read-only connector boundary |
| `zabbix-server` | 4 | 16 GiB | 200 GiB | Dedicated Zabbix and separate PostgreSQL |

The baseline totals 40 vCPU, 184 GiB RAM and 980 GiB of VMDKs. DS-C was the initial
capacity-based proposal, not a current free-space or storage-health observation. Reconcile the
existing allocations and refresh capacity for any approved storage change; never create these
guests again to satisfy a stale checklist. The original creation sequence remains in the
[server plan](SERVER_PLAN.md) for rebuild planning.

## 1. Open the private change record

Use the approved private record outside Git. Resolve the `required_inputs` keys for the
specific operation from `deploy/server-dependencies/`; do not fill a missing value by inference.
At minimum, record privately:

- approver, operator, authorized actions, maintenance window, stop conditions, and
  rollback owner;
- actual VM names, datastore mapping, addresses, DNS names, VLAN/firewall sources,
  administrator route, recovery-console route, and SSH host keys;
- exact Ubuntu image/checksum, VM hardware compatibility, firmware, Secure Boot decision,
  virtual NIC/storage controllers, thin/thick policy, and guest disk layout;
- current available CPU/RAM, reservations, contention, current DS-C free space, thin-disk
  commitments, snapshot/consolidation needs, ESXi swap placement, and storage health;
- local DNS/time/PKI dependencies, certificate renewal/revocation, package source,
  backup destination, restore staging, RPO/RTO, and monitoring route;
- reference identifiers for secrets. Never copy a password, token, private key, recovery
  secret, real address, datastore UUID, or route into this repository or a model prompt.

For an approved storage change, preserve the approximately 900-GiB DS-C free-space target after
all commitments and overhead. Count VMX files, snapshots, staging/restore copies, growth and
powered-off VM swap without double counting current usage. Do not shrink, delete, migrate,
repartition or change a memory reservation as part of this checklist.

## 2. Pass the host-side gate for an approved change

Using only the authorized read-only ESXi/management interface, confirm:

1. The target is the intended existing VM, with its identity and rollback route reconciled.
2. Current CPU, memory, datastore, storage-health, and outstanding-commitment evidence is
   fresh for the change window.
3. The existing VM compatibility level and guest CPU exposure remain supported by ESXi 8.0.3;
   ESXi itself remains unchanged.
4. Management access, console rollback and local DNS/time work without public Internet. Record
   independent-backup status separately; the owner's recovery deferral does not make it passed.
5. The approved network rules provide only the flows in each server dossier. The app and
   model server have no direct target-management access; only the connector boundary has
   narrowly approved routes and credentials.

Stop if authorization is absent, evidence is stale, the target cannot be reconciled, storage
health is unknown, the DS-C margin would be breached, or rollback access is unavailable.

## 3. Run a fresh guest preflight inside the approved window

On each in-scope existing Ubuntu guest, capture these read-only checks privately after target
access is separately authorized:

```bash
cat /etc/os-release
uname -r
systemd-detect-virt
lscpu
free -h
lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS,ROTA
findmnt
df -hT
timedatectl status
sudo ss -lntup
```

Compare the result with the last accepted guest baseline: OS/kernel, CPU/RAM/disk, reviewed
mounts, trusted local time, listeners, service health and capacity. Stop on an unexplained
difference; do not normalize it away. Keep full output private because it may contain
infrastructure identifiers.

## 4. Validate a package bundle only if the approved change requires packages

The existing guests have already undergone controlled package maintenance. Do not rerun an
installer for an application-release promotion unless the approved change explicitly includes
an OS-package change. If it does, prepare the exact authenticated offline role bundle outside Git
and follow the [installer operator guide](../../deploy/installers/README.md). For the app role,
`--check` validates the bundle without applying packages or changing services:

```bash
./deploy/installers/install-nextops-app.sh --check \
  --bundle-dir /srv/nextops-bundles/nextops-app \
  --bundle-manifest-sha256 "$APP_BUNDLE_MANIFEST_SHA256"
```

Use the matching `install-nextops-ai.sh`, `install-nextops-connectors-ro.sh`, or
`install-zabbix-server.sh` entry on the other roles. Stop validation if the exact package
lock, separately approved manifest hash, or signed local repository is missing. Run
`--apply` only after separate package-installation authorization, successful Ubuntu
24.04/VMware preflight, root ownership/non-writable bundle checks, and the required
authorization marker and change ID from the operator guide. These scripts install only the
exact Ubuntu package layer: they do not initialize a database, configure or start services,
deploy NextOps, import a model, or prove a server ready.

The current server-specific holds are:

- **`nextops-app`:** preserve the serving release and restricted PostgreSQL 16 cluster until
  guarded promotion is authorized. Verify exact candidate bytes, compatible schema, private
  credentials, last-known-good link and rollback access. The candidate's local install is not
  a passing live answer, WAN-isolation or restart result.
- **`nextops-ai`:** preserve the pinned CPU-only llama.cpp runtime and model, service limits and
  internal authentication. A change to either artifact requires its own hashes, license review,
  measured bilingual quality/latency and rollback; do not add GPU or cloud fallback.
- **`nextops-connectors-ro`:** preserve read-only method and target scope, process egress limits,
  protected runner credentials and audit. Do not broaden routes or expose a target credential
  to the app, browser or model.
- **`zabbix-server`:** preserve its dedicated PostgreSQL 16 cluster and service ordering. No
  disk/database initialization or LVM command is part of application promotion. A rebuilt disk
  needs separate exact-device evidence and destructive authorization.

## 5. Do not call a serving VM “production ready”

The controlled deployment has evidence for several earlier gates, but the serving application's
held-out answer semantics failed. The corrected candidate still needs an approved guarded
promotion, exact-code-digest correlation, human bilingual evidence review, and same-release WAN,
restart and rollback qualification. Independent backup and isolated restore, certificate
notification/rotation, host network policy, release integrity and named sign-off remain open.
Neither a healthy listener nor CI alone upgrades a gate or authorizes a server action.

Return a sanitized summary containing the change identifier, timestamps, actual resource
values, guest OS/kernel, mount verification, local dependency reachability, backup/restore
status, each acceptance result, deviations, and rollback outcome. Store raw infrastructure
output and all secrets only in the approved private system.

The source of truth for each machine is its YAML dossier and the paired
[deployment-dossier guide](DEPLOYMENT_DOSSIERS.md). The detailed Zabbix disk and service
plan is in [ZABBIX_SERVER](ZABBIX_SERVER.md).
