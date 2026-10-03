# Saved conversations: operation and qualification

[فارسی](../fa/CONVERSATIONS.md) · [Specification](CONVERSATION_MEMORY_SPEC.md)

Controlled live release 69c9260, 2026-10-03: saved standard chat is enabled; thinking is disabled
at both application and inference boundaries after failed live trials. Configured context is 16,384
tokens with actual local template/token admission. Full-budget context quality/latency is not qualified.
The UI/UX workflow guided keyboard-accessible history controls; OCS brand assets are unchanged.
The named-server repair does not train the model or certify general technical accuracy. Persian
identifier-only replies retained the correct ID but violated the requested format on both this
release and the rollback baseline; that quality gate remains unaccepted. See [testing](TESTING.md).

The 2026-10-03 full-adapter qualification failed the near-16K 120-second deadline. Source-only
format/envelope repairs passed four narrow format checks but failed technical semantic review;
they do not enable the serving flag. Standard browser recovery and two audit checks passed.
The private opt-in runner exits 1 for measured failure or 2 for partial diagnostics pending
semantic/matched application acceptance; a native completion never means feature acceptance.

## User behavior

Source-only repair: [CAP-01–CAP-06](AI_CAPABILITY_SPEC.md) adds task-adaptive guidance and skips
oversized history pairs in favor of older fitting pairs, without clipping. It supplies the existing
omission flag internally. Transcripts, browser controls, budgets and provenance do not change.
This is not yet live.

General chats are saved in local PostgreSQL for your account. Choose
a conversation in the sidebar to resume it. New conversation does not delete old chats; Delete
this conversation explicitly removes its transcript. Logout clears private page content and the
browser token, not saved history. Do not paste passwords, keys or other secrets.

The page displays at most 12 exchanges. API pages contain at most 20, with a before_sequence cursor.
The model sees at most six complete accepted pairs, within 12,000 characters; an omission notice
means you must restate missing details. Old saved answers are not fresh generations. General
memory is not proof of current server status; live modes still fetch fresh scoped evidence.

Standard is the only enabled choice. Think more remains hidden and denied by the API. If a future
separate qualification enables it, its private
reasoning is discarded; only a final answer is displayed/saved. It may be slower or still wrong.
This is inference and conversation storage, not model training.

## API and configuration reference

All routes require a current bearer session. IDs alone grant no access.

| Route | Contract |
| --- | --- |
| GET /api/v1/conversations/config | Enabled/thinking flags, context and retention bounds |
| POST /api/v1/conversations | locale; creates owner-scoped empty chat |
| GET /api/v1/conversations | At most 50 owner summaries, newest first |
| GET /api/v1/conversations/{id} | Last 20 pairs; optional before_sequence 1–101 |
| POST /api/v1/conversations/{id}/messages | request_id UUID, locale, question 1–4000, thinking boolean |
| DELETE /api/v1/conversations/{id} | Explicit transcript deletion; audit metadata remains |

Legacy /assistant/generate and live contracts keep their existing public limits. Completed
request retries return the same saved response. Concurrent requests conflict; provider failure
clears the pending lease if the same session is still valid. A crash/cancelled request expires
after 540 seconds; no unbounded automatic retries are introduced.

Serving app flags: NEXTOPS_CONVERSATIONS_ENABLED=1; NEXTOPS_CHAT_THINKING_ENABLED=0.
Serving AI flags: NEXTOPS_EXPANDED_CHAT_ENABLED=1; NEXTOPS_THINKING_ENABLED=0;
NEXTOPS_CONTEXT_TOKENS=16384 must match actual runtime n_ctx. Defaults are disabled/8192.
Keep existing 120-second generation deadline for initial qualification; a separate measured profile
decision is required if expanded replies fail it. Never widen deadlines to relabel a failed test.

## Promotion and rollback sequence

1. Preserve the exact serving app, AI API, model-selection file/drop-in and artifact hashes.
2. Apply additive Alembic migration 0003 with the protected migration role in the existing reviewed
   deployment workflow. Do not pass a secret-bearing database URL on a command line.
3. Install the exact tested app/AI package with flags disabled. Existing paths must still pass.
4. Qualify the thinking runtime drop-in at 16384 context, 16 threads, one slot, zero GPU layers,
   384 reasoning tokens and no reasoning preservation. The first 1024-token trial hit an unrelated
   30-second proxy timeout and continued to the 120-second provider deadline without a final answer.
   The corrected 384-token trial also failed at 120 seconds; a separate 128-token direct probe
   did not produce an accepted final answer. Do not enable thinking or claim its budget is qualified.
   Only the default non-thinking path is selected. Native restrictions
   remain inherited; no runtime download option is present. Real template/tokenization passed on
   the current exact runtime; this did not generate or qualify a thinking answer.
5. Enable matched flags only after EN/FA relevance, follow-up, provenance separation, latency,
   failure, authorization, offline and rollback checks. Record exact release identities and results.
6. Roll back by disabling flags and restoring exact previous app/AI/runtime profiles. Leave tables
   intact to preserve transcripts; destructive downgrade requires an export and separate approval.

The saved-message route must inherit the existing inference proxy policy: 180-second proxy
transport timeout and the same request rate limit, not the generic 30-second page timeout.
This does not change the 120-second model deadline, queue bounds or authentication. Preserve and
restore the exact previous proxy configuration when rolling back this matched deployment.

The research-only 122B record pins two shards totaling 77,616,511,296 bytes. Its conversion lineage,
bytes, template, CPU latency and quality are not verified. More assigned vCPUs do not justify more
threads automatically. Current guest preflight: 64 vCPUs, 193185 MiB usable RAM, one guest NUMA node;
actual host placement/reservations remain unknown. Do not resize again before benchmark evidence.
