# Development, GitHub and release workflow

[فارسی](../fa/DEVELOPMENT.md) · [Index](INDEX.md)

**Status: development policy with isolated application CI and guarded package-layer
automation; complete deployment automation is not configured.** Source: master specification sections 4, 7–8 and 21–26.

## Inspect before implementation

Read [AGENTS.md](../../AGENTS.md), the master specification, project state and next task. Inspect Git status, instructions, tracked files, manifests, locks, tests, migrations and deployment definitions. Preserve dirty changes and existing implementations. Review scripts before running them in an isolated environment without production credentials. Do not use destructive reset/clean, overwrite work or rewrite history.

The repository now has typed policy/application boundaries, local identity, durable
PostgreSQL state and audit, a bounded local CPU inference path, a bilingual browser UI,
and read-only Zabbix/Linux connectors. Controlled releases serve user testing on the four
existing role guests; the exact identities and gate results are in the
[release manifest](../status/current-release.yaml). The recorded deployed baseline on 2026-10-07
is exact `52e5179` for app, AI API and canonical MCP/source runner, with matching collectors; the
[all-role live record](../requirements/AUDIT_REPAIR_LIVE_QUALIFICATION_2026-10-07.md) separates
the retained release from earlier checkpoints. Scoped diagnostic safeguards and source-scoped
MCP gateway/runner reads are deployed for controlled testing; local MCP fixture results are
not their live acceptance. See [MCP](MCP.md). Expanded raw-model semantics, thinking and
full-context acceptance remain open; current-release WAN/VM/load qualification is separate.

The owner-authorized [audit repair](../requirements/AUDIT_REPAIR_2026-10-07.md) is retained live
after exact-source CI, real bilingual evidence/saved-chat/audit checks and exact all-role rollback.
Twelve source findings are repaired; repository protection GOV-01 needs administration access.
Current source publication and architecture documentation do not redeploy servers or qualify
failed/unrun model, WAN, VM, load or recovery gates.
Guarded Ubuntu package-layer scripts and desktop offline-bundle checks exist, but they do
not grant another serving-host change or production acceptance. Phase 0 architecture was
accepted on 2026-09-21; later infrastructure operations and acceptance gates remain
separately controlled.

For the current Python slice, install the generated lock with
`uv sync --extra dev --extra mcp --frozen`, then use `uv run --frozen --extra dev --extra mcp`
before each Ruff, mypy or pytest command. Ruff covers `packages migrations tests scripts
deploy/installers`; mypy covers `packages tests scripts deploy/installers`. Run
`pytest -m "not integration and not browser" -q` for the isolated local suite. Including the
MCP extra is required for protocol-test collection and canonical gateway/runner packaging;
the ordinary app/AI dependency layer need not include it.
Add `--offline` only after dependencies are provisioned. See [exact checks](TESTING.md).
Real database acceptance additionally requires an isolated PostgreSQL URL in
`NEXTOPS_TEST_DATABASE_URL`; a skipped database suite is not a pass. Regenerate `uv.lock`
only with reviewed dependency changes and run the pinned dependency audit before release
work.

## Module discipline

Keep domain invariants independent from framework I/O; application use cases depend on ports, infrastructure implements them. Define typed contracts across API, workflow, policy, gateway and connector boundaries. Python uses type hints, clear docstrings and handled exceptions; avoid duplicated logic and giant agent/utility files. English code identifiers remain stable; user-facing documentation and product strings support Persian and English.

Create source directories, manifests and locks when the corresponding implementation begins, not as misleading placeholders. Unsupported behavior must fail explicitly rather than return simulated success in production paths.

## Reviewable GitHub delivery

Use short-lived branches, small commits, clear acceptance criteria and pull requests. Link each feature to an original requirement and phase. Update both language guides, project state, next task and traceability with each delivered increment. CODEOWNERS and templates support review; they do not prove branch protection is enabled. Protected main and review rules must be explicitly configured and verified when available.

