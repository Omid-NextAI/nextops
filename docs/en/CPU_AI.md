# Local CPU-only AI and capacity planning

## Model option review and fresh guest observation — 2026-10-04

Read-only inspection now observes 80 online guest vCPUs and 135024599040 usable RAM bytes
(about 125.75 GiB), with the recorded Qwen3.5-35B-A3B runtime/model links active. This is a guest
observation, not proof of saved ESXi allocation or spare host capacity; it supersedes the older
point-in-time sizing below. No resources, runtime, model or thinking flags were changed.

The official [MiMo-V2.6-Pro-RL card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
reports 1.02T total/42B active parameters, 1M context and MIT licensing. The official
[Kimi K3 card](https://huggingface.co/moonshotai/Kimi-K3) reports 2.8T total/104B active,
1048576 context, native MXFP4 and its own license. K3 also expects preserved thinking history;
NextOps currently saves only final answers, so this is an interface/privacy design consideration,
not permission to start storing private reasoning.

Arithmetic inference, **not measured requirements**: ideal four-bit weights alone are about
510 GB/475 GiB for MiMo and 1400 GB/1304 GiB for K3, before metadata, KV/state, activations,
runtime and other guests. Active parameters reduce computation, not total stored weights. K3's
lower bound already leaves inadequate headroom on the documented host; MiMo might fit a larger
reviewed lab allocation, but usable CPU latency, artifact size and compatibility are unproven.
Neither is a qualified drop-in for the pinned CPU-only runtime. Advertised context is not an
accepted application budget, and vendor benchmarks do not establish Persian/NOC correctness.

Recommendation: preserve the serving model; first qualify an auditable CPU-compatible artifact
with frozen EN/FA/coding/live-evidence cases, measured latency/NUMA/memory, cold start, offline
behavior and exact rollback. Review license, source/revision/hash and conversion code before any
provisioning. Keep host/app/database/Zabbix capacity and storage-growth headroom; “all G10 resources”
does not imply that current co-resident services can safely lose their resources. No download,
API fallback, architecture migration or new resource allocation is authorized by this comparison.

## Current guest sizing and standard-chat profile — 2026-09-30

After the owner's resource extension, authorized read-only guest preflight observes 64 vCPUs,
193185 MiB usable RAM, zero swap use and one guest NUMA node/64 virtual sockets. This supersedes
the older AI guest allocation for current sizing, not the measured inference limits: the serving
profile has 16 threads, 16384 context, one slot, 18 CPU-quota equivalents and 96 GiB MemoryMax.
No further resize or ESXi topology change was made. Host placement/reservations remain unknown.
The [standard-chat profile](CONVERSATION_MEMORY_SPEC.md) is serving in controlled b5e74f9;
thinking failed and is disabled. Four-guest WAN/reboot and fresh short-context answers passed,
not full-budget context quality/latency. 122B is pinned research, not downloaded or selected.

[فارسی](../fa/CPU_AI.md) · [Index](INDEX.md)

**Status: bounded CPU evidence and tested native profiles; full benchmark and production acceptance remain open.** Source: master specification sections 2, 9–10 and 21. Exact bounded restart/rollback observations are recorded below. Current-release WAN/VM cold start passed; sustained expanded-profile throughput, production behavior and independent restore remain unqualified.

## Current larger-model qualification — 2026-09-29

Selected controlled profile: pinned Bartowski 35B-A3B Q4_K_M, protected immutable bytes, source
95c6e50 and unchanged llama.cpp b29c606e. Twelve API cases completed in 12.7–93.6s; twelve browser
cases and exact model/source rollback passed. Six final re-promotion confirmations and four
additional audit/hash pairs passed; their latency was 21.3–94.3s. Original 8B/source rollback is protected. GGUF architecture qwen35moe and template
SHA are recorded with trusted `enable_thinking=false` and configured context 8192. Its base-model
metadata names Qwen3.5-35B-A3B-Base; the upstream instruct reference is not verified conversion
lineage. Do not infer lineage or enlarge context to the native limit. VM/resources/one slot/queue/
384 tokens/120 seconds remain unchanged; no projector/MTP/GPU is enabled. Raw/full quality and
sustained load/NUMA/WAN/VM/production acceptance remain partial or not run. Older checkpoints:


Earlier continuation: protected 35B import passed; fourteen CPU samples stopped in 13.5–64.5s.
The first bb81109 guarded trial completed twelve API cases, but Persian CPU-idle labeling failed.
Exact rollback restored 8d1f1d2/8B; 35B is protected, not selected. Point process RSS was about
35.4 GiB; cgroup peak is not total resident RAM. VM/runtime/threads/context/queues/tokens/deadlines
remain unchanged. The source-only semantic repair requires fresh qualification. Raw provenance,
sustained/NUMA/server-WAN/VM/production gates are partial or not run. Earlier observations follow.


Fourteen matched development cases used the corrected app prompts, 384 output tokens, 16 threads
and one slot. Every sample completed: 8B took about 1.5–21 seconds; 14B about 4–54 seconds.
Semantic review rejected 14B: its Persian RAM answer called RAM flash memory and its Persian
calculation gave 50/200 as 50%, not 25%. Source/time/stale qualifiers also failed some cases.
The 8B baseline likewise had unsupported stale-health wording and source omissions. Completion,
fluency and enough RAM are not accuracy. The serving 8B and deterministic safeguards remain intact.

Official Qwen3-32B Q4_K_M is pinned in
[32B metadata](../../deploy/inference/qwen3-32b-q4-k-m.candidate.json) at revision
`938a7432affaec9157f883a87164e2646ae17555`, 19,762,149,024 bytes, SHA-256
`efd971561896866f0e910cce52761ca77b1b138090c7f15fe284676d57d1f689`, Apache-2.0.
Desktop and protected server import passed size/hash verification. Eleven answers completed in
9.9–97.6 seconds, with correct RAM/arithmetic and explicit English stale/source/time qualifiers.
The Persian stale request exceeded 120 seconds; testing stopped before injection cases. Its
latency gate failed, quality remains partial, and it was not selected. The transient cgroup peak
was 18,324,066,304 bytes, not a sustained memory/capacity benchmark.

Pinned [Qwen3-30B-A3B-GGUF](https://huggingface.co/Qwen/Qwen3-30B-A3B-GGUF), with 30.5B total and
3.3B active parameters, passed desktop/server size/hash import. All fourteen matched questions
completed in 1.3–23.7 seconds with the same prompts, 384-token ceiling, 16 threads and one slot.
This is a bounded observation, not sustained throughput. Raw source/collection/partial qualifiers
and Persian terminology remain partial. Unchanged assurance replay retained typed evidence and
replaced incomplete evidence prose; it does not prove arbitrary correctness.

The earlier timed 3deba0d/30B-A3B app trial returned twelve authenticated responses, but browser review
exposed Latin-prefix Persian LTR rendering. Exact model and source rollback restored c4351fd/8B
with fresh bilingual generation. The response-locale direction repair passed seven browser fixtures.
The corrected 8d1f1d2/30B-A3B trial passed eleven strict browser cases, then failed raw Persian
filesystem completion. Persian technical errors also rejected selection: SSD was called main
memory and non-native terms recurred. Twelve API responses and four stored evidence/audit hash
checks are not a semantic pass. [The artifact record](../../deploy/inference/qwen3-30b-a3b-q4-k-m.candidate.json)
now records failed bilingual quality and unrun offline cold start. Runtime, deadline, queue, network restrictions
and the existing 24-vCPU/128-GiB guest are unchanged; no cloud, runtime download or VM increase is
introduced. Full held-out and production acceptance remain separate.

Only the exact RTL source repair is live as 8d1f1d2 with original 8B. Twelve fresh API requests
passed literal/code checks; the strict browser likewise failed final raw Persian filesystem
completion after eleven cases. A separate focused-answer display check passed, without claiming
raw completion. The shared 384-token finding needs bounded prompt-scope review, not a larger queue
or deadline. Do not claim baseline 8B is universally accurate either.

The next bounded candidate is [Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B), with
35B total/3B active parameters. The [pinned artifact record](../../deploy/inference/qwen3-5-35b-a3b-q4-k-m.candidate.json)
uses [Bartowski's Q4_K_M quantization](https://huggingface.co/bartowski/Qwen_Qwen3.5-35B-A3B-GGUF),
not an official Qwen GGUF publication. Both cards declare Apache-2.0. Upstream reference revision
is not verified conversion lineage. Provisioning and source fixtures are not a load/quality pass.
Qwen3.5 needs trusted `chat_template_kwargs.enable_thinking=false`; Qwen3's soft suffix is not
supported. The native context is not the configured context: retain 8192, CPU-only, one slot,
the existing ceilings, no vision projector and no speculative MTP. Preserve older provider payloads.

## Non-negotiable execution boundary

Generation, planning, embeddings, reranking, AI anomaly processing and optional automated model judging run on local CPUs. No external AI endpoint or silent cloud fallback is permitted. An OpenAI-compatible request format is only a protocol shape, not authorization to call an external provider. GitHub is not a runtime AI dependency.

Use deterministic parsers, inventory resolution, policy checks, scheduling, basic correlation and known runbooks wherever possible. Logical planner/collector/analyst/verifier roles do not require multiple simultaneous models.

## Runtime and model candidates

The baseline is one dedicated service built from a pinned llama.cpp CPU revision. Verify the selected build's GPU-disable options, zero offload configuration and startup device report. Do not install CUDA/ROCm, GPU containers, accelerator-only dependencies or remote-code model loaders.

| Workload | Starting evaluation, not a final selection |
|---|---|
| General diagnostics | Approximately 7–9B multilingual quantized model; Qwen3-8B is one candidate |
| Triage | Smaller model versus deterministic classification |
| More difficult synthesis | Roughly 14B candidate after the baseline |
| Larger generation | 24–32B only when measured quality improvement justifies latency |
| Embeddings | Small multilingual encoder versus a candidate such as Qwen3-Embedding-0.6B |
| Reranking | Optional; enable only with measured retrieval gains within budget |

Compare supported Q4_K_M/Q5_K_M quantizations where available. Verify chat templates, structured-output behavior, tool arguments and Persian quality on the exact model/runtime combination. Do not choose 70B+ solely because weights fit in RAM. Ollama, OpenVINO CPU and vLLM CPU are alternatives to evaluate, not three additional mandatory services.

### Stage 1B repository candidate

The source-level evaluation pair is now recorded in the schema-validated
[`qwen3-8b-q4-k-m.yaml`](../../deploy/inference/qwen3-8b-q4-k-m.yaml): llama.cpp
`v0.4.1` at commit `b29c606e28a01b1bc8c1351026a0fa6e616bf6c4`, plus the official
`Qwen3-8B-Q4_K_M.gguf` at repository revision
`7c41481f57cb95916b40956ab2f0b139b296d974`. The model source records size
5,027,783,488 bytes and SHA-256
`d98cdcbd03e17ce47681435b5150e34c1417f50b5c0019dd560e4882c5745785`.

The pinned runtime was built with the recorded compiler/flags and OpenBLAS/OpenMP, promoted with its
binary SHA-256, and the model matched its expected filename, size, and SHA-256 before and after
promotion. A bounded authenticated CPU-only loopback smoke test succeeded. The repository now also
contains the paired hardened native units documented in [AI_SYSTEMD](AI_SYSTEMD.md), two file-backed
credential boundaries, fixed loopback origins, one llama.cpp slot, and the one-active/two-queued API
scheduler. These are source and smoke-test results, not full bilingual quality, latency, memory,
failure, offline cold-start, backup, restore, rollback, or production acceptance.

### Larger clarity candidate — 2026-09-29

The owner requested a larger local model. The official [Qwen3-14B-GGUF](https://huggingface.co/Qwen/Qwen3-14B-GGUF)
Q4_K_M artifact is pinned in [candidate metadata](../../deploy/inference/qwen3-14b-q4-k-m.candidate.json):
revision `530227a7d994db8eca5ab5ced2fb692b614357fd`, 9,001,752,960 bytes, SHA-256
`500a8806e85ee9c83f3ae08420295592451379b4f8cf2d0f41c15dffeb6b81f0`, upstream Apache-2.0.
It ran with the existing pinned CPU runtime in a temporary loopback-only comparison. Desktop and
guest size/hash checks and protected artifact import passed. Eight serial 192-token cases found
a truncated Persian RAM answer and wording/source omissions; a four-case 384-token follow-up
using the actual general prompt completed in about 13–41 seconds. The comparison used 16 threads,
one slot and a 32 GiB memory ceiling; it was not a sustained capacity or NUMA benchmark. Quality
remains failed and resource comparison partial. The serving 8B artifact and rollback are preserved.
Explicit `NEXTOPS_MODEL_ID` accepts only the reviewed 8B/14B/32B/30B-A3B/Qwen3.5-35B-A3B source aliases; arbitrary
names/URLs fail. Source compatibility is not serving selection or quality acceptance.
Runtime alias, local file and configuration must match, and missing files must not trigger a download.

Compare the same English/Persian questions, completion state, relevance, evidence preservation,
latency and resources. A larger model is a candidate, not a guarantee of accuracy or production
acceptance. Provisioning downloads occur outside the model service, not through runtime Internet.

## Hardware discovery before tuning

Confirm CPU model, physical/logical cores, sockets, NUMA nodes, effective affinity/cgroup allocation, instruction sets, available RAM, storage and existing workload contention. “G10” and “90 CPU” establish none of these details. Discovery must not install packages or stress the host; see [installation](INSTALL.md).

## Staged benchmark

Begin with one small candidate, one active request and a bounded prompt/output. Compare generation and prompt-processing thread counts, physical-core versus SMT placement and NUMA-local versus controlled multi-node execution. Then compare model sizes and quantizations using the same versioned corpus. Increase active requests from one to two and then four only when latency and resource pressure remain acceptable. Initially evaluate representative 2K/4K/8K input contexts and verify total-versus-per-slot context semantics. Finally test bounded mixed traffic: chat, incident synthesis, embeddings, ingestion, database work and builds.

Record exact model/build/revision, flags, CPU mask, memory placement, input/output token counts, sample count, cold/warm state, queue delay, time to first token, prompt and generation throughput, total latency, p50/p95, peak memory, CPU pressure, swap/page faults, cancellations and errors. Evaluate complete answers and correct tool arguments, not tokens/second alone.

## Resource policy

Maintain one budget across all services. Reserving roughly 20% of effective CPU capacity for the OS/control plane is only an unvalidated starting experiment from the specification. Replace it with measured allocations. Do not allocate 90 threads per request or start 90 API workers. Cap runtime/BLAS/OpenMP thread pools, worker counts, queue lengths, context, output, tool fan-out and investigation concurrency.

Enforce limits through validated container controls or systemd/cgroups. Give interactive work priority over re-indexing; use backpressure and cancellation. API access, audit and manual incident views must remain usable when inference is saturated or absent.

## Artifact and acceptance record

Every model record includes source, immutable revision, license, quantization, tokenizer/template, dimensions where relevant, file size and checksum. Provision or import artifacts explicitly; missing files must fail preflight rather than trigger downloads. Keep weights outside Git.

Select the production candidate only after held-out bilingual quality and latency tests, explicit CPU execution verification, no-Internet acceptance tests and a documented operating envelope. Capacity targets must be labeled targets until measured.
