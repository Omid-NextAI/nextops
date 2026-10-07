# Operations, observability and disaster recovery

[فارسی](../fa/OPERATIONS.md) · [Index](INDEX.md)

## Recorded controlled release — 2026-10-07

The [release manifest](../status/current-release.yaml) and
[project state](../PROJECT_STATE.md) record app `48e3a8a`, AI API `ec1ed32` and connector/MCP
`2a7c8dc`. The app serves the supplied OCS identity, static login and compact conversation
workspace. Native Qwen3.8-27B Q8/no-BLAS remains selected with the recorded owner quality
exception; this interface rollout did not replace its runtime/model, credentials or schema.
The [OCS live qualification](../requirements/OCS_UI_LIVE_QUALIFICATION_2026-10-07.md) records
bounded app checks, saved follow-up, fresh secondary evidence and exact app rollback. The
[earlier capability qualification](../requirements/UI_QWEN38_SOURCE_QUALIFICATION_2026-10-07.md)
is separate evidence. Failed harness reports and the observed inference 504 remain in those
records; broad semantics, thinking/privacy/full-context and current WAN/VM/load gates are not
accepted. Controlled user testing is not production acceptance; independent recovery remains
owner-deferred, not qualified by VM snapshots.

The owner-authorized [audit repair](../requirements/AUDIT_REPAIR_2026-10-07.md) is source
implementation and qualification in progress, not a new deployment. Do not substitute its
fixture results for serving-host checks or reuse a completed window's rollback guard. Any
promotion needs current preflight, exact artifacts, compatible role ordering and verified
rollback. For a presentation-only issue, do not roll back the MCP gateway/runner or model.

## Historical app-only UI release — 2026-10-05

On 2026-10-05, app `836b1ea` served the reference UI; connector `2a7c8dc` and inference `7ce9d29`
were unchanged. These are historical identities, not the recorded current release above.
The [dated record](../requirements/REFERENCE_UI_LIVE_QUALIFICATION_2026-10-05.md) identifies the
immutable artifacts and tested app-only `2a7c8dc` rollback. Protected qualification scripts and
reports are retained; the completed window's rollback timer is stopped. A future rollback requires
a new authorized window and current checks, not blind reuse of an old timer. Do not perform the
MCP gateway/runner rollback below for a presentation-only issue. No new migration or policy change
was required for that UI release. Qwen upgrade was a separate capacity/qualification checkpoint.

## Controlled MCP operations — 2026-10-04

The existing connector guest serves `nextops-mcp.service` and `nextops-source-runner.service`;
`nextops-connector.service` is disabled. App source selection and protected deployment identities
are documented in [MCP](MCP.md) and the [live record](../requirements/MCP_LIVE_QUALIFICATION_2026-10-04.md).
For matched rollback restore connector release/SSH restrictions first, then app/tunnel/Nginx.
Restart the app tunnel after connector restoration if the order differs; an existing SSH connection
retains its earlier forwarding restrictions. Verify fresh authenticated primary evidence, not just
healthz. Retain additive migration 0004 and accounts. Do not expose target tokens in the app/gateway,
re-enable HTTP as an automatic fallback, or treat temporary WAN qualification as permanent firewall
policy. Runtime/model and their rollback records are unchanged.

**Status: the controlled services are installed and logical isolated restore has passed; no independent backup job or disaster-recovery procedure exists.** Restart, rollback, failure recovery, bounded load and socket-only restores of both PostgreSQL 16 databases passed. Independent storage, WAL/PITR, artifact recovery and disaster recovery remain open. See the [backup specification](BACKUP_RESTORE_SPEC.md) and [Stage 1 report](STAGE_1_COMPLETION_REPORT.md).

## Environments and service boundaries

Use separate development, staging and production identities, databases, volumes, ports and inventories. On one G10 these remain one physical failure domain. Only intended UI ingress is exposed; inference, database, MCP and telemetry administration remain internal. Verify container and host rules together rather than assuming every published port is protected.

Use restricted users/capabilities, bounded resources and reviewed restart policies. Lifecycle scripts must be idempotent, preflight changes, protect existing services and avoid secret output. Do not change SSH/firewalls, reboot or reformat without explicit authorization and recovery access. Serialize migrations.

## Controlled SSH and host firewall

The four serving guests now install `deploy/ssh/00-nextops-hardening.conf` before the cloud-init
drop-in. It requires public keys, denies passwords and keyboard-interactive authentication, and
disables direct root login. Operators use their named key-authenticated account and `sudo`; service
tunnels retain their separate restricted keys. For a reviewed change, retain a working session and
an automatic rollback timer, run `sudo sshd -t`, reload SSH, and prove a **new** key-only login
before cancelling rollback. Check effective settings with:

```bash
sudo sshd -T | grep -E '^(permitrootlogin|passwordauthentication|kbdinteractiveauthentication|authenticationmethods) '
```

The expected values are `no`, `no`, `no`, and `publickey`, respectively. Restart and verify the
application-to-AI and application-to-connector tunnel services after SSH changes; existing SSH
sessions alone are not evidence that new handshakes work. The AI guest now has active UFW with
deny-incoming/OpenSSH and no externally bound AI/model listener. The historical four-guest
WAN-disconnection test used a temporary outbound policy, not a permanent firewall rule:
administrator shells can currently reach public IPv4, while the app/AI/model service units deny
non-loopback IP traffic. Recheck login, AI readiness, Zabbix evidence and the direct Linux collector
after firewall changes. A permanent host-wide egress policy needs an explicit DNS/time/proxy
allowlist and guarded rollout. Do not infer that the current OpenSSH allow rule is a final approved
management-network allowlist.