The pinned workflow in `.github/workflows/ci.yml` runs formatting, lint, types,
unit/API and browser cases, documentation/dossier/inference/installer/release-status
validation, package build, dependency audit, full-history secret scanning, and
PostgreSQL 16/17 integration tests. It has read-only default permissions and no
infrastructure credential or management-network route. The private wheel-backed
SBOM enrichment is an offline local evidence step, not hosted CI or legal approval;
offline signing, hardware/lab acceptance, serving-host package application and
branch-protection enforcement remain separate.

Untrusted pull-request code must run in disposable isolated workers with no production secrets or management-LAN access. Never attach a privileged persistent G10 runner to arbitrary PR execution. Do not execute an untrusted checkout under `pull_request_target` with secrets. Trusted hardware tests need a separate authorized and resource-limited workflow.

## Verified repository-policy gap and owner setup

Read-only GitHub checks on 2026-09-28 at `de52e43` reported `main` as unprotected, status-check
enforcement off, and no repository or inherited rulesets. All five CI checks passed, but their
success does not enforce a merge policy. This is an open part of `release_supply_chain_review`.
The connected GitHub installation excludes administration access; no settings were changed.

The owner must approve the policy and name an eligible independent reviewer first. Current
`CODEOWNERS` names only `AmirMo10`; do not create an unfulfillable code-owner approval gate.
An authorized repository administrator can use Settings → Branches to create a classic protection
rule matching `main`. See the [GitHub setup guide](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule).
Proposed NextOps policy, not an approval:

- Require a PR, an independent approval, review again after new commits, and code-owner approval
  after reviewer eligibility is established.
- Require an up-to-date branch and these five checks from GitHub Actions: `Quality and unit tests`,
  `PostgreSQL 16 integration`, `PostgreSQL 17 integration`, `Browser acceptance`, `Secret scan`.
  The observed check source was `github-actions`, app ID `15368`; recheck it when configuring.
- Apply the restrictions to administrators; do not permit bypass, force pushes or branch deletion.

With an already approved and authenticated GitHub CLI, the owner can inspect settings read-only:

```powershell
gh api repos/Omid-NextAI/nextops/branches/main --jq '{protected: .protected}'
gh api 'repos/Omid-NextAI/nextops/rulesets?includes_parents=true'
gh api repos/Omid-NextAI/nextops/branches/main/protection
```

The last endpoint needs repository administration read permission; a permission error is not
evidence of absent protection. See the [REST permission reference](https://docs.github.com/en/rest/branches/branch-protection#get-branch-protection).
Keep tokens out of commands, Git and chat. Acceptance needs effective-setting review and an approved
non-serving PR test proving that missing review or failed checks prevent merge. Do not test by
writing directly to `main`. Repository enforcement does not sign artifacts or authorize deployment.

## Release and deployment

Tag verified releases and record application, dependency, container and model identities plus checksums and software/model bills of materials. The owner explicitly promotes a verified release; a push must not automatically deploy production. The host may pull approved artifacts through an outbound route without public SSH exposure.

Before deployment, verify artifact identity, configuration compatibility, backup state, serialized migrations and resource/port preflight. After deployment, verify health and expected behavior. Application rollback does not reverse a database migration; document schema compatibility or a tested restoration path. Offline bundles are explicit release artifacts, not runtime downloads.

## Multi-agent coordination and done

Parallel work is useful only for bounded independent tasks. The principal architect owns contracts; security reviews execution/credentials/approval; CPU/SRE reviews resources and operations; product/UX reviews native Persian and complete user flows. Use separate branches/worktrees when applicable. Do not let agents concurrently rewrite migrations, shared contracts or locks. No claim of parallel agents is permitted when tools did not run them.

An increment is complete only with functional code, boundary tests, recorded commands/results, security review, bilingual documentation, traceability and a meaningful commit. A mock is not a device test. Failed tests must be fixed or accurately reported, not weakened to make a check green.