## Connector-only egress boundary

The credential-holding connector now uses a systemd IP policy that denies every destination except
loopback and the reviewed, deployment-specific LAN range. Render
`deploy/systemd/nextops-connector-egress.conf.template` from the protected target inventory;
never commit the real range or blindly use a broad RFC1918 allowlist. Install it as a root-owned
service drop-in, validate with `systemd-analyze verify` and `systemctl show` for
`IPAddressDeny`/`IPAddressAllow`, then restart the connector under a timed rollback guard. Exercise
the Zabbix API and all approved direct Linux targets with fresh authenticated investigations
before cancelling rollback. This process policy does not block administrator-shell or other
host-wide Internet access.

## Offline Zabbix Agent 2 patching

The app, AI and connector guests have no configured Zabbix apt origin. Their Agent 2 `7.0.31`
packages were imported from the Zabbix guest's configured repository cache after matching the
exact package SHA-256 to its apt metadata. Keep the prior and candidate `.deb` files and a
configuration snapshot in a root-only change directory. Simulate first, install guests serially
with `dpkg --force-confold -i` under a timed rollback guard, and compare the configuration hash.
Require `zabbix_agent2 -V`, an active unit, no passive port `10050`, fresh Zabbix data, no new
warnings and no failed units before cancelling rollback. A zero `apt list --upgradable` result on
these guests does not detect a future Agent 2 release.

## Observe the platform itself

Track API/worker/connector health, durable queue age, collection failures, inference queue/TTFT/tokens, CPU/RAM/swap pressure, database state, audit failures, storage growth, backup age and restore-test status. Use structured logs, metrics and justified traces without hosted telemetry dependence. Avoid sensitive prompts and unbounded asset/user identifiers in metric labels.

Distinguish host health, application readiness, model readiness and each connector's actual capability. Ordinary logs support diagnosis; security audit provides a separate record of authorized decisions and effects.

## Local certificate lifecycle

The application and Zabbix TLS frontends use the same offline-safe certificate check. A persistent
daily timer runs `scripts/check_certificate_expiry.py` under the dedicated non-login
`nextops-certcheck` identity. It reads only the public certificate, calls the pinned local OpenSSL
binary, emits bounded JSON without names or addresses, and fails when the certificate is not yet
valid, expired, or within the configured warning window. The controlled warning window is 90 days.
The private key remains root-only and is never an input to the checker. See the
[certificate lifecycle specification](../requirements/CERTIFICATE_LIFECYCLE_SPEC.md).

Install the reviewed script, unit and timer from a verified release; create the dedicated identity;
and give it traverse/read access only to the certificate directory and public certificate. Keep the
key at `root:root` mode `0600`. Place the role-specific certificate path, bounded label and warning
days in root-owned `/etc/nextops/certificate-check.env`, then run:

```bash
systemd-analyze verify /etc/systemd/system/nextops-certificate-check.service \
  /etc/systemd/system/nextops-certificate-check.timer
systemctl daemon-reload
systemctl enable --now nextops-certificate-check.timer
systemctl start nextops-certificate-check.service
systemctl status --no-pager nextops-certificate-check.service \
  nextops-certificate-check.timer
```

An authorized rotation stages the new pair in a root-only directory, compares the public key from
the certificate with the key-derived public key, verifies the local CA chain and validity window,
and preserves the exact prior pair. Validate Nginx before atomic promotion; reload rather than stop;
then prove an ordinary TLS handshake, fresh offline login and Zabbix HTTPS/API access. On any
failure, restore the preserved pair, revalidate Nginx, reload and repeat the client checks. Do not
disable hostname/expiry validation or fetch a certificate during runtime. The controlled deployment
feeds service result and timer state to four one-minute active-agent items and six tagged local
Zabbix triggers; a guarded timer outage and recovery passed. This proves local detection and problem
state, not operator delivery. Production sign-off still requires an approved notification route
plus an observed rotation and rollback exercise.

## Degraded operation

| Failure | Required behavior |
|---|---|
| Model absent/saturated | Keep API, audit and manual evidence views usable; queue/reject work within limits |
| Connector fails | Return typed partial results; isolate the failure; bounded eligible-read retries |
| Database unavailable | Do not pretend jobs or approvals are durable; expose degraded readiness |
| Audit unavailable | Block mutations and alert; never silently drop the record |
| Mutation timeout | Mark unknown outcome; reconcile target state before retry |
| Host loss | Recover from independent backups and external recovery instructions |

Alert-storm handling deduplicates and groups evidence before expensive synthesis. Required outage notifications need a path outside the failed host.

## Backup and restore

Back up PostgreSQL consistently, permitted sanitized evidence, non-secret configuration and model manifests. Keep encryption recovery material in a separate protected process. Models can be re-imported only when documented in the recovery plan. Encrypt backup artifacts, define retention and access, and test restoration in an isolated environment.

An independent off-host destination is a production decision. A second partition, local directory or container on the G10 is staging, not disaster recovery. Define proposed recovery point/time objectives, then measure them in a restore drill. Validate restored identity, authorization, evidence references, audit continuity and keys; protect against accidentally connecting the restored test instance to production assets.

## Release and rollback

Promote verified artifacts explicitly. Record release identity and configuration/model/schema compatibility, take required backups, run serialized migrations and verify health. Rolling back an image is not a schema rollback. Prefer compatible expand/contract changes or a tested restore path when needed. Compensation on remote equipment requires separate authorization and may not be possible.

The operational handover must include offline bundle contents/checksums, clean-start procedure, monitoring ownership, recovery access, backup destination, retention, measured limits, known single-host risks and a dated readiness decision.
