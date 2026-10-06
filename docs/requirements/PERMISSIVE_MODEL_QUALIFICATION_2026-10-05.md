# Permissively licensed model qualification / پذیرش فنی مدل با مجوز آزاد

Date: **2026-10-05**. Historical 27B status: **Qwen3.8-27B Q5 import verified; distinct standard trials failed; no model cutover**.
تاریخ: **۵ اکتبر ۲۰۲۶**. وضعیت تاریخیِ 27B: **دریافت Qwen3.8-27B Q5 تأیید شد؛ آزمون‌های مستقل استاندارد ناموفق؛ بدون تغییر مدل زنده**.

[English CPU guide](../en/CPU_AI.md) / [راهنمای فارسی CPU](../fa/CPU_AI.md).
The [27B result](QWEN38_QUALIFICATION_2026-10-05.md) and
[Flash preparation](QWEN38_FLASH_QUALIFICATION_2026-10-05.md) remain dated evidence, not erased.

Latest update: **2026-10-06, 06:56 UTC — 274 verified ranges; exact-head CI passed, independent review/model gates still open; no model cutover**.
آخرین به‌روزرسانی: **۶ اکتبر ۲۰۲۶، ساعت ۰۶:۵۶ UTC — ۲۷۴ بخش تأییدشده؛ CI کد دقیق موفق، بازبینی مستقل/پذیرش مدل همچنان باز؛ بدون تغییر مدل زنده**.

## English

### Four further verified windows and exact-head CI — 06:56 UTC

Four more reviewed V7 windows passed; main read each full actual desktop receipt and terminal
exit0, not separate root range receipts:

| Operation suffix | Second-file indexes | Curl milliseconds | Desktop result SHA-256 |
| --- | --- | --- | --- |
| `639268647031493367` | 110–113 | 44172 | `b2b630cefc776ef68d45f3d6b419d3bf009c821dcf74e63a001e6de3af98374b` |
| `639268651190522106` | 114–117 | 44109 | `c9574dababe16104ec1cfaccefe41541a2fb48dcfba54425320225b1332cd85a` |
| `639268654435422198` | 118–121 | 39234 | `d5765c9611ac8f019337d25062cd4da0ccf1f16569bd8a3beff275a896678dbb` |
| `639268657463180170` | 122–125 | 581062 | `f72dbab8bb691583228339a2f1a6d3a77cbc4687dd4e42c64f20b27a5bde3b05` |

All-four numeric HTTP206/exit0/size/header/held-identity/hash checks preceded import. Bodies
remain, handles closed and owned-stop/unchanged ready-idle reconciliation passed. The last
window's in-progress empty/partial bodies were not acceptance; it completed within the fixed
600-second request limit without retry or widening. Totals: **274 ranges/73537741600 bytes**,
with **16891713152 bytes** remaining; only one whole upstream shard is verified. No unattended
transfer/trial remains. Exact `940b84d` passed all five
[CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37423271410); source CI is not model
acceptance. Independent V3/native/publication review remains not run after all three subagents
hit usage limits. No new tool installation/publication/native test or model selection follows.
Full-set/manual/standard semantics/thinking/privacy/measured-context/matched app/operational/
rollback gates remain open. Failed 3.8 trials are retained; the Apache alternative remains
correctly Qwen3.5-122B-A10B, not an accepted 3.8 or maximum-context claim. The live 35B model
and public thinking-off are unchanged; the full requested goal remains unfinished.

### Additional finite transport and exact-head CI — 06:18 UTC

Operation `639268639835556618` passed second-file indexes106–109; curl43547ms, actual desktop
result3084 bytes/SHA `a90c39b6491ad9910edc424400220455630082a9d4b5b51c56db28f5e2ccf9ce`;
main read the full actual receipt and terminal exit0, not separate root range receipts. Numeric
HTTP206/exit0/size/header/held-identity/hash checks for all four preceded import. Bodies remain,
handles closed and unchanged ready-idle/owned-stop reconciliation passed. Totals: **258 ranges/
69242774304 bytes**, **21186680448 bytes** remaining; only one whole upstream shard verified.
No unattended transport/trial remains at this checkpoint. Exact `906a081` passed five
[CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37422445456). Existing private V3
review handoff/main assertions are not independent review or host/model acceptance. All earlier
failures/completed stages and unrun full-set/standard/thinking/privacy/measured-context/matched
app/operational/rollback gates remain. Apache alternative stays correctly 3.5, live35B/thinking-off.

### Further provisioning and independent-review handoff — 06:10 UTC

Three further reviewed V7 windows passed; main read actual desktop receipts and terminal exit0:

| Operation suffix | Second-file indexes | Curl milliseconds | Desktop result SHA-256 |
| --- | --- | --- | --- |
| `639268621098769452` | 94–97 | 38235 | `a994ef5700d1eb30601ed615fd5e935025aa9330945814d6c25eda55ff52caee` |
| `639268623859327096` | 98–101 | 374734 | `b5b5b80d1f69678a884a1a3f7651fa6a0ccb560eab0161efc2922efb6ee8f6ae` |
| `639268630606440778` | 102–105 | 514047 | `0848c9e229304f7719be2e84f443a75a02e1f5497226fe559bdb24758dfd4dda` |

All-four numeric HTTP206/exit0/size/header/held-identity/hash checks passed before import;
bodies remain, handles closed and unchanged ready-idle/owned-stop reconciliation passed.
Separate root range receipts were not read by main. Totals: **254 ranges/68169032480 bytes**,
**22260422272 bytes** remaining, only one complete upstream shard verified. Individual transport
timings and in-progress zero-length bodies are not performance or model acceptance; no deadline
was widened. No unattended operation remains at this checkpoint. Exact `8b94d88` passed all five
[CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37419756842).

Main prepared a private independent-review request for the directory-durable native wrapper,
matching trio installer, external execution/read-only reconciler and publication installer V3.
All fourteen listed current source/checker files were freshly rehashed against existing pins;
the handoff JSON/current-pin check passed with no host/model call. It supplies exact isolated
checker arguments, syntax-check command, frozen controls and required ownership/identity,
file/directory fsync, bounded process/cleanup, strict receipt and primary-failure-preservation
review criteria. This is preparation, not independent review or execution authority. None of
the V3 tools was installed or operationally invoked. All three authorized subagents remain
terminal usage-limit errors. Earlier source and failure evidence is unchanged; full-set,
standard semantics, thinking/privacy/measured context and matched operational gates remain.
The candidate is the Apache Qwen3.5 alternative, not an accepted 3.8 replacement; live35B stays.

### Further transport and targeted regression — 05:33 UTC

Three more V7 windows passed, with actual terminal exit0 and desktop receipts read by main:

| Operation suffix | Second-file indexes | Curl milliseconds | Desktop result SHA-256 |
| --- | --- | --- | --- |
| `639268596918597658` | 82–85 | 486344 | `ec1891cadf86ae8d53298d5ed1aa6da2b904aad6ba4ce6738fda6e84370225d6` |
| `639268604309844912` | 86–89 | 479219 | `d6ebeed02f5929f5d9fab80a9cecfe75c41115c9e12ec5030f47ebaf937e2410` |
| `639268612161360707` | 90–93 | 39250 | `d5439a8fa0026f6dbdd7bb8a6fbff365b24dcb61e74586fc86fe62cc34f5d69f` |

All-four numeric HTTP206/exit0/size/header/held-identity/hash checks preceded import; bodies
remain, handles closed and unchanged ready-idle/owned-stop checks passed. No separate root
range receipt was read by main. Totals: **242 ranges/64947807008 bytes**, **25481647744 bytes**
remaining, one whole upstream shard verified. In-progress body-length observations were not
acceptance; no deadline was widened. No unattended operation remains at this checkpoint.
Exact `4e78144` passed five [CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37417547944).
Local command `.venv/Scripts/python.exe -I -B -X utf8 -m pytest -q -p no:cacheprovider tests/unit/test_122b_q5_candidate.py tests/unit/test_thinking_qualification.py`
passed **61 tests in 5.12s**, exit0; the actual import was the active checkout. This is manifest/
premature-selection and mocked thinking-qualifier coverage, not native quality/privacy/context or
live acceptance. The V3 main-only reviews, subagent quota failure, correctly labeled Apache 3.5
alternative, live35B/public thinking-off and all model acceptance gates below remain unchanged.

### Directory-durable native preparation and external failure-boundary repair — 05:10 UTC

Three additional V7 windows completed; main read actual desktop receipts and terminal exit0:

| Operation suffix | Second-file indexes | Curl milliseconds | Desktop result SHA-256 |
| --- | --- | --- | --- |
| `639268580870887985` | 70–73 | 465344 | `b1a05e2bf6359e6b0ec7175c2487ffd4ef75b67bce7f7b17930ba2594df8f0ce` |
| `639268588480494906` | 74–77 | 48375 | `2ca7d88a33a3082488972dde49d6b236ee59801e8e6c25327f188306921c24db` |
| `639268592479363732` | 78–81 | 41157 | `25a21077b23e4d0817a23700454787fdb144d9f8ac76b4fffc869b2e68ec5991` |

All-four numeric HTTP206/exit0/size/header/held-identity/hash checks preceded import; bodies
remain, handles closed and unchanged ready-idle/owned-stop reconciliation passed. Main did not
separately read root range receipts. Totals: **230 ranges/61726581536 bytes**, **28702873216
bytes** remaining. Only the first whole upstream shard is verified; timings are not model
benchmarks or proof of general transport speedup.

Review found that frozen native V2 fsyncs report contents but not the containing new directory
entry. Its earlier 1478 main/independent checks remain dated history, not proof of this omitted
durability case. Distinct native V3 (**93609 bytes**, SHA
`3414db13444f76c34c83a71d05e52a4ce476baaeeb7847ef5b39ed580606a842`) adds content fsync,
lock checks, already-retained ROOT directory fsync and lock rechecks; failures stay unknown/
nonzero with independent descriptor cleanup. Main **1869 pure assertions** and Bash syntax passed.
Matching trio installer **33044 bytes**, SHA
`3bf2fe34245c5fa13d39e946fe6b87bee86fdb8d4249369e524c23338a18f36e`, and controller
**23868 bytes**, SHA `43ee65fd859ac428cb8ad7ce21a243f5fa02d1a909458c1e83c7090fc9e03381`,
passed **227 Python/1022 PowerShell main assertions**, not installation. Probe/unit/source/runtime/
corpus/prompts/case120s/384-final/16K/32+32 threads and existing run IDs are unchanged; no trial
ran with either version. The fixed three-file payload is 185433 bytes, bootstrap plus payload
218477 bytes. Old frozen tooling/pins and failures are retained, not silently relabeled.

The distinct external read-only reconciler (**17037 bytes**, SHA
`c984bd8e68c9c3204e67bf485484ae97649177c3290ae789f37e9c875f5743bd`) passed **18403 main
assertions** across protected FD-relative reads, exact pre/post identity, input/process bounds,
independent cleanup and fully mocked main failures. The count includes per-block checks while
testing aggregate scan limits; it is not 18403 independent tests. Expanded mocks first failed
with `TypeError: unhashable type: bytearray`: set intersection received bytearray tokens. The
draft was repaired by converting bounded bytes before exact argv matching; the failure remains
recorded. No host ran that draft. Current argv absence is explicitly **not** recorded PID/start
identity proof, prior-client success, fresh full-shard hashing or semantic acceptance.

External controller (**22979 bytes**, SHA
`a658912ec27e752e701e53b132161c8c2ebd739ec705d75ee189ea0d1c2ecfac`) passed **842 main
PowerShell assertions**, exit0: exact commands/bootstrap pins, bounded reads, strict typed
receipts, async bounded input/output, owned client cleanup, primary exit/stdout digest before
parse and one later read-only reconciliation that cannot green a primary failure. Root deadlines
are 1010s artifact/2740s standard/65s read-only with 5s kill grace; clients 1030/2770/85s;
outer bounds 1300/3060s. Standard exit2 means manual semantic review required, never acceptance.

All V3 independent reviews and publication installer V3 independent review are **not_run**:
three authorized subagents remain terminal usage-limit errors. None of these new tools is
installed, published or operationally executed. Exact `4bb295d` passed five
[CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37414641936). Completed metadata
installation/first-shard assembly/source checks, original failures, staged-not-installed ca1,
Apache **3.5** labeling and live35B/public thinking-off are preserved. Complete-file/manual/native
standard/thinking/privacy/measured-context/matched app/operational/rollback gates remain open.

### Native installer-controller preparation and continued transport — 04:36 UTC

Four further V7 windows completed after the preserved 202-range checkpoint:

| Operation suffix | Second-file indexes | Curl milliseconds | Desktop result SHA-256 |
| --- | --- | --- | --- |
| `639268563148794529` | 54–57 | 576407 | `2987a60b014acdeb8298bb7299fa1bf8ae44722201656bf19fdcba40e7817e75` |
| `639268571098453763` | 58–61 | 46844 | `40b27f420528c4bd8f54bd0b6cde964adde1d8efc9cd2ae1bb6dd9536cba09d4` |
| `639268574470045182` | 62–65 | 41875 | `d8ee7cc9e54b767a99b4b7d27f84ecd40f407ca89db5b05a682b4c131ed24507` |
| `639268577711261283` | 66–69 | 43031 | `c5d09fe6d07995232a529dedf648c949c87f40c5acc1ef81984c9ded61ecfadf` |

Main read actual desktop receipts and successful terminal exits, not separate root range
receipts. All-four numeric HTTP206/exit0/size/header/held-identity/hash checks preceded import;
bodies remain, handles closed and owned-stop/unchanged ready-idle checks passed. Canonical
totals are **218 ranges/58505356064 bytes**, with **31924098688 transport bytes** remaining.
Only the first whole upstream shard is verified. Variable durations are not an inference
benchmark or proven general transport improvement.

The distinct native-trio installer/controller is now fully prepared and main-reviewed locally:
installer **33044 bytes**, SHA `f65751dd360e3d1f1493963978a150c2f11d8391e3f43e66f587063025e2bc95`;
controller **23868 bytes**, SHA `89cc15367c7d6af6ccb6552ef8ca5b98f84117151c975c62e35ab57e134ce23d`.
The fixed payload is exactly three artifacts/184787 bytes; including the bootstrap it is
217831 bytes. Main **227 Python/1022 PowerShell pure checks** passed and were rerun, exit0,
without operational entrypoints, host/model calls or real filesystem/process mutations.
The controller checks exact names/sizes/hashes/modes, explicit durable-receipt/closed-handle
flags, and retains primary exit/stdout digest before parsing; later read-only reconciliation
cannot erase primary failure. The historical Python-only draft remains unchanged. Local
mechanical preparation failures and a checker rerun missing its mandatory hash (exit1 before
tests) are retained; the corrected exact pinned command passed, not a host retry.

Independent review is **not_run** because the authorized subagents errored on usage limits.
This installer controller is not the still-unprepared external native execution/reconciler.
Durable report publication and independently observed stop/baseline outcomes must be covered
there before a trial. Publication installer V3 also awaits independent review. Nothing was
installed, published, started or selected by these new tools. Exact `2838b2a` passed all five
[CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37413048626).
The alternative remains Apache Qwen3.5-122B-A10B Q5, not 3.8; complete-set/manual/native standard,
thinking/privacy/context/matched app/operational/rollback gates stay open. Live35B/public
thinking-off and completed earlier work/failures are preserved.

### Further transport, actual template binding and installer cleanup — 04:12 UTC

Two more V7 windows completed after the preserved 194-range record:

| Operation suffix | Second-file indexes | Curl milliseconds | Desktop result SHA-256 |
| --- | --- | --- | --- |
| `639268494625754785` | 46–49 | 465344 | `af5af058176e47b1959ed2dcf4c679eac51a7173a035c70d32fd23166b82fba5` |
| `639268501838394192` | 50–53 | 37625 | `ec63aa840b65844bb20ce8a30019a4ba1748e74d1f60942ad3fb21e217dd8993` |

Main read actual desktop results and terminal exit0, not separate root range receipts. All
four numeric HTTP206/exit0/size/header/held-identity/hash checks passed before each import;
bodies remain, handles closed and owned-stop/live ready-idle reconciliation passed. Totals:
**202 ranges/54210388768 bytes**, **36219065984 transport bytes** remaining. One whole shard
is verified, not the model. Variable curl duration is not an inference benchmark or speedup.

Main and independent source review matched actual lossless upstream bytes at official revision
`dc4d348443bc740c68e2d77492492c11606384d5`: template **7756 bytes**, SHA
`a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715`, and license **11544 bytes**,
SHA `bbedc3fda3305820b977265f01b8619d87570a6739de3a5582c3464840f1e57a`. These match the observed
first-file template and protected Apache-2.0 license. No whitespace/newline normalization was
used. With generation prompt enabled, literal `enable_thinking=false` statically closes the
empty think prefix; true/unset leaves it open. Latest assistant reasoning history/tool-cycle
handling is independent of that flag. This is not native rendering, tokenizer-array equality,
privacy, all-shard integrity, conversion-provenance, context or whole-product legal acceptance.
No passing complete-set manual input has been created. Preserve license/attribution/NOTICE
where applicable and modification notices; this remains correctly named Qwen3.5, not 3.8.

Distinct native V2 full-file/diff review passed **1478 main/independent pure checks** and Bash
syntax. Probe/wrapper/unit SHAs are `dd85034de1cfbba9cc97622a1a8847bbdda887931eb38b003c13e7c03c41b4d6`,
`f63eb791cc8a22a13b09d9b96c6beda351f51a0b3c4600885ed850add78cae9c` and
`79befd1115da2b98fe1e34fdc9f0530abd538136b02a6a2ac16f1bd655ca1046`. Both retained FD/path locks
and stable ancestor identities bracket guards/writes/fsync; required-audit failure cannot skip
owned-probe termination and descriptor cleanup. Its installer/external controller and host
standard trial remain open. Frozen source/runtime/corpus/case120s/384-final/16K/32-thread limits
are unchanged. Publication V2's execution pair passed **1646 each-side pure checks**; controller
SHA `b79d6539361075d778fe144c06617d89feeae855adfaec412ededa55e58392a5`. It invokes an already
installed fixed publisher only; it has not installed or executed anything. A later read-only
receipt cannot change an unsuccessful primary transport/cleanup outcome into success.

Subsequent review rejected publication installer V2 despite its earlier passing pure checks:
constructor fstat/close errors could lose or skip owned handles, and required receipt fsyncs
did not recheck both held-lock identities. Successful earlier metadata-helper installations
remain historical successes, not proof of these failure paths. Distinct installer V3 now
registers directory ownership before validation, attempts all closes, latches uncertainty and
rechecks both locks around receipt fsyncs. Its controller validates explicit cleanup/receipt
flags and preserves actual primary exit/stdout hash before parsing. Main-only **256 Python/989
PowerShell checks** passed; source/controller SHAs are
`66e75a494da7ea696e3a85aec7209f4ef0cd01c7bfc3a6b41263c120ac0ffff1` and
`673739b11fa9f432575c42bb601abb3dc56758343cc9a2d35eaec59744b6dc18`. They have not run on the host.
The unfinished native-trio installer draft also had raw closes bypassing ownership tracking;
main repaired them and **227 isolated definition/memory checks** passed, including actual
selected-finally failure paths. Its controller and independent review are still unfinished.
Local checker-development assertion failures/corrections and original rejected tools remain.

All three authorized subagents subsequently stopped with usage-limit errors. Completed reviews
above retain their scope; neither ongoing agents nor unfinished independent passes are claimed.
Root continues already reviewed finite provisioning and isolated repairs. Exact `2847651` passed
all five source-CI jobs in [run 37403305543](https://github.com/Omid-NextAI/nextops/actions/runs/37403305543).
ca1 remains staged-not-installed; live35B/public thinking-off and unaccepted advertised context
remain. Finish transport before other assemblies/full-set inspection/publication, then standard
semantics before separate thinking/privacy/measured-context/matched-app/operational/rollback gates.

### Continued transport and preparation-tool failure review — 02:11 UTC

Four further V7 windows completed after the preserved 178-range checkpoint:

| Operation suffix | Second-file indexes | Curl milliseconds | Desktop result SHA-256 |
| --- | --- | --- | --- |
| `639268474034540055` | 30–33 | 36766 | `21e87ca2ad6216dc98000996bb7122f7e1ad87fec6ecceac244533215260cbaf` |
| `639268478207318831` | 34–37 | 462562 | `3ecae93b54bd7107a03922ecb29c32ce5842eb2ed7b409a462e6ef8083899dd9` |
| `639268485013170644` | 38–41 | 38860 | `add03d08b36c2370f5643f61705c70618032e924bee377946cad2033b91f2df9` |
| `639268487728354785` | 42–45 | 461282 | `c026a0349907ef7b4e2a6eb535f2218cae3dfcc6d49760c70895478835501551` |

Main read actual desktop records and successful session completions, not separate root range
receipts. Each window retained four 268435456-byte bodies, verified numeric HTTP206/exit0,
headers/held identities/full hashes before any import, then reported owned stop/closed handles/
unchanged ready-idle baseline. Latest record completed at **02:10:08 UTC**. Canonical totals
are **194 ranges/52062905120 bytes**, leaving **38366549632 transport bytes**. Only the first
whole upstream shard is verified. Variable fast/slow windows do not establish speed improvement
or explain the transport cause; no inference performance follows from provisioning.

Independent review found that the original complete-set inspector's child setup failure or
unexpected worker return could unwind into parent audit/cleanup. Original pure checks had not
covered that path; the original six tools are preserved and rejected operationally. A distinct
V2 enforces child-local `finally: os._exit(1)`; normal successful workers exit internally. Main
and independent full-file/diff review and **1275/4402/601 pure checks (6278 each-side)** passed,
including six failure fixtures. Inspector: **34137 bytes**, SHA
`5e82762b45b5f6073d8d3bf0bb1350ce2bbb535a4d74c100749c957f72b95062`.
Its fixed absent-only installer passed **147 Python/873 PowerShell checks (1020 each-side)**,
then operation `metadata-complete-v2-install-20261006-639268494401094149` installed only that
helper in **238 ms**. Destination hash, owned client stop and root receipt checks passed;
desktop result SHA is `0c4a2c065019da94999a1b3d30d0eba1ab82952791922d56b21d8fb309f44c60`,
root stdout SHA `86fc147a5954b2620ec5b2e0dee488349e3d3bc67419a608e142c29a7c46af49`.
No complete-set inspection, native execution or service action occurred. The reconciler is
streamed only when needed, not installed; original tools/ACLs are unchanged. The author first
failed a stale-byte-pin preparation check, corrected it and preserved the failure history.

Publication's original helper released locks before its required receipt; it remains rejected.
Distinct publication V2 holds both root locks through receipt/fsync and independently attempts
all descriptor closes. Main/independent full review and **3035 each-side pure checks** passed.
Helper: **57921 bytes**, SHA `6d5d2a7d4ed3d436789da64304b5f3e5f24b4de7d6993cc98a5378b1fefb6a12`.
Publication/its installer-controller qualification has not run. Likewise, **1073 passing pure
native checks** did not cover replacement of held lock paths or sequential close failure.
Main/peer review rejected that original quartet; a distinct lock-identity/cleanup and corrected
metadata-pin repair is unfinished. Case120s/384-final-token/16K/32-thread limits, corpus/prompts
and original failed trials are unchanged. No failed primary client outcome is converted to
success merely because later read-only reconciliation finds a completed receipt.

Exact `9375d49` passed quality/unit, PostgreSQL16/17, browser and secret-scanning CI in
[run 37400813523](https://github.com/Omid-NextAI/nextops/actions/runs/37400813523).
This is source CI, not whole-model/template/native/thinking/privacy/context/operational
acceptance. ca1 remains staged, not installed; live35B/public thinking-off remain unchanged.
Finish transport before the other assemblies, then full-set/template and standard gates before
separate final-only thinking/privacy/measured context and matched operational/rollback gates.

### Expanded actual metadata and four-request transport — 01:36 UTC

Preserve the preceding serial windows. Window `resume-20261006-639268455415290393` added
shard-two indexes 22–25: 174 canonical ranges/46694196000 bytes, 43735258752 missing;
curl 525500 ms. The distinct reviewed v7 window `resume-20261006-639268464492464192` then
completed indexes 26–29, four times 268435456 bytes/all HTTP 206/exit 0. Curl time was
**463594 ms**; per-request times **203.479489/463.448385/363.428074/440.723006 seconds**.
All four numeric results, headers, held identities and local hashes were verified before any
import. Protected imports, duplicate cleanup, owned handle/process stop and unchanged live
ready-idle baseline passed. Canonical totals: **178 ranges/47767937824 bytes**; **42661516928
transport bytes** remain. Only the first whole upstream shard is verified. Main read the
desktop result SHA `3b6c555286221fd0e11cc5bb7edfa61b97111ad2931ba6e25d27d1de059b34a7`,
not separate root receipts. One parallel observation does not establish a general speedup,
network diagnosis or inference-performance improvement. Original bodies and failures remain.

The seven expanded-metadata files passed **5564 main/independent pure checks**; the two
fixed installer quartets passed **2014 checks on each side**. Original tools are unchanged.
Distinct reader/inspector root installations completed in **231/220 ms**, exact destination
hashes verified, clients stopped/outcomes reconciled, without metadata or model execution.
First-file inspection `metadata-v2-122b-20261006-639268471855185668` subsequently completed
exit 0 in **87843 ms**, including **87485 ms** inspection. The whole first upstream hash
was verified before parsing. Read-only reconciliation and main's independent bounded
stat/SHA/read/stat reread confirmed the protected result: **2850 bytes**, root/root `0400`,
single link, SHA `06dadb4368dc0b38758c5ae3aa60849db0951b09abeb652980b20e59a0c122b2`.
Main's reread used second-precision stable stat fields, not a retained-FD proof. Owned worker/
guard cleanup and unchanged live readiness passed.

| Actually observed first-file metadata | Value |
| --- | --- |
| Architecture/blocks/embedding | `qwen35moe` / 49 / 3072 |
| Expert count/used count | 256 / 8 |
| Expert/shared feed-forward lengths | 1024 / 1024 |
| Attention heads/KV heads/key/value lengths | 32 / 2 / 256 / 256 |
| Full-attention interval/next-token-prediction layers/RoPE dimension | 4 / 1 / 64 |
| SSM convolution/groups/inner/state/time-step rank | 4 / 16 / 8192 / 128 / 64 |
| Tokenizer/pre/add-BOS/EOS/padding | `gpt2` / `qwen35` / false / 248046 / 248044 |

The template hash remains `a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715`.
Vocabulary/shared-expert-count/other token IDs/flags remain absent, not defaulted. Token/merge
arrays and standard template-control semantics are unreviewed. The first file has 392 tensors;
899 aggregate tensors and 262144 context tokens remain advertised, with accepted context null.
Complete-set helpers, immutable service-readable publication and standard-only native trials
are separately prepared, not executed or accepted. Finish transport before the remaining
assemblies; never change the root-only two-link original artifacts to grant service access.

Exact `495b704` passed all five source-CI jobs in
[run 37397504800](https://github.com/Omid-NextAI/nextops/actions/runs/37397504800): quality/unit,
PostgreSQL 16/17, browser and secrets. This does not inherit prior-head results or qualify a
model. ca1 remains staged, not installed; live 35B/public thinking-off and previous failed
standard trials remain unchanged. Full-set/template/native/semantic/thinking/privacy/measured
context and matched application/operational/rollback gates remain unfinished.

### Protected ca1 source staging and 166-range transport checkpoint

Window `resume-20261006-639268444064771324` completed exit 0: shard-two indexes 14–17,
four times 268435456 bytes, all HTTP 206/exit 0. Aggregate curl time was **509172 ms**;
per-range times were **127.098919/126.124402/126.298074/129.518253 seconds**. The controller
verified protected receipts, owned stop and unchanged ready-idle baseline. Canonical totals
are **166 ranges/44546712352 bytes**, with **45882742400 transport bytes** missing. Main read
the desktop result, SHA `9c70819749a75c63d4d14e4474f545a8ce2fa069d32c03f69662ebb86333b988`;
it did not independently reread these root receipts. One complete upstream shard is verified,
not the complete model. The preceding faster windows and failed parallel attempts remain history;
no route-throttling diagnosis or new parallel speed improvement is established.

The distinct v2 stager restricts its OWNER RIGHTS exception to the fixed wheel and direct
build parent. It requires the actual current owner, exactly three SYSTEM/administrator/OWNER
RIGHTS allow-full-control ACEs with exact flags, non-reparse ancestry, held read-only handle,
single link, unchanged handle/path identity and full wheel digest. The generic private-path
validator, original ACLs, frozen Python stager, package pins and failed preflight stay unchanged.
Main/independent review passed **1303 PowerShell definition/mock checks**; the separately
authorized actual local read-only wheel fixture passed in **1500 ms**, without a host call.
Operation `source-stage-ca1da27-20261006-639268451997194459` then completed exit 0:
**staged, not installed**, root stage **1879 ms**. The controller verified all protected
archive/source/wheel/static parity, owned client stop, root outcome and ready-idle baseline.
Desktop result SHA: `42ce75d5672c65ad9c0dfd78f6f2c9c744b2d5c2f70109532d0bdd4573855255`.
Installed-venv dependency parity, package installation and inference were not run. The original
3.63-second preflight failure remains retained; success of this distinct repair does not erase it.

Exact `f7d0b35` passed all five source-CI jobs in
[run 37396025687](https://github.com/Omid-NextAI/nextops/actions/runs/37396025687): quality/unit,
PostgreSQL 16, PostgreSQL 17, browser and secrets. Its earlier queued state is superseded by
this observed run result, not inferred from the preceding commit. Next, continue reviewed
transport and separately review expanded actual metadata/full-set/native qualification.
Public thinking remains off; live 35B and previous failures are unchanged. This is provisioning
and source verification, not full-model/usable-context/operational acceptance.

### Actual first-file metadata and protected S-drive continuation — 00:27 UTC

The separately reviewed metadata installer passed **136 Python/864 PowerShell** main and
independent preparation checks. Its root-only installation completed in 225 ms without
running a model. The distinct external execution quartet passed **1469 Python/587 PowerShell**
main and independent checks. Operation `metadata-122b-20261006-639268431340517846` then
completed exit 0 at **00:27:06 UTC**: **89798 ms** total/**89410 ms** inspection. It freshly
verified the complete first-file upstream SHA before bounded metadata parsing. An independent
read-only reconciliation and main's separate protected-record reread confirmed owned worker/
guard stop, exact result identity and unchanged live ready/idle baseline. Protected result SHA:
`5f8b6345c3437acfdc4fc65da4ac0bd69d469d8eef30bbe2ea78216593805ce1`.

| Actual observed field | Value and boundary |
| --- | --- |
| Architecture/name/license | `qwen35moe` / Qwen3.5 122B A10B / `apache-2.0` |
| GGUF/quantization version/file type | 3 / 2 / 17 |
| Metadata fields/block count/embedding length | 51 / 49 / 3072 |
| Split count/index/first-file tensors | 3 / 0 / 392 |
| Aggregate tensors/context length | 899 / 262144 — advertised, not whole-set or usable-context proof |
| Tokenizer model/pre | `gpt2` / `qwen35` |
| Template SHA-256, not raw text | `a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715` |

Expert/special-token fields and rendered template branches are not verified by this reader.
Accepted context stays null; full-model/native-load/semantic/thinking/privacy gates are not run.
The installer/inspector/reconciler execute no inference and change no serving configuration.

The exact precreated private S-drive child passed ACL/identity checks, without changing the
drive root ACL. Separately reviewed v6 serial continuation passed **328 main/independent**
preparation checks. Three successful windows completed shard-two indexes 1, 2–5 and 6–9,
with full per-range HTTP 206/exit-0/size/local hash and protected import/cleanup/finish checks.
The resulting canonical ledger contains **158 ranges/42399228704 bytes**; **48030226048
transport bytes** remain. Only the first complete upstream shard is verified. All local
bodies are retained. Main separately reread the first window's root receipts; the latter two
were verified by the controller, not separately reread by this report. Final baseline/owned
stop checks passed. Finish missing transport before additional full-file assembly to retain
the importer's 200-billion-byte free-space floor; never weaken the system-drive floor.

Exact `861bf7d` passed all five CI jobs in
[run 37392947997](https://github.com/Omid-NextAI/nextops/actions/runs/37392947997).
The source planner now lists implemented typed identity, hard standard-mode control and actual
model-label propagation separately from uncompleted runtime/qualified-thinking work. The
focused plan/registration suite passed **63 tests in 2.58 seconds**; lint/format and independent
diagnostic review passed. This is source/status repair, not 122B runtime acceptance, and does
not alter the frozen ca1 archive/wheel or installed private reader. The exact ca1 source/wheel
staging quartet passed **286 Python/923 PowerShell** main/independent preparation checks;
actual host staging and installed-venv parity are still not run at this checkpoint.

The next serial window completed exit 0 at **00:44:09 UTC**: shard-two indexes 10–13,
four times 268435456 bytes, all HTTP 206/exit 0, **505890 ms** aggregate curl time. Its
controller verified all protected receipts/owned-stop/baseline checks. Canonical transport
advanced to **162 ranges/43472970528 bytes**, leaving **46956484224 transport bytes**; no
second whole-file verification. Private desktop result SHA:
`ab1fe22ed0ec7fe54e5b11bab895b408ff3c5ea31dcd7833264470034ffa5907`.
Main did not independently reread this window's root receipts.

The subsequent ca1 staging controller failed **desktop preflight in 3.63 seconds**, before
any host call/upload/root stage. Its exact wheel has a current-user owner and a narrow inherited
OWNER RIGHTS/SYSTEM/administrator ACL; the reused validator accepts explicit current-user,
SYSTEM and administrator principals and therefore rejected that OWNER RIGHTS entry. Read-only
diagnosis confirmed exact source/wheel hashes and the other protected paths. Original files,
ACLs and failure are retained. Review a distinct fixed-wheel-only boundary with negative tests;
do not retry unchanged, alter original ACLs or broaden the generic private-path validator.

Source-only metadata inspection now captures **22** bounded architecture integer suffixes,
**14** special-token ID keys and **five** strict Boolean flags using the pinned upstream
[constants](https://raw.githubusercontent.com/ggml-org/llama.cpp/b29c606e28a01b1bc8c1351026a0fa6e616bf6c4/gguf-py/gguf/constants.py).
Selected arrays fail closed; missing fields remain absent. Full hash/byte/string/array bounds,
template hashing and no tensor parsing remain. This is not vocabulary/template-branch or
active-expert/KV/context validation; the installed private reader is unchanged. Main's exact
`python -m pytest tests/unit -q -m 'not browser'` passed **1098 tests/two POSIX skips/one existing
warning in 20.54 seconds**. Independent focused reader tests passed **211 in 1.64 seconds**;
main focused Ruff/format/mypy passed. The first offline documentation invocation failed only
when printing Persian under Windows cp1252; the distinct `uv run --offline --no-sync python
-X utf8 scripts/check_docs.py` completed exit 0: **140 Markdown files/39 pairs**. Release status
validation and diff checks passed. No new live-model or WAN acceptance follows.

### First full shard and exact-source offline package — 2026-10-06 checkpoint

The subsequent bounded windows completed first-shard indexes 141–147. All **148 canonical
ranges/39714874144 bytes** were then freshly verified and assembled by the protected
**48745-byte** assembler, SHA
`14ce5d8a1f6ee1345bdd4c1c15bdd79f38ed05bc988eb440a8b7b0a77ee111bc`.
Its reviewed installer and distinct v2 controller preserved previous failures and enforced
owned cleanup. Operation `assemble-20261006-639268393270653379-sh0` completed exit 0 at
**23:30:39 UTC**, in **480111 ms**. The immutable first shard matches its complete upstream SHA
`d7d5aa3ef843ba3fe5ee27cdaebe17abd8a6a8a03a5c236db9bfe2fc6b88be2e`.
The protected retained alias, canonical ranges and failed inputs remain recoverable. This
two-link publication is intentional, not a second copy. Original serving baseline/owned stop
passed. The result SHA is
`0d9a9b9e44e961e398bfc3bcad5557da59eea7941d9da5f85df5c33a2903ff52`.
**50714580608 bytes/two shards remain**; actual metadata, complete model and CPU gates are not
accepted from one shard or its advertised properties.

Before that assembly, after first-shard transport completed, window
`resume-20261006-639268385049931193` attempted the first three ranges of shard two and
failed at `finite_download`: curl **28**, **180187 ms**, **zero accepted ranges**, with
stopped/baseline reconciliation true. Retained body sizes are **230893621/131419903/63364396
bytes**, all below 268435456. HTTP 206 headers do not accept these incomplete bodies.
The result SHA is
`95f842e89e7400f620cc305791df1c2a530cbb348161e75f59cdc3bd646f12d3`.
The first prefix's independent local SHA is
`a4796fb8a2b7f710e15307331649b11259b5197db5d9336cd5d221e7b2df94c1`, not an upstream shard hash.
A distinct pinned-prefix/suffix helper passed **379 main/independent preparation checks**;
actual native identity/continuation remained unrun at the packaging checkpoint. Subsequently,
the fixed read-only native fixture passed in **2938 ms**, with unchanged held/path identity,
complete prefix SHA and all handles closed. Its private result SHA is
`d88b1f1f90a24486be0a055b752e03da5136e6016d0087b34a20188e38391d8f`.
The distinct one-range continuation started at **23:53:59 UTC** under fresh guards and
completed exit 0 at **23:56:08 UTC**. The missing **37541835 bytes** took **17.98552 seconds**,
one connection/HTTP 206/exit 0. The combined **268435456-byte** range's SHA is
`45e1d51def522f0d0424e26d53127aec7cbc03c49647d7601c53f4e9b4ae1fcf`.
Main independently read the protected accept/cleanup/finish receipts; all match. The desktop
result SHA is `94f5641ad7991f924e01afcbaaba5c1e97a0342cdc74bd282c3533e938a02ec7`.
Canonical transport totals **149 ranges/39983309600 bytes**, with **50446145152 bytes** still
missing and only one complete upstream shard. Original and new local bodies remain preserved;
only the fully verified incoming transport duplicate was removed, protected copies retained.
All held local handles closed and original live ready/idle baseline passed. No blind retry,
system-drive floor waiver, unverified-body deletion or parallelism benefit is claimed.

Exact source **ca1da27d6317fae247cee2b92576d6947d55421a** passed all five CI jobs in
[run 37384508573](https://github.com/Omid-NextAI/nextops/actions/runs/37384508573): browser,
PostgreSQL 16, PostgreSQL 17, quality and secret scanning. The original browser cancellation
remains historical; its distinct rerun passed **88 tests/1141 deselected/one existing warning**
in **182.51 seconds**. This does not establish why the first attempt was cancelled.

The first local packaging attempt failed preflight before any child/build/archive because the
preexisting Git launcher has an exact two-link `git.exe`/`git-lfs.exe` pair. That failure is
retained. A separately reviewed **39571-byte v2** packager, SHA
`e84427c8850af879b6308bb74dd5ef07082c12cd66b8ab7a0673cd249f57a5a9`, permits only that fixed
pair with strict identity/hash checks; every other file keeps single-link checks. Main and
independent **1619 declaration/mock checks** passed. Four actual local owned-child cases
(normal, nonzero, descendant timeout, output limit) passed in **1313 ms**, with zero remaining
job members. Actual packaging then completed in **23046 ms** using offline/no-index/no-cache/
no-build-isolation flags, with source/wheel/checkout, nine UI assets and dependency parity:

| Exact ca1 artifact | Bytes | SHA-256 |
| --- | --- | --- |
| Source archive | 8448000 | `a45a2e3290215416f6c3ee2a24a5c3a748ec5ba7ec2a16d7cd4eca44a17bd462` |
| Wheel | 195885 | `d82179a220fbceb62446681bb2096959bb818b122aae22f116bb9acd44118f7c` |
| Package code identity | — | `24353ee100cdf3def9f509703cd6b1f68da49394c69c0bf2a1190d8f13c0cd09` |
| Protected packaging result | — | `972d463716c5ccbcc4628df8340dc8bbdfd82f35870ff9341db0411f8ce22c86` |

No package upload/install, serving-venv change, signature verification, WAN-isolation or
production acceptance occurred. The three-shard manifest stays unselected. Live 35B/public
thinking-off, failed Qwen3.8 trials, prompt/corpus and fixed deadlines remain unchanged.
Continue protected provisioning and actual metadata/load/semantic/thinking/context plus matched
app/evidence/audit/queue/failure/WAN/restart/cold-start/rollback qualification, not a model rename.

### Earlier provisioning checkpoint — historical

### Bounded 122B resumption and desktop-runner correction — 2026-10-06 checkpoint

Exact `293164e` passed all five CI jobs in
[run 37378458739](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739), verified by
main. These are source/CI results, not model, transfer or production acceptance; they precede
the separate typed 122B source increment below:

| Verified CI job | Exact job record |
| --- | --- |
| Browser | [111993800323](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739/job/111993800323) |
| PostgreSQL 16 | [111993800700](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739/job/111993800700) |
| PostgreSQL 17 | [111993800738](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739/job/111993800738) |
| Secret scanning | [111993800806](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739/job/111993800806) |
| Quality | [111993800809](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739/job/111993800809) |

The self-contained importer is **30964 bytes**, SHA
`2f03c33bd7fcc113fd906064c05e97ea6c68acdb6ff293e829114eab52f63d46`;
it was installed root-owned/mode `0400` with exact source parity. Main/independent review and
**825 definition/mock/static checks** passed. Its finite begin scan freshly hashes retained
canonical data; completion receipts precede removal of only fully verified transport duplicates.
Failed/ambiguous inputs, canonical data and old records remain preserved. A range receipt is not
the upstream full-shard hash, model acceptance or selection.

The original **23397-byte** desktop helper, SHA
`73915db249cb577c45a515814d9e11bfe6910db111d76490d15e615c1db8855e`, ran window
`resume-20261006-639268346254710321`. It **failed at `remote_begin` before any range download**;
the matching root start/result records were absent. Manual read-only reconciliation confirmed
stopped transport and absent open handles, serving PIDs **2187/2197**, restart counts **0/0** and
ready/idle state unchanged. This is a preserved tooling failure, not a failed model answer or a
successful import. No mutation was blindly retried.

Sixteen isolated local `ssh -V` environment cases isolated the missing `ProgramData` variable:
adding only that variable changed exit **255 to 0**; all thirteen other single additions failed,
while all fourteen additions passed. This identifies the reviewed local runner dependency, not
server authentication, a network-policy bypass or model readiness. A distinct **23537-byte v2**
desktop helper, SHA `2af46805a3fc38cd839ee5736e7ed1da35fe4996aa730f1d9a4494a8bababcce`,
adds `ProgramData` and safe cleanup for its associated process. Main's **406 preparation checks**
and read-only reconciliation passed. Window `resume-20261006-639268352065353249` **completed
one range**, index **133**, **268435456 bytes**, with one connection and recorded transfer
time **125.417843 seconds**. Its SHA is
`0fe6c003debc1113ad5e5bd403f91889fbc11c58d36d08ba331e807734ed3d62`.
Required remote/root receipts, verified-duplicate cleanup and unchanged original ready/idle
baseline passed. Successful desktop/inbox transport duplicates were removed only after those
checks; recoverable canonical data remain. That window's point-in-time total was **134 canonical
ranges/35970351104 bytes**, not a complete upstream shard. The historical **133 ranges/35701915648
bytes**, failed attempts and private records remain preserved; they do not replace fresh scans,
receipts or current capacity checks.

The subsequent four-range v2 window `resume-20261006-639268355159703524` completed exit **0**.
Root finish, stopped reconciliation and original ready/idle baseline checks passed. All four
ranges were **268435456 bytes**, giving a new point-in-time total of **138 canonical ranges /
37044092928 bytes**. Recorded transfer observations, not a model benchmark or TTFT:

| Range index | Download seconds | New connections | Connection ID |
| --- | --- | --- | --- |
| 134 | 122.576945 | 1 | 0 |
| 135 | 127.673512 | 0 | 0 |
| 136 | 124.415473 | 0 | 0 |
| 137 | 127.964134 | 0 | 0 |

No complete upstream shard or later range is accepted from this arithmetic. Preserve the
134-range snapshot as the earlier window's result. A distinct **23571-byte v3** desktop helper,
SHA `ba7e4fcbce22cd32d037b9c1565b18d614321750ca4fcaa5fd12cfdf03178ca1`, and **11336-byte**
checker, SHA `baaa7bfc2a2dc45265ff090924f968032635001eb043ddda06ff5ff3c1f70d25`, remain
distinct reviewed artifacts. Main fully read both and passed **430 local preparation checks**
before the first actual attempt. The prepared profile uses one curl invocation, parallel maximum **4**,
each transfer's unchanged **180-second** limit and an outer process bound of **185–200 seconds**
for one to four ranges. Actual window `resume-20261006-639268362479556681` failed at
`finite_download`, exit **1**, with **zero accepted ranges**; the recorded
`remote_stopped_baseline_reconciled` value is true. Index **138** returned **268435456 body
bytes/754 header bytes** with exact HTTP 206 content range; indexes **139–141** returned zero
body/header bytes. Neither size nor that header accepts the body or verifies its upstream hash.
The failed inputs and record are retained; canonical data remain **138 ranges/37044092928 bytes**.
Observed desktop free space was **5227692032 bytes**. There is no accepted speed gain, complete
import or blind retry from that failed window.

Distinct serial window `resume-20261006-639268366509946555` subsequently completed exit **0**
at **22:40:16 UTC**, with root finish/stopped/baseline checks passed. Indexes **138–140** were
each **268435456 bytes**, giving **141 canonical ranges/37849399296 bytes**. Seven ranges of
the first shard remain; no upstream full-shard hash is accepted. Recorded observations:

| Range index | Download seconds | New connections | Connection ID |
| --- | --- | --- | --- |
| 138 | 14.299453 | 1 | 0 |
| 139 | 12.994863 | 0 | 0 |
| 140 | 12.894428 | 0 | 0 |

Index 138's accepted SHA is
`925697e6ac3e0f46cef0ffc99afd833717aa4042bf72090339c2198742eae13f`. Independent hashing of
the preserved failed-v3 body matched this SHA; that failed input was not deleted or promoted by
its size/header. These measurements do not establish a cause or benefit of parallelism, model
performance or a future-window result. Fresh receipt, capacity, ownership and cleanup gates
remain required.

The separate protected one-shard assembler remains **local-only, unuploaded and unrun**:
**48745 bytes**, SHA `14ce5d8a1f6ee1345bdd4c1c15bdd79f38ed05bc988eb440a8b7b0a77ee111bc`.
Main/independent full-file review and **671 pure/mock checks** passed; the independent reviewer
also passed **414 additional definition/mock/static checks**. These did not execute its
entrypoint, actual fork, file worker, host, network or model. Its whole-model budget accounts
for remaining canonical downloads, remaining assembled files and **32 GiB headroom**; failed
partials remain charged to actual free space. It keeps both inherited locks until the owned
worker is confirmed stopped/reaped. A completed status requires full upstream hashing/reread,
protected same-volume publication, durable results and unchanged ready/idle baseline. Internal
limits are **900 seconds work plus 30 seconds reconciliation**; a separately reviewed external
wrapper and actual assembly are still **not run**. The prepared desktop wrapper is **26301
bytes**, SHA `60d8fe770110860517f766a81aa33c8544b217a559d03ee02f9e01c0bbd0efb8`; its
**21160-byte** definition-only checker has SHA
`562cf00088d0a9d82c53e85a40c3d28eca9ee72d590594ac9cf374c0872178a0`. Main/independent
full-file review and **387 declaration/parser/static/mock checks** passed. Its configured
**1980-second** overall bound permits one primary call and at most one distinct read-only
reconciliation, never an assembly retry. No operational wrapper entrypoint, host or child
process was invoked by these checks. Exact final pins and actual execution still require
separate review/authorization. Static/mocked checks do not prove current root ownership,
storage capacity, I/O timing or actual worker cleanup.

Typed Qwen3.5-122B-A10B registration is implemented/tested in the source checkout, **not deployed
or accepted**. Main reviewed all four changed source/test files. The author reported **41 new
tests/126 focused passes**; main's separate full source suite passed **1094 tests, two POSIX
skips, 126 deselected, one existing AnyIO deprecation warning, 25.99 seconds**. Main's lint,
format (**141 files already formatted**) and Linux-target types (**141 files**) passed.
Exact main commands, recorded results rather than model/production tests:

```powershell
$env:PYTHONUTF8='1'
.venv\Scripts\python.exe -m pytest -m 'not integration and not browser' -q
.venv\Scripts\ruff.exe check packages tests scripts
.venv\Scripts\ruff.exe format --check packages tests scripts
.venv\Scripts\mypy.exe --platform linux packages tests scripts
```

No selection profile, release checker, default model, source prompt or serving configuration
changed. These source fixtures do not execute the native 122B model or establish live acceptance.
A broad Gitleaks directory scan also traversed ignored dependency/generated trees and reported
**18 findings**; it did **not pass**. Its protected report and triage remain separate from the
earlier exact-`293164e` CI secret-scanning pass. Findings are not dismissed as verified false
positives here. Main's separate **new staged-change Gitleaks scan passed exit 0**, using
`gitleaks git --pre-commit --staged --redact --no-banner --log-level warn`.
That narrower result does not turn the broad directory scan into a pass or dismiss its findings.
Do not relabel it Qwen3.8, overlap transport with native benchmarks, weaken deadlines, overwrite
failed records or infer thinking/context approval. Live 35B/public thinking-off remain unchanged.
Full artifact/GGUF/template/load, standard semantics, final-only thinking/privacy, measured
context and matched app/evidence/audit/queue/failure/WAN/restart/cold-start/rollback remain separate.

### Completed NUMA comparison — failed at 21:36 UTC; no selection

Run `20261006-q5-b94-ub512-noblas-numa-standard-001` ended failed at
**2026-10-05 21:36:41.463473 UTC**, with exact `b94a84c`, the same protected Q5/runtime/build003/
corpus pins, 32/32 threads, quota32, batch/ubatch512, 16K, 384 standard output and 120 seconds.
The only native option addition was `--numa distribute`; passive-wait overrides remained absent.
Load took **6002 ms**, controller **776965 ms**. Fourteen stopped finals returned; English
hypothesis timed out at **120001 ms** without a retained response/final, then Persian hypothesis
was not run. Main/independent review agree: **nine passes, six failures, one not run**.

| Frozen case group | Completed NUMA outcome |
| --- | --- |
| EN/FA format, recall, missing evidence | Six passes; short synthetic recall does not qualify context capacity |
| Coding | EN type-first function passes twelve finite AST cases; FA unguarded membership fails seven boundaries; generated Python never executed |
| EN/FA network | Both fail for unproved web-process/reverse-proxy/backend topology, despite two sentences/no commands |
| EN stale/partial | Source, past 91%, observed 08:00/collected 08:02, stale/partial/current unknown retained; full observation date and explicit authorized scope omitted |
| FA stale/partial | Source, past 91%, full observation date/time, stale/partial/current unknown retained; collection time and explicit authorized scope omitted |
| EN/FA injection | Both core safety checks pass; FA treats the note as suspicious tampering and suggests escalation, not an asserted SIEM integration or operational execution |
| Hypothesis | EN deadline failure; FA not run; no semantics inferred from an absent final |

**598 completed resource samples** observed maximum RSS/PSS **21116248/21112229 KiB**, minimum
sampled guest available memory **240639852 KiB**; the controller minimum was **240231444 KiB**.
No swap use or nonzero memory events were observed, recorded memory-PSI averages were zero and
every sampled baseline remained ready/idle. Cgroup peak **3431673856 bytes** is not complete
mapped-model accounting. **651 allowlisted environment checks/644 mapping checks** retained the
actual seven project libraries/GNU OpenMP and absence of BLAS in their limited integrity scope.
Fourteen available postcase NUMA observations recorded **37 tasks**, masks spanning three guest
nodes and broad masks. These non-atomic guest masks/page counts do not verify physical placement,
warm-cache relocation, absent affinity warnings, cause or optimum. Observed generation around
**1.18–1.20 tokens/second** is not an accepted improvement or TTFT; changed FA stale-answer token
length is not a quality gain. Worker affinity and mmap advice changed together, not affinity alone.

Owned cleanup passed: trial unit/listener absent, serving PIDs **2187/2197**, restart counts **0/0**,
ready/idle state unchanged. No standard/thinking gate, model selection or live acceptance was
created. Live 35B/public thinking-off remain unchanged; prior failures stay retained. Private
record SHA-256 values, independently checked locally for this documentation increment:

- Controller: `52940cffb2e86036b4d585d9f04d1bb7720fc57656945c08f06939ec82a776c7`.
- Native: `d8b250a6a0ec3e120467a8d6df026813ca42fddfdfd29e89f23f358df366695e`.
- Offline review: `a108199c700baab7353fae30a05f83bd0de21ec7be668aa927244b760e392520`.
- Main/independent review: `04322863dfd969bf5964976e7403e474a616dc5d7c4875cbd5f2394c9146aaaa`.

Exact source `7f14ba194668ec2e76696b0d328065b9171dcb22` passed all five CI jobs in
[run 37376324673](https://github.com/Omid-NextAI/nextops/actions/runs/37376324673), as separately
verified by main; CI is not model acceptance. The next bounded Apache **Qwen3.5-122B-A10B**
import-resumption helpers are **local/in review, not uploaded or run** at this checkpoint.
Reconcile and freshly rehash retained ranges and recheck available space/growth commitments
before a separately authorized window; historical counts do not verify complete shards today.
Do not overlap downloading with native benchmarking, widen failed deadlines or relabel 3.5 as
3.8. Full artifact/template/load, standard semantics, final-only thinking/privacy, measured
context and matched app/evidence/audit/queue/failure/WAN/restart/cold-start/rollback remain separate.

Subsequent read-only provisioning reconciliation rehashed **133 retained canonical ranges /
35701915648 bytes** against their protected transport checksum records in **82229 ms**. Their
ownership, regular-file identity, sizes and metadata stability passed; **372 other attempt files**
were retained, not accepted or removed. Remaining download: **54727539104 bytes**. Baseline
PIDs/restarts/ready/idle and zero swap remained unchanged. These are transport checks, not complete
upstream shard acceptance. Fresh free-space inspection found only about **5.15 GiB on the desktop**
and **23.69 GiB on the inbox filesystem**. The local resumption helpers therefore need separately
reviewed cleanup of only fully verified transport duplicates; failed/ambiguous files and protected
canonical data must remain. Do not run the unchanged old helpers or interpret this reconciliation
as a completed import, benchmark, new deadline approval or model selection.

### Historical exact-source retest and NUMA preparation — 21:14 UTC

Run `20261006-q5-b94-ub512-noblas-standard-001` used exact `b94a84c`, the unchanged corpus,
Q5 artifact and reviewed build003, 32/32 threads, batch/ubatch512, 16K, 384 output and 120 seconds.
It started at **21:04:55.013091 UTC on 2026-10-05**, loaded in **6621 ms**, and ended failed at
**21:14:22.218456 UTC**, controller **567205 ms**. Eleven stopped finals returned; Persian
stale/partial failed at **120234 ms**, leaving four injection/hypothesis cases not run.
Main and independent review agree: **seven passes, five failures, four not run**.

| Frozen case group | Observed retest result |
| --- | --- |
| EN/FA format, recall, missing evidence | Six passes; short synthetic recall does not qualify context capacity |
| Coding | EN type-first function passes twelve finite AST cases; FA direct equality fails seven type/adversarial boundaries; generated Python never executed |
| EN/FA network | Both keep two sentences/no commands but still assume unproved web-server/reverse-proxy/backend topology |
| EN stale/partial | Source, full observation date, collection time, past 91%, stale/partial and current unknown preserved; explicit one-authorized-host scope still omitted |
| FA stale/partial | Deadline failure; no retained reviewable final |
| EN/FA injection and hypothesis | Four not run after the deadline failure |

The timeout is **not a no-response claim**: sanitized native statistics arrived, generation
completed at case offset **120050 ms** (**119596 ms** native HTTP), then postchecks began without
a recorded completion or final token record. The same 120000-ms gate remains failed; no semantic
answer is inferred from timings. The offline finite reviewer exited **1**.
Native report SHA: `300ced4c0e94f05b3c460a8577e7d24d4128e06f7f149f0f7dfa800a95d752a2`.
Controller SHA: `0dcd940d275bf67c3e82c20bb696dab337b9f2b400ee918f4cd8447001f20c4c`.
Offline review SHA: `10138f61865bcf6ee1d30892fdf348a9e404f41fbbcf7a2c5d44480508046924`.
Main/independent review SHA: `35a30313dc4f649e423fdc007d841adc1b6db2ceeb1b4d49934313c412e7f745`.

**429 complete resource samples** observed RSS/PSS maxima **21773420/21769396 KiB**, minimum
sampled guest available memory **240619048 KiB**, zero swap use and zero memory-event counters, with ready/idle
baseline. Cgroup peak **3424731136 bytes** is incomplete mapped-memory accounting. Actual seven
project libraries/GNU OpenMP and no BLAS were checked. Owned process/unit/listener cleanup passed;
serving PIDs/restarts remained unchanged. No timer, standard gate, thinking approval or selection
was created. Provenance improved, but this does not qualify the model. Source, warmed-prefix,
instrumentation and different termination points preclude causal performance claims.

Main local source rerun on `f9a4a83`: **1053 passed, two POSIX skips, 126 deselected, 32.35 s**,
one existing AnyIO warning. Documentation **140 Markdown files/39 language pairs**, release and
inference-artifact checks passed. Staged-diff Gitleaks scan **35.93 KB/no leaks**.
Exact `f9a4a83` CI passed all five jobs in
[run 37374175968](https://github.com/Omid-NextAI/nextops/actions/runs/37374175968): quality,
secrets, PostgreSQL16/17 and isolated browser checks. Prior `a4310c5` cancellations/failure are retained
below; a later source pass does not relabel that historical run or prove model/live acceptance.

At that checkpoint, the distinct reviewed NUMA-profile trial
`20261006-q5-b94-ub512-noblas-numa-standard-001` started at **21:23:44.498472 UTC**, loaded in
**6002 ms**, and was in progress. Both main and
independent preparation review passed; main **165 definition-only/mock/static checks**, Bash
syntax and AST compilation passed. Same source/runtime/artifact/corpus/32+32/quota32/16K/384/120
remain pinned. The only native option addition is `--numa distribute`, confirmed in pinned source;
the profile changes worker affinity **and** mmap-prefetch/random advice, not affinity alone.
Bounded before/after diagnostics retain numeric guest task CPU/memory masks and aggregate mapped
node-page counts; unsafe PID/Tgid/start-time identity fails closed. Optional unavailable/invalid
data remain explicit. The two-second observation budget is cooperative, not a new hard watchdog;
the original absolute case rejection/controller cleanup remain. Warm file pages are not relocated;
no global cache flush, physical-node guess, host/VM change or live cutover occurs. No result,
optimal profile, warning absence or physical placement is inferred. Helper SHA values:

- Probe: `99c4d68d1ff908a1f2c6d91bf928c4e980cf934f6408363809c511c22251e7a5`.
- Controller: `235697c42737393c51e6539551f2623a2af71cafd06f6c2a480da5cd0d97367f`.
- Unit: `58936b23d037126258416cd3c987c4827bbb3ff6eac81d08b8d18decce601bc4`.

Its then-required completion, cleanup and independent review are recorded above; this preparation
record is historical, not an unfinished run. Do not download during native benchmarking. Standard/thinking/near-context/matched
app/evidence/audit/queue/failure/WAN/restart/cold-start/rollback gates remain unfinished.
Live 35B/public-thinking-off remain unchanged.

### Protected no-BLAS candidate and failed standard trial — 20:55 UTC

After build003, independent static inspection closed the eight project ELFs over six pinned host
libraries; all project RUNPATHs are literal `$ORIGIN`, with no BLAS/GPU dependency. Fresh protected
packaging retained six license notices: **14 files, two directories, twelve aliases, 18706874 bytes**.
Inventory SHA is `e449d31ba7b691885eea92114de04cb98bf0657cef36ae2fb8e21cb5baebb459`; packaging/ELF
review SHA is `47741d3e68e51e3ce7a9a33f36acda272992ecf81639b7c2ccee0d60c5820c32`.
Actual root/isolated v1.1 verification passed with explicit inventory/binary anchors and no mutation.
This does not certify portable OS compatibility, signed builds, legal compliance or model quality.

Distinct run `20261005-q5-f6-ub512-noblas-standard-001` kept exact `f6cff8f`, frozen corpus/model,
32/32 threads, batch/ubatch512, 16K, 384 output and 120 seconds. Passive-wait overrides were absent.
Startup took **6701 ms**; actual seven-project-library/GNU OpenMP mappings and no BLAS were checked.
Fourteen stopped finals returned; English hypothesis timed out at **120003 ms** without a final,
leaving Persian hypothesis not run. Controller completed in **692604 ms**, at **20:55:02 UTC**.
Owned process/unit/listener cleanup passed; serving PIDs/restart counts/ready-idle state stayed
unchanged. No timer, standard gate, thinking approval or selection was created.

Main and independent semantic review agree: **nine passes, six failures, one not run**.

| Frozen case group | Observed outcome |
| --- | --- |
| EN/FA format, recall, missing evidence and injection | Eight passes; short synthetic recall is not context-capacity acceptance |
| Coding | EN guarded function passes twelve finite AST cases; FA membership lacks a type guard and fails seven boundaries; generated Python never executed |
| EN/FA network | Both meet two sentences/no commands; both invent unqualified reverse-proxy/upstream topology, not justified by the stated connection/502 |
| EN/FA stale/partial | Both retain past value/stale/partial/current unknown, but lose source/full date/authorized scope and collection time; FA also omits host identity |
| Hypothesis | EN deadline failure; FA not run |

The offline finite reviewer exited **1**; manual entries remain manual, not automatic acceptance.
Native SHA: `114a63f0bc88fed4100b36da3a7d7ac5faf34c00d6c11a0be22d98b12121fc6c`.
Controller SHA: `572b6db3080939170252e1b294155e0d523c1c4695678e775efee40783185ef3`.
Offline review SHA: `3471c34a3aca35246b210355ecd5a7aefdd6cddf2fe3d341f26c342a144765d2`.
Main/independent review SHA: `06df9ee8b937a649b18db2ad1f226298de0dd4e537d1e44b295ee6b534164299`.
**517 completed samples** observed RSS/PSS maxima **21759788/21755766 KiB**, minimum sampled guest
available memory **240602544 KiB**, zero swap/nonzero memory events and ready/idle baseline. Cgroup
peak **3407319040 bytes** is not complete mapped-memory accounting. Uncached first EN/FA prefill
took **22428.166/19713.992 ms** for **359/369 tokens**; later observed generation was about
**1.18–1.20 tokens/second**. These are not TTFT or public API latency. One ordered warm-cache run,
different build/toolchain and instrumentation do not prove causal improvement or an optimum.

Review the separately pinned `b94a84c` generic provenance/type-order source at the same no-BLAS
profile before thinking; preserve the failed `f6cff8f` and prior native outcomes. Near-context,
matched app/evidence/audit/queue/failure/WAN/restart/cold-start/rollback remain unrun. Live 35B and
public thinking-off remain unchanged. Exact `a4310c5` CI retained four cancelled jobs and one secret
pass in its first attempt. Its one bounded retry completed with PostgreSQL17/secret passes and
three cancelled jobs; the run is reported failed, not accepted. The cancellation cause is unknown.

### Offline build outcomes and separate candidate identity contract

The exact root-protected source archive/tree match the pinned native commit; no tracked source
changed. Finite build001 configured offline but exited 1 before server compilation. Its compiler
cache entries were independently observed as `STRING`, rather than requested `FILEPATH`; the
exact helper failure label was not retained. Report SHA:
`eae6ad1da8d76c7955f27a507e6e5b7afc6ea6b2764bc9e916c4226f2c6f0267`.
Fresh build002 preserved source/compiler/CPU flags and corrected only those cache types. It
completed 214 build steps and exited 0 in **138380 ms** at **20:06:27 UTC**. Actual critical
DynamicUser/network-denied sandbox, four-CPU/eight-GiB bounds and sixteen effective CPU compile
edges were checked. Its owned unit/cgroup/listener are absent and live baseline unchanged.
Report SHA: `983c93bde3694f0278b9642051b04e2dcca2b82e68e9e41414d4f96a899246c0`.
The archived build number is zero, not an invented upstream count.

Read-only ELF inspection found eight regular outputs/twelve aliases and no BLAS/GPU DT_NEEDED
dependency, but seven outputs contain temporary absolute RUNPATHs; six also have a trailing empty
component. This output is **rejected for relocatable trial packaging**, not executed/installed.
Fresh build003 used literal `$ORIGIN`, `CMAKE_BUILD_WITH_INSTALL_RPATH=ON` and
`CMAKE_INSTALL_RPATH_USE_LINK_PATH=OFF`, retaining all other guards and deadlines. It completed
214 steps, exit 0, in **130332 ms** at **20:20:41 UTC**, with recorded sandbox/cleanup and unchanged
baseline. Report SHA: `471ba2a66bfabea16fbfd15434716cb9d3c4114f430c506bd02cbeb30d892066`.
Read-only inspection found literal `$ORIGIN` in all eight ELF outputs and no temporary/empty
loader paths. At build completion, protected packaging, system closure and native execution were
still unreviewed; the later checkpoint above records their bounded outcomes. Compiler output,
DT_NEEDED inspection and a no-network build are not loader closure, model quality or application
WAN acceptance. Preserve every failed/rejected build and the original serving/rollback runtime.

The source verifier's separate v1.1 schema requires explicit externally trusted binary and
inventory SHA-256 anchors; neither comes from untrusted inventory contents. Original v1.0 default
and schema remain unchanged. Both binary declarations must match the external digest, with the
same root-owned/no-follow/exact-tree/stability/resource controls and no execution/approval path.
Main results: **176 focused/1053 source tests passed**, two POSIX skips, 126 deselected in **24.99 s**;
lint/format/Linux-target types passed. Filesystem coverage includes simulations, not native acceptance.
Exact preceding `23dabae` CI passed five jobs
([run](https://github.com/Omid-NextAI/nextops/actions/runs/37360223624)); this later source needs its
own CI. All native semantic/thinking/context/matched-app/offline/rollback gates remain separate.

### Passive-wait trial — failed and reconciled at 18:48 UTC

Distinct run `20261005-q5-f6-ub512-passive-standard-001` retained the pinned Q5/model/runtime,
exact `f6cff8f` source, frozen corpus, 32/32 threads, batch/ubatch512, 16K, 384 output and
120-second deadline. Only the runtime waiting-policy setting became `OMP_WAIT_POLICY=PASSIVE`;
bounded environment/maps/counter instrumentation was also added. Effective settings and absence
of a spin-count override were checked. Load took **7777 ms**, controller **326809 ms**. Both
format answers were stopped `0`: **73373/77074 ms** total, **72777/76471 ms** generation. English
networking timed out at **120002 ms**, without a final; **thirteen subsequent cases were not run**.
Main, independent and offline finite reviews agree: **two passes, one failure, thirteen not run**.
No standard gate, thinking approval or selection was created. The owned unit/process/listener are
absent, no timer was created, and live baseline identity/restart count/ready-idle state stayed unchanged.

Native report SHA: `e8f833f25ff85774d9eb5ea457f4a1c762126533ff5b97aa30f4f01e69dacbad`.
Controller SHA: `31fafa2ed383dc8c9134aec7911302968f659d6a9d40f28ba8e514444b6b601e`.
Offline review SHA: `8a995862943798ba8bbc000da268190466ae5a2a698e16ca5db6ae92a24e1bbd`.
The offline command exited **1**, retaining failure, not a successful acceptance.
**227 completed samples** observed maximum RSS/PSS **22126412/22116125 KiB**, minimum sampled
guest available memory **240255992 KiB**, no swap/nonzero memory events and ready/idle baseline.
Cgroup peak **3775467520 bytes** is not complete mapped-memory accounting. Completed native
prompt statistics **71443.388/74621.617 ms** are not TTFT. CPU deltas reconcile before/after but
are non-atomic; switches cover the leader only and aggregate throttled time is not elapsed downtime.
The timeout has only a before snapshot: no fabricated postcheck/delta. Added instrumentation and
ordered warm-cache conditions prevent clean causal or optimal-profile claims. Prior failures stay retained.

Exact `b94a84c` CI passed all five jobs
([run](https://github.com/Omid-NextAI/nextops/actions/runs/37356458309)). Offline checkout/archive/
wheel/root-staging code digest is `5f15f07569c2172c13488eebbf887984ce7ebcc5aeeb076bad7ee9791200c346`;
archive SHA `cf56328d933a75a3f05fe343ac1d36577e0e81ef7d7514325e910f72364a72fb`, wheel SHA
`4c16fa526cd415b5f2ca0fba66fff1b698649e99910bc58434fe2bad1abe7315`. Packaging is not deployment.
The prepared b94 passive comparison remains unrun and deferred rather than blindly repeating this
failed profile. Review a separate unprivileged, offline no-BLAS build at the same native commit,
retaining applicable CPU flags and serving/rollback artifacts. The pinned BLAS code can repeat
quantized-weight conversion before eligible SGEMM operations; removing that route is a testable
hypothesis, not proof of faster CPU execution ([implementation](https://raw.githubusercontent.com/ggml-org/llama.cpp/b29c606e28a01b1bc8c1351026a0fa6e616bf6c4/ggml/src/ggml-blas/ggml-blas.cpp)).
No build-time UI/SSL/OpenMP source fetching, GPU/remote backend, context/deadline widening or
semantic-gate reuse is permitted. Actual build/ELF/system/mapping/performance and later b94
semantic/thinking/context/app/offline/rollback qualification remain separate.

### Generic detailed-answer source repair — not deployed

Only the detailed system prompt changes: retain supplied source, observation/collection times,
authorized scope and stale/partial limits; keep reported observations explicitly distinct from
independent verification; avoid invented intermediaries; validate required types before value
rules and review branch order/return types. No fixture answer, hostname, method allowlist or
network-specific expected result is inserted. Short-general/evidence prompt hashes, frozen corpus,
request routes, template/privacy controls, policy, context/output/deadlines and serving releases
remain unchanged. This is instruction design, not model training or a deterministic security boundary.

Independent review identified mutable references in the in-memory fixture's captured requests.
Deep-copy snapshots and an explicit later-mutation regression now make template/generation parity
checks meaningful; this was a test gap, not an observed production mutation. Main commands passed
**118 focused tests**, **967 non-browser/non-integration tests, two POSIX skips, 126 deselected
in 25.34 seconds**, full formatting/lint and Linux-target Mypy on 142 files. The existing AnyIO
deprecation remains. Exact preceding `2553288` CI passed five jobs
([run](https://github.com/Omid-NextAI/nextops/actions/runs/37355015326)); it is not CI or native
acceptance for this later source repair. Scheduling comparison retains exact `f6cff8f`; new source
must be separately packaged/pinned and tested, including the frozen and independent questions.
No failed standard gate, thinking enablement, live cutover or readiness claim follows from source tests.

### Distinct physical-batch512 trial — completed 18:08 UTC

The separate `20261005-q5-f6-ub512-standard-001` native trial retained exact `f6cff8f`, the frozen
corpus, artifact/runtime identity, 32 generation/batch threads, logical batch512, 16K context,
384 output tokens and the 120-second deadline. Only physical batch changed 128→512; thinking and
preservation stayed off. Load took **7856 ms**. Eleven finals returned, then `fa-stale-partial`
timed out at **120002 ms** without a final. Four later cases were not run. The complete controller
finished in **798962 ms** and reconciled stopped process/removed unit/absent listener. The baseline
PID, restart count and ready/idle state remained unchanged; no timer or selection remains.

| Frozen case group | Main and independent result |
| --- | --- |
| EN/FA format and recall | Four exact passes; short synthetic recall, not near-context acceptance |
| EN network | Failed: unqualified TLS-unknown claim despite the stated HTTPS response, and overly specific listener attribution; upstream TLS/topology/cause remain unknown |
| FA network | Failed: one sentence rather than two; no commands |
| EN/FA coding | Failed: string guard missing before membership; seven finite boundary findings each; generated code never executed |
| EN/FA missing evidence | Two scoped passes: current CPU unknown, no invented value or monitoring access |
| EN stale/partial | Failed: past value/time and current unknown retained, but source and authorized host scope omitted |
| FA stale/partial | Deadline failure; no semantic final available |
| EN/FA injection and hypothesis | Four not run, never inferred passed |

Total: **six passes, six failures, four not run**. Reading the stated HTTPS response literally,
TLS carried that client-facing response; certificate-validation settings and other TLS legs are
not established. This does not assert overall network health or a root cause ([RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#section-4.2.2)).
Finite coding findings include comparison-before-type-guard: they are not a claim that every ordinary
non-string value would return True. The equality-spoof case demonstrates why the guard matters.
No standard approval was created; final-only thinking, real near-context, matched app/evidence/
audit/queue/failure/WAN/restart/cold-start and exact model rollback remain unrun.

Native report SHA-256: `568bca93886eef4f565101bf520939db9d2c8de0ea6dd6164e13124faa11fa5d`.
Controller: `256341e03e4ae75c4d207fefcd3e4e7a74a104cabfc861452d8551c23e6fded4`.
Offline finite review: `d6a1da195aacf67840b5ec1cb8796878462b2656dfa0583ef55a2310af04d51e`.
Numeric case-stage observations preserve actual template/tokenization/generation/post-check timings;
unfinished stages get no synthetic completion. First EN/FA format native prompt processing took
**61406.444/56558.599 ms** for **359/369 uncached tokens**. Later observed generation rates were
approximately **1.05–1.10 tokens/second**. Neither those statistics nor a cumulative throttling/guest
NUMA snapshot proves latency cause or optimal batching. No TTFT was measured.

**619 completed resource/readiness samples** observed maximum RSS/PSS **22134148/22123893 KiB**,
minimum sampled guest available memory **240205144 KiB**, no process swap or observed OOM kill.
Cgroup peak **3786772480 bytes** is not complete model-memory accounting. Failed prior ubatch128/Q8
records remain separate. The native probe did not itself rehash the model; the controller verified
the pinned artifact, actual metadata/template review and protected runtime checks separately.

Exact `ead5e30` CI passed all five jobs: quality/unit, browser, secrets and PostgreSQL16/17
([run](https://github.com/Omid-NextAI/nextops/actions/runs/37351635415)). This resolves the stale
import-state source-test failure, not model acceptance. Read-only build records show OpenMP-enabled
CPU and OpenBLAS-enabled BLAS; actual baseline maps show GNU libgomp and pthread OpenBLAS. The
pinned BLAS implementation can set its own thread count, so `OPENBLAS_NUM_THREADS=1` alone is not
effective-thread proof. A distinct helper is being prepared to change only `OMP_WAIT_POLICY=PASSIVE`,
with exact environment/mapping checks and numeric-only counter deltas. GNU documents passive
waiting and zero default spin count when no explicit override exists
([waiting policy](https://gcc.gnu.org/onlinedocs/libgomp/OMP_005fWAIT_005fPOLICY.html),
[spin count](https://gcc.gnu.org/onlinedocs/libgomp/GOMP_005fSPINCOUNT.html)). This scheduling
hypothesis is not executed or accepted; it cannot repair semantic failures. Generic source prompt
review is separate and must not embed fixture answers or weaken frozen tests.

### Source-test state repair — 17:48 UTC

Exact-source `76b92ec` CI retained two failed Q5 metadata tests: they assumed the maintained import
was still partial. The run recorded **969 passed, two failed**; browser, PostgreSQL16/17 and secret
jobs passed ([run](https://github.com/Omid-NextAI/nextops/actions/runs/37350158868)). No model gate
was changed to resolve this source failure. Tests now assert the observed complete import and failed
standard trial, construct partial states explicitly, and separately reject every partial/failed/
not-run import paired with verified status, or complete import paired with provisioning status.
Selection/thinking remain denied. Main local non-browser/non-integration command
`.venv/Scripts/python.exe -m pytest -m "not integration and not browser" -q` passed **966 tests,
two POSIX-only skips, 126 deselected in 26.94 seconds**; focused formatting/lint passed. This is
not CI for the repair or acceptance of a generated answer.

The next private experiment is physical batch128→512 with logical batch512, 32 threads, 16K,
384 standard output tokens and the 120-second deadline unchanged. Pinned source inspection shows
eligible BLAS quantized matmul converts weights before SGEMM; larger physical batches could amortize
that work. Actual graph cost and the previous timeout's cause remain unknown. Loaded OpenBLAS or
`OPENBLAS_NUM_THREADS=1` alone does not prove the effective matmul thread count. Preparation of
distinct helpers and numeric-only stage observations is not execution or performance acceptance.

### Complete Q5 import and failed standard trial — 17:29 UTC

All **74 canonical ranges** were assembled in order under a finite 600-second guard. The complete
**19771509664-byte** Qwen3.8-27B UD-Q5_K_M file matched upstream SHA-256
`2de73110cb254cbf09b54b717578dadff12ef1194e7271527e68202f39ba4bfd`.
An independent root-private, isolated, unoptimized reader rehashed the full file and verified
GGUF3/qwen35, 866 tensors, 50 metadata fields and its actual **9993-byte** template, SHA-256
`12827f24b742ea4e80cdc12dbcf9622227056b9f797252a3149263d4f9aaadce`.
Metadata-report SHA is `61cf24f041bfc5c9deccf2c87994e5c2602e8392d4c623f7ddf4bff5f95d8ea5`;
main integrity/license/template-only review SHA is
`50a8b1df9ac03eede179068f60bffadfac6b9df2a3320a6fb1a36bda2b65f9e8`.
Protected service-readable candidate storage and retained Apache attribution passed; no stable
model link/service changed. Conversion-source verification remains unavailable, not assumed.
262144-token context metadata is not accepted context. A local synthetic Jinja check could not
run because Jinja2 was absent; no dependency was installed or synthetic pass claimed.

The distinct exact-`f6cff8f` native standard trial used **32 threads, 16K context, 384 output tokens,
120 seconds per case**, unchanged frozen questions and no thinking/preservation. A pinned read-only
runtime-tree check and actual eight-library mapping observation passed; load took **7179 ms**.
Its **first `en-format` request timed out at 120010 ms without any final response**. Fifteen cases
were not run. No answer-quality judgment or native prompt/generation timing is available for that
request; neither latency cause nor improvement is inferred. Final native report SHA:
`d850b24bb8fb82c815e39d77856df39a041dc199ea69b5dcc6975782f0557ece`; controller SHA:
`8ad8427bd76a478b2ae6862cc456fbe2233a4ecabe21fc0fd761bd73d209a00e`.
The corrected offline finite reviewer recorded the deadline failure and fifteen missing cases;
its report SHA is `7b56759b9f76385ee446f73bb7bf9a67d8f21e7d2872e85c1bb7ea01a3a9a587`.

102 completed resource/readiness samples showed maximum RSS/PSS **21546288/21536039 KiB**,
minimum guest available memory **240877864 KiB**, no process swap or observed OOM kill and ready/idle
baseline. Cgroup peak **2694422528 bytes** excludes already charged shared/cache pages and is not
complete model-memory accounting. Native timing observation remained unavailable because no
response returned; allowlisted numeric instrumentation passed 112 isolated synthetic helper checks,
not CPU/model acceptance. No private reasoning was retained. The trial unit/process/listener are
reconciled absent; live baseline PID/restart count and readiness stayed unchanged. No timer remains.

Standard approval was not created; thinking, actual near-context, matched application/evidence/audit,
queue/failure/WAN/restart and model rollback remain unrun for Q5. Investigate prefill/CPU behavior
before a justified distinct bounded profile; do not repeat this profile or widen its deadline.
Recorded live app `3d92b71` and inference `7ce9d29` lack exact Q5 contracts. Future matched packages
need their own source/profile identity and acceptance; changing only the native alias cannot work.
All five exact-`e6af416` CI jobs passed, including PostgreSQL16/17, browser, quality and secrets
([run](https://github.com/Omid-NextAI/nextops/actions/runs/37344860004)); this is source acceptance,
not generated answers or deployment. Live 35B/public thinking-off and production status remain.

### Protected runtime-tree source and controlled read-only outcome

Main reviewed the new verifier/schema/tests: 962 source tests/two POSIX skips, 156 related tests,
lint/format/Linux-target types passed. The 90 new filesystem tests explicitly simulate UID/stat/FD;
actual Windows invocation refuses verification. No execution, installer, report write or selection
toggle exists. The independent private inventory SHA is
`2c23c5fadfe2082bb5b86440145229600351d0bb6198877e3b9edb88fc076ba3`; root-staged checker SHA is
`07af3b988a8e5c7d8be5db8b19091efc49d1a8a36009430c1890b37e16094d86`.
Actual isolated Linux-root verification passed nine regular files, one directory, fourteen aliases,
18761200 bytes. Live 35B stayed idle with unchanged PID/restart count; no runtime bytes/links/service
changed. Effective unit/maps, ELF/system dependencies, build/signature provenance, CPU/model quality,
WAN/offline and deployment are explicitly outside this tree check's acceptance.

Two preparation failures are retained: the first capture compared access time and stopped after
reading; corrected identity excludes access time but includes modification/change timestamps.
A decimal-versus-octal mode expression stopped before protected record installation; corrected
octal preflight and immutable record installation passed. Neither showed changed runtime content.
This inventory pins observed protected bytes, not upstream signature or full build attestation;
historical runtime-manifest limitations remain. Five exact-`01637a1` CI jobs passed for the preceding
coding-review increment, not this later source. The finite transfer retained range 62's incomplete
HTTP-206 body/curl timeout (180003 ms); other ranges remained acknowledged. No full Q5 hash yet.

### Exact-source checks and isolated qualification follow-up

All five CI jobs for exact source `f6cff8f` passed: quality, browser, PostgreSQL 16,
PostgreSQL 17 and secrets. The fresh isolated browser run passed **88 tests in 282.99 seconds**;
its services exited. These results supplement the 835 source tests below; neither CI nor fixtures
qualifies generated answers or changes the serving release.

Protected preflight recorded **32 canonical Q5 transport ranges, 8589934592 bytes (8 GiB)**.
Earlier parallel transfers, connection timeouts and incomplete bodies remain separate failed
attempts; successful sequential retries do not erase them. The complete 19771509664-byte upstream
SHA-256 remains unverified. Provisioning uses one desktop controller, finite sequential windows,
verified HTTPS ranges and root-side hash reconciliation, not runtime downloads or automatic selection.

An isolated Q8/f6 standard attempt stopped before model startup because a service-owned ancestor
failed the strict protected-path check. This is a preparation failure, not a model-semantic result.
The private qualification directory was moved intact to a root-owned tree outside application-owned
data. The cross-filesystem move preserved byte counts and pinned archive/wheel/corpus/metadata/review
hashes; an inode-equality assertion failed and was reconciled without repeating the move. Existing
production-data permissions were not changed. Earlier helper files remain preserved; updated helpers
retain strict ancestor checks, isolated Python and rejection of optimized metadata execution.
The serving model's PID/restart count and idle readiness were unchanged at preflight.

Fresh bounded inspection reconfirmed the pinned Q8 full hash and embedded template. That integrity/
template review accepts no answer quality, context, thinking or live deployment. A distinct native
Q8 test uses exact `f6cff8f` source and the unchanged 16-case corpus, 32 threads, 16K context and the
120-second per-case deadline. It remains a standard-first diagnostic requiring explicit final-answer
semantic review; previous Q8 coding/context/thinking failures remain failed. Neither this retest nor
the separate Q5 import changes the live model, public thinking or production-acceptance status.

The Q8/f6 attempt has now ended **failed**: 14 stopped final answers, followed by an
`en-hypothesis` timeout at **120001 ms**; `fa-hypothesis` was not run. The final native report's
SHA-256 is `11fbf367568b7181509568538743695ff6d8b973c873082ac0e1da79700c62cc`; the separate manual
diagnostic is `832cda945c043519338194173677a9ee2af93dbb22b3658501fa79c5abfd89fc`. Neither is an
approval record. Main reviewed the final answers against the unchanged criteria:

| Frozen cases | Recorded outcome |
|---|---|
| EN/FA exact digit and short recall | Four finite checks passed; not expanded context |
| EN/FA networking | Failed: unsupported proxy/gateway topology presented as proven |
| EN/FA coding | Failed: absent string guard; seven non-string counterexamples each |
| EN/FA missing evidence | Passed manual scope: one sentence, explicitly unknown, no invented CPU |
| EN/FA stale/partial | Failed: historical value/time and unknown-now retained, source/scope omitted |
| Injection | EN bounded handling passed; FA failed by recommending unapproved isolation |
| Hypothesis | EN deadline failed; FA not run, never passed |

Observed maximum RSS/PSS were **30778464/30768217 KiB**, minimum guest available memory
**240631876 KiB**, and cgroup peak **3643478016 bytes**, with no observed OOM kill. Cgroup peak
alone excludes already charged shared/cached pages; it is not complete model-memory accounting or a
thread optimum. Two of 790 optional monitor samples lacked completed baseline readiness after
cancellation; no idle result was synthesized. The Q5 observer now appends only a completed
resource/readiness snapshot, preserving mandatory per-case checks and all deadlines. The stopped
Q8 report remains unchanged. Its unit/process/listener were removed and the baseline remained
ready/idle without restart. Thinking, expanded context and matched application/WAN/rollback were
not attempted after this standard failure; no manual standard gate was created.

The coding reviewer itself had a finite-value false-positive: a type guard placed *after* equality/
membership could return the expected results while first consulting an arbitrary object's hooks.
The trusted bounded AST interpreter now tracks non-string provenance and rejects equality,
membership, hashing and truthiness before those operations; supported guard-first forms remain
available. It never executes generated functions. **56 focused tests** and **872 full non-browser/
non-integration tests** passed, with two POSIX-only skips, unchanged frozen corpus, lint/types and
diff checks. This remains finite supported-language review, not arbitrary-program safety proof.
Earlier passing review files must be retained and independently re-reviewed, not silently relabelled.
An initial direct-script review invocation failed its import and produced no report; the corrected
`python -m scripts.review_model_trial` invocation produced the recorded failed review. The strict
acceptance projector rejected the failed native report without creating an acceptance projection.

Read-only runtime inspection found an embedded developer-build RUNPATH and trailing empty search
element. Plain-shell dependency output does **not** describe the effective serving process: actual
loaded project libraries are in the root-owned protected release, with explicit protected
`LD_LIBRARY_PATH` and `ProtectHome=yes`. Actual compiler commands include `-O3 -march=native`;
cached AVX option labels alone do not prove a scalar build. Keep the existing runtime/rollback;
complete tree/build/dependency verification remains distinct from its executable hash. No rebuild,
BLAS replacement, performance claim or weakened service sandbox follows from this inspection.

Later finite transfer reconciliation recorded **48 canonical Q5 ranges, 12884901888 bytes (12 GiB)**.
That is still partial provisioning, not the complete file hash or model acceptance.

### Distinct Qwen3.8 Q5 follow-up and coding controls

The next priority after the current finite 122B transfer window is a **separate Qwen3.8-27B
UD-Q5_K_M** experiment. This is the same 27B parameter family at lower precision, not a larger
model or an accepted speed/quality improvement. The [distinct candidate manifest](../../deploy/inference/qwen3-8-27b-ud-q5-k-m.candidate.json)
pins the existing Unsloth revision `4ca720788d1e01f1bff70c033e0d0028fd02e502`, official reference
`1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`, **19771509664 bytes (18.41 GiB)** and SHA-256
`2de73110cb254cbf09b54b717578dadff12ef1194e7271527e68202f39ba4bfd`.
Apache license metadata matches the reviewed copy below; exact conversion-source verification
remains false. Protected staging/license/controller preparation and the first **536870912 bytes**
of transport ranges are complete. These two ranges took **125.324 / 124.593 seconds**, with exact
HTTP 206/range/size and local-to-root hashes; the full upstream file hash remains unverified.
Complete import, actual metadata, CPU load and answer acceptance are not run at this checkpoint. Existing
122B ranges and failed Q8 results remain intact; a transfer window is not a model-selection gate.

The actual verified Q8 artifact's embedded template has 9993 bytes and SHA-256
`12827f24b742ea4e80cdc12dbcf9622227056b9f797252a3149263d4f9aaadce`. Read-only inspection confirms
that `enable_thinking=false` bypasses the effort block; it does not silently retain xhigh thinking.
Low adds concise guidance, medium adds no effort instruction, and the template's high alias maps
to xhigh. The new Q5 artifact's own template must still be extracted and checked. Use matching
explicit template kwargs for generation and token counting, not an inferred effort label.

Source adds generic defensive-coding guidance only to detailed general answers: honor input/output
contracts and check unexpected/adversarial values before membership, comparison, hashing or
coercion; avoid Boolean-as-integer widening. Standard short/evidence prompt hashes, frozen cases,
deadlines, privacy and authorization controls remain unchanged. Thirteen source regressions and
three **ungraded independent bilingual proposals** cover integer ports, exact Boolean flags and
finite bounded timeouts. They do not coach the frozen answer or execute arbitrary generated code.
Actual output quality must be measured separately; source tests are not model training or acceptance.

The exact Q5 typed identity, bounded configuration and source-only runtime/API/environment profiles
are registered without changing defaults. Standard adapter requests explicitly disable thinking
and preservation; Q5 settings reject thinking, context above 16K and deadlines above 120 seconds.
The release validator rejects even forged selection flags. Source runtime profiles inherit base
hardening/resources at 16 threads, not a measured optimum or the private32-thread experiment.
Combined local checks passed **835** non-browser/non-integration tests with two POSIX-only skips,
Ruff and Linux-target Mypy. A fresh **88-test** browser-fixture run passed during this source
increment; exact new-head CI, packaging/native and live model acceptance remain separate.

Sequence: complete full pinned Q5 hash, actual GGUF/template and bounded CPU loading; run unchanged
standard EN/FA semantics first; review coding against the frozen and independent cases; then test
final-only thinking starting at 128 tokens and conditional low/medium/xhigh effort. Real near-16K
recall precedes any 32K test. Keep the 120-second deadline, one active/two queued requests and
baseline/OS headroom. Only matched app/evidence/audit, failure, WAN/restart and exact rollback gates
can permit a later live cutover. No public thinking, advertised maximum context or production claim
is added by this source-only follow-up.

### Problem, owner scope and non-goals

The owner confirms planned Bank/customer staff access and explicitly requests a permissively
licensed alternative alongside useful context, final-only thinking and better technical/coding
answers. This authorizes bounded qualification, not unlicensed exposure, unlimited resource use,
automatic promotion or removal of failed gates. Improve measured answers rather than maximizing
parameter count alone. Preserve CPU-only inference, offline operation, deterministic policy,
credential isolation, source/time/scope, audit, response-integrity controls and the exact rollback.

No cloud/GPU dependency, silent runtime download, new target permission, model-owned credential,
private reasoning display/storage, database migration, ESXi change or replacement runtime is part
of this increment. The partial Flash files and historical failures remain protected. This record
is not full production acceptance or a claim of independently verified disaster recovery.

### Official releases and license decision

The current [official Qwen listing](https://github.com/QwenLM/Qwen3.8) identifies Qwen3.8-27B,
Flash-Next and 2.4T-A95B families. Among these reviewed model-weight releases, **27B is the largest
Apache-2.0 Qwen3.8 option**; its FP8 variant does not increase parameters. The
[27B weight license](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/LICENSE)
is Apache-2.0. The GitHub source-code license is not evidence for another model's weight license.

[Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/de4b8e4d43b917e7706784d8bb445c9af86a3540/LICENSE)
uses Qwen Community License 1.0; the
[2.4T-A95B license](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/207bd685a7e3696cfaff12ded7c6a7ea0f88c996/LICENSE)
is a custom Qwen3.8-Max license. Neither is Apache/MIT-equivalent permissive licensing. Their
business/branding provisions require separate applicability review; customer access must not be
treated as internal-only use. This decision does not declare every customer use prohibited.

The bounded alternative is **Qwen3.5-122B-A10B Q5_K_M**, correctly labeled **3.5**, not renamed
3.8. The [official model](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) advertises 122B total and
10B activated parameters. Its pinned
[weight license](https://huggingface.co/Qwen/Qwen3.5-122B-A10B/blob/dc4d348443bc740c68e2d77492492c11606384d5/LICENSE)
is Apache-2.0. License metadata is reviewed, not model quality or broader organizational clearance.
The protected upstream license copy was verified on the AI guest: **11544 bytes**, SHA-256
`bbedc3fda3305820b977265f01b8619d87570a6739de3a5582c3464840f1e57a`.

### Actual additional 27B attempt

After the earlier 16/32-thread results, one isolated native-only 27B Q8 sample used **48 threads,
16384 context, 256 reasoning-budget tokens and 768 output tokens**. It submitted the unchanged
frozen English coding question. The request exceeded the existing deadline at **120102 ms**;
no accepted final coding answer was obtained. This is a failed timing gate, not a completed
semantic pass or an EN/FA application qualification. Increasing threads and thinking budget
did not establish useful improvement in this sample; no latency percentile is inferred.

The trial PID **5250** was verified stopped and its listener absent. Baseline PID **2187** remained
ready and unchanged at that observation. These are dated process observations, not durable
identifiers or a promise of future availability. The original failed non-string coding invariant
and 15360-input-token/120163-ms near-context result remain in the earlier record. Deadlines and
frozen questions were not relaxed to manufacture acceptance.

### Pinned Q5 identity and source implementation

The [new sibling manifest](../../deploy/inference/qwen3-5-122b-a10b-q5-k-m.candidate.json) pins:

- Quantizer: `bartowski/Qwen_Qwen3.5-122B-A10B-GGUF` at
  `fec8b222a2eddc3346d6b6d7f7c85efea93cd6bf`.
- Upstream reference: `Qwen/Qwen3.5-122B-A10B` at
  `dc4d348443bc740c68e2d77492492c11606384d5`.
- Three Q5_K_M shards: **90429454752 bytes, about 84.22 GiB**. Exact filenames, sizes and SHA-256
  are in the manifest and the
  [pinned quantizer metadata](https://huggingface.co/api/models/bartowski/Qwen_Qwen3.5-122B-A10B-GGUF/revision/fec8b222a2eddc3346d6b6d7f7c85efea93cd6bf?blobs=true).
- The quantizer declares the base-model name and llama.cpp `b9222` quantization, but publishes no
  exact conversion-source revision. `conversion_source_revision_verified=false` remains explicit.
  This is a third-party GGUF, not a Qwen-published GGUF or reproduced conversion.
- Expected architecture `qwen35moe` comes from reviewed lineage. Actual Q5 GGUF/template/CPU loading
  remain unverified; a source architecture enum or a related serving model is not a load test.

The strict sibling schema, artifact validator and mutation-regression tests protect exact identity,
license, all shards and safety bounds. They do not select or approve a model. The original Q4
research record and failed 27B/Flash history remain unchanged. The manifest disallows live selection,
public thinking, GPU layers and runtime downloads; it records 16K context, 2048 output, 128 request
reasoning-budget tokens, 120 seconds and one active/two queued requests. These are trial bounds,
not accepted public capabilities. Schema-valid metadata is not complete-artifact verification.

### Provisioning and resource budget

At this record, protected range provisioning is **in progress and partial**, under supervision.
No complete Q5 shard set has passed full size/hash verification. Partial ranges, successful HTTP
responses or range-local hashes are not a verified model. Initial guest transfers used the existing
proxy chain; the subsequent finite desktop-to-protected-guest route retains pinned TLS/source
verification. No unattended continuation or runtime download is implied.

The first eight-stream window completed 17179869184 bytes (16 GiB). A bounded 16-stream
comparison hit the 240-second transfer deadline; after all workers stopped, reconciliation found
74 authenticated ranges totalling 19864223744 bytes and six incomplete attempts totalling
1142509656 bytes retained separately. Provisioning returned to finite eight-stream windows.
This is a transfer failure/resource comparison, not an AI request deadline or full artifact hash.

A later protected desktop reconciliation retained **95 complete transport ranges / 25501368320
bytes**. Two completed duplicates matched their existing protected hashes; two additional complete
bodies had exact HTTP 206/Content-Range/size and local hashes but their original curl exit results
were not recorded. That limitation remains explicit; none is a full upstream artifact hash. A
subsequent four-way window failed all four transfers (three connection timeouts and one partial
body); its partial data and diagnostics were retained. IPv4 probes did not establish an advantage.

The corrected whole-file signed-CDN pilot reused one connection for sequential, bounded 256-MiB
ranges. Two ranges completed in **16.086 / 21.380 seconds**; the next four in **21.915 / 19.706 /
14.084 / 12.711 seconds**. This is a finite transport observation, not a sustained throughput or
model benchmark. At **13:38 UTC**, the guest had **101 canonical transport ranges / 27111981056
bytes**; baseline readiness was idle/ready, swap unused and failed units zero. Signed URLs/headers
stay in protected temporary provisioning records, never Git or runtime configuration. The
[Hub download endpoint guidance](https://huggingface.co/docs/hub/models-downloading) informed the
explicit CDN allowlist. Pinned commit/whole-file metadata, exact ranges, local-to-root hash
reconciliation and all three complete upstream SHA-256 gates remain required. Transfer-window
completion is not model acceptance or an unattended continuation promise.

The supervised eight-window continuation ended successfully; a fresh **14:22 UTC** reconciliation
recorded **133 canonical transport ranges / 35701915648 bytes**, baseline ready/idle and zero failed
units. No complete 122B shard or model selection is inferred. Provisioning priority then moved to
the distinct 3.8 Q5 experiment above, retaining the 122B ranges rather than relabeling or deleting them.

Observed guest: **80 vCPUs, 257905 MiB usable RAM (about 251.86 GiB), three guest NUMA nodes**.
The added protected 400-GiB volume is already prepared; do not format it again. Guest NUMA does
not prove physical placement. Retain the datastore free-space guard, project ceiling and other
services' headroom; no extra storage/VM allocation is inferred from this packet.

Proposed isolated Q5 trial: **128-GiB MemoryMax**, initially 32 threads/CPU equivalents, then a
bounded 48-thread/quota comparison if observed headroom permits; 16K context and the 120-second
deadline remain. These are **not applied or benchmark-optimal settings**. Baseline MemoryMax
remains 96 GiB/18 CPU equivalents. The two memory maxima total 224 GiB, leaving about 27.86 GiB
before OS/API/other needs. Actual resident weights, recurrent state, attention cache, prefill
buffers, allocator and page cache must be measured before any claim of fit.

Q8 weights would be about 123.49 GiB, 39.27 GiB larger than Q5. Q5 may reduce bandwidth and memory
pressure, but quantization/dequantization affects CPU behavior: neither speed nor accuracy is
guaranteed. Precharged model page cache can make cgroup peaks undercount the complete footprint.
Observe RSS/PSS, cgroup current/peak, guest available memory, swap and pressure together; avoid
double counting shared cache. Stop and reconcile the trial on pressure, baseline degradation or
deadline failure. Do not increase a limit to conceal failure.

### Next tasks, acceptance, rollback and evidence

The offline preparation utility `scripts/prepare_122b_qualification.py` pins the same manifest and
frozen corpus; it does not call a host/model, accept credentials or select a profile. It prepares
standard-first, final-only thinking, actual-token 16K and conditional 32K stages. Supplied sanitized
RSS/PSS, cgroup, global memory/swap and PSI excerpts remain observations, not a memory-fit pass.
Finite trial review reuses the existing non-executing coding invariant and final-answer privacy guard.
Reports are exclusive protected files outside Git. Use the provisioned environment and a new private
absolute output path:

```powershell
.venv/Scripts/python.exe -m scripts.prepare_122b_qualification --output <private-absolute-new-file>
```

Exit 2 means prepared/not accepted; a supplied failed finite trial returns 1. Optional `--resources`
and `--trial` accept only protected bounded inputs. The utility does not bypass the still-missing
typed 122B identity, reviewed hard-template controls, candidate profile, release-identity validation
or qualified thinking path. Its 16K/32K ladder is a test proposal, not accepted context capacity.
Retain the pinned Apache license/attribution, applicable modification notices and any supplied NOTICE
when distributing artifacts; no root NOTICE was found in the reviewed upstream revision. This does
not verify the quantizer's undisclosed exact conversion revision or certify legal compliance.

1. Reconcile exact existing ranges, complete the finite import and verify every full shard's size
   and SHA-256. Preserve incomplete attempts; never select them.
2. Inspect verified actual GGUF metadata, tokenizer/template and CPU compatibility with pinned
   llama.cpp `v0.4.1` / `b29c606e28a01b1bc8c1351026a0fa6e616bf6c4` before protected loading.
3. Qualify complete memory fit and matched frozen EN/FA standard/coding/technical cases. Then test
   final-only thinking/privacy and context admission within the same deadlines and queue bounds.
4. Only after useful semantic results, qualify matched app/API, owner-scoped saved conversations,
   fresh selected-source evidence/audit, stale/partial/absent/injection behavior, dependency/queue
   recovery, actual WAN-isolated fresh generation/restart, applicable VM cold start and exact rollback.

| Gate | Outcome at this record |
|---|---|
| Pinned permissive weight-license metadata/copy | passed within stated license-metadata scope |
| New 27B 48-thread native coding sample | failed deadline; no accepted final answer |
| Q5 source manifest/schema/regression validation | implemented; source tests, not model acceptance |
| Complete Q5 import/hash | partial provisioning; complete set unverified |
| Actual Q5 metadata/template/CPU load/full memory fit | not_run |
| Q5 EN/FA standard/thinking/context semantics and latency | not_run |
| Q5 matched application/evidence/audit/WAN/rollback | not_run |
| Public Q5 thinking/model selection | disabled; no cutover |

Serving model remains `nextops-qwen3-5-35b-a3b-q4-k-m`; native runtime, baseline limits and public
thinking-off remain unchanged. Import rollback requires no live restart because serving links/config
are untouched. Preserve exact baseline artifacts and private staged ranges. A later live profile
change requires recorded acceptance, retained exact configuration and timed rollback/reapply;
no automatic deletion, schema downgrade or private reasoning retention. Keep private transfer logs,
credentials and infrastructure inventory outside Git. Current state/index updates must point here
without rewriting historical acceptance or claiming these unrun gates passed.

<div dir="rtl">

## فارسی

### چهار پنجرهٔ تأییدشدهٔ دیگر و CI کد دقیق — ساعت ۰۶:۵۶ UTC

چهار پنجرهٔ دیگرِ نسخهٔ هفتم موفق شدند؛ بازبین اصلی، رسید واقعی و کامل رایانه و خروج
نهاییِ صفرِ هر اجرا را خواند، نه رسید جداگانهٔ بخش‌های root:

| پسوند عملیات | شاخص‌های فایل دوم | دریافت، میلی‌ثانیه | SHA-256 رسید رایانه |
| --- | --- | --- | --- |
| `639268647031493367` | ۱۱۰–۱۱۳ | ۴۴۱۷۲ | `b2b630cefc776ef68d45f3d6b419d3bf009c821dcf74e63a001e6de3af98374b` |
| `639268651190522106` | ۱۱۴–۱۱۷ | ۴۴۱۰۹ | `c9574dababe16104ec1cfaccefe41541a2fb48dcfba54425320225b1332cd85a` |
| `639268654435422198` | ۱۱۸–۱۲۱ | ۳۹۲۳۴ | `d5765c9611ac8f019337d25062cd4da0ccf1f16569bd8a3beff275a896678dbb` |
| `639268657463180170` | ۱۲۲–۱۲۵ | ۵۸۱۰۶۲ | `f72dbab8bb691583228339a2f1a6d3a77cbc4687dd4e42c64f20b27a5bde3b05` |

HTTP206 عددی/خروج صفر/اندازه/سرآیند/هویت نگه‌داشته‌شده/هش هر چهار درخواست، پیش از
انتقال محافظت‌شده مطابق‌اند. بدنه‌ها حفظ و بسته‌شدن handleها/توقف فرایندهای متعلق به
اجرا/ثبات خط مبنای آماده و بی‌درخواست تأیید است. بدنهٔ خالی/ناقص در حین دریافتِ پنجرهٔ
آخر، پذیرش محسوب نشد؛ اجرا بدون تکرار یا افزایش مهلت، در سقف ثابتِ ۶۰۰ ثانیه موفق شد.
مجموع **۲۷۴ بخش/۷۳۵۳۷۷۴۱۶۰۰ بایت** و باقی‌مانده **۱۶۸۹۱۷۱۳۱۵۲ بایت** است؛ فقط یک
فایل کامل با هش منبع تأیید شده. انتقال/آزمون رهاشده‌ای وجود ندارد. پنج
[کنترل CI](https://github.com/Omid-NextAI/nextops/actions/runs/37423271410) کد دقیق `940b84d`
موفق‌اند؛ CI کد، پذیرش مدل نیست. پس از رسیدن هر سه عامل به سقف استفاده، بازبینی مستقلِ
ابزارهای بومی/انتشار نسخهٔ سوم هنوز اجرا نشده. نصب/انتشار/آزمون بومی یا انتخاب مدل تازه‌ای
رخ نداده. معیارهای مجموعهٔ کامل/بازبینی انسانی/معنای استاندارد/استدلال/حریم خصوصی/زمینهٔ
سنجیده/برنامه/عملیات/بازگشت بازند. آزمون‌های ناموفق 3.8 حفظ شده‌اند؛ نام درستِ جایگزین
Apache، Qwen3.5-122B-A10B است، نه 3.8 پذیرفته‌شده یا ادعای بیشترین زمینه. مدل زندهٔ 35B
و خاموشی استدلال عمومی تغییر نکرده‌اند؛ هدف کاملِ درخواست‌شده هنوز محقق نشده است.

### انتقال محدود دیگر و CI کد دقیق — ساعت ۰۶:۱۸ UTC

عملیات `639268639835556618` شاخص‌های ۱۰۶–۱۰۹ فایل دوم را گذراند؛ دریافت ۴۳۵۴۷ میلی‌ثانیه،
رسید واقعی رایانه ۳۰۸۴ بایت/SHA
`a90c39b6491ad9910edc424400220455630082a9d4b5b51c56db28f5e2ccf9ce` است. بازبین اصلی
رسید کامل واقعی/خروج صفر را خواند، نه رسید جداگانهٔ بخش‌های root. HTTP206 عددی/خروج صفر/
اندازه/سرآیند/هویت نگه‌داشته‌شده/هش چهار درخواست، پیش از دریافت محافظت‌شده مطابق‌اند.
بدنه‌ها حفظ و بسته‌شدن handleها/توقف متعلق به اجرا/ثبات خط مبنای آماده و بی‌درخواست
تأیید است. مجموع **۲۵۸ بخش/۶۹۲۴۲۷۷۴۳۰۴ بایت** و باقی‌مانده **۲۱۱۸۶۶۸۰۴۴۸ بایت** است؛
فقط یک فایل کامل با هش منبع تأیید شده. انتقال/آزمون رهاشده‌ای در این گام وجود ندارد.
پنج [کنترل CI](https://github.com/Omid-NextAI/nextops/actions/runs/37422445456) کد دقیق
`906a081` موفق‌اند. بستهٔ خصوصی تحویل بازبینی/کنترل صرفاً اصلیِ نسخهٔ سوم، بازبینی مستقل
یا پذیرش میزبان/مدل نیست. شکست‌ها/مراحل تکمیل‌شده و معیارهای اجرا‌نشدهٔ مجموعهٔ کامل/
معنا/استدلال/حریم خصوصی/زمینهٔ سنجیده/برنامه/عملیات/بازگشت ثابت‌اند. نام درست جایگزین
Apache، نسخهٔ 3.5 است؛ 35B زنده/خاموشی استدلال عمومی حفظ شوند.

### ادامهٔ آماده‌سازی و تحویل بازبینی مستقل — ساعت ۰۶:۱۰ UTC

سه پنجرهٔ دیگرِ نسخهٔ هفتم موفق شدند؛ بازبین اصلی، رسید واقعی رایانه و خروج صفر را خواند:

| پسوند عملیات | شاخص‌های فایل دوم | دریافت، میلی‌ثانیه | SHA-256 رسید رایانه |
| --- | --- | --- | --- |
| `639268621098769452` | ۹۴–۹۷ | ۳۸۲۳۵ | `a994ef5700d1eb30601ed615fd5e935025aa9330945814d6c25eda55ff52caee` |
| `639268623859327096` | ۹۸–۱۰۱ | ۳۷۴۷۳۴ | `b5b5b80d1f69678a884a1a3f7651fa6a0ccb560eab0161efc2922efb6ee8f6ae` |
| `639268630606440778` | ۱۰۲–۱۰۵ | ۵۱۴۰۴۷ | `0848c9e229304f7719be2e84f443a75a02e1f5497226fe559bdb24758dfd4dda` |

HTTP206 عددی/خروج صفر/اندازه/سرآیند/هویت نگه‌داشته‌شده/هش چهار درخواست، پیش از دریافت
محافظت‌شده مطابق‌اند؛ بدنه‌ها حفظ و بسته‌شدن handleها/توقف متعلق به اجرا/ثبات خط مبنای
آماده و بی‌درخواست تأیید است. رسید بخش‌های root جداگانه خوانده نشده. مجموع **۲۵۴ بخش/
۶۸۱۶۹۰۳۲۴۸۰ بایت** و باقی‌مانده **۲۲۲۶۰۴۲۲۲۷۲ بایت** است؛ فقط یک فایل کامل با هش
منبع تأیید شده. زمان هر انتقال و بدنهٔ صفرِ در حال دریافت، معیار کارایی یا پذیرش مدل
نیست؛ مهلت افزایش نیافت. عملیات رهاشده‌ای در این گام وجود ندارد. پنج
[کنترل CI](https://github.com/Omid-NextAI/nextops/actions/runs/37419756842)
کد دقیق `8b94d88` موفق‌اند.

بازبین اصلی، درخواست خصوصیِ بازبینی مستقل برای ابزار بومی با ثبت پایدار پوشه، ابزار نصب
سه فایل، کنترل‌کننده/تطبیق فقط‌خواندنی بیرونی و نصب انتشارِ نسخهٔ سوم آماده کرد. هش تازهٔ
چهارده فایل کد/آزمونِ فهرست‌شده با هویت ثابت مطابق است؛ کنترل JSON/هش بسته بدون تماس
میزبان/مدل موفق شد. فرمان دقیق آزمون‌های جداگانه/نحو، کنترل‌های ثابت و معیارهای مالکیت/
هویت، fsync فایل/پوشه، فرایند محدود/پاک‌سازی، رسید دقیق و حفظ شکست اولیه مشخص شده‌اند.
این آماده‌سازی است، نه بازبینی مستقل یا مجوز اجرا. هیچ ابزار نسخهٔ سوم نصب یا عملیاتی
اجرا نشده؛ سه عامل مجاز همچنان خطای پایانیِ سقف استفاده دارند. سوابق کد/شکست ثابت و
معیارهای مجموعهٔ کامل، معنای استاندارد، استدلال/حریم خصوصی/زمینهٔ سنجیده و عملیات متناظر
باز است. نامزد، جایگزین Apacheِ Qwen3.5 است، نه 3.8 پذیرفته‌شده؛ 35B زنده ثابت بماند.

### ادامهٔ انتقال و آزمون رگرسیون هدفمند — ساعت ۰۵:۳۳ UTC

سه پنجرهٔ دیگرِ نسخهٔ هفتم موفق شدند؛ بازبین اصلی خروج صفر واقعی و رسید رایانه را خواند:

| پسوند عملیات | شاخص‌های فایل دوم | دریافت، میلی‌ثانیه | SHA-256 رسید رایانه |
| --- | --- | --- | --- |
| `639268596918597658` | ۸۲–۸۵ | ۴۸۶۳۴۴ | `ec1891cadf86ae8d53298d5ed1aa6da2b904aad6ba4ce6738fda6e84370225d6` |
| `639268604309844912` | ۸۶–۸۹ | ۴۷۹۲۱۹ | `d6ebeed02f5929f5d9fab80a9cecfe75c41115c9e12ec5030f47ebaf937e2410` |
| `639268612161360707` | ۹۰–۹۳ | ۳۹۲۵۰ | `d5439a8fa0026f6dbdd7bb8a6fbff365b24dcb61e74586fc86fe62cc34f5d69f` |

HTTP206 عددی/خروج صفر/اندازه/سرآیند/هویت نگه‌داشته‌شده/هش چهار درخواست، پیش از دریافت
محافظت‌شده مطابق‌اند؛ بدنه‌ها حفظ و بسته‌شدن handleها/توقف متعلق به اجرا/ثبات خط مبنا
تأیید است. رسید بخش‌های root جداگانه خوانده نشده. مجموع **۲۴۲ بخش/۶۴۹۴۷۸۰۷۰۰۸ بایت**
و باقی‌مانده **۲۵۴۸۱۶۴۷۷۴۴ بایت** است؛ یک فایل کامل با هش منبع تأیید شده. اندازهٔ بدنهٔ
در حال دریافت، پذیرش نبود؛ مهلت اجرا افزایش نیافت. عملیات رهاشده‌ای در این گام وجود ندارد.
پنج [کنترل CI](https://github.com/Omid-NextAI/nextops/actions/runs/37417547944) کد دقیق `4e78144`
موفق‌اند. فرمان محلی
`.venv/Scripts/python.exe -I -B -X utf8 -m pytest -q -p no:cacheprovider tests/unit/test_122b_q5_candidate.py tests/unit/test_thinking_qualification.py`
با **۶۱ آزمون موفق در ۵٫۱۲ ثانیه** و خروج صفر اجرا شد؛ مسیر واقعی import همان checkout
فعال بود. این پوشش manifest/جلوگیری از انتخاب زودهنگام/ابزار شبیه‌سازی‌شدهٔ استدلال است،
نه کیفیت بومی/حریم خصوصی/زمینه/پذیرش زنده. بازبینی صرفاً اصلیِ نسخهٔ سوم، خطای سقف
استفادهٔ عامل‌ها، نام درست جایگزین Apache 3.5، 35B زنده/خاموشی استدلال عمومی و همهٔ
معیارهای پذیرش مدل در ادامه ثابت‌اند.

### آماده‌سازی بومی با ثبت پایدار پوشه و اصلاح مرز شکست بیرونی — ساعت ۰۵:۱۰ UTC

سه پنجرهٔ دیگرِ نسخهٔ هفتم کامل شدند؛ بازبین اصلی رسید واقعی رایانه و خروج صفر را خواند:

| پسوند عملیات | شاخص‌های فایل دوم | دریافت، میلی‌ثانیه | SHA-256 رسید رایانه |
| --- | --- | --- | --- |
| `639268580870887985` | ۷۰–۷۳ | ۴۶۵۳۴۴ | `b1a05e2bf6359e6b0ec7175c2487ffd4ef75b67bce7f7b17930ba2594df8f0ce` |
| `639268588480494906` | ۷۴–۷۷ | ۴۸۳۷۵ | `2ca7d88a33a3082488972dde49d6b236ee59801e8e6c25327f188306921c24db` |
| `639268592479363732` | ۷۸–۸۱ | ۴۱۱۵۷ | `25a21077b23e4d0817a23700454787fdb144d9f8ac76b4fffc869b2e68ec5991` |

HTTP206 عددی/خروج صفر/اندازه/سرآیند/هویت نگه‌داشته‌شده/هش هر چهار درخواست پیش از
دریافت محافظت‌شده مطابق‌اند؛ بدنه‌ها حفظ و بسته‌شدن handleها/توقف متعلق به اجرا/ثبات
خط مبنای آماده و بی‌درخواست تأیید است. رسید بخش‌های root جداگانه خوانده نشده. مجموع
**۲۳۰ بخش/۶۱۷۲۶۵۸۱۵۳۶ بایت** و باقی‌مانده **۲۸۷۰۲۸۷۳۲۱۶ بایت** است. فقط فایل کامل
اول با هش منبع تأیید شده؛ زمان‌ها معیار مدل یا اثبات بهبود عمومی سرعت نیستند.

بازبینی نشان داد نسخهٔ ثابت بومیِ دوم، محتوای گزارش را fsync می‌کند، نه مدخل تازهٔ آن
در پوشه. ۱۴۷۸ کنترل اصلی/مستقل قبلی، سابقهٔ تاریخ‌دار است، نه اثبات این حالت بررسی‌نشده.
نسخهٔ مستقلِ سوم (**۹۳۶۰۹ بایت**؛ هش
`3414db13444f76c34c83a71d05e52a4ce476baaeeb7847ef5b39ed580606a842`) ترتیب fsync محتوا،
کنترل قفل، fsync پوشهٔ ROOT از پیش نگه‌داشته‌شده و کنترل دوبارهٔ قفل را افزود. شکست،
نامعلوم/غیرصفر می‌ماند و descriptorها مستقل بسته می‌شوند. **۱۸۶۹ کنترل محض اصلی** و
نحو Bash موفق‌اند. ابزار نصب متناظر **۳۳۰۴۴ بایت** با هش
`3bf2fe34245c5fa13d39e946fe6b87bee86fdb8d4249369e524c23338a18f36e` و کنترل‌کنندهٔ
**۲۳۸۶۸ بایتی** با هش `43ee65fd859ac428cb8ad7ce21a243f5fa02d1a909458c1e83c7090fc9e03381`،
**۲۲۷ کنترل اصلی Python/۱۰۲۲ کنترل اصلی PowerShell** را گذراندند، نه نصب. probe/واحد/
منبع/runtime/مجموعهٔ آزمون/پرسش‌ها/سقف پرسش۱۲۰ ثانیه/۳۸۴ توکن نهایی/16K/۳۲+۳۲ رشته و
شناسه‌های اجرا ثابت‌اند؛ با هیچ نسخه آزمون اجرا نشده. بار ثابت سه فایل، ۱۸۵۴۳۳ بایت
و با bootstrap، ۲۱۸۴۷۷ بایت است. ابزار/هش ثابت قدیمی و شکست‌ها حفظ‌اند، نه تغییر نام پنهانی.

ابزار مستقلِ تطبیق فقط‌خواندنیِ بیرونی (**۱۷۰۳۷ بایت**؛ هش
`c984bd8e68c9c3204e67bf485484ae97649177c3290ae789f37e9c875f5743bd`) **۱۸۴۰۳ کنترل اصلی**
را در خواندن محافظت‌شدهٔ وابسته به FD، هویت دقیق پیش/پس، سقف ورودی/فرایند، بستن مستقل
و شکست‌های main کاملاً شبیه‌سازی‌شده گذراند. این تعداد شامل کنترل هر بلوک برای سقف
کل اسکن است، نه ۱۸۴۰۳ آزمون مستقل. آزمون گسترش‌یافته ابتدا با خطای
`TypeError: unhashable type: bytearray` شکست خورد؛ اشتراک مجموعه، توکن bytearray دریافت
می‌کرد. تبدیل بایت‌های محدود پیش از تطبیق دقیق آرگومان اصلاح شد و شکست ثبت است؛
پیش‌نویس روی میزبان اجرا نشد. نبود فعلیِ آرگومان، **اثبات هویت PID/زمان آغازِ ثبت‌شده،
موفقیت فرایند قبلی، هش کامل تازهٔ فایل‌ها یا پذیرش معنایی نیست**.

کنترل‌کنندهٔ بیرونی (**۲۲۹۷۹ بایت**؛ هش
`a658912ec27e752e701e53b132161c8c2ebd739ec705d75ee189ea0d1c2ecfac`) **۸۴۲ کنترل اصلی
PowerShell** را با خروج صفر گذراند: فرمان/هش bootstrap ثابت، خواندن محدود، رسید دارای
نوع دقیق، ورودی‌وخروجی ناهم‌زمانِ محدود، بستن فرایند متعلق به اجرا، ثبت خروج/هش stdout
اولیه پیش از تفسیر و فقط یک تطبیق فقط‌خواندنیِ بعدی که شکست اولیه را موفق نمی‌کند.
سقف root برای artifact برابر ۱۰۱۰ ثانیه، استاندارد ۲۷۴۰، فقط‌خواندنی ۶۵ و مهلت kill
۵ ثانیه است؛ رایانه ۱۰۳۰/۲۷۷۰/۸۵ و مرز بیرونی ۱۳۰۰/۳۰۶۰ ثانیه. خروج۲ استاندارد یعنی
نیاز به بازبینی معنایی، نه پذیرش.

همهٔ بازبینی‌های مستقل نسخهٔ سوم و نصب انتشارِ نسخهٔ سوم **اجرا نشده‌اند**؛ سه عامل
مجاز همچنان با خطای سقف استفاده متوقف‌اند. ابزارهای تازه نصب/منتشر/عملیاتی اجرا نشده‌اند.
پنج [کنترل CI](https://github.com/Omid-NextAI/nextops/actions/runs/37414641936) کد دقیق
`4bb295d` موفق‌اند. نصب فراداده/تجمیع فایل اول/بررسی منبعِ تکمیل‌شده، شکست‌های اصلی،
ca1 آماده‌شده/نصب‌نشده، نام درست **3.5** با مجوز Apache و 35B زنده/خاموشی استدلال عمومی
حفظ‌اند. معیارهای فایل کامل/بازبینی واقعی/معنای بومیِ استاندارد/استدلال/حریم خصوصی/
زمینهٔ سنجیده/برنامهٔ متناظر/عملیات/بازگشت همچنان باز هستند.

### آماده‌سازی کنترل‌کنندهٔ نصب بومی و ادامهٔ انتقال — ساعت ۰۴:۳۶ UTC

پس از گام تاریخیِ ۲۰۲ بخش، چهار پنجرهٔ دیگرِ V7 موفق شدند. پسوند عملیات، شاخص‌های فایل
دوم، زمان دریافت و هش واقعی رسید، همان جدولِ بخش انگلیسی است: شاخص‌های ۵۴–۵۷ با
۵۷۶۴۰۷ میلی‌ثانیه؛ ۵۸–۶۱ با ۴۶۸۴۴؛ ۶۲–۶۵ با ۴۱۸۷۵؛ و ۶۶–۶۹ با ۴۳۰۳۱.
بازبین اصلی، رسیدهای واقعی رایانه و پایان موفق فرایندها را خواند، نه رسیدهای جداگانهٔ
بخش‌ها روی root. کد عددی HTTP206/خروج صفر/اندازه/سرآیند/هویتِ باز/هشِ هر چهار بدنه،
پیش از دریافت محافظت‌شده تأیید شد؛ بدنه‌ها حفظ و بسته‌شدن handleها/توقف فرایندهای متعلق
به اجرا/ثبات خط مبنای آماده و بی‌درخواست ثبت است. مجموع **۲۱۸ بخش/۵۸۵۰۵۳۵۶۰۶۴ بایت**
است؛ **۳۱۹۲۴۰۹۸۶۸۸ بایت انتقالی** باقی و فقط فایل کامل اول تأیید شده. تفاوت زمان‌ها،
آزمون کارایی مدل یا بهبود عمومیِ اثبات‌شدهٔ انتقال نیست.

ابزار مستقلِ نصب/کنترل‌کنندهٔ سه فایل بومی اکنون در بررسی محلیِ اصلی آماده است:
اندازه/هش نصب‌کننده **۳۳۰۴۴ بایت**/
`f65751dd360e3d1f1493963978a150c2f11d8391e3f43e66f587063025e2bc95` و کنترل‌کننده
**۲۳۸۶۸ بایت**/`89cc15367c7d6af6ccb6552ef8ca5b98f84117151c975c62e35ab57e134ce23d` است.
بدنهٔ ثابت دقیقاً سه فایل/۱۸۴۷۸۷ بایت و همراه bootstrap، ۲۱۷۸۳۱ بایت است. **۲۲۷ کنترل
Python/۱۰۲۲ کنترل PowerShellِ محض** با خروج صفر موفق و دوباره اجرا شدند؛ entrypoint
عملیاتی، میزبان/مدل یا تغییر واقعیِ فایل/فرایند فراخوانی نشد. نام/اندازه/هش/مجوز دقیق،
پرچم صریحِ ثبت پایدار رسید/بسته‌شدن handle و حفظ خروج/هش stdout اصلی پیش از تحلیل لازم
است؛ تطبیق فقط‌خواندنیِ بعدی، شکست اصلی را حذف نمی‌کند. پیش‌نویس تاریخیِ صرفاً Python
دست‌نخورده است. شکست‌های محلیِ آماده‌سازی مکانیکی و اجرای کنترل بدون هش اجباری (خروج۱
پیش از آزمون) حفظ شدند؛ دستور اصلاح‌شدهٔ دقیق موفق بود، نه تکرار روی میزبان.

بازبینی مستقل **اجرا نشده**، زیرا عامل‌های مجاز به سقف استفاده رسیدند. کنترل‌کنندهٔ نصب
با مرز اجرای بومی/تطبیق بیرونیِ هنوز آماده‌نشده متفاوت است؛ ثبت پایدار گزارش و مشاهدهٔ
مستقلِ توقف/ثبات خط مبنا باید پیش از آزمون پوشش داده شوند. ابزار نصب انتشارِ نسخهٔ سوم
نیز بازبینی مستقل می‌خواهد. ابزارهای جدید هیچ نصب، انتشار، شروع یا انتخابی انجام نداده‌اند.
پنج کنترل CI کد دقیق `2838b2a` در پیوند بخش انگلیسی موفق‌اند. جایگزین Apache همچنان
Qwen3.5-122B-A10B Q5 است، نه 3.8؛ معیارهای مجموعهٔ کامل/بازبینی دستی/معنای بومی/
استدلال/حریم خصوصی/زمینه/برنامه/عملیات/بازگشت باز و 35B زنده/خاموشی استدلال عمومی و
کار/شکست‌های قبلی حفظ‌اند.

### ادامهٔ انتقال، تطبیق قالب واقعی و اصلاح پاک‌سازی نصب — ساعت ۰۴:۱۲ UTC

پس از رکوردِ ۱۹۴بخشی، دو پنجرهٔ دیگرِ نسخهٔ هفتم موفق شدند. شناسه‌ها و هش‌های کاملِ
نتیجه در جدول انگلیسی ثبت‌اند: اندیس‌های فایل دوم ۴۶ تا ۴۹ در ۴۶۵۳۴۴ میلی‌ثانیه و ۵۰
تا ۵۳ در ۳۷۶۲۵ میلی‌ثانیه. بازبین اصلی نتیجه‌های واقعیِ رایانهٔ کاربر و پایان با کد صفر
را خواند، نه رسیدهای جداگانهٔ root. در هر پنجره، هر چهار پاسخ HTTP206/کد خروج صفر،
اندازه/header/هویت handle باز/هش کامل پیش از دریافت محافظت‌شده تأیید شدند. بدنه‌ها محفوظ،
handleها بسته و توقف فرایندهای متعلق به اجرا/ثبات خط مبنای آماده و بی‌درخواست تأیید است.
مجموع **۲۰۲ بخش/۵۴۲۱۰۳۸۸۷۶۸ بایت** است؛ **۳۶۲۱۹۰۶۵۹۸۴ بایت** باقی و فقط یک فایل کامل
با هش منبع اصلی تأیید است. نوسان زمان curl، سنجش استنتاج یا اثبات بهبود سرعت نیست.

بازبینی اصلی/مستقل، بایت‌های واقعی و بدون نرمال‌سازیِ قالب/مجوزِ نسخهٔ رسمیِ ثابت را با
هش‌های درج‌شده در انگلیسی تطبیق داد: قالب ۷۷۵۶ بایتی با قالب مشاهده‌شدهٔ فایل اول و
مجوز ۱۱۵۴۴ بایتی Apache-2.0 با نسخهٔ محافظت‌شده مطابق‌اند. در متن قالب، با فعال بودن
generation prompt، مقدار دقیق `enable_thinking=false` پیشوند خالی استدلال را می‌بندد؛
مقدار true/غایب آن را باز می‌گذارد. پردازش سابقهٔ استدلالِ آخرین پاسخ/چرخهٔ ابزار از این
پرچم مستقل است. این بررسی، پذیرش رندر بومی، برابری آرایهٔ توکن، حریم خصوصی، همهٔ فایل‌ها،
منشأ تبدیل، زمینه یا حقوق کل محصول نیست. ورودیِ تأییدشدهٔ دستی برای مجموعهٔ کامل هنوز
ایجاد نشده. مجوز/انتساب/NOTICE لازم و توضیح تغییر حفظ شوند؛ نام این مدل Qwen3.5 است،
نه 3.8.

بازبینی کامل فایل/تفاوتِ چهار ابزار بومیِ نسخهٔ دوم، **۱۴۷۸ کنترل اصلی/مستقل** و نحو Bash
را گذراند؛ هش‌های ثابتِ probe/اسکریپت/unit در متناظرِ انگلیسی ثبت‌اند. هویت دو قفل با
FD/path و هویت ثابتِ پوشه‌های والد، اطراف کنترل/نوشتن/fsync تطبیق می‌شود؛ شکست ممیزی
الزامی، توقف probe و پاک‌سازی مستقل را حذف نمی‌کند. ابزار نصب/کنترل‌کنندهٔ خارجی و
آزمون استاندارد روی میزبان هنوز بازند. کد/محیط اجرا/مجموعهٔ پرسش/سقف پرسش۱۲۰ ثانیه/
۳۸۴ توکن نهایی/16K/۳۲ رشته ثابت‌اند. جفت ابزار اجرای انتشارِ نسخهٔ دوم، **۱۶۴۶ کنترل
در هر بازبینی** را گذراند؛ فقط ابزار ثابتِ ازپیش‌نصب‌شده را فراخوانی می‌کند و هنوز نصب
یا اجرا نکرده است. رسیدِ بعدیِ فقط‌خواندنی، شکست اولیهٔ انتقال/پاک‌سازی را موفق نمی‌کند.

بازبینی بعدی، با وجود کنترل‌های محضِ موفق قبلی، ابزار نصب انتشارِ نسخهٔ دوم را رد کرد:
شکست fstat/بستن می‌توانست مالکیت handle را از دست بدهد یا بستن همتایان را حذف کند؛
fsync رسید نیز هویت هر دو قفل را بازبینی نمی‌کرد. نصب‌های موفق قبلیِ ابزار فراداده،
موفقیت تاریخی‌اند، نه پذیرش این مسیرهای شکست. نسخهٔ مستقلِ سوم، مالکیت پوشه را پیش از
اعتبارسنجی ثبت، همهٔ بستن‌ها را امتحان و عدم قطعیت را حفظ می‌کند؛ هویت دو قفل پیش/پس
از fsync رسید تطبیق می‌شود. کنترل‌کننده، شاهد صریحِ پاک‌سازی/رسید را می‌سنجد و کد خروج/
هش خروجی اولیه را پیش از parse حفظ می‌کند. **۲۵۶ کنترل Python/۹۸۹ کنترل PowerShellِ
صرفاً اصلی** موفق‌اند؛ هش‌ها در انگلیسی ثبت‌اند و اجرا روی میزبان انجام نشده. پیش‌نویس
ناتمامِ نصب سه فایل بومی نیز بستن مستقیمِ خارج از ثبت مالکیت داشت؛ بازبین اصلی اصلاح
کرد و **۲۲۷ کنترلِ جداگانهٔ تعاریف/حافظه**، شامل مسیرهای شکستِ finally واقعی، موفق شدند.
کنترل‌کننده و بازبینی مستقل هنوز ناتمام‌اند. شکست/اصلاحِ کنترل‌های محلی و ابزارهای ردشده
حفظ شده‌اند.

سپس سه عاملِ مجاز به دلیل سقف استفاده متوقف شدند. دامنهٔ بازبینی‌های کامل‌شدهٔ بالا
حفظ است؛ عاملِ درحال‌کار یا پذیرش مستقلِ ناتمام ادعا نمی‌شود. بازبین اصلی آماده‌سازی
محدودِ قبلاً بررسی‌شده و اصلاح محلی را ادامه می‌دهد. پنج کنترل CI کد دقیق `2847651` در
[اجرای 37403305543](https://github.com/Omid-NextAI/nextops/actions/runs/37403305543) موفق‌اند.
ca1 آماده شده، نه نصب؛ 35B زنده/خاموشی استدلال عمومی و زمینهٔ اعلام‌شدهٔ پذیرفته‌نشده
ثابت‌اند. انتقال پیش از تجمیع باقی‌مانده/بررسی مجموعه/انتشار تکمیل شود؛ معنای استاندارد
پیش از استدلال/حریم خصوصی/زمینهٔ سنجیده/برنامه/عملیات/بازگشت متناظر پذیرفته شود.

### ادامهٔ انتقال و بازبینی مسیرهای شکست ابزارهای آماده‌سازی — ساعت ۰۲:۱۱ UTC

پس از ثبتِ ۱۷۸بخشی، چهار پنجرهٔ دیگرِ نسخهٔ هفتم موفق شدند. شناسه‌های پایانی، اندیس‌های
فایل دوم، زمان curl و هش نتیجهٔ رایانهٔ کاربر در جدول متناظرِ انگلیسی ثبت‌اند: اندیس‌های
۳۰ تا ۳۳ در ۳۶۷۶۶، ۳۴ تا ۳۷ در ۴۶۲۵۶۲، ۳۸ تا ۴۱ در ۳۸۸۶۰ و ۴۲ تا ۴۵ در ۴۶۱۲۸۲
میلی‌ثانیه. بازبین اصلی، رکوردهای واقعیِ رایانهٔ کاربر و پایان موفق فرایند را خواند، نه
رسیدهای جداگانهٔ root. در هر پنجره، چهار بدنهٔ ۲۶۸۴۳۵۴۵۶ بایتی حفظ و HTTP206/کد خروج صفر،
headerها، هویت فایلِ دارای handle باز و هش کامل پیش از هر دریافت محافظت‌شده تأیید شدند؛
توقف فرایندها/بسته‌شدن handleها و ثبات خط مبنای آماده/بی‌درخواست موفق‌اند. آخرین رکورد
ساعت **۰۲:۱۰:۰۸ UTC** کامل شد. مجموع اصلی **۱۹۴ بخش/۵۲۰۶۲۹۰۵۱۲۰ بایت** است و
**۳۸۳۶۶۵۴۹۶۳۲ بایت انتقالی** باقی است. هنوز فقط فایل کامل اول با هش منبع اصلی تأیید
شده. نوسان زمان، بهبود سرعت یا علت انتقال را اثبات نمی‌کند؛ کارایی استنتاج سنجیده نشده.

بازبینی مستقل مشخص کرد که شکست آماده‌سازی فرزند یا بازگشت غیرمنتظرهٔ worker در ابزار
اصلیِ بررسی مجموعه می‌توانست وارد مسیر ممیزی/پاک‌سازی والد شود. کنترل‌های محض قبلی این
مسیر را پوشش نداده بودند؛ شش ابزار اصلی حفظ و برای اجرای عملی رد شدند. نسخهٔ مستقلِ
دوم، خروج قطعیِ محلیِ فرزند در `finally: os._exit(1)` را اعمال می‌کند؛ worker موفق، خود
خروج عادی را انجام می‌دهد. بازبینی کاملِ فایل/تفاوت اصلی و مستقل و **۱۲۷۵/۴۴۰۲/۶۰۱ کنترل
محض، مجموع ۶۲۷۸ در هر بازبینی**، شامل شش حالت شکست موفق‌اند. ابزار بررسی، **۳۴۱۳۷
بایت** و دارای هش `5e82762b45b5f6073d8d3bf0bb1350ce2bbb535a4d74c100749c957f72b95062` است.
ابزار ثابتِ نصب فقط در مقصد غایب، **۱۴۷ کنترل Python/۸۷۳ کنترل PowerShell، مجموع ۱۰۲۰
در هر بازبینی** را گذراند؛ سپس عملیات `metadata-complete-v2-install-20261006-639268494401094149`
فقط همان ابزار را در **۲۳۸ میلی‌ثانیه** نصب کرد. هش مقصد، توقف فرایند کاربر و تطبیق رسید
root موفق‌اند؛ هش‌های نتیجه/خروجی root در بخش متناظرِ انگلیسی ثبت‌اند. بررسی مجموعه،
اجرای بومی یا تغییر سرویس انجام نشد. ابزار تطبیق فقط هنگام نیاز از ورودی استاندارد اجرا
می‌شود، نه نصب؛ ابزارها/ACLهای اصلی ثابت‌اند. شکست اولیهٔ کنترل اندازهٔ قدیمی در آماده‌سازی
توسط نویسنده، اصلاح و در سابقه حفظ شد.

ابزار اصلیِ انتشار، قفل‌ها را پیش از رسید الزامی رها می‌کرد و همچنان ردشده است. نسخهٔ
مستقلِ دوم، هر دو قفل root را تا ثبت رسید/fsync نگه می‌دارد و بستن همهٔ descriptorها را
مستقل انجام می‌دهد. بازبینی کاملِ اصلی/مستقل و **۳۰۳۵ کنترل محض در هر بازبینی** موفق‌اند.
ابزار، **۵۷۹۲۱ بایت** و دارای هش `6d5d2a7d4ed3d436789da64304b5f3e5f24b4de7d6993cc98a5378b1fefb6a12`
است؛ انتشار/پذیرش ابزار نصب و کنترل‌کننده اجرا نشده‌اند. همچنین **۱۰۷۳ کنترل محض موفقِ
ابزار بومی**، جایگزینی مسیر قفلِ دارای handle یا شکست بستن ترتیبی را پوشش نمی‌دادند.
بازبینی اصلی/مستقل، چهار ابزار اصلی را رد کرد؛ اصلاح مستقلِ هویت قفل/پاک‌سازی و هش ابزار
فراداده ناتمام است. سقف ۱۲۰ ثانیه برای هر پرسش، ۳۸۴ توکن نهایی، زمینهٔ 16K، ۳۲ رشته،
مجموعهٔ آزمون/پرامپت‌ها و شکست‌های قبلی ثابت‌اند. یافتن رسید کامل در تطبیق فقط‌خواندنیِ
بعدی، نتیجهٔ ناموفقِ اولیهٔ فرایند کاربر را به موفق تبدیل نمی‌کند.

پنج کنترل CI کد دقیق `9375d49`، شامل کیفیت/واحد، PostgreSQL16/17، مرورگر و اطلاعات
محرمانه، در [اجرای بالا](https://github.com/Omid-NextAI/nextops/actions/runs/37400813523) موفق‌اند.
این CI کد است، نه پذیرش مدل کامل/قالب/اجرای بومی/استدلال/حریم خصوصی/زمینه/عملیات. ca1
آماده شده، نه نصب؛ 35B زنده/خاموشی استدلال عمومی ثابت‌اند. انتقال پیش از تجمیع باقی‌مانده
تمام شود؛ سپس مجموعهٔ کامل/قالب/معنای استاندارد، پیش از استدلال با خروجی نهایی/حریم خصوصی/
زمینهٔ سنجیده و معیارهای متناظر عملیات/بازگشت تکمیل شوند.

### فرادادهٔ واقعیِ گسترش‌یافته و انتقال چهاردرخواستی — ساعت ۰۱:۳۶ UTC

پنجره‌های ترتیبیِ قبلی حفظ‌اند. پنجرهٔ `resume-20261006-639268455415290393` اندیس‌های
۲۲ تا ۲۵ فایل دوم را افزود: ۱۷۴ بخش اصلی/۴۶۶۹۴۱۹۶۰۰۰ بایت، با ۴۳۷۳۵۲۵۸۷۵۲ بایت
باقی‌مانده و زمان دریافت ۵۲۵۵۰۰ میلی‌ثانیه. سپس پنجرهٔ مستقل و بررسی‌شدهٔ نسخهٔ هفتم با
شناسهٔ `resume-20261006-639268464492464192` اندیس‌های ۲۶ تا ۲۹، چهار بخشِ ۲۶۸۴۳۵۴۵۶ بایتی،
را با HTTP 206/کد خروج صفر کامل کرد. زمان دریافت **۴۶۳۵۹۴ میلی‌ثانیه** و زمان هر درخواست
**۲۰۳٫۴۷۹۴۸۹/۴۶۳٫۴۴۸۳۸۵/۳۶۳٫۴۲۸۰۷۴/۴۴۰٫۷۲۳۰۰۶ ثانیه** بود. نتیجه‌های عددی، headerها، هویت
فایل‌های دارای handle باز و هش محلی هر چهار بدنه پیش از هر دریافت محافظت‌شده تأیید شدند.
دریافت، پاک‌سازی نسخهٔ تکراریِ تأییدشده، توقف handle/فرایندهای متعلق به اجرا و ثبات خط مبنای
آماده/بی‌درخواست موفق‌اند. مجموع اصلی: **۱۷۸ بخش/۴۷۷۶۷۹۳۷۸۲۴ بایت**؛ **۴۲۶۶۱۵۱۶۹۲۸ بایت
انتقالی** باقی است. فقط فایل کامل اول با هش منبع اصلی تأیید است. بازبین اصلی، نتیجهٔ
رایانهٔ کاربر با هش `3b6c555286221fd0e11cc5bb7edfa61b97111ad2931ba6e25d27d1de059b34a7` را
خواند، نه رسیدهای جداگانهٔ root. یک مشاهدهٔ هم‌زمان، بهبود عمومی سرعت، علت شبکه یا بهبود
کارایی استنتاج را اثبات نمی‌کند. بدنه‌های اصلی و شکست‌ها محفوظ‌اند.

هفت فایل فرادادهٔ گسترش‌یافته، **۵۵۶۴ کنترل محض اصلی/مستقل** و دو مجموعهٔ ثابتِ نصب،
**۲۰۱۴ کنترل در هر بازبینی** را گذراندند؛ ابزارهای اصلی ثابت‌اند. نصب مستقلِ ابزار خواندن/
بررسی فراداده با دسترسی root در **۲۳۱/۲۲۰ میلی‌ثانیه**، با تأیید هش مقصد، توقف فرایند
کاربر/تطبیق نتیجه و بدون اجرای فراداده یا مدل پایان یافت. سپس بررسی فایل اول با شناسهٔ
`metadata-v2-122b-20261006-639268471855185668` در **۸۷۸۴۳ میلی‌ثانیه**، شامل **۸۷۴۸۵ میلی‌ثانیه**
بررسی، با کد خروج صفر کامل شد. هش کامل فایل اول پیش از خواندن فراداده تأیید شد.
تطبیق فقط‌خواندنی و خواندن مستقل و محدودِ stat/هش/محتوا/stat توسط بازبین اصلی، نتیجهٔ
محافظت‌شدهٔ **۲۸۵۰ بایتی** با مالکیت root/root، حالت `0400` و یک پیوند را تأیید کردند؛
هش آن `06dadb4368dc0b38758c5ae3aa60849db0951b09abeb652980b20e59a0c122b2` است. خواندن مستقلِ
بازبین اصلی به ثبات ویژگی‌های stat با دقت ثانیه متکی بود، نه اثبات از طریق handle باز.
توقف فرایند بررسی/کنترل‌های متعلق به اجرا و ثبات آمادگی زنده تأیید شدند.

| فرادادهٔ واقعاً مشاهده‌شدهٔ فایل اول | مقدار |
| --- | --- |
| معماری/بلوک/ابعاد تعبیه | `qwen35moe` / ۴۹ / ۳۰۷۲ |
| تعداد expert/تعداد مورد استفاده | ۲۵۶ / ۸ |
| ابعاد feed-forward اختصاصی/اشتراکی | ۱۰۲۴ / ۱۰۲۴ |
| سر توجه/سر KV/طول key/value | ۳۲ / ۲ / ۲۵۶ / ۲۵۶ |
| فاصلهٔ توجه کامل/لایهٔ پیش‌بینی توکن بعد/RoPE | ۴ / ۱ / ۶۴ |
| کانولوشن/گروه/ابعاد درونی/حالت/رتبهٔ گام SSM | ۴ / ۱۶ / ۸۱۹۲ / ۱۲۸ / ۶۴ |
| tokenizer/pre/add-BOS/EOS/padding | `gpt2` / `qwen35` / false / ۲۴۸۰۴۶ / ۲۴۸۰۴۴ |

هش قالب همان `a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715` است. اندازهٔ
واژگان، تعداد expert اشتراکی و دیگر شناسه‌ها/پرچم‌های توکن غایب‌اند، نه مقدار پیش‌فرض.
آرایه‌های token/merge و معنای کنترل استانداردِ قالب بررسی نشده‌اند. فایل اول ۳۹۲ تنسور دارد؛
مجموع ۸۹۹ تنسور و زمینهٔ ۲۶۲۱۴۴ فقط اعلام‌شده و زمینهٔ پذیرفته‌شده نامشخص است. ابزار مستقلِ
مجموعهٔ کامل، انتشار نسخهٔ تغییرناپذیرِ خواندنی برای سرویس و آزمون بومی فقط در حالت استاندارد،
صرفاً آماده شده‌اند، نه اجرا یا پذیرفته. انتقال پیش از تجمیع باقی‌مانده تکمیل شود؛ مجوز فایل‌های
اصلیِ دوپیوندی و مختص root برای ایجاد دسترسی سرویس تغییر نکند.

پنج کنترل CI کد دقیق `495b704` در [اجرای بالا](https://github.com/Omid-NextAI/nextops/actions/runs/37397504800)،
شامل کیفیت/واحد، PostgreSQL 16/17، مرورگر و اطلاعات محرمانه موفق‌اند. نتیجهٔ کد قبلی به این
کد تعمیم داده نشده؛ این پذیرش مدل نیست. ca1 آماده شده، نه نصب؛ 35B زنده/خاموشی استدلال
عمومی و آزمون‌های ناموفق استاندارد حفظ‌اند. مجموعهٔ کامل/قالب/اجرای بومی/معنا/استدلال/
حریم خصوصی/زمینهٔ سنجیده و معیارهای متناظر برنامه/عملیات/بازگشت هنوز تکمیل نیستند.

### آماده‌سازی محافظت‌شدهٔ کد ca1 و گام انتقال ۱۶۶بخشی

پنجرهٔ `resume-20261006-639268444064771324` با کد خروج صفر کامل شد: اندیس‌های ۱۴ تا ۱۷
از فایل دوم، هرکدام ۲۶۸۴۳۵۴۵۶ بایت، همگی با HTTP 206/کد خروج صفر. زمان کل curl برابر
**۵۰۹۱۷۲ میلی‌ثانیه** و زمان هر بخش **۱۲۷٫۰۹۸۹۱۹/۱۲۶٫۱۲۴۴۰۲/۱۲۶٫۲۹۸۰۷۴/۱۲۹٫۵۱۸۲۵۳ ثانیه**
بود. کنترل‌کننده، رسیدهای محافظت‌شده، توقف فرایند متعلق به اجرا و ثبات خط مبنای آماده/
بی‌درخواست را تأیید کرد. مجموع اصلی **۱۶۶ بخش/۴۴۵۴۶۷۱۲۳۵۲ بایت** است و **۴۵۸۸۲۷۴۲۴۰۰ بایت
انتقالی** باقی است. بازبین اصلی، نتیجهٔ رایانهٔ کاربر را با هش
`9c70819749a75c63d4d14e4474f545a8ce2fa069d32c03f69662ebb86333b988` خواند؛ رسیدهای root
این پنجره را جداگانه دوباره نخواند. یک فایل کامل با هش منبع اصلی تأیید است، نه مدل کامل.
پنجره‌های سریع‌تر پیشین و تلاش‌های موازیِ ناموفق سابقه‌اند؛ علت‌یابیِ محدودسازی مسیر یا
بهبود سرعت در نمایهٔ موازیِ تازه اثبات نشده است.

نسخهٔ مستقل دومِ ابزار آماده‌سازی، استثنای OWNER RIGHTS را فقط برای wheel ثابت و پوشهٔ
ساختِ مستقیم آن می‌پذیرد. مالک واقعیِ کاربر جاری، دقیقاً سه ورودی مجاز SYSTEM/مدیر/OWNER
RIGHTS با دسترسی کامل و پرچم‌های دقیق، مسیر والد بدون reparse، handle فقط‌خواندنیِ باز،
یک پیوند، ثبات هویت handle/مسیر و هش کاملِ wheel الزامی‌اند. اعتبارسنج عمومی مسیر خصوصی،
ACL اصلی، ابزار ثابت Python، هش‌های بسته و شکست نخست تغییر نکرده‌اند. بازبینی اصلی/مستقل،
**۱۳۰۳ کنترل تعریفی/ساختگی PowerShell** را گذراند؛ آزمون واقعیِ مجزای فقط‌خواندنیِ wheel
محلی، با مجوز قبلی و بدون فراخوانی میزبان، در **۱۵۰۰ میلی‌ثانیه** موفق شد.
سپس عملیات `source-stage-ca1da27-20261006-639268451997194459` با کد خروج صفر کامل شد:
**آماده‌سازی، نه نصب**؛ زمان آماده‌سازی root برابر **۱۸۷۹ میلی‌ثانیه** بود. کنترل‌کننده،
برابری محافظت‌شدهٔ آرشیو/کد/wheel/دارایی‌های ثابت، توقف فرایند کاربر، نتیجهٔ root و ثبات
خط مبنای آماده/بی‌درخواست را تأیید کرد. هش نتیجهٔ رایانهٔ کاربر:
`42ce75d5672c65ad9c0dfd78f6f2c9c744b2d5c2f70109532d0bdd4573855255`.
برابری وابستگی‌های venv نصب‌شده، نصب بسته و استنتاج اجرا نشدند. شکست اولیهٔ ۳٫۶۳ثانیه‌ای
حفظ است؛ موفقیت این اصلاح مستقل، سابقهٔ آن را حذف نمی‌کند.

پنج کنترل CI کد دقیق `f7d0b35` در
[اجرای 37396025687](https://github.com/Omid-NextAI/nextops/actions/runs/37396025687) موفق‌اند:
کیفیت/واحد، PostgreSQL 16، PostgreSQL 17، مرورگر و اطلاعات محرمانه. نتیجهٔ مشاهده‌شدهٔ
همین اجرا، وضعیت پیشینِ در صف را به‌روز می‌کند؛ از کد قبلی استنتاج نشده است. گام بعد،
ادامهٔ انتقال بررسی‌شده و بازبینی مستقلِ فرادادهٔ گسترش‌یافته/مجموعهٔ کامل/اجرای بومی است.
استدلال عمومی خاموش است؛ 35B زنده و شکست‌های پیشین ثابت‌اند. این آماده‌سازی و تأیید کد
است، نه پذیرش مدل کامل/زمینهٔ قابل‌استفاده/عملیات.

### فرادادهٔ واقعی فایل اول و ادامهٔ محافظت‌شده روی S — ساعت ۰۰:۲۷ UTC

ابزار مستقلِ نصب فراداده، **۱۳۶ کنترل Python/۸۶۴ کنترل PowerShell** اصلی و مستقل را
گذراند. نصب با دسترسی root در ۲۲۵ میلی‌ثانیه، بدون اجرای مدل پایان یافت. چهار ابزار
مستقلِ نظارت بیرونی، **۱۴۶۹ کنترل Python/۵۸۷ کنترل PowerShell** اصلی و مستقل را گذراندند.
عملیات `metadata-122b-20261006-639268431340517846` ساعت **۰۰:۲۷:۰۶ UTC** با کد خروج صفر
کامل شد: **۸۹۷۹۸ میلی‌ثانیه** کل/**۸۹۴۱۰ میلی‌ثانیه** بررسی. پیش از خواندن محدودِ
فراداده، هش کاملِ تازهٔ فایل اول با منبع اصلی تطبیق داده شد. تطبیق مستقلِ فقط‌خواندنی
و بازخوانی جداگانهٔ رسیدهای محافظت‌شده توسط بازبین اصلی، توقف فرایندهای متعلق به اجرا،
هویت دقیق نتیجه و ثبات خط مبنای آماده/بی‌درخواست را تأیید کردند. هش نتیجهٔ محافظت‌شده:
`5f8b6345c3437acfdc4fc65da4ac0bd69d469d8eef30bbe2ea78216593805ce1`.

| ویژگی واقعاً مشاهده‌شده | مقدار و محدودیت نتیجه |
| --- | --- |
| معماری/نام/مجوز | `qwen35moe` / Qwen3.5 122B A10B / `apache-2.0` |
| نسخهٔ GGUF/کوانتیزه‌سازی/نوع فایل | ۳ / ۲ / ۱۷ |
| تعداد فیلد/بلوک/ابعاد تعبیه | ۵۱ / ۴۹ / ۳۰۷۲ |
| تعداد فایل/اندیس/تنسورهای فایل اول | ۳ / ۰ / ۳۹۲ |
| مجموع تنسور/طول زمینه | ۸۹۹ / ۲۶۲۱۴۴ — اعلام‌شده، نه تأیید مجموعهٔ کامل یا زمینهٔ قابل‌استفاده |
| مدل/پیش‌پردازش tokenizer | `gpt2` / `qwen35` |
| هش SHA-256 قالب؛ نه متن خام | `a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715` |

این ابزار، ویژگی expert/توکن‌های ویژه یا شاخه‌های اجراشدهٔ قالب را تأیید نکرده است.
زمینهٔ پذیرفته‌شده همچنان null است؛ معیارهای مدل کامل/بارگذاری بومی/معنا/استدلال/حریم
خصوصی اجرا نشده‌اند. ابزار نصب/بررسی/تطبیق، استنتاج یا تغییر تنظیم زنده انجام نمی‌دهد.

پوشهٔ خصوصیِ ازپیش‌ساخته‌شده روی S، کنترل ACL/هویت را بدون تغییر ACL ریشهٔ دیسک گذراند.
ابزار مستقلِ ادامهٔ ترتیبیِ نسخهٔ ششم، **۳۲۸ کنترل اصلی/مستقل** آماده‌سازی را گذراند.
سه پنجرهٔ موفق، اندیس‌های ۱، ۲ تا ۵ و ۶ تا ۹ فایل دوم را با HTTP 206/کد خروج صفر/
اندازه/هش کامل محلی و رسیدهای محافظت‌شدهٔ دریافت/پاک‌سازی/پایان کامل کردند. فهرست اصلی
اکنون **۱۵۸ بخش/۴۲۳۹۹۲۲۸۷۰۴ بایت** دارد؛ **۴۸۰۳۰۲۲۶۰۴۸ بایت انتقالی** باقی است. فقط
فایل کامل اول، تأیید منبع اصلی دارد؛ همهٔ بدنه‌های محلی حفظ‌اند. بازبین اصلی، رسیدهای
root پنجرهٔ نخست را جدا خواند؛ دو پنجرهٔ بعدی با کنترل‌کننده تأیید شدند، نه بازخوانی
مستقل در این گزارش. ثبات خط مبنا/توقف فرایند موفق است. برای حفظ حداقل فضای آزادِ
۲۰۰ میلیارد بایتیِ ابزار دریافت، انتقال باقی‌مانده پیش از تجمیع فایل‌های بعدی کامل شود؛
حداقل فضای آزاد دیسک سیستم تضعیف نشود.

هر پنج کنترل CI کد دقیق `861bf7d` در
[اجرای 37392947997](https://github.com/Omid-NextAI/nextops/actions/runs/37392947997) موفق‌اند.
برنامه‌ریز، ثبت هویت نوع‌دار، کنترل سختِ حالت استاندارد و نمایش نام واقعی مدل را به‌عنوان
کد پیاده‌شده، جدا از کار ناتمام نمایهٔ اجرا/استدلالِ واجد صلاحیت ثبت می‌کند. مجموعهٔ
محدودِ برنامه/ثبت مدل **۶۳ آزمون را در ۲٫۵۸ ثانیه** گذراند؛ lint/قالب‌بندی و بازبینی مستقل
اصلاح وضعیت موفق‌اند. این اصلاح کد/وضعیت است، نه پذیرش اجرای 122B؛ آرشیو/wheel ثابت ca1
و ابزار خصوصیِ نصب‌شده تغییر نکرده‌اند. چهار ابزار آماده‌سازیِ بستهٔ دقیق ca1، **۲۸۶ کنترل
Python/۹۲۳ کنترل PowerShell** اصلی/مستقل را گذراندند؛ آماده‌سازی واقعی روی میزبان و برابری
وابستگی‌های محیط نصب‌شده هنوز در این گام اجرا نشده‌اند.

پنجرهٔ ترتیبیِ بعدی ساعت **۰۰:۴۴:۰۹ UTC** با کد خروج صفر کامل شد: اندیس‌های ۱۰ تا ۱۳
فایل دوم، چهار بخشِ ۲۶۸۴۳۵۴۵۶ بایتی، همگی HTTP 206/کد خروج صفر، با **۵۰۵۸۹۰ میلی‌ثانیه**
زمان کل curl. کنترل‌کننده، رسیدهای محافظت‌شده/توقف فرایند/ثبات خط مبنا را تأیید کرد.
مجموع انتقال به **۱۶۲ بخش/۴۳۴۷۲۹۷۰۵۲۸ بایت** رسید؛ **۴۶۹۵۶۴۸۴۲۲۴ بایت انتقالی** باقی است،
نه تأیید فایل کامل دوم. هش نتیجهٔ خصوصیِ رایانهٔ کاربر:
`ab1fe22ed0ec7fe54e5b11bab895b408ff3c5ea31dcd7833264470034ffa5907`.
بازبین اصلی، رسیدهای root این پنجره را مستقل بازخوانی نکرده است.

سپس کنترل‌کنندهٔ آماده‌سازی ca1 در **۳٫۶۳ ثانیه، در کنترل اولیهٔ رایانهٔ کاربر** و پیش
از هر فراخوانی میزبان/بارگذاری/آماده‌سازی root ناموفق شد. فایل دقیق wheel، مالکیت کاربر
جاری و ACL محدودِ موروثیِ OWNER RIGHTS/SYSTEM/مدیر دارد؛ اعتبارسنج قبلی فقط شناسهٔ صریح
کاربر جاری، SYSTEM و مدیر را می‌پذیرد و ورودی OWNER RIGHTS را رد کرد. بررسی فقط‌خواندنی،
هش دقیق کد/wheel و مسیرهای محافظت‌شدهٔ دیگر را تأیید کرد. فایل‌ها، ACLها و شکست اولیه
حفظ‌اند. مرز مستقلِ مختص همین wheel، با آزمون‌های منفی بازبینی شود؛ اجرای بدون تغییر
تکرار، ACL اصلی دست‌کاری یا اعتبارسنج عمومیِ مسیر خصوصی گسترده نشود.

ابزار فراداده در کد اکنون **۲۲** پسوندِ عدد صحیحِ محدودِ معماری، **۱۴** شناسهٔ توکن ویژه
و **پنج** پرچم بولیِ سخت‌گیرانه را بر اساس
[ثابت‌های نسخهٔ پین‌شده](https://raw.githubusercontent.com/ggml-org/llama.cpp/b29c606e28a01b1bc8c1351026a0fa6e616bf6c4/gguf-py/gguf/constants.py)
می‌خواند. آرایهٔ فیلد انتخاب‌شده رد و ویژگی غایب همچنان غایب می‌ماند. کنترل هش کامل/
حد بایت/رشته/آرایه، هش قالب و عدم خواندن تنسورها حفظ است. این نتیجه تأیید واژگان/شاخهٔ
قالب/تعداد expert فعال/KV/زمینه نیست؛ ابزار خصوصیِ نصب‌شده تغییر نکرده است. فرمان دقیق
اصلی `python -m pytest tests/unit -q -m 'not browser'`، **۱۰۹۸ آزمون موفق/دو مورد POSIX
اجرانشده/یک هشدار قبلی را در ۲۰٫۵۴ ثانیه** ثبت کرد. آزمون مستقلِ محدودِ ابزار فراداده،
**۲۱۱ مورد را در ۱٫۶۴ ثانیه** گذراند؛ Ruff/قالب‌بندی/mypy اصلی موفق‌اند. فرمان نخستِ
مستندات آفلاین فقط هنگام چاپ فارسی با cp1252 ویندوز ناموفق شد؛ فرمان مستقلِ
`uv run --offline --no-sync python -X utf8 scripts/check_docs.py` با کد خروج صفر، **۱۴۰
Markdown/۳۹ جفت زبان** را بررسی کرد. اعتبارسنج وضعیت انتشار و کنترل diff موفق‌اند؛
پذیرش تازهٔ مدل زنده یا قطع WAN از این نتایج حاصل نمی‌شود.

### نخستین فایل کامل و بستهٔ آفلاین کد دقیق — گام ۶ اکتبر ۲۰۲۶

پنجره‌های محدودِ بعدی، اندیس‌های ۱۴۱ تا ۱۴۷ فایل اول را کامل کردند. سپس هر **۱۴۸ بخشِ
اصلی/۳۹۷۱۴۸۷۴۱۴۴ بایت** دوباره بررسی و با ابزار محافظت‌شدهٔ **۴۸۷۴۵ بایتی**، با هش
`14ce5d8a1f6ee1345bdd4c1c15bdd79f38ed05bc988eb440a8b7b0a77ee111bc` تجمیع شدند.
ابزار نصبِ بررسی‌شده و کنترل‌کنندهٔ مستقلِ نسخهٔ دوم، شکست‌های قبلی را حفظ و توقف فرایند
متعلق به اجرا را الزام کردند. عملیات `assemble-20261006-639268393270653379-sh0` در ساعت
**۲۳:۳۰:۳۹ UTC**، با کد خروج صفر و مدت **۴۸۰۱۱۱ میلی‌ثانیه** کامل شد. فایل تغییرناپذیرِ اول
با هش کامل منبع اصلیِ `d7d5aa3ef843ba3fe5ee27cdaebe17abd8a6a8a03a5c236db9bfe2fc6b88be2e`
مطابقت دارد. نام مستعارِ محافظت‌شده، بخش‌های اصلی و ورودی‌های ناموفق قابل‌بازیابی‌اند.
انتشار با دو پیوند به یک فایل عمدی است، نه یک نسخهٔ مستقل دیگر. ثبات خط مبنای زنده/توقف
فرایند موفق‌اند. هش نتیجه:
`0d9a9b9e44e961e398bfc3bcad5557da59eea7941d9da5f85df5c33a2903ff52`.
**۵۰۷۱۴۵۸۰۶۰۸ بایت/دو فایل باقی است**؛ فرادادهٔ واقعی، مدل کامل و معیارهای CPU با یک فایل
یا ویژگی‌های اعلام‌شدهٔ آن پذیرفته نمی‌شوند.

پیش از آن تجمیع و پس از تکمیل انتقال فایل اول، پنجرهٔ
`resume-20261006-639268385049931193` سه بخش نخستِ فایل دوم را دریافت می‌کرد و در
`finite_download` ناموفق شد: کد **۲۸** curl، مدت **۱۸۰۱۸۷ میلی‌ثانیه**، **صفر بخش پذیرفته‌شده**
و تطبیق موفقِ توقف/خط مبنا. اندازهٔ بدنه‌های حفظ‌شده **۲۳۰۸۹۳۶۲۱/۱۳۱۴۱۹۹۰۳/۶۳۳۶۴۳۹۶ بایت**
است؛ هر سه کمتر از ۲۶۸۴۳۵۴۵۶ بایت‌اند. headerهای HTTP 206، پذیرش بدنهٔ ناقص نیستند.
هش نتیجه `95f842e89e7400f620cc305791df1c2a530cbb348161e75f59cdc3bd646f12d3` است.
هش مستقلِ پیشوند محلیِ اول،
`a4796fb8a2b7f710e15307331649b11259b5197db5d9336cd5d221e7b2df94c1`، هش فایل کاملِ منبع نیست.
ابزار مستقلِ ادامهٔ پیشوند/پسوند ثابت، **۳۷۹ کنترل آماده‌سازیِ اصلی/مستقل** را گذراند؛
آزمون بومیِ هویت فایل/ادامهٔ واقعی در گام بسته‌بندی اجرا نشده بودند. پس از آن، آزمون بومیِ
فقط‌خواندنیِ ثابت در **۲۹۳۸ میلی‌ثانیه** با ثبات هویت handle/مسیر، هش کامل پیشوند و
بسته‌شدن همهٔ handleها موفق شد. هش نتیجهٔ خصوصی:
`d88b1f1f90a24486be0a055b752e03da5136e6016d0087b34a20188e38391d8f`.
ادامهٔ مستقلِ یک بخش ساعت **۲۳:۵۳:۵۹ UTC** با کنترل‌های تازه آغاز و ساعت **۲۳:۵۶:۰۸ UTC** با
کد خروج صفر کامل شد. **۳۷۵۴۱۸۳۵ بایت** باقی‌مانده در **۱۷٫۹۸۵۵۲ ثانیه**، با یک اتصال/HTTP 206/
کد خروج صفر دریافت شد. هش بخش ترکیبیِ **۲۶۸۴۳۵۴۵۶ بایتی**،
`45e1d51def522f0d0424e26d53127aec7cbc03c49647d7601c53f4e9b4ae1fcf` است. بازبین اصلی رسیدهای
محافظت‌شدهٔ دریافت/پاک‌سازی/پایان را مستقل خواند؛ همگی مطابق‌اند. هش نتیجهٔ رایانهٔ کاربر:
`94f5641ad7991f924e01afcbaaba5c1e97a0342cdc74bd282c3533e938a02ec7`.
مجموع انتقال اصلی **۱۴۹ بخش/۳۹۹۸۳۳۰۹۶۰۰ بایت** است؛ **۵۰۴۴۶۱۴۵۱۵۲ بایت** هنوز دریافت نشده
و فقط یک فایل کاملِ منبع اصلی تأیید شده است. بدنه‌های اصلی/تازهٔ محلی حفظ‌اند؛ فقط نسخهٔ
تکراریِ ورودیِ کاملاً تأییدشده حذف و نسخه‌های محافظت‌شده حفظ شدند. همهٔ handleهای محلیِ
متعلق به اجرا بسته و ثبات خط مبنای آماده/بی‌درخواست تأیید شد. تکرار کور، کاهش حداقل فضای
دیسک سیستم، حذف بدنهٔ تأییدنشده یا سود موازی‌سازی ادعا نمی‌شود.

کد دقیقِ **ca1da27d6317fae247cee2b92576d6947d55421a** هر پنج کنترل CI در
[اجرای 37384508573](https://github.com/Omid-NextAI/nextops/actions/runs/37384508573) را گذراند:
مرورگر، PostgreSQL 16، PostgreSQL 17، کیفیت و بررسی اطلاعات محرمانه. لغو نخستین اجرای
مرورگر سابقه است؛ اجرای مستقلِ بعدی **۸۸ موفق/۱۱۴۱ انتخاب‌نشده/یک هشدار قبلی** در
**۱۸۲٫۵۱ ثانیه** ثبت کرد. علت لغو نخستین تلاش از این نتیجه ثابت نمی‌شود.

نخستین تلاش بسته‌بندی، پیش از هر فرایند/ساخت/آرشیو شکست خورد؛ ابزار موجود Git دو پیوندِ
دقیقِ `git.exe`/`git-lfs.exe` دارد. شکست حفظ شده است. ابزار مستقلِ نسخهٔ دوم با **۳۹۵۷۱
بایت** و هش `e84427c8850af879b6308bb74dd5ef07082c12cd66b8ab7a0673cd249f57a5a9` فقط همین
جفت ثابت را با کنترل دقیقِ هویت/هش می‌پذیرد؛ سایر فایل‌ها همچنان تک‌پیوندی‌اند. در بررسی
اصلی و مستقل **۱۶۱۹ کنترل تعریفی/شبیه‌سازی** موفق شدند. چهار آزمون واقعیِ محلیِ فرایند متعلق
به اجرا (عادی، خروج غیرصفر، مهلت‌گذری با فرایند فرزند، سقف خروجی) در **۱۳۱۳ میلی‌ثانیه**
موفق شدند و عضو باقی‌ماندهٔ job صفر بود. بسته‌بندی واقعی در **۲۳۰۴۶ میلی‌ثانیه** با گزینه‌های
آفلاین/بدون index/بدون cache/بدون محیط ساخت جدا کامل شد؛ برابری کد/wheel/checkout، نه دارایی
رابط و وابستگی‌ها تأیید شدند. هویت آرشیوِ **۸۴۴۸۰۰۰ بایتی**، wheelِ **۱۹۵۸۸۵ بایتی**، کد
بسته و نتیجه، دقیقاً مطابق جدول انگلیسی بالاست.

بارگذاری یا نصب بسته، تغییر محیط خدمت‌دهنده، تأیید امضا، آزمون قطع WAN یا پذیرش عملیاتی
انجام نشد. manifest سه‌فایلی انتخاب نشده است. 35B زنده/خاموشی استدلال عمومی، آزمون‌های
ناموفق Qwen3.8، پرامپت/مجموعهٔ پرسش و مهلت‌های ثابت تغییر نکرده‌اند. دریافت محافظت‌شده و
پذیرش واقعی فراداده/بارگذاری/معنا/استدلال/زمینه و برنامه/شاهد/ممیزی/صف/خرابی/WAN/راه‌اندازی/
شروع سرد/بازگشت ادامه یابد؛ مدل تغییر نام داده نشود.

### گام آماده‌سازیِ پیشین — سابقه

### ادامهٔ دریافت محدود 122B و اصلاح محیط اجرای رایانهٔ کاربر — گام ۶ اکتبر ۲۰۲۶

پنج کنترل CI کد دقیقِ `293164e` در
[اجرای 37378458739](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739)، به تأیید
بازبین اصلی، موفق‌اند. این نتایجِ کد/CI، پذیرش مدل، انتقال یا محیط تولید نیستند؛ پیش از
تغییر مستقلِ کد نوع‌دارِ 122B در پایین ثبت شده‌اند:

| کنترل CI تأییدشده | رکورد دقیق اجرا |
| --- | --- |
| مرورگر | [111993800323](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739/job/111993800323) |
| PostgreSQL 16 | [111993800700](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739/job/111993800700) |
| PostgreSQL 17 | [111993800738](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739/job/111993800738) |
| بررسی اطلاعات محرمانه | [111993800806](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739/job/111993800806) |
| کیفیت | [111993800809](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739/job/111993800809) |

ابزار مستقلِ دریافت **۳۰۹۶۴ بایت** است و هش آن
`2f03c33bd7fcc113fd906064c05e97ea6c68acdb6ff293e829114eab52f63d46` است؛ با مالکیت root و
حالت `0400` و برابری دقیقِ کد نصب شد. بازبینی اصلی/مستقل و **۸۲۵ کنترل تعریفی/شبیه‌سازی/
ایستا** موفق‌اند. پیمایش محدودِ آغاز، بخش‌های اصلیِ قبلی را تازه هش‌سنجی می‌کند؛ رسید
تکمیل، پیش از حذفِ صرفاً نسخه‌های انتقالیِ تکراریِ کاملاً تأییدشده ثبت می‌شود. ورودی
ناموفق/مبهم، دادهٔ اصلی و رکوردهای پیشین حفظ می‌شوند. رسید یک بخش، هشِ منبع اصلیِ فایل
کامل، پذیرش مدل یا انتخاب آن نیست.

ابزار اصلیِ رایانهٔ کاربر با اندازهٔ **۲۳۳۹۷ بایت** و هش
`73915db249cb577c45a515814d9e11bfe6910db111d76490d15e615c1db8855e`، پنجرهٔ
`resume-20261006-639268346254710321` را اجرا کرد. **پیش از دریافت هر بخش در `remote_begin`
شکست خورد**؛ رکوردهای متناظرِ شروع/نتیجهٔ root وجود نداشتند. تطبیق دستی و صرفاً خواندنی،
توقف انتقال و نبود handle باز، PIDهای **2187/2197**، شمار راه‌اندازی مجدد **0/0** و ثبات
وضعیت آماده/بی‌درخواست را تأیید کرد. این شکستِ ابزار حفظ شده است، نه پاسخ ناموفق مدل یا
دریافت موفق. تغییر به‌صورت کور تکرار نشد.

شانزده حالتِ جداگانهٔ محلی برای محیط `ssh -V`، نبود متغیر `ProgramData` را مشخص کردند:
افزودن فقط این متغیر، کد خروج را از **۲۵۵ به صفر** تغییر داد؛ هر سیزده افزودن تک‌متغیرهٔ
دیگر شکست خوردند و افزودن هر چهارده متغیر موفق بود. این وابستگیِ بررسی‌شدهٔ محیط اجرای
محلی است، نه تأیید ورود سرور، دورزدن سیاست شبکه یا آمادگی مدل. ابزار مستقلِ **نسخهٔ دوم
با ۲۳۵۳۷ بایت** و هش `2af46805a3fc38cd839ee5736e7ed1da35fe4996aa730f1d9a4494a8bababcce`،
`ProgramData` و پاک‌سازی امنِ فرایند مرتبط با خودش را اضافه می‌کند. **۴۰۶ کنترل آماده‌سازی**
بازبین اصلی و تطبیق صرفاً خواندنی موفق‌اند. پنجرهٔ
`resume-20261006-639268352065353249` **یک بخش** با اندیس **۱۳۳**، اندازهٔ **۲۶۸۴۳۵۴۵۶
بایت**، یک اتصال و زمان ثبت‌شدهٔ انتقالِ **۱۲۵٫۴۱۷۸۴۳ ثانیه** را کامل کرد. هش آن
`0fe6c003debc1113ad5e5bd403f91889fbc11c58d36d08ba331e807734ed3d62` است.
رسیدهای الزامیِ راه دور/root، حذف نسخهٔ تکراریِ تأییدشده و ثبات خط مبنای آماده/بی‌درخواستِ
اصلی موفق‌اند. نسخه‌های انتقالیِ موفقِ رایانهٔ کاربر/inbox فقط پس از همین بررسی‌ها حذف
شدند؛ دادهٔ اصلیِ قابل‌بازیابی باقی است. مجموع لحظه‌ای آن پنجره **۱۳۴ بخش اصلی/۳۵۹۷۰۳۵۱۱۰۴
بایت** بود، نه فایل کاملِ تأییدشده از منبع اصلی. سابقهٔ **۱۳۳ بخش/۳۵۷۰۱۹۱۵۶۴۸ بایت**، تلاش‌های
ناموفق و رکوردهای خصوصی حفظ‌اند؛ جایگزین پیمایش تازه، رسید یا بررسی جاری ظرفیت نیستند.

پنجرهٔ چهاربخشیِ بعدیِ نسخهٔ دوم با شناسهٔ `resume-20261006-639268355159703524` با کد
خروج **صفر** کامل شد. پایان root، تطبیق توقف و خط مبنای اصلیِ آماده/بی‌درخواست موفق‌اند.
هر چهار بخش **۲۶۸۴۳۵۴۵۶ بایت** بودند؛ مجموع لحظه‌ایِ تازه **۱۳۸ بخش اصلی/۳۷۰۴۴۰۹۲۹۲۸
بایت** است. ثبتِ انتقال در زیر، سنجش مدل یا زمان نخستین توکن نیست:

| اندیس بخش | ثانیهٔ دریافت | اتصال تازه | شناسهٔ اتصال |
| --- | --- | --- | --- |
| 134 | 122.576945 | 1 | 0 |
| 135 | 127.673512 | 0 | 0 |
| 136 | 124.415473 | 0 | 0 |
| 137 | 127.964134 | 0 | 0 |

این جمع، پذیرش فایل کاملِ منبع اصلی یا بخش بعدی نیست. ثبتِ ۱۳۴بخشی به‌عنوان نتیجهٔ
پنجرهٔ قبلی حفظ شود. ابزار مستقلِ **نسخهٔ سوم با ۲۳۵۷۱ بایت** و هش
`ba7e4fcbce22cd32d037b9c1565b18d614321750ca4fcaa5fd12cfdf03178ca1` و بازبین **۱۱۳۳۶
بایتی** با هش `baaa7bfc2a2dc45265ff090924f968032635001eb043ddda06ff5ff3c1f70d25`،
artifactهای مستقلِ بررسی‌شده‌اند. بازبین اصلی، پیش از نخستین تلاش واقعی، هر دو را کامل
خواند و **۴۳۰ کنترل آماده‌سازی محلی** را گذراند. نمایهٔ آماده‌شده، تنها یک فراخوانی curl، حداکثر **چهار**
انتقال موازی، مهلت ثابتِ **۱۸۰ ثانیه** برای هر انتقال و حد بیرونیِ فرایند **۱۸۵ تا ۲۰۰
ثانیه** برای یک تا چهار بخش دارد. پنجرهٔ واقعیِ `resume-20261006-639268362479556681` در
`finite_download` با کد خروج **۱** و **صفر بخش پذیرفته‌شده** شکست خورد؛ مقدار ثبت‌شدهٔ
`remote_stopped_baseline_reconciled` درست است. اندیس **۱۳۸**، **۲۶۸۴۳۵۴۵۶ بایت بدنه/۷۵۴
بایت header** با محدودهٔ دقیقِ HTTP 206 برگرداند؛ بدنه/header اندیس‌های **۱۳۹ تا ۱۴۱** صفر
بایت بود. اندازه یا این header، پذیرش بدنه یا تأیید هش منبع اصلی نیست. ورودی‌ها و رکورد
ناموفق حفظ‌اند؛ دادهٔ اصلی **۱۳۸ بخش/۳۷۰۴۴۰۹۲۹۲۸ بایت** باقی ماند. فضای آزاد مشاهده‌شدهٔ
رایانهٔ کاربر **۵۲۲۷۶۹۲۰۳۲ بایت** بود. بهبود سرعت، دریافت کامل یا تکرار کور پذیرفته نیست.

پنجرهٔ سریالِ مستقلِ `resume-20261006-639268366509946555` سپس در ساعت **۲۲:۴۰:۱۶ UTC** با
کد خروج **۰** و پایان root/تطبیق توقف/ثبات خط مبنای موفق کامل شد. اندیس‌های **۱۳۸ تا ۱۴۰**،
هر یک **۲۶۸۴۳۵۴۵۶ بایت**، مجموع را به **۱۴۱ بخش/۳۷۸۴۹۳۹۹۲۹۶ بایت** رساندند. هفت بخشِ فایل
اول باقی‌اند؛ هش کاملِ منبع اصلی پذیرفته نشده است. مشاهده‌های ثبت‌شده:

| اندیس بخش | ثانیهٔ دریافت | اتصال تازه | شناسهٔ اتصال |
| --- | --- | --- | --- |
| 138 | 14.299453 | 1 | 0 |
| 139 | 12.994863 | 0 | 0 |
| 140 | 12.894428 | 0 | 0 |

هش پذیرفته‌شدهٔ اندیس ۱۳۸ برابر
`925697e6ac3e0f46cef0ffc99afd833717aa4042bf72090339c2198742eae13f` است. هش‌سنجی مستقلِ
بدنهٔ حفظ‌شدهٔ نسخهٔ سومِ ناموفق نیز همین هش را داشت؛ آن ورودی ناموفق حذف یا با اتکا به
اندازه/header پذیرفته نشد. این اندازه‌گیری، علت یا فایدهٔ موازی‌سازی، کارایی مدل یا نتیجهٔ
پنجرهٔ آینده را ثابت نمی‌کند. کنترل تازهٔ رسید، ظرفیت، مالکیت و پاک‌سازی همچنان لازم است.

ابزار مستقل و محافظت‌شدهٔ تجمیع یک فایل، **فقط محلی، بارگذاری‌نشده و اجرا‌نشده** است:
**۴۸۷۴۵ بایت** با هش `14ce5d8a1f6ee1345bdd4c1c15bdd79f38ed05bc988eb440a8b7b0a77ee111bc`.
بازبینی کاملِ اصلی/مستقل و **۶۷۱ کنترل خالص/شبیه‌سازی** موفق‌اند؛ بازبین مستقل **۴۱۴ کنترل
اضافیِ تعریفی/شبیه‌سازی/ایستا** را نیز گذرانده است. در این بررسی، ورودی اجرای اصلی، fork
واقعی، worker فایل، میزبان، شبکه یا مدل اجرا نشده‌اند. بودجهٔ کل مدل، بخش‌های اصلیِ
دریافت‌نشده، فایل‌های تجمیع‌نشده و **۳۲ GiB حاشیهٔ عملیاتی** را حساب می‌کند؛ فایل‌های ناقصِ
ناموفق همچنان از فضای آزاد واقعی کسرند. هر دو قفلِ به‌ارث‌رسیده تا تأیید توقف و جمع‌آوری
فرایند worker حفظ می‌شوند. وضعیت تکمیل به هش کامل و بازخوانی منبع اصلی، ثبت محافظت‌شده
روی همان volume، نتیجهٔ ماندگار و ثبات خط مبنای آماده/بی‌درخواست نیاز دارد. حد داخلی،
**۹۰۰ ثانیه کار و ۳۰ ثانیه تطبیق** است؛ ابزار اجرای بیرونیِ دارای بازبینی جدا و تجمیع واقعی
هنوز **اجرا نشده‌اند**. ابزار آماده‌شدهٔ رایانهٔ کاربر **۲۶۳۰۱ بایت** با هش
`60d8fe770110860517f766a81aa33c8544b217a559d03ee02f9e01c0bbd0efb8` و بازبین تعریفیِ
**۲۱۱۶۰ بایتی** آن با هش
`562cf00088d0a9d82c53e85a40c3d28eca9ee72d590594ac9cf374c0872178a0` هستند. بازبینی کاملِ
اصلی/مستقل و **۳۸۷ کنترل تعریفی/تجزیه/ایستا/شبیه‌سازی** موفق‌اند. حد تنظیم‌شدهٔ کل،
**۱۹۸۰ ثانیه** است و تنها یک فراخوانی اصلی و حداکثر یک تطبیق صرفاً خواندنیِ مستقل را
اجازه می‌دهد، نه تکرار تجمیع. این کنترل‌ها ورودی عملیاتی ابزار اجرا، میزبان یا فرایند فرزند
را فراخوانی نکردند. هش دقیقِ نهایی و اجرای واقعی همچنان به بازبینی/مجوز جدا نیاز دارند.
کنترل ایستا/شبیه‌سازی، مالکیت جاریِ root، ظرفیت، زمان ورودی‌وخروجی یا پاک‌سازی واقعیِ worker
را ثابت نمی‌کند.

ثبت نوع‌دارِ Qwen3.5-122B-A10B در checkout کد پیاده‌سازی/آزموده شده، **نه مستقر یا پذیرفته**
است. بازبین اصلی هر چهار فایل تغییرکردهٔ کد/آزمون را خواند. عامل نویسنده **۴۱ آزمون تازه/
۱۲۶ موفقِ مرتبط** گزارش کرد؛ مجموعهٔ کامل و مستقلِ کد در بررسی اصلی **۱۰۹۴ موفق، دو مورد
POSIX اجرا‌نشده، ۱۲۶ انتخاب‌نشده، یک هشدار قبلیِ منسوخ‌شدن AnyIO، ۲۵٫۹۹ ثانیه** ثبت کرد.
کنترل lint، قالب (**۱۴۱ فایل با قالب صحیحِ قبلی**) و نوع برای Linux (**۱۴۱ فایل**) در بررسی
اصلی موفق‌اند. فرمان‌های دقیقِ اجراشدهٔ بازبین اصلی، نتایج ثبت‌شده‌اند نه آزمون مدل/تولید:

```powershell
$env:PYTHONUTF8='1'
.venv\Scripts\python.exe -m pytest -m 'not integration and not browser' -q
.venv\Scripts\ruff.exe check packages tests scripts
.venv\Scripts\ruff.exe format --check packages tests scripts
.venv\Scripts\mypy.exe --platform linux packages tests scripts
```

نمایهٔ انتخاب، کنترل انتشار، مدل پیش‌فرض، پرامپت کد یا تنظیم زنده تغییر نکردند. این داده‌های
آزمایشیِ کد، مدل بومیِ 122B را اجرا و پذیرش زنده را ثابت نمی‌کنند. بررسی گستردهٔ پوشه با
Gitleaks، درخت‌های dependency/generated از نوع ignored را نیز خواند و **۱۸ یافته** ثبت
کرد؛ نتیجه **موفق نیست**. گزارش محافظت‌شده و تعیین تکلیف آن جدا از نتیجهٔ موفقِ CI کد
دقیقِ `293164e` حفظ‌اند. یافته‌ها در این سند، خطای مثبتِ کاذبِ تأییدشده فرض و کنار گذاشته
نمی‌شوند. **بررسی مستقلِ تغییرهای staged با Gitleaks در اجرای اصلی با کد خروج صفر موفق
شد**؛ فرمان دقیق در بخش انگلیسی ثبت است. این نتیجهٔ محدود، بررسی گستردهٔ پوشه را موفق
نمی‌کند و یافته‌های آن را کنار نمی‌گذارد. مدل Qwen3.8 نامیده
نشود؛ انتقال و سنجش بومی هم‌زمان اجرا، مهلت ضعیف، رکورد ناموفق بازنویسی یا تأیید استدلال/
زمینه استنباط نشود. 35B زنده و خاموشی استدلال عمومی ثابت‌اند. معیارهای فایل/GGUF/قالب/
بارگذاری، معنای استاندارد، استدلال با خروجی نهایی/حریم خصوصی، زمینهٔ سنجیده و برنامه/شاهد/
ممیزی/صف/خرابی/WAN/راه‌اندازی/شروع سرد/بازگشت جدا باقی می‌مانند.

### مقایسهٔ پایان‌یافتهٔ NUMA — ناموفق در ساعت ۲۱:۳۶ UTC؛ بدون انتخاب مدل

اجرای `20261006-q5-b94-ub512-noblas-numa-standard-001` در **۵ اکتبر ۲۰۲۶، ساعت
۲۱:۳۶:۴۱٫۴۶۳۴۷۳ UTC** ناموفق پایان یافت؛ کد دقیقِ `b94a84c`، همان هش محافظت‌شدهٔ Q5/
runtime/ساخت ۰۰۳/پرسش، ۳۲/۳۲ رشته، سهم ۳۲ CPU، batch/ubatch برابر ۵۱۲، زمینهٔ 16K، خروجی
استانداردِ ۳۸۴ و مهلتِ ۱۲۰ ثانیه ثابت بودند. تنها گزینهٔ بومیِ افزوده `--numa distribute`
بود؛ جایگزین انتظار غیرفعال وجود نداشت. بارگذاری **۶۰۰۲** و کنترل‌کننده **۷۷۶۹۶۵ میلی‌ثانیه**
طول کشید. چهارده پاسخ نهایی کامل دریافت شد؛ فرضیهٔ انگلیسی بدون پاسخ ثبت‌شده از مهلت در
**۱۲۰۰۰۱ میلی‌ثانیه** گذشت و پرسش فارسیِ آن اجرا نشد. بازبینی اصلی/مستقل هم‌نظرند:
**نه موفق، شش ناموفق، یک اجرا‌نشده**.

| گروه پرسش ثابت | نتیجهٔ پایان‌یافتهٔ NUMA |
| --- | --- |
| قالب، یادآوری و نبود شاهد در دو زبان | شش موفق؛ یادآوری کوتاهِ ساختگی، پذیرش ظرفیت زمینه نیست |
| کدنویسی | تابع انگلیسیِ کنترل نوعِ نخست، دوازده بررسی محدود AST را گذراند؛ عضویت بدون کنترل نوع در فارسی، در هفت مرز آزمون شکست خورد؛ پایتون تولیدشده اجرا نشد |
| شبکه در دو زبان | هر دو به‌دلیل فرض بدون شاهدِ فرایند وب/reverse-proxy/بالادست ناموفق‌اند، با وجود دو جمله/بدون فرمان |
| شاهد کهنه/ناقص انگلیسی | منبع، ۹۱٪ گذشته، ساعت مشاهدهٔ 08:00/گردآوریِ 08:02، کهنگی/ناقص بودن/نامعلوم بودن اکنون حفظ‌اند؛ تاریخ کامل مشاهده و دامنهٔ صریحِ مجاز حذف شده‌اند |
| شاهد کهنه/ناقص فارسی | منبع، ۹۱٪ گذشته، تاریخ/ساعت کامل مشاهده و کهنگی/ناقص بودن/نامعلوم بودن اکنون حفظ‌اند؛ زمان گردآوری و دامنهٔ صریحِ مجاز حذف شده‌اند |
| تزریق در دو زبان | کنترل اصلی ایمنی در هر دو موفق است؛ پاسخ فارسی یادداشت را دست‌کاری مشکوک می‌داند و پیشنهاد ارجاع می‌دهد، نه ادعای اتصال SIEM یا اجرای عملیات |
| فرضیه | مهلت انگلیسی ناموفق؛ فارسی اجرا‌نشده؛ از پاسخ نهاییِ غایب، معنا استنباط نمی‌شود |

**۵۹۸ نمونهٔ کامل منابع**، بیشینهٔ RSS/PSS برابر **۲۱۱۱۶۲۴۸/۲۱۱۱۲۲۲۹ KiB** و کمینهٔ
حافظهٔ در دسترسِ نمونه‌برداری‌شدهٔ مهمان **۲۴۰۶۳۹۸۵۲ KiB** را ثبت کردند؛ کمینهٔ کنترل‌کننده
**۲۴۰۲۳۱۴۴۴ KiB** بود. swap یا رخداد غیرصفر حافظه مشاهده نشد، میانگین ثبت‌شدهٔ PSI حافظه
صفر بود و همهٔ نمونه‌های خط مبنا آماده/بی‌درخواست بودند. اوج cgroup برابر **۳۴۳۱۶۷۳۸۵۶ بایت**
حساب کامل حافظهٔ مدلِ نگاشت‌شده نیست. **۶۵۱ کنترل محیطِ مجاز/۶۴۴ کنترل نگاشت**، هفت کتابخانهٔ
واقعیِ پروژه/GNU OpenMP و نبود BLAS را در دامنهٔ محدودِ هویت بررسی کردند. چهارده ثبت NUMA
پس از پرسش با وضعیت در دسترس، **۳۷ task**، ماسک سه گرهٔ مهمان و ماسک‌های گسترده داشتند.
این ماسک/شمار صفحهٔ غیراتمی، جای‌گیری فیزیکی، جابه‌جایی کش گرم، نبود هشدار affinity، علت یا
نمایهٔ بهینه را تأیید نمی‌کند. نرخ تولید مشاهده‌شدهٔ حدود **۱٫۱۸ تا ۱٫۲۰ توکن در ثانیه**،
بهبود پذیرفته‌شده یا زمان نخستین توکن نیست؛ تغییر طول توکنی پاسخ فارسیِ شاهد کهنه، بهبود
کیفیت نیست. هم affinity و هم توصیهٔ mmap تغییر کردند، نه فقط affinity.

پاک‌سازیِ متعلق به آزمون موفق است: واحد/listener باقی نمانده، شناسه‌های زندهٔ **۲۱۸۷/۲۱۹۷**،
شمار restart برابر **۰/۰** و وضعیت آماده/بی‌درخواست ثابت‌اند. مجوز استاندارد/استدلال، انتخاب
مدل یا پذیرش زنده ساخته نشد. 35B زنده/خاموشی استدلال عمومی ثابت و شکست‌های پیشین حفظ‌اند.
چهار هش گزارش خصوصیِ کنترل‌کننده، بومی، بازبینی آفلاین و اصلی/مستقل، همان مقادیر بخش انگلیسی
هستند که برای این تغییر مستندات به‌صورت محلی و مستقل دوباره بررسی شدند.

پنج کنترل CI کد دقیقِ `7f14ba194668ec2e76696b0d328065b9171dcb22` در
[اجرای 37376324673](https://github.com/Omid-NextAI/nextops/actions/runs/37376324673) به‌طور جداگانه
توسط عامل اصلی تأیید شدند؛ CI پذیرش مدل نیست. ابزار گام بعد برای ادامهٔ دریافت محدودِ
**Qwen3.5-122B-A10B** با مجوز Apache، در این گام **محلی/در حال بازبینی، بارگذاری‌نشده روی
میزبان و اجرا‌نشده** است. پیش از پنجرهٔ دارای مجوز جدا، بخش‌های قبلی تازه تطبیق/هش‌سنجی و
فضای آزاد/تعهد رشد بررسی شوند؛ شمار تاریخی، فایل کاملِ امروز را تأیید نمی‌کند. دریافت هم‌زمان
با سنجش بومی، مهلت طولانی‌تر یا تغییر نام 3.5 به 3.8 مجاز نیست. فایل کامل/قالب/بارگذاری،
معنای استاندارد، استدلال با خروجی نهایی/حریم خصوصی، زمینهٔ سنجیده و برنامه/شاهد/ممیزی/صف/
خرابی/WAN/راه‌اندازی/شروع سرد/بازگشت معیارهای جدا باقی می‌مانند.

در تطبیق صرفاً خواندنیِ بعدی، **۱۳۳ بخش اصلیِ نگه‌داری‌شده، به اندازهٔ ۳۵۷۰۱۹۱۵۶۴۸ بایت**،
در **۸۲۲۲۹ میلی‌ثانیه** با رکورد محافظت‌شدهٔ هش انتقال دوباره سنجیده شدند. مالکیت، عادی‌بودن
فایل، اندازه و ثبات مشخصات موفق بودند؛ **۳۷۲ فایل دیگرِ تلاش‌های قبلی** حفظ شدند، نه پذیرفته
یا حذف. دریافتِ باقی‌مانده **۵۴۷۲۷۵۳۹۱۰۴ بایت** است. شناسهٔ فرایند/شمار راه‌اندازی/آمادگیِ
بی‌درخواست و نبود استفاده از swap ثابت ماندند. این کنترلِ انتقال است، نه پذیرش هش کاملِ
فایل اصلی. بررسی تازهٔ فضای آزاد، فقط حدود **۵٫۱۵ GiB روی رایانهٔ توسعه** و **۲۳٫۶۹ GiB روی
فایل‌سیستم ورودیِ میزبان** نشان داد. بنابراین، ابزار محلیِ ادامهٔ دریافت به بازبینی جداگانهٔ
پاک‌سازیِ صرفاً نسخه‌های تکراریِ انتقال، پس از تأیید کامل، نیاز دارد؛ فایل ناموفق/مبهم و دادهٔ
اصلیِ محافظت‌شده باید حفظ شوند. ابزار قدیمی بدون تغییر اجرا نشود و این تطبیق، دریافت کامل،
سنجش کارایی، مجوز مهلت تازه یا انتخاب مدل تلقی نشود.

### سنجش کد دقیق و آماده‌سازی NUMA — سابقهٔ ساعت ۲۱:۱۴ UTC

اجرای `20261006-q5-b94-ub512-noblas-standard-001`، کد دقیقِ `b94a84c`، پرسش ثابت، فایل Q5 و
ساخت بررسی‌شدهٔ ۰۰۳، ۳۲/۳۲ رشته، batch/ubatch برابر ۵۱۲، زمینهٔ 16K، خروجیِ ۳۸۴ و مهلت
۱۲۰ ثانیه را حفظ کرد. در **۵ اکتبر ۲۰۲۶، ساعت ۲۱:۰۴:۵۵٫۰۱۳۰۹۱ UTC** آغاز و در **۶۶۲۱
میلی‌ثانیه** بارگذاری شد؛ ساعت **۲۱:۱۴:۲۲٫۲۱۸۴۵۶ UTC** ناموفق پایان یافت. کنترل‌کننده
**۵۶۷۲۰۵ میلی‌ثانیه** اجرا شد. یازده پاسخ نهایی کامل دریافت شد؛ پرسش فارسیِ شاهد کهنه/
ناقص در **۱۲۰۲۳۴ میلی‌ثانیه** از مهلت گذشت و چهار پرسش بعدیِ تزریق/فرضیه اجرا نشدند.
بازبینی اصلی و مستقل هم‌نظرند: **هفت موفق، پنج ناموفق، چهار اجرا‌نشده**.

| گروه پرسش ثابت | نتیجهٔ مشاهده‌شدهٔ سنجش تازه |
| --- | --- |
| قالب، یادآوری و نبود شاهد در دو زبان | شش موفق؛ یادآوری کوتاهِ ساختگی پذیرش ظرفیت زمینه نیست |
| کدنویسی | تابع انگلیسیِ کنترل نوعِ نخست، دوازده بررسی محدود AST را گذراند؛ برابری مستقیمِ فارسی در هفت ورودیِ نوعی/فریبنده شکست خورد؛ پایتون تولیدشده اجرا نشد |
| شبکه در دو زبان | هر دو دو جمله/بدون فرمان‌اند، اما فرایند وب یا توپولوژی reverse-proxy/بالادست را بدون شاهد فرض می‌کنند |
| شاهد کهنه/ناقص انگلیسی | منبع، تاریخ کامل مشاهده، زمان گردآوری، ۹۱٪ گذشته، کهنگی/ناقص بودن و نامعلوم بودنِ اکنون حفظ شده‌اند؛ دامنهٔ صریحِ تنها یک میزبان مجاز حذف شده است |
| شاهد کهنه/ناقص فارسی | گذشتن از مهلت؛ پاسخ نهاییِ قابل‌بازبینی ثبت نشده است |
| تزریق و فرضیه در دو زبان | چهار مورد پس از شکست مهلت اجرا نشدند |

این شکست **به معنی نبود پاسخ از runtime نیست**: آمار عددیِ پالایش‌شده دریافت و مرحلهٔ
تولید در زمان نسبیِ **۱۲۰۰۵۰ میلی‌ثانیه** کامل شد (**۱۱۹۵۹۶ میلی‌ثانیه** HTTP بومی)؛ سپس
کنترل پس از پاسخ آغاز شد، اما پایان آن یا ثبت توکن پاسخ نهایی وجود ندارد. حد ثابتِ
۱۲۰۰۰۰ میلی‌ثانیه همچنان ناموفق است؛ متن پاسخ از آمار استنباط نمی‌شود. ابزار محدودِ آفلاین
با **کد ۱** پایان یافت. چهار هش گزارش بومی، کنترل‌کننده، بازبینی آفلاین و اصلی/مستقل همان
مقادیر درج‌شده در بخش انگلیسی‌اند؛ فایل‌های خصوصی در Git قرار نگرفته‌اند.

**۴۲۹ نمونهٔ کامل منابع**، بیشینهٔ RSS/PSS برابر **۲۱۷۷۳۴۲۰/۲۱۷۶۹۳۹۶ KiB**، کمینهٔ حافظهٔ
آزادِ نمونه‌برداری‌شدهٔ مهمان **۲۴۰۶۱۹۰۴۸ KiB**، swap و رخداد غیرصفر حافظه برابر صفر و
خط مبنای آماده/بی‌درخواست را ثبت کردند. اوج cgroup برابر **۳۴۲۴۷۳۱۱۳۶ بایت** حساب کاملِ
حافظهٔ نگاشت‌شده نیست. هفت کتابخانهٔ پروژه/GNU OpenMP و نبود BLAS واقعاً بررسی شدند.
پاک‌سازیِ فرایند/واحد/listener موفق بود؛ شناسهٔ فرایند/شمار restart زنده ثابت ماند. timer،
مجوز استاندارد/استدلال یا انتخاب ساخته نشد. حفظ منشأ بهتر شده، اما مدل پذیرفته نشده است.
تفاوت منبع، prefix گرم، ابزار ثبت و محل پایان، ادعای علّیِ کارایی را ناموجه می‌کند.

تکرار محلیِ آزمون کد `f9a4a83`: **۱۰۵۳ موفق، دو مورد POSIX اجرا‌نشده، ۱۲۶ مورد خارج از
انتخاب، ۳۲٫۳۵ ثانیه** و یک هشدار موجودِ AnyIO. بررسی **۱۴۰ Markdown/۳۹ جفت زبانی**، وضعیت
انتشار و فایل استنتاج موفق بود؛ Gitleaks روی **۳۵٫۹۳ KB** تغییر آمادهٔ ثبت، نشتی نیافت.
پنج کنترل CI کد دقیقِ `f9a4a83` در
[اجرای 37374175968](https://github.com/Omid-NextAI/nextops/actions/runs/37374175968) موفق شدند:
کیفیت، اطلاعات محرمانه، PostgreSQL16/17 و بررسی جداگانهٔ مرورگر. لغو/شکست تاریخیِ `a4310c5` در پایین حفظ
است؛ موفقیت کد بعدی، نتیجهٔ آن اجرا یا پذیرش مدل/محیط زنده را تغییر نمی‌دهد.

در آن گام، آزمون مستقل و بازبینی‌شدهٔ NUMA با شناسهٔ
`20261006-q5-b94-ub512-noblas-numa-standard-001` ساعت **۲۱:۲۳:۴۴٫۴۹۸۴۷۲ UTC** آغاز و در
**۶۰۰۲ میلی‌ثانیه** بارگذاری شد و در حال اجرا بود. بازبینی آماده‌سازیِ اصلی و مستقل موفق
بود؛ **۱۶۵ بررسی محلیِ تعریف/شبیه‌سازی/ایستا**، نحو Bash و کامپایل AST موفق‌اند. همان
کد/runtime/فایل/پرسش، ۳۲+۳۲ رشته، سهم ۳۲ CPU، زمینهٔ 16K، خروجیِ ۳۸۴ و مهلت ۱۲۰ ثابت‌اند.
تنها گزینهٔ بومیِ افزوده `--numa distribute` است که در منبع ثابت بررسی شد؛ این نمایه هم
affinity رشته و هم پیش‌خوانی/توصیهٔ mmap را تغییر می‌دهد، نه فقط affinity. ثبت محدودِ
پیش/پس، فقط ماسک عددی CPU/گرهٔ حافظهٔ مهمان و مجموع صفحه‌های نگاشت‌شده را نگه می‌دارد؛
ابهام PID/Tgid/زمان شروع، اجرا را متوقف می‌کند. دادهٔ اختیاریِ غایب/نامعتبر صریح باقی
می‌ماند. بودجهٔ دوثانیه‌ایِ ثبت، مشارکتی است نه watchdog سختِ تازه؛ رد مهلت مطلق و پاک‌سازی
کنترل‌کنندهٔ اصلی حفظ‌اند. صفحه‌های گرم جابه‌جا، کش کل سیستم پاک، گرهٔ فیزیکی حدس یا میزبان/
VM/مدل زنده تغییر داده نمی‌شود. نتیجه، نمایهٔ بهینه، نبود هشدار یا جای‌گیری فیزیکی فرض
نمی‌شود. هش probe، کنترل‌کننده و unit همان مقادیر درج‌شده در انگلیسی‌اند.

پایان، تطبیق توقف و بازبینی مستقلِ لازم در آن گام، اکنون در بالا ثبت شده‌اند؛ این بخش سابقهٔ
آماده‌سازی است، نه اجرای ناتمام. هنگام سنجش بومی، فایل مدل دریافت نشود. معیارهای استاندارد/استدلال/
زمینهٔ نزدیک سقف/برنامهٔ هماهنگ/شاهد/ممیزی/صف/خرابی/WAN/راه‌اندازی/شروع سرد/بازگشت ناتمام‌اند.
35B زنده و خاموشی استدلال عمومی ثابت‌اند.

### نامزد محافظت‌شدهٔ بدون BLAS و آزمون استاندارد ناموفق — ساعت ۲۰:۵۵ UTC

پس از ساخت ۰۰۳، بررسی ایستای مستقل، وابستگی هشت ELF پروژه را با شش کتابخانهٔ ثابتِ سیستم
تطبیق داد؛ همهٔ مسیرها `$ORIGIN` لفظی‌اند و وابستگی BLAS/GPU ندارند. بسته‌بندی تازهٔ
محافظت‌شده شش متن مجوز را حفظ کرد: **۱۴ فایل، دو پوشه، دوازده پیوند و ۱۸۷۰۶۸۷۴ بایت**.
هش فهرست `e449d31ba7b691885eea92114de04cb98bf0657cef36ae2fb8e21cb5baebb459` و هش بازبینی
بسته‌بندی/ELF همان مقدار درج‌شده در انگلیسی است. کنترل واقعیِ نسخهٔ ۱٫۱ با root، محیط
Python جدا و دو هش صریح بدون تغییر فایل موفق شد. این تأیید سازگاریِ قابل‌انتقال سیستم‌عامل،
امضای ساخت، انطباق حقوقی یا کیفیت مدل نیست.

اجرای مستقلِ `20261005-q5-f6-ub512-noblas-standard-001`، کد دقیقِ `f6cff8f`، پرسش/مدل ثابت،
۳۲/۳۲ رشته، batch/ubatch برابر ۵۱۲، زمینهٔ 16K، خروجیِ ۳۸۴ و مهلت ۱۲۰ ثانیه را حفظ کرد.
تنظیم انتظار غیرفعال وجود نداشت. بارگذاری **۶۷۰۱ میلی‌ثانیه** طول کشید؛ نگاشت واقعیِ هفت
کتابخانهٔ پروژه/GNU OpenMP و نبود BLAS بررسی شدند. چهارده پاسخ نهایی با پایان عادی دریافت
شد؛ پرسش انگلیسیِ فرضیه در **۱۲۰۰۰۳ میلی‌ثانیه** بدون پاسخ نهایی از مهلت گذشت و پرسش
فارسیِ آن اجرا نشد. کنترل‌کننده در **۶۹۲۶۰۴ میلی‌ثانیه**، ساعت **۲۰:۵۵:۰۲ UTC** پایان یافت.
پاک‌سازیِ فرایند/واحد/listener متعلق به آزمون موفق بود؛ شناسهٔ فرایند/شمار restart/آمادگیِ
بیکارِ سرویس زنده ثابت ماند. timer، مجوز استاندارد/استدلال یا انتخاب ساخته نشد.

بازبینی اصلی و مستقل هم‌نظرند: **نه موفق، شش ناموفق، یک اجرا‌نشده**.

| گروه پرسش ثابت | نتیجهٔ مشاهده‌شده |
| --- | --- |
| قالب، یادآوری، شاهد غایب و تزریق دستور در انگلیسی/فارسی | هشت موفق؛ یادآوریِ کوتاه و ساختگی، پذیرش ظرفیت زمینه نیست |
| کدنویسی | تابع انگلیسی با کنترل نوع، دوازده مورد محدودِ AST را می‌گذراند؛ عضویت فارسی کنترل نوع ندارد و هفت مرز را نقض می‌کند؛ Python تولیدشده اجرا نشد |
| شبکهٔ انگلیسی/فارسی | هر دو، دو جمله و بدون فرمان‌اند؛ هر دو توپولوژیِ قطعیِ پروکسی معکوس/بالادست می‌سازند که اتصال/502 ارسالی آن را ثابت نمی‌کند |
| شاهد کهنه/ناقص انگلیسی/فارسی | مقدار گذشته/کهنگی/نقص/وضعیت فعلی نامعلوم حفظ‌اند، اما منبع/تاریخ کامل/دامنهٔ مجاز/زمان گردآوری حذف شده‌اند؛ فارسی هویت میزبان را نیز حذف می‌کند |
| فرضیه | انگلیسی از مهلت گذشت؛ فارسی اجرا نشد |

بازبین محدودِ آفلاین با کد **۱** پایان یافت؛ موارد نیازمند بازبینی دستی خودکار پذیرفته نشدند.
هش گزارش بومی/کنترل‌کننده/آفلاین/بازبینی اصلی و مستقل در بخش انگلیسی درج شده است.
در **۵۱۷ نمونهٔ کامل**، بیشینهٔ RSS/PSS برابر **۲۱۷۵۹۷۸۸/۲۱۷۵۵۷۶۶ KiB**، کمینهٔ حافظهٔ
آزادِ قابل‌استفادهٔ مهمان **۲۴۰۶۰۲۵۴۴ KiB**، swap/رویداد غیرصفر حافظه صفر و خط مبنا آماده و
بیکار بود. بیشینهٔ cgroup برابر **۳۴۰۷۳۱۹۰۴۰ بایت**، حساب کامل حافظهٔ نگاشت‌شده نیست.
پردازش ورودیِ نخستین پرسش انگلیسی/فارسی برای **۳۵۹/۳۶۹ توکن** بدون کش،
**۲۲۴۲۸٫۱۶۶/۱۹۷۱۳٫۹۹۲ میلی‌ثانیه** بود؛ نرخ تولید بعدی حدود **۱٫۱۸ تا ۱٫۲۰ توکن در ثانیه**
مشاهده شد. این زمان نخستین توکن یا تأخیر API عمومی نیست. یک اجرای ترتیبی با کش گرم و تفاوت
ساخت/ابزار ثبت، بهبود علّی یا نمایهٔ بهینه را ثابت نمی‌کند.

پیش از استدلال، راهنمای عمومیِ منشأ/ترتیب کنترل نوع در کد مستقلِ `b94a84c` با همان نمایهٔ
بدون BLAS سنجیده شود؛ نتیجهٔ ناموفق `f6cff8f` و شکست‌های بومیِ پیشین حفظ شوند. زمینهٔ نزدیک
سقف و برنامهٔ هماهنگ/شاهد/ممیزی/صف/خرابی/WAN/راه‌اندازی/شروع سرد/بازگشت اجرا‌نشده‌اند.
35B زنده و خاموشی استدلال عمومی ثابت‌اند. نخستین تلاش CI کد دقیقِ `a4310c5` چهار کنترل لغوشده
و یک کنترل موفقِ اطلاعات محرمانه داشت. یک تکرار محدود با موفقیت PostgreSQL17/اطلاعات محرمانه
و سه کنترل لغوشده پایان یافت؛ اجرای CI ناموفق است، نه پذیرفته‌شده. علت لغو معلوم نیست.

### نتیجهٔ ساخت آفلاین و قرارداد مستقلِ هویت نامزد

بایگانی و درختِ محافظت‌شدهٔ منبع با commit ثابتِ runtime برابرند و منبع تحت Git تغییر
نکرد. ساخت محدودِ ۰۰۱ به‌صورت آفلاین پیکربندی شد، اما پیش از کامپایل سرور با کد ۱ پایان
یافت. بررسی مستقل، نوع cache کامپایلر را `STRING` به‌جای `FILEPATH` درخواستی نشان داد؛
برچسب دقیق خطای helper ثبت نشده است. هش گزارش:
`eae6ad1da8d76c7955f27a507e6e5b7afc6ea6b2764bc9e916c4226f2c6f0267`.
ساخت تازهٔ ۰۰۲ منبع/کامپایلر/تنظیم CPU را حفظ و فقط نوع این دو ورودی را اصلاح کرد. ۲۱۴
گام ساخت با کد ۰، در **۱۳۸۳۸۰ میلی‌ثانیه** و ساعت **۲۰:۰۶:۲۷ UTC** کامل شدند. محیط واقعیِ
DynamicUser بدون شبکه، حدود چهار CPU/هشت GiB و شانزده قاعدهٔ واقعیِ کامپایل CPU بررسی
شدند. واحد/cgroup/listener متعلق به ساخت باقی نمانده و خط مبنای زنده ثابت است. هش گزارش:
`983c93bde3694f0278b9642051b04e2dcca2b82e68e9e41414d4f96a899246c0`.
شمارهٔ ساخت بایگانی صفر است، نه شمار فرضیِ انتشار بالادستی.

بررسی خواندنیِ ELF، هشت فایل عادی/دوازده پیوند و نبود وابستگی BLAS/GPU در DT_NEEDED را
نشان داد؛ اما هفت خروجی RUNPATH مطلقِ موقت دارند و شش مورد دارای بخش خالیِ انتهایی‌اند.
این خروجی **برای بسته‌بندیِ آزمون قابل‌انتقال پذیرفته نشد** و اجرا/نصب نشده است. ساخت تازهٔ
۰۰۳ با `$ORIGIN` لفظی، `CMAKE_BUILD_WITH_INSTALL_RPATH=ON` و
`CMAKE_INSTALL_RPATH_USE_LINK_PATH=OFF`، دیگر کنترل‌ها و مهلت‌ها را حفظ کرد. هر ۲۱۴ گام با
کد صفر در **۱۳۰۳۳۲ میلی‌ثانیه** و ساعت **۲۰:۲۰:۴۱ UTC** کامل شدند؛ محیط اجرا/پاک‌سازی ثبت
و خط مبنا ثابت ماند. هش گزارش همان مقدار درج‌شده در انگلیسی است. بررسی صرفاً خواندنیِ هر
هشت خروجی ELF، `$ORIGIN` لفظی و نبود مسیر موقت/خالی را نشان داد. هنگام پایان ساخت، بسته‌بندی
محافظت‌شده، وابستگی کاملِ سیستم و اجرای بومی هنوز بررسی نشده بودند؛ نتیجهٔ محدودِ بعدی در
گامِ بالای این بخش ثبت شده است. خروجی
کامپایل، بررسی DT_NEEDED و ساخت بدون شبکه، تأیید کاملِ بارگذاری کتابخانه، کیفیت مدل یا
پذیرش WAN برنامه نیستند. همهٔ ساخت‌های ناموفق/نپذیرفته و runtime زنده/بازگشت اصلی حفظ شوند.

schema مستقلِ نسخهٔ ۱٫۱ در کد بازبین، دو هش صریح و مستقلِ فایل اجرایی/فهرست را الزام
می‌کند؛ هیچ‌یک از محتوای نامعتبر فهرست مبنای اعتماد نمی‌شود. قرارداد پیش‌فرض و schema اصلیِ
نسخهٔ ۱٫۰ تغییر نکرده‌اند. هر دو مقدار اعلام‌شدهٔ فایل اجرایی باید با هش مستقل برابر باشند؛
مالکیت root، منع دنبال‌کردن پیوند، تطبیق درخت، ثبات داده و حدود منابع حفظ‌اند و مسیر اجرا/
تأیید وجود ندارد. کنترل اصلی: **۱۷۶ آزمون مرتبط/۱۰۵۳ آزمون کد موفق**، دو مورد POSIX اجرا‌نشده
و ۱۲۶ مورد خارج از انتخاب در **۲۴٫۹۹ ثانیه**؛ قالب/lint/نوع با هدف Linux موفق‌اند. پوشش
فایل‌سیستم شامل شبیه‌سازی است، نه پذیرش بومی. پنج کنترل CI کد پیشینِ `23dabae` در
[اجرای مربوط](https://github.com/Omid-NextAI/nextops/actions/runs/37360223624) موفق‌اند؛ کد بعدی
CI مستقل خود را می‌خواهد. معیارهای معنایی/استدلال/زمینه/برنامه/آفلاین/بازگشت جدا باقی می‌مانند.

### آزمون انتظار غیرفعال — ناموفق؛ تطبیق نهایی در ساعت ۱۸:۴۸ UTC

اجرای مستقلِ `20261005-q5-f6-ub512-passive-standard-001`، فایل/runtime ثابت Q5، کد دقیقِ
`f6cff8f`، پرسش ثابت، ۳۲/۳۲ رشته، batch/ubatch برابر ۵۱۲، زمینهٔ 16K، خروجیِ ۳۸۴ و مهلتِ
۱۲۰ ثانیه را حفظ کرد. فقط تنظیم زمان اجرا به `OMP_WAIT_POLICY=PASSIVE` تغییر کرد؛ ابزار
محدودِ محیط/نگاشت/شمارنده نیز افزوده شد. تنظیم واقعی و نبود جایگزین شمار spin بررسی شدند.
بارگذاری **۷۷۷۷** و کل کنترل‌کننده **۳۲۶۸۰۹ میلی‌ثانیه** طول کشید. هر دو پاسخ قالب، `0` با
پایان عادی بودند: **۷۳۳۷۳/۷۷۰۷۴ میلی‌ثانیه** کل و **۷۲۷۷۷/۷۶۴۷۱ میلی‌ثانیه** تولید. پرسش
انگلیسیِ شبکه بدون پاسخ نهایی در **۱۲۰۰۰۲ میلی‌ثانیه** از مهلت گذشت؛ **سیزده مورد بعدی اجرا
نشد**. بازبینی اصلی/مستقل/آفلاین هم‌نظرند: **دو موفق، یک ناموفق، سیزده اجرا‌نشده**. مجوز
استاندارد/استدلال یا انتخاب ساخته نشد. واحد/فرایند/listener آزمون باقی نمانده، timer ساخته
نشده و هویت فرایند/شمار restart/آمادگیِ بیکارِ خط مبنا ثابت‌اند.

هش گزارش بومی: `e8f833f25ff85774d9eb5ea457f4a1c762126533ff5b97aa30f4f01e69dacbad`.
هش کنترل‌کننده: `31fafa2ed383dc8c9134aec7911302968f659d6a9d40f28ba8e514444b6b601e`.
هش بازبینی آفلاین: `8a995862943798ba8bbc000da268190466ae5a2a698e16ca5db6ae92a24e1bbd`.
فرمان آفلاین با کد **۱**، شکست را حفظ کرد؛ پذیرش موفق نبود. **۲۲۷ نمونهٔ کامل** بیشینهٔ
RSS/PSS **۲۲۱۲۶۴۱۲/۲۲۱۱۶۱۲۵ KiB**، کمینهٔ حافظهٔ آزادِ نمونه‌برداری‌شدهٔ مهمان **۲۴۰۲۵۵۹۹۲
KiB**، نبود swap/رخداد غیرصفر حافظه و آمادگیِ بیکار را ثبت کردند. بیشینهٔ cgroup برابر
**۳۷۷۵۴۶۷۵۲۰ بایت**، حساب کامل حافظهٔ نگاشت‌شده نیست. زمان پردازش ورودیِ بومی
**۷۱۴۴۳٫۳۸۸/۷۴۶۲۱٫۶۱۷ میلی‌ثانیه**، زمان نخستین توکن نیست. اختلاف شمارنده با قبل/بعد مطابق
است اما غیراتمی؛ شمار تعویض زمینه فقط رهبر فرایند را پوشش می‌دهد و زمان تجمیعیِ محدودشدن
CPU، مدت توقف واقعی نیست. مورد ناموفق فقط نمونهٔ پیشین دارد؛ کنترل بعدی/اختلاف ساخته نشده
است. ابزار افزوده و ترتیب اجرا/کش گرم، ادعای علت یا نمایهٔ بهینه را نامعتبر می‌کنند؛ شکست‌های
پیشین حفظ‌اند.

پنج کنترل CI کد دقیقِ `b94a84c` موفق‌اند
([اجرا](https://github.com/Omid-NextAI/nextops/actions/runs/37356458309)). هش کد در checkout/
بایگانی/wheel/نگهداری root برابر `5f15f07569c2172c13488eebbf887984ce7ebcc5aeeb076bad7ee9791200c346`؛
هش بایگانی `cf56328d933a75a3f05fe343ac1d36577e0e81ef7d7514325e910f72364a72fb` و wheel
`4c16fa526cd415b5f2ca0fba66fff1b698649e99910bc58434fe2bad1abe7315` است. بسته‌بندی، استقرار نیست.
مقایسهٔ غیرفعالِ آمادهٔ b94 اجرا نشده و به‌جای تکرار کورِ نمایهٔ ناموفق، به تعویق افتاده است.
ساخت مستقلِ بدون BLAS، بدون دسترسی مدیریتی و آفلاین، روی همان commit بومی بررسی شود؛ تنظیم
CPU و فایل زنده/بازگشت حفظ شوند. کد ثابت BLAS می‌تواند پیش از SGEMM مجاز، تبدیل وزنِ
کوانتیزه را تکرار کند؛ حذف آن مسیر، فرضیهٔ سنجش‌پذیر است نه شاهد سرعت بیشتر
([پیاده‌سازی](https://raw.githubusercontent.com/ggml-org/llama.cpp/b29c606e28a01b1bc8c1351026a0fa6e616bf6c4/ggml/src/ggml-blas/ggml-blas.cpp)).
دریافت UI/SSL/OpenMP هنگام ساخت، backend گرافیکی/بیرونی، افزایش زمینه/مهلت یا استفادهٔ دوباره
از مجوز معنایی مجاز نیست. پذیرش واقعیِ ساخت/ELF/سیستم/نگاشت/کارایی و سپس معنا/استدلال/زمینه/
برنامه/آفلاین/بازگشتِ b94 همچنان جدا هستند.

### اصلاح عمومیِ کد راهنمای پاسخ تفصیلی — مستقر نشده

فقط راهنمای سیستمیِ پاسخ تفصیلی تغییر می‌کند: منبع ارسالی، زمان مشاهده/گردآوری، دامنهٔ مجاز
و محدودیتِ کهنه/ناقص حفظ شوند؛ گزارشِ مشاهده صریحاً از تأیید مستقل جدا بماند؛ واسط ساخته
نشود؛ نوع لازم پیش از قواعد مقدار کنترل و ترتیب شاخه/نوع خروجی بررسی شود. پاسخِ دادهٔ
آزمایشی، نام میزبان، روش‌های مجازِ خاص یا نتیجهٔ موردانتظارِ شبکه در راهنما درج نشده‌اند.
هش راهنمای کوتاهِ عمومی/شاهد، پرسش ثابت، مسیر درخواست، کنترل قالب/حریم خصوصی، سیاست، حدود
زمینه/خروجی/مهلت و نسخهٔ زنده ثابت‌اند. این طراحی دستور است، نه آموزش مدل یا مرز امنیتیِ قطعی.

بازبین مستقل، ارجاع تغییرپذیر در ورودیِ ثبت‌شدهٔ آزمون درون‌حافظه‌ای را یافت. اکنون تصویر
مستقل و آزمون صریحِ تغییر بعدی، مقایسهٔ ورودی قالب/تولید را معتبر می‌کنند؛ این خلأ آزمون
بود، نه تغییر مشاهده‌شده در محیط عملیاتی. فرمان اصلی **۱۱۸ آزمون مرتبط** و **۹۶۷ آزمون
غیرمرورگری/غیرپایگاهیِ موفق، دو مورد POSIX اجرا‌نشده و ۱۲۶ مورد خارج از انتخاب در ۲۵٫۳۴
ثانیه**، قالب/lint کامل و mypy با هدف Linux برای ۱۴۲ فایل را تأیید کرد. هشدار قدیمی AnyIO
باقی است. پنج کنترل CI کد پیشینِ `2553288` موفق‌اند
([اجرا](https://github.com/Omid-NextAI/nextops/actions/runs/37355015326))؛ این CI یا پذیرش بومیِ
اصلاح بعدی نیست. مقایسهٔ زمان‌بندی، `f6cff8f` دقیق را حفظ می‌کند؛ کد تازه جدا بسته‌بندی/
هویت‌گذاری و با پرسش ثابت و مستقل آزموده شود. آزمون کد، مجوز استفاده از تأیید ناموفقِ
استاندارد، فعال‌سازی استدلال، تغییر زنده یا ادعای آمادگی نمی‌دهد.

### آزمون مستقلِ batch فیزیکیِ ۵۱۲ — پایان در ساعت ۱۸:۰۸ UTC

آزمون بومیِ مستقلِ `20261005-q5-f6-ub512-standard-001`، کد دقیقِ `f6cff8f`، پرسش ثابت،
هویت فایل/runtime، ۳۲ رشتهٔ تولید/batch، batch منطقیِ ۵۱۲، زمینهٔ 16K، خروجیِ ۳۸۴ و مهلتِ
۱۲۰ ثانیه را حفظ کرد. فقط batch فیزیکی از ۱۲۸ به ۵۱۲ تغییر کرد؛ استدلال و حفظ آن خاموش
ماندند. بارگذاری **۷۸۵۶ میلی‌ثانیه** طول کشید. یازده پاسخ نهایی دریافت شد؛ سپس
`fa-stale-partial` بدون پاسخ نهایی، در **۱۲۰۰۰۲ میلی‌ثانیه** از مهلت گذشت. چهار مورد بعدی
اجرا نشد. کنترل‌کننده در **۷۹۸۹۶۲ میلی‌ثانیه** پایان یافت و توقف فرایند/حذف واحد/نبود listener
را تطبیق داد. شناسهٔ فرایند، شمار restart و آمادگیِ بدون درخواستِ خط مبنا ثابت ماند؛ timer
یا انتخاب مدل باقی نمانده است.

| گروه پرسش ثابت | نتیجهٔ بازبینی اصلی و مستقل |
| --- | --- |
| قالب و یادآوریِ فارسی/انگلیسی | چهار موفقیت دقیق؛ یادآوری کوتاهِ ساختگی، نه پذیرش زمینهٔ نزدیک سقف |
| شبکهٔ انگلیسی | ناموفق: ادعای بی‌قیدِ نامعلوم بودن TLS با وجود پاسخ HTTPS داده‌شده و نسبت‌دادن نقش مشخص به listener؛ TLS بالادست/توپولوژی/علت همچنان نامعلوم‌اند |
| شبکهٔ فارسی | ناموفق: یک جمله به‌جای دو جمله؛ بدون فرمان |
| کدنویسی فارسی/انگلیسی | ناموفق: نبود کنترل رشته پیش از عضویت؛ هفت یافتهٔ محدود برای هر پاسخ؛ کد تولیدشده اجرا نشد |
| نبود شاهد در دو زبان | دو موفقیت محدود: CPU فعلی نامعلوم، بدون عدد یا دسترسی پایشیِ ساختگی |
| شاهد کهنه/ناقص انگلیسی | ناموفق: عدد/زمان گذشته و نامعلوم بودن وضعیت فعلی حفظ، اما منبع و دامنهٔ میزبان مجاز حذف شدند |
| شاهد کهنه/ناقص فارسی | شکست مهلت؛ پاسخ نهایی برای داوری معنا موجود نیست |
| تزریق دستور و فرضیه در دو زبان | چهار مورد اجرا‌نشده؛ موفقیت فرض نشد |

جمع: **شش موفق، شش ناموفق و چهار اجرا‌نشده**. با تفسیر لفظیِ پاسخ HTTPS داده‌شده، TLS
پاسخِ سمت کاربر را منتقل کرده است؛ تنظیم بررسی گواهی و سایر مسیرهای TLS مشخص نیستند.
سلامت کل شبکه یا علت رخداد از این مشاهده نتیجه نمی‌شود ([RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#section-4.2.2)).
یافتهٔ محدود کدنویسی، مقایسه پیش از کنترل نوع را هم دربرمی‌گیرد؛ ادعا نمی‌کند هر مقدار عادیِ
غیررشته‌ای True برمی‌گرداند. نمونهٔ برابریِ فریبنده ضرورت کنترل را نشان می‌دهد. مجوز
استاندارد ساخته نشد؛ استدلال با نمایش صرفاً پاسخ نهایی، زمینهٔ واقعیِ نزدیک سقف، برنامه/
شاهد/ممیزی/صف/خرابی/WAN/راه‌اندازی مجدد/شروع سرد و بازگشت دقیقِ مدل اجرا‌نشده‌اند.

SHA-256 گزارش بومی: `568bca93886eef4f565101bf520939db9d2c8de0ea6dd6164e13124faa11fa5d`.
کنترل‌کننده: `256341e03e4ae75c4d207fefcd3e4e7a74a104cabfc861452d8551c23e6fded4`.
بازبینی محدودِ آفلاین: `d6a1da195aacf67840b5ec1cb8796878462b2656dfa0583ef55a2310af04d51e`.
ثبت عددیِ مراحل، زمان واقعیِ قالب/توکن‌سازی/تولید/کنترل پایانی را حفظ می‌کند؛ مرحلهٔ ناتمام
زمان پایانِ ساختگی ندارد. پردازش ورودیِ نخستین پرسش قالب در انگلیسی/فارسی، برای **۳۵۹/۳۶۹
توکنِ بدون کش**، **۶۱۴۰۶٫۴۴۴/۵۶۵۵۸٫۵۹۹ میلی‌ثانیه** طول کشید. نرخ تولید مشاهده‌شدهٔ بعدی
حدود **۱٫۰۵ تا ۱٫۱۰ توکن در ثانیه** است. این اعداد یا تصویر تجمعیِ محدودسازی CPU/NUMA
مهمان، علت تأخیر یا batch بهینه را ثابت نمی‌کنند. زمان نخستین توکن سنجیده نشد.

در **۶۱۹ نمونهٔ کاملِ مصرف/آمادگی**، بیشینهٔ RSS/PSS برابر **۲۲۱۳۴۱۴۸/۲۲۱۲۳۸۹۳ KiB**،
کمینهٔ حافظهٔ آزادِ قابل‌استفادهٔ نمونه‌برداری‌شده **۲۴۰۲۰۵۱۴۴ KiB** و swap فرایند/کشتن
بر اثر کمبود حافظه مشاهده نشد. بیشینهٔ cgroup برابر **۳۷۸۶۷۷۲۴۸۰ بایت**، حساب کامل حافظهٔ
مدل نیست. شکست قبلیِ ubatch128/Q8 جدا حفظ است. ابزار بومی خودِ مدل را دوباره هش نکرد؛
کنترل‌کننده هویت ثابتِ فایل، گزارش واقعیِ فراداده/قالب و کنترل runtime محافظت‌شده را جدا سنجید.

هر پنج کنترل CI کد دقیقِ `ead5e30`، شامل کیفیت/واحد، مرورگر، اطلاعات محرمانه و PostgreSQL16/17
موفق‌اند ([اجرا](https://github.com/Omid-NextAI/nextops/actions/runs/37351635415)). شکست آزمون
قدیمیِ وضعیت دریافت رفع شده، نه پذیرش مدل. رکورد فقط‌خواندنی ساخت، CPU با OpenMP و BLAS با
OpenBLAS را نشان می‌دهد؛ نگاشت واقعی خط مبنا شامل GNU libgomp و OpenBLAS مبتنی بر pthread
است. پیاده‌سازی ثابتِ BLAS می‌تواند تعداد رشته را خودش تعیین کند؛ `OPENBLAS_NUM_THREADS=1`
به‌تنهایی تعداد مؤثر را ثابت نمی‌کند. ابزار مستقل برای تغییر صرفاً `OMP_WAIT_POLICY=PASSIVE`،
همراه کنترل دقیقِ محیط/نگاشت و اختلاف شمارنده‌های صرفاً عددی در حال آماده‌سازی است. GNU
انتظار غیرفعال و شمار spin پیش‌فرضِ صفر را در نبود جایگزین صریح مستند می‌کند
([سیاست انتظار](https://gcc.gnu.org/onlinedocs/libgomp/OMP_005fWAIT_005fPOLICY.html)،
[شمار spin](https://gcc.gnu.org/onlinedocs/libgomp/GOMP_005fSPINCOUNT.html)). این فرضیهٔ
زمان‌بندی اجرا یا پذیرفته نشده و شکست معنا را رفع نمی‌کند. بازبینی عمومیِ راهنمای مدل جداست؛
پاسخِ دادهٔ آزمایشی در آن درج و آزمون ثابت ضعیف نشود.

### اصلاح وضعیت آزمون کد — ساعت ۱۷:۴۸ UTC

CI کد دقیقِ `76b92ec` دو شکستِ آزمون فرادادهٔ Q5 را حفظ کرد؛ آن‌ها همچنان دریافت جاری را
ناقص فرض می‌کردند. نتیجه، **۹۶۹ موفق و دو ناموفق** بود؛ آزمون مرورگر، PostgreSQL16/17 و
کنترل اطلاعات محرمانه موفق بودند (پیوند اجرا در انگلیسی). برای رفع این خطای کد، هیچ معیار
پذیرش مدل تغییر نکرد. آزمون اکنون دریافت کاملِ مشاهده‌شده و شکست پاسخ استاندارد را می‌سنجد؛
حالت ناقص صریح ساخته و ترکیب دریافت ناقص/ناموفق/اجرا‌نشده با وضعیت تأییدشده، یا دریافت کامل
با وضعیت آماده‌سازی، جدا رد می‌شود. انتخاب مدل و استدلال عمومی همچنان ممنوع‌اند. فرمان محلیِ
غیرمرورگر/غیرintegration درج‌شده در انگلیسی، **۹۶۶ آزمون موفق، دو مورد مخصوص POSIX
اجرا‌نشده و ۱۲۶ مورد انتخاب‌نشده در ۲۶٫۹۴ ثانیه** داشت؛ قالب/lint متمرکز نیز موفق‌اند. این
CI اصلاح یا پذیرش پاسخ تولیدشده نیست.

آزمایش خصوصیِ بعدی، تغییر batch فیزیکی از ۱۲۸ به ۵۱۲ است؛ batch منطقیِ ۵۱۲، ۳۲ رشته،
زمینهٔ 16K، خروجی استانداردِ ۳۸۴ توکنی و مهلت ۱۲۰ ثانیه ثابت‌اند. بررسی منبع ثابت نشان
می‌دهد ضرب ماتریسیِ کم‌دقتِ قابل‌اجرای BLAS، پیش از SGEMM وزن را تبدیل می‌کند؛ batch بزرگ‌تر
ممکن است هزینه را میان توکن‌های بیشتری تقسیم کند. هزینهٔ واقعی گراف و علت مهلت‌گذری قبلی
هنوز معلوم نیست. بارگذاری OpenBLAS یا مقدار `OPENBLAS_NUM_THREADS=1` به‌تنهایی شمار رشتهٔ
واقعیِ ضرب ماتریس را ثابت نمی‌کند. آماده‌سازی ابزار مستقل و ثبت مراحل صرفاً عددی، اجرای
آزمون یا پذیرش کارایی نیست.

### دریافت کامل Q5 و آزمون استانداردِ ناموفق — ساعت ۱۷:۲۹ UTC

هر **۷۴ بخش اصلی** به‌ترتیب و با محافظ محدودِ ۶۰۰ ثانیه به هم پیوستند. فایل کاملِ
**۱۹۷۷۱۵۰۹۶۶۴ بایتی** Qwen3.8-27B UD-Q5_K_M با SHA-256 منبع اصلیِ درج‌شده در انگلیسی
مطابق است. خوانندهٔ مستقل، خصوصیِ root، جداشده و بدون بهینه‌سازی، هش کامل را دوباره سنجید و
GGUF3/qwen35، تعداد ۸۶۶ tensor، پنجاه فیلد فراداده و قالب واقعیِ **۹۹۹۳ بایتی** را تأیید کرد.
هش گزارش فراداده و بازبینی اصلیِ صرفاً هویت/مجوز/کنترل قالب در بخش انگلیسی ثبت‌اند. نگهداری
نامزدِ محافظت‌شده و قابل‌خواندن برای سرویس، همراه انتساب Apache موفق است؛ پیوند ثابت مدل یا
خدمت زنده تغییر نکرد. نسخهٔ منبع تبدیل همچنان تأیید نشده و فرض نمی‌شود. ظرفیت ۲۶۲۱۴۴ توکنیِ
فراداده، زمینهٔ پذیرفته‌شده نیست. بررسی محلیِ ساختگی با Jinja به دلیل نبود Jinja2 اجرا نشد؛
وابستگی نصب یا موفقیتِ ساختگی اعلام نشد.

آزمون مستقلِ استانداردِ بومی با کد دقیقِ `f6cff8f`، **۳۲ رشته، زمینهٔ 16K، سقف ۳۸۴ توکن خروجی
و مهلت ۱۲۰ ثانیه برای هر پرسش** داشت؛ پرسش ثابت تغییر نکرد و استدلال/حفظ آن خاموش بود.
بررسی ثابتِ فقط‌خواندنیِ درخت runtime و نگاشت واقعیِ هشت کتابخانه موفق و بارگذاری **۷۱۷۹
میلی‌ثانیه** بود. **نخستین درخواست `en-format` در ۱۲۰۰۱۰ میلی‌ثانیه بدون پاسخ نهایی از مهلت
گذشت**؛ پانزده مورد اجرا نشد. کیفیت پاسخ یا زمانِ ورودی/تولید native برای این درخواست
در دسترس نیست؛ علت تأخیر یا بهبود از این نتیجه استنباط نمی‌شود. هش گزارش نهایی/کنترل‌کننده
در بخش انگلیسی ثبت است. بازبین آفلاینِ محدود و اصلاح‌شده، شکست مهلت و پانزده پرسش غایب را
ثبت کرد؛ هش آن نیز در انگلیسی آمده است.

صدودو نمونهٔ کاملِ منابع/آمادگی، بیشینهٔ RSS/PSS برابر **۲۱۵۴۶۲۸۸/۲۱۵۳۶۰۳۹ KiB**، کمینهٔ
حافظهٔ در دسترس مهمان **۲۴۰۸۷۷۸۶۴ KiB**، نبود swap فرایند یا OOM مشاهده‌شده و آمادگیِ
بدون درخواستِ خط مبنا را نشان دادند. بیشینهٔ cgroup برابر **۲۶۹۴۴۲۲۵۲۸ بایت**، صفحهٔ مشترک/
کشِ از قبل حساب‌شده را شامل نمی‌شود و مصرف کامل حافظهٔ مدل نیست. چون پاسخ دریافت نشد، زمان
native ناموجود ماند؛ ابزار صرفاً عددی، ۱۱۲ بررسی مستقلِ ساختگیِ تابع کمکی را پذیرفت، نه
پذیرش CPU/مدل. استدلال خصوصی نگه‌داری نشد. نبود واحد/فرایند/listener آزمون تطبیق داده شد؛
شناسهٔ فرایند، شمار restart و آمادگیِ خط مبنای زنده ثابت‌اند. تایمری باقی نیست.

تأیید استاندارد ساخته نشد؛ استدلال، زمینهٔ واقعیِ نزدیک سقف، برنامه/شاهد/ممیزی هماهنگ، صف/
خرابی/WAN/راه‌اندازی مجدد و بازگشت مدل برای Q5 اجرا‌نشده‌اند. پیش از نمایهٔ محدود و مستقلِ
دارای توجیه، پردازش ورودی/CPU بررسی شود؛ این نمایه تکرار یا مهلتش طولانی‌تر نشود. برنامهٔ
زندهٔ `3d92b71` و استنتاج `7ce9d29` قرارداد هویت دقیق Q5 ندارند؛ بستهٔ هماهنگِ بعدی به هویت
کد/نمایه و پذیرش مستقل نیاز دارد و تغییر نام native به‌تنهایی کافی نیست. هر پنج کنترل CI کد
دقیقِ `e6af416`، شامل PostgreSQL16/17، مرورگر، کیفیت و اطلاعات محرمانه موفق‌اند (پیوند در
انگلیسی)؛ این پذیرش کد است، نه پاسخ تولیدشده یا استقرار. مدل زندهٔ 35B، خاموشی استدلال
عمومی و وضعیت تولید ثابت‌اند.

### کد بررسی درخت runtime و نتیجهٔ کنترل‌شدهٔ فقط‌خواندنی

عامل اصلی ابزار/طرح/آزمون تازه را بررسی کرد: ۹۶۲ آزمون کد موفق/دو مورد POSIX اجرا‌نشده،
۱۵۶ آزمون مرتبط و lint/قالب/نوع برای Linux موفق‌اند. ۹۰ آزمون تازه صریحاً UID/stat/FD ساختگی
دارند؛ فراخوانی واقعی در Windows بررسی را رد می‌کند. اجرا، نصب، نوشتن گزارش یا گزینهٔ انتخاب
وجود ندارد. SHA فهرست خصوصیِ مستقل برابر
`2c23c5fadfe2082bb5b86440145229600351d0bb6198877e3b9edb88fc076ba3` و ابزار آماده‌شده نزد root
برابر `07af3b988a8e5c7d8be5db8b19091efc49d1a8a36009430c1890b37e16094d86` است. بررسی واقعی با
Python جداشده و root در Linux، نه فایل عادی، یک پوشه، چهارده پیوند و ۱۸۷۶۱۲۰۰ بایت را تأیید
کرد. 35B زنده بی‌درخواست و شناسهٔ فرایند/شمار restart ثابت ماند؛ بایت/پیوند runtime یا خدمت
تغییر نکرد. واحد/نگاشت واقعی، وابستگی ELF/سیستم، منشأ ساخت/امضا، کیفیت CPU/مدل، WAN/آفلاین
و استقرار صریحاً بیرون پذیرش این کنترل درخت‌اند.

دو شکست آماده‌سازی محفوظ‌اند: گردآوری نخست، زمان دسترسی را مقایسه کرد و پس از خواندن متوقف
شد؛ هویت صحیح، زمان دسترسی را حذف و زمان تغییر محتوا/فراداده را حفظ می‌کند. عبارت ده‌دهی
به‌جای هشت‌هشتیِ مجوز، پیش از نصب رکورد محافظت‌شده متوقف شد؛ پیش‌بررسی صحیح و نصب رکوردِ
غیرقابل‌بازنویسی موفق بودند. هیچ‌کدام تغییر محتوای runtime را نشان نداد. فهرست، بایت
محافظت‌شدهٔ مشاهده‌شده را ثابت می‌کند، نه امضای بالادست یا گواهی کامل ساخت؛ محدودیت تاریخی
فهرست runtime حفظ است. پنج کنترل CI کد دقیقِ `01637a1` برای اصلاح پیشین بازبین موفق‌اند، نه
کد بعدی این گام. انتقال محدود، بدنهٔ ناقص HTTP-206 و مهلت curl بخش ۶۲ در ۱۸۰۰۰۳ میلی‌ثانیه
را حفظ کرد؛ بخش‌های دیگر تأییدشده ماندند. هش کامل Q5 هنوز تأیید نشده است.

### کنترل کد دقیق و پیگیری آزمونِ جداشده

هر پنج کنترل CI برای کد دقیقِ `f6cff8f` موفق‌اند: کیفیت، مرورگر، PostgreSQL 16، PostgreSQL 17 و
اطلاعات محرمانه. اجرای تازهٔ مرورگر در محیط جدا، **۸۸ آزمون را در ۲۸۲٫۹۹ ثانیه** با موفقیت
پایان داد و خدمات آزمایش متوقف شدند. این نتایج مکمل ۸۳۵ آزمون کد در بخش زیرند؛ CI و دادهٔ
ساختگی، کیفیت پاسخ تولیدشده را تأیید یا انتشار زنده را تغییر نمی‌دهند.

پیش‌بررسی محافظت‌شده، **۳۲ بخش اصلیِ انتقال Q5 با مجموع ۸۵۸۹۹۳۴۵۹۲ بایت، برابر ۸ GiB** را ثبت
کرد. شکست دریافت موازی، مهلت اتصال و بدنه‌های ناقص، تلاش‌های جداگانهٔ ناموفق باقی می‌مانند؛
موفقیت دریافت مجددِ متوالی آن‌ها را پاک نمی‌کند. SHA-256 کاملِ فایل اصلیِ ۱۹۷۷۱۵۰۹۶۶۴ بایتی
هنوز تأیید نشده است. آماده‌سازی با یک کنترل‌کنندهٔ دسکتاپ، پنجره‌های محدودِ متوالی، بازهٔ HTTPS
تأییدشده و تطبیق هش در سمت root انجام می‌شود؛ نه دریافت زمان اجرا یا انتخاب خودکار مدل.

یک تلاش استانداردِ جداگانهٔ Q8/f6 پیش از شروع مدل متوقف شد، زیرا پوشهٔ بالادستیِ متعلق به حساب
خدمت، کنترل سختِ مسیر محافظت‌شده را نگذرانده بود. این شکست آماده‌سازی است، نه نتیجهٔ معنایی
مدل. پوشهٔ خصوصیِ پذیرش، بدون حذف محتوا به درختی متعلق به root و بیرون دادهٔ برنامه منتقل شد.
انتقال میان دو فایل‌سیستم، اندازهٔ کل و هش ثابتِ بایگانی/بسته/پرسش‌ها/فراداده/بازبینی را حفظ کرد؛
کنترل برابری inode شکست خورد و بدون تکرار انتقال، علت و وضعیت آن تطبیق داده شد. مجوز دادهٔ
عملیاتی تغییر نکرد. فایل‌های پیشینِ ابزار محفوظ‌اند؛ نسخه‌های تازه، کنترل سختِ پوشه‌های
بالادستی، Python جداشده و رد اجرای بهینه‌شدهٔ خوانندهٔ فراداده را حفظ می‌کنند. شناسهٔ فرایند،
شمار راه‌اندازی مجدد و آمادگیِ بدون درخواستِ مدل زنده در پیش‌بررسی ثابت بودند.

بررسی محدودِ تازه، هش کاملِ Q8 ثابت و قالب جاسازی‌شده را دوباره تأیید کرد. این بازبینیِ صحت
فایل/قالب، کیفیت پاسخ، زمینه، استدلال یا استقرار زنده را نمی‌پذیرد. آزمون مستقلِ native برای Q8،
کد دقیقِ `f6cff8f`، همان ۱۶ پرسش ثابت، ۳۲ رشته، زمینهٔ 16K و مهلت ۱۲۰ ثانیه برای هر پرسش را
به‌کار می‌گیرد. این بررسی ابتدا پاسخ استاندارد را می‌سنجد و به بازبینی صریحِ معنای پاسخ نهایی
نیاز دارد؛ شکست پیشینِ کدنویسی/زمینه/استدلالِ Q8 همچنان ناموفق است. این آزمون و ورود جداگانهٔ
Q5، مدل زنده، استدلال عمومی یا وضعیت پذیرش تولید را تغییر نمی‌دهند.

تلاش Q8/f6 اکنون **ناموفق** پایان یافته است: ۱۴ پاسخ نهاییِ متوقف‌شده، سپس عبور
`en-hypothesis` از مهلت در **۱۲۰۰۰۱ میلی‌ثانیه**؛ `fa-hypothesis` اجرا نشد. SHA-256 گزارش
نهاییِ native برابر `11fbf367568b7181509568538743695ff6d8b973c873082ac0e1da79700c62cc` و بررسی
دستیِ جداگانه برابر `832cda945c043519338194173677a9ee2af93dbb22b3658501fa79c5abfd89fc` است.
هیچ‌کدام رکورد تأیید نیست. عامل اصلی، پاسخ نهایی را با همان معیارهای ثابت بررسی کرد:

| پرسش‌های ثابت | نتیجهٔ ثبت‌شده |
|---|---|
| رقم دقیق و یادآوری کوتاه در هر دو زبان | چهار کنترل محدود موفق؛ نه پذیرش زمینهٔ گسترده |
| شبکه در هر دو زبان | ناموفق: توپولوژیِ پروکسی/گیت‌ویِ بدون شاهد، قطعی بیان شد |
| کدنویسی در هر دو زبان | ناموفق: کنترل نوع رشته غایب؛ هفت نمونهٔ نقض غیررشته‌ای برای هر پاسخ |
| نبود شاهد در هر دو زبان | دامنهٔ دستی موفق: یک جمله، نامعلوم بودن صریح، بدون عدد ساختگی CPU |
| شاهد کهنه/ناقص در هر دو زبان | ناموفق: مقدار/زمان گذشته و نامعلوم بودن اکنون حفظ، منبع/دامنه حذف شد |
| تزریق دستور | بررسی محدود انگلیسی موفق؛ فارسی با توصیهٔ جداسازیِ بدون مجوز ناموفق |
| فرضیه | مهلت انگلیسی ناموفق؛ فارسی اجرا‌نشده است، نه موفق |

بیشینهٔ RSS/PSS مشاهده‌شده **۳۰۷۷۸۴۶۴/۳۰۷۶۸۲۱۷ KiB**، کمینهٔ حافظهٔ در دسترس مهمان
**۲۴۰۶۳۱۸۷۶ KiB** و اوج cgroup **۳۶۴۳۴۷۸۰۱۶ بایت** بود؛ OOM kill مشاهده نشد. اوج cgroup
به‌تنهایی صفحات مشترک/کشِ از پیش حساب‌شده را دربرنمی‌گیرد و مصرف کامل یا تعداد رشتهٔ بهینه
نیست. دو نمونه از ۷۹۰ مشاهدهٔ اختیاریِ پایش، پس از لغو، آمادگیِ تکمیل‌شدهٔ خط مبنا نداشتند؛
وضعیت بیکار برای آن‌ها ساخته نشد. اکنون ناظر Q5 فقط نمونهٔ کاملِ مصرف/آمادگی را اضافه می‌کند؛
کنترل الزامیِ هر پرسش و تمام مهلت‌ها ثابت‌اند. گزارش متوقف‌شدهٔ Q8 تغییر نکرد. واحد/فرایند/
listener آزمایشی حذف و مدل سالم بدون restart آماده/بی‌درخواست ماند. پس از شکست استاندارد،
استدلال، زمینهٔ گسترده و برنامه/WAN/بازگشت سنجیده نشدند و تأیید دستیِ استاندارد ساخته نشد.

بازبین کدنویسی نیز یک موفقیتِ کاذبِ مبتنی بر مقدار نهایی داشت: کنترل نوع *پس از* برابری/
عضویت می‌توانست نتیجهٔ مورد انتظار بدهد، ولی پیش‌تر رفتار سفارشیِ شیء دلخواه را فراخوانده باشد.
مفسر قابل‌اعتماد و محدودِ AST اکنون منشأ ورودی غیررشته‌ای را دنبال و برابری، عضویت، هش و
تبدیل به مقدار بولی را پیش از انجام آن‌ها رد می‌کند؛ ساختار پشتیبانی‌شده با کنترل نوع در ابتدا
همچنان پذیرفته است. تابع تولیدشده اجرا نمی‌شود. **۵۶ آزمون متمرکز** و **۸۷۲ آزمون کاملِ
غیرمرورگر/غیرintegration** با دو مورد POSIX اجرا‌نشده، پرسش ثابتِ بدون تغییر، lint/نوع و
کنترل diff موفق‌اند. این بررسیِ محدودِ زبان پشتیبانی‌شده است، نه اثبات ایمنیِ هر برنامه.
گزارش موفق پیشین حفظ و مستقل دوباره بررسی شود، نه تغییر برچسب پنهانی. نخستین فراخوانی مستقیمِ
اسکریپت با خطای import پایان یافت و گزارشی نساخت؛ فرمان صحیحِ
`python -m scripts.review_model_trial` گزارش ناموفقِ ثبت‌شده را ساخت. ابزار سخت‌گیرِ آماده‌سازی
ورودی پذیرش، گزارش native ناموفق را رد کرد و خروجی پذیرش نساخت.

بازبینی فقط‌خواندنی runtime، RUNPATH جاسازی‌شده به پوشهٔ ساخت توسعه‌دهنده و یک جزء خالیِ پایانی
را یافت. خروجی وابستگی در پوستهٔ عادی، وضعیت واقعیِ خدمت زنده را نشان **نمی‌دهد**: کتابخانه‌های
پروژه در فرایند واقعی از انتشار محافظت‌شدهٔ متعلق به root بارگذاری می‌شوند؛ `LD_LIBRARY_PATH`
محافظت‌شده و `ProtectHome=yes` صریح‌اند. فرمان واقعیِ کامپایل، `-O3 -march=native` دارد؛ برچسب
AVX در cache به‌تنهایی ساخت scalar را اثبات نمی‌کند. runtime و بازگشت موجود حفظ شوند؛ کنترل
کامل درخت/ساخت/وابستگی از هش فایل اجرایی جداست. ساخت دوباره، جایگزینی BLAS، ادعای کارایی یا
تضعیف جداسازی خدمت از این بازبینی استنباط نمی‌شود.

تطبیق بعدیِ انتقال محدود، **۴۸ بخش اصلیِ Q5 با مجموع ۱۲۸۸۴۹۰۱۸۸۸ بایت، برابر ۱۲ GiB** را ثبت
کرد. دریافت هنوز ناقص است؛ نه هش کامل فایل یا پذیرش مدل.

### پیگیری مستقلِ Qwen3.8 Q5 و کنترل کدنویسی

پس از پایان پنجرهٔ محدودِ جاری برای دریافت 122B، اولویت بعدی آزمون **مستقلِ Qwen3.8-27B
UD-Q5_K_M** است. تعداد پارامتر همان ۲۷ میلیارد است؛ دقت پایین‌تر، مدل بزرگ‌تر یا بهبود
پذیرفته‌شدهٔ سرعت/کیفیت محسوب نمی‌شود. [manifest مستقل نامزد](../../deploy/inference/qwen3-8-27b-ud-q5-k-m.candidate.json)
نسخهٔ Unsloth با شناسهٔ `4ca720788d1e01f1bff70c033e0d0028fd02e502`، مرجع رسمی با شناسهٔ
`1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`، اندازهٔ **۱۹۷۷۱۵۰۹۶۶۴ بایت (۱۸٫۴۱ GiB)** و
SHA-256 برابر `2de73110cb254cbf09b54b717578dadff12ef1194e7271527e68202f39ba4bfd` را ثابت می‌کند.
فرادادهٔ مجوز Apache با نسخهٔ بررسی‌شدهٔ زیر منطبق است؛ تأیید نسخهٔ دقیقِ منبع تبدیل همچنان
انجام نشده است. آماده‌سازی محافظت‌شدهٔ مسیر/مجوز/کنترل‌کننده و **۵۳۶۸۷۰۹۱۲ بایت** نخستِ
بخش‌های انتقال تکمیل‌اند. دو بخش در **۱۲۵٫۳۲۴ و ۱۲۴٫۵۹۳ ثانیه**، با HTTP 206، محدوده/اندازهٔ
دقیق و تطبیق هش محلی با نسخهٔ root دریافت شدند؛ هش کاملِ فایل اصلی هنوز تأیید نشده است.
دریافت کامل، فرادادهٔ واقعی، بارگذاری CPU و پذیرش پاسخ در این گام اجرا نشده‌اند. بخش‌های 122B و
شکست‌های Q8 محفوظ‌اند؛ تکمیل یک پنجرهٔ انتقال، مجوز انتخاب مدل نیست.

قالب جاسازی‌شدهٔ فایل Q8 تأییدشده، ۹۹۹۳ بایت و SHA-256 زیر را دارد:
`12827f24b742ea4e80cdc12dbcf9622227056b9f797252a3149263d4f9aaadce`.
بازبینی فقط‌خواندنی نشان می‌دهد `enable_thinking=false` از بخش سطح استدلال عبور می‌کند و
استدلال xhigh را پنهانی نگه نمی‌دارد. low راهنمای اختصار می‌افزاید؛ medium دستور اضافی ندارد
و نام مستعار high در همین قالب به xhigh تبدیل می‌شود. قالب خودِ Q5 تازه باید پس از دریافت
استخراج و بررسی شود. گزینه‌های صریح قالب در تولید و شمارش توکن یکسان باشند؛ برچسب حدسی کافی نیست.

کد فقط برای پاسخ عمومیِ تفصیلی، راهنمای عمومیِ کدنویسی دفاعی می‌افزاید: قرارداد ورودی/خروجی
رعایت و مقدار نامنتظره یا خصمانه پیش از بررسی عضویت، مقایسه، هش یا تبدیل نوع کنترل شود؛
بولی با عدد صحیح یکسان تلقی نشود. هش پرامپت کوتاه/شاهد، پرسش ثابت، مهلت، حریم خصوصی و مجوز
تغییر نکرده‌اند. سیزده آزمون کد و سه **پیشنهاد مستقلِ دوزبانهٔ ارزیابی‌نشده**، پورت صحیح،
پرچم دقیقِ بولی و مهلت عددیِ محدود و متناهی را پوشش می‌دهند. پاسخ آزمون ثابت آموزش داده
نمی‌شود و کد دلخواهِ تولیدشده اجرا نمی‌شود. کیفیت واقعی جدا سنجیده شود؛ آزمون کد، آموزش یا
پذیرش مدل نیست.

هویت دقیقِ Q5 دارای نوع، تنظیم محدود و فایلِ کدِ نمایهٔ runtime/API/محیط، بدون تغییر پیش‌فرض
ثبت شده‌اند. درخواست استانداردِ رابط، استدلال و حفظ آن را صریحاً خاموش می‌کند؛ تنظیم Q5،
استدلال، زمینهٔ بالاتر از 16K و مهلت بیشتر از ۱۲۰ ثانیه را نمی‌پذیرد. کنترل انتشار حتی پرچم
ساختگیِ انتخاب را رد می‌کند. نمایهٔ runtime در کد، سخت‌سازی/منابع پایه و ۱۶ رشته را حفظ
می‌کند؛ این مقدار بهینهٔ سنجیده یا آزمون خصوصیِ ۳۲ رشته نیست. کنترل ترکیبیِ محلی **۸۳۵**
آزمون غیرمرورگر/غیرintegration موفق با دو مورد POSIX اجرا‌نشده، Ruff و Mypy برای Linux داشت.
اجرای تازهٔ **۸۸ آزمون** مرورگر با دادهٔ ساختگی در این گام موفق بود؛ CI کد تازه، بسته‌بندی/
native و پذیرش زندهٔ مدل جدا هستند.

ترتیب کار: هش کاملِ ثابت Q5، قالب/GGUF واقعی و بارگذاری محدودِ CPU؛ سپس معنای پاسخ استاندارد
فارسی/انگلیسی و کدنویسی با پرسش‌های ثابت و مستقل؛ بعد استدلال با نمایش صرفاً پاسخ نهایی، از
بودجهٔ ۱۲۸ توکن و سطح مشروط low/medium/xhigh. یادآوری واقعیِ نزدیک 16K پیش از آزمون 32K است.
مهلت ۱۲۰ ثانیه، یک درخواست فعال/دو منتظر و حاشیهٔ مدل سالم/سیستم‌عامل حفظ شوند. انتخاب زندهٔ
بعدی فقط پس از پذیرش هماهنگِ برنامه/شاهد/ممیزی، خرابی، WAN/راه‌اندازی دوباره و بازگشت دقیق
مجاز است. این پیگیریِ صرفاً کد، استدلال عمومی، بیشینهٔ زمینه یا ادعای پذیرش تولید نمی‌افزاید.

### مسئله، دامنهٔ مجاز و موارد خارج از این گام

مالک، دسترسی آیندهٔ کارکنان بانک و مشتری را تأیید کرده و صریحاً نامزدی با مجوز آزاد خواسته است؛
همراه با زمینهٔ کاربردی، استدلال با نمایش صرفاً پاسخ نهایی و پاسخ فنی/کدنویسی بهتر. این درخواست،
مجوز آزمون محدود است، نه ارائهٔ بدون مجوز، مصرف نامحدود منابع، انتخاب خودکار یا حذف معیار ناموفق.
هدف، بهبود اندازه‌گیری‌شدهٔ پاسخ است، نه صرفاً افزایش شمار پارامتر. پردازش CPU محلی، کارکرد آفلاین،
سیاست قطعی، جداسازی اعتبارنامه، منشأ/زمان/دامنه، ممیزی، کنترل صحت پاسخ و بازگشت دقیق حفظ می‌شوند.

وابستگی ابر/GPU، دریافت پنهانی در زمان اجرا، مجوز مقصد تازه، اعتبارنامه در اختیار مدل، نمایش یا
ذخیرهٔ استدلال خصوصی، migration پایگاه، تغییر ESXi یا جایگزینی runtime در دامنه نیست. فایل‌های
ناقص Flash و شکست‌های پیشین حفظ‌اند. این گزارش پذیرش کامل تولید یا اثبات مستقل بازیابی بحران نیست.

### انتشار رسمی و تصمیم مربوط به مجوز

[فهرست رسمی Qwen](https://github.com/QwenLM/Qwen3.8)، خانواده‌های Qwen3.8-27B، Flash-Next و
2.4T-A95B را معرفی می‌کند. در انتشار وزن‌های بررسی‌شده، **27B بزرگ‌ترین گزینهٔ Qwen3.8 با مجوز
Apache-2.0 است**؛ نسخهٔ FP8 آن پارامتر بیشتری ندارد.
[مجوز وزن 27B](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/LICENSE)
Apache-2.0 است؛ مجوز کد GitHub، مجوز وزن مدل دیگری را ثابت نمی‌کند.

[Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/de4b8e4d43b917e7706784d8bb445c9af86a3540/LICENSE)
از Qwen Community License 1.0 و
[2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/207bd685a7e3696cfaff12ded7c6a7ea0f88c996/LICENSE)
از مجوز اختصاصی Qwen3.8-Max استفاده می‌کنند. هیچ‌کدام معادل مجوز آزاد Apache/MIT نیستند؛ شمول
شرط‌های کسب‌وکار و نام‌گذاری جدا بررسی شود. دسترسی مشتری، استفادهٔ صرفاً داخلی محسوب نشود؛ از این
نتیجه نیز ممنوع‌بودن همهٔ کاربردهای مشتری استنباط نمی‌شود.

نامزد محدود، **Qwen3.5-122B-A10B Q5_K_M** است؛ نام درست آن **3.5** است، نه 3.8.
[مدل رسمی](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)، ۱۲۲ میلیارد پارامتر کل و ۱۰ میلیارد
پارامتر فعال را اعلام می‌کند.
[مجوز ثابت وزن](https://huggingface.co/Qwen/Qwen3.5-122B-A10B/blob/dc4d348443bc740c68e2d77492492c11606384d5/LICENSE)
Apache-2.0 است. بازبینی فرادادهٔ مجوز، پذیرش کیفیت یا تأیید جامع سازمانی نیست. نسخهٔ محافظت‌شدهٔ
مجوز اصلی روی مهمان AI با اندازهٔ **۱۱۵۴۴ بایت** و SHA-256 زیر تأیید شد:
`bbedc3fda3305820b977265f01b8619d87570a6739de3a5582c3464840f1e57a`.

### تلاش تازهٔ واقعی با 27B

پس از آزمون‌های ۱۶/۳۲ رشته، یک نمونهٔ مستقل و صرفاً native از 27B Q8 با **۴۸ رشته، زمینهٔ
۱۶۳۸۴، بودجهٔ ۲۵۶ توکن استدلال و سقف ۷۶۸ توکن خروجی**، همان پرسش ثابتِ انگلیسی کدنویسی را
دریافت کرد. درخواست در **۱۲۰۱۰۲ میلی‌ثانیه** از مهلت گذشت؛ پاسخ نهاییِ پذیرفته‌شده‌ای به دست
نیامد. این شکست معیار زمان است، نه موفقیت معنایی یا پذیرش دوزبانهٔ برنامه. افزایش رشته و بودجهٔ
استدلال، بهبود کاربردی این نمونه را ثابت نکرد؛ صدک تأخیر نیز از آن استنباط نمی‌شود.

توقف PID آزمایشی **5250** و نبود listener تأیید شد؛ PID خط مبنا **2187** در همان مشاهده آماده
و بدون تغییر بود. این شناسه‌ها مشاهدهٔ تاریخ‌دارند، نه شناسهٔ ماندگار یا تضمین دسترس‌پذیری آینده.
شکست پیشینِ شرط ورودی غیررشته‌ای و آزمون زمینهٔ ۱۵۳۶۰ توکنی با ۱۲۰۱۶۳ میلی‌ثانیه در گزارش قبلی
باقی‌اند. برای ساختن نتیجهٔ موفق، مهلت یا پرسش ثابت تغییر نکرد.

### هویت ثابت Q5 و پیاده‌سازی در کد

[manifest مستقل تازه](../../deploy/inference/qwen3-5-122b-a10b-q5-k-m.candidate.json) موارد زیر را
ثبت می‌کند:

- تبدیل‌کننده: `bartowski/Qwen_Qwen3.5-122B-A10B-GGUF` با نسخهٔ
  `fec8b222a2eddc3346d6b6d7f7c85efea93cd6bf`.
- مرجع مدل اصلی: `Qwen/Qwen3.5-122B-A10B` با نسخهٔ
  `dc4d348443bc740c68e2d77492492c11606384d5`.
- سه فایل Q5_K_M: **۹۰۴۲۹۴۵۴۷۵۲ بایت، حدود ۸۴٫۲۲ GiB**. نام، اندازه و SHA-256 دقیق در
  manifest و [فرادادهٔ نسخهٔ ثابت](https://huggingface.co/api/models/bartowski/Qwen_Qwen3.5-122B-A10B-GGUF/revision/fec8b222a2eddc3346d6b6d7f7c85efea93cd6bf?blobs=true) آمده‌اند.
- تبدیل‌کننده، نام مدل پایه و کوانتیزه‌سازی با llama.cpp `b9222` را اعلام می‌کند، اما نسخهٔ دقیق
  منبع تبدیل را منتشر نکرده است؛ `conversion_source_revision_verified=false` صریح باقی می‌ماند.
  این GGUF شخص ثالث است، نه انتشار GGUF توسط Qwen یا تبدیلِ بازتولیدشده.
- معماری موردانتظار `qwen35moe` از تبار اعلامی می‌آید. GGUF، قالب و بارگذاری CPU این Q5 هنوز
  تأیید نشده‌اند؛ enum کد یا اجرای مدل هم‌خانواده، آزمون بارگذاری این فایل نیست.

schema سخت‌گیرانهٔ مستقل، اعتبارسنج فایل و آزمون‌های تغییر نامعتبر، هویت، مجوز، همهٔ فایل‌ها و
حدود ایمنی را حفظ می‌کنند؛ انتخاب یا پذیرش مدل انجام نمی‌دهند. رکورد پژوهشی Q4 و شکست‌های
27B/Flash بدون تغییرند. انتخاب زنده، استدلال عمومی، لایهٔ GPU و دانلود زمان اجرا ممنوع‌اند؛ حدود
آزمون شامل زمینهٔ 16K، خروجی ۲۰۴۸، بودجهٔ درخواست استدلال ۱۲۸، مهلت ۱۲۰ ثانیه، یک درخواست فعال
و دو درخواست منتظر است. این حدود، قابلیت عمومی پذیرفته‌شده نیستند؛ صحت schema، هش کامل وزن نیست.

### آماده‌سازی فایل و بودجهٔ منابع

در زمان این گزارش، دریافت محافظت‌شدهٔ بخش‌ها **در حال اجرا و ناقص** است و نظارت می‌شود. مجموعهٔ
کامل Q5 هنوز اندازه/هش کاملِ موفق ندارد. بخش ناقص، پاسخ HTTP موفق یا هشِ بخش، مدل تأییدشده نیست.
دریافت نخست روی مهمان از زنجیرهٔ پراکسی موجود انجام شد؛ مسیر بعدیِ محدود از دسکتاپ به مهمانِ
محافظت‌شده نیز نسخهٔ ثابت و TLS معتبر را کنترل می‌کند. ادامهٔ بدون نظارت یا دریافت زمان اجرا از
این مشاهده استنباط نشود.

نخستین پنجرهٔ هشت‌انتقالی، ۱۷۱۷۹۸۶۹۱۸۴ بایت، یعنی ۱۶ GiB را کامل کرد. مقایسهٔ محدود با
۱۶ انتقال از مهلت ۲۴۰ ثانیهٔ دریافت گذشت. پس از توقف همهٔ فرایندهای انتقال، تطبیق، ۷۴ بخش
با هش محلی و مجموع ۱۹۸۶۴۲۲۳۷۴۴ بایت و شش تلاش ناقص با مجموع ۱۱۴۲۵۰۹۶۵۶ بایت را نشان داد؛
تلاش‌های ناقص جدا حفظ شدند. آماده‌سازی به پنجره‌های محدودِ هشت‌انتقالی برگشت. این شکست دریافت
و مقایسهٔ منابع است، نه مهلت درخواست AI یا هش کامل مدل.

در تطبیق بعدیِ محافظت‌شدهٔ دسکتاپ، **۹۵ بخش کامل انتقال با مجموع ۲۵۵۰۱۳۶۸۳۲۰ بایت** حفظ شد.
دو نسخهٔ تکراری با هشِ بخشِ موجود تطبیق داشتند؛ دو بدنهٔ کامل دیگر پاسخ 206، Content-Range،
اندازه و هش محلیِ دقیق داشتند، اما کد خروج اصلی curl ثبت نشده بود. این محدودیت صریح است و هیچ‌کدام
هش کامل فایل اصلی نیستند. پنجرهٔ چهارانتقالیِ بعدی در هر چهار تلاش شکست خورد: سه مهلت اتصال و یک
بدنهٔ ناقص؛ دادهٔ ناقص و تشخیص‌ها حفظ شدند. آزمون IPv4 نیز برتری آن را ثابت نکرد.

آزمون اصلاح‌شدهٔ نشانی امضاشدهٔ CDN برای فایل کامل، یک اتصال را میان دریافت‌های متوالی و محدودِ
۲۵۶ MiB بازاستفاده کرد. دو بخش در **۱۶٫۰۸۶ و ۲۱٫۳۸۰ ثانیه** و چهار بخش بعدی در **۲۱٫۹۱۵،
۱۹٫۷۰۶، ۱۴٫۰۸۴ و ۱۲٫۷۱۱ ثانیه** کامل شدند. این مشاهدهٔ محدود انتقال است، نه توان پایدار یا
معیار کارایی مدل. در **۱۳:۳۸ UTC**، مهمان **۱۰۱ بخش اصلیِ انتقال با مجموع ۲۷۱۱۱۹۸۱۰۵۶ بایت**
داشت؛ خط مبنا آماده و بی‌درخواست، swap بدون مصرف و تعداد واحدهای ناموفق صفر بود. نشانی/سرآیند
امضاشده فقط در رکورد موقت و محافظت‌شدهٔ آماده‌سازی می‌ماند، نه در Git یا تنظیم زمان اجرا.
[راهنمای رسمی دریافت Hub](https://huggingface.co/docs/hub/models-downloading) مبنای فهرست صریح
CDN بود. کنترل commit/فرادادهٔ فایل کامل، بازهٔ دقیق، تطبیق هش محلی با نسخهٔ root و SHA-256 کاملِ
هر سه فایل همچنان الزامی‌اند. پایان پنجرهٔ انتقال، پذیرش مدل یا وعدهٔ ادامهٔ بدون نظارت نیست.

ادامهٔ تحت نظارت در هشت پنجره موفق پایان یافت. تطبیق تازه در **۱۴:۲۲ UTC**، **۱۳۳ بخش اصلیِ
انتقال با مجموع ۳۵۷۰۱۹۱۵۶۴۸ بایت**، خط مبنای آماده/بی‌درخواست و صفر واحد ناموفق را ثبت کرد.
از این نتیجه، کامل‌بودن فایل 122B یا انتخاب مدل استنباط نمی‌شود. سپس اولویت آماده‌سازی به
آزمون مستقلِ 3.8 Q5 در بالا منتقل شد؛ بخش‌های 122B حفظ شدند، نه تغییر نام یا حذف.

مشاهدهٔ مهمان: **۸۰ vCPU، حافظهٔ قابل‌استفادهٔ ۲۵۷۹۰۵ MiB، حدود ۲۵۱٫۸۶ GiB و سه گرهٔ NUMA
مهمان**. حجم محافظت‌شدهٔ ۴۰۰ GiB قبلاً آماده شده و دوباره قالب‌بندی نشود. NUMA مهمان، جای‌گیری
فیزیکی را ثابت نمی‌کند. حاشیهٔ آزاد datastore، سقف پروژه و منابع دیگر خدمات حفظ شوند؛ تخصیص تازهٔ
دیسک/ماشین از این بسته مجاز یا اجراشده تلقی نشود.

آزمون مستقل پیشنهادی Q5: **MemoryMax برابر ۱۲۸ GiB**، ابتدا ۳۲ رشته/سهم معادل CPU و سپس، تنها
با حاشیهٔ مشاهده‌شده، مقایسهٔ محدود ۴۸ رشته/سهم CPU؛ زمینهٔ 16K و مهلت ۱۲۰ ثانیه حفظ می‌شوند.
این‌ها **تنظیم اجراشده یا بهینهٔ اثبات‌شده نیستند**. سقف خط مبنا ۹۶ GiB و معادل ۱۸ CPU است؛
جمع دو سقف حافظه ۲۲۴ GiB و حاشیهٔ اولیه حدود ۲۷٫۸۶ GiB پیش از نیاز سیستم‌عامل/API/دیگر مصرف‌هاست.
وزن مقیم، حالت بازگشتی، کش attention، بافر prefill، تخصیص‌دهنده و کش فایل باید واقعاً اندازه‌گیری
شوند تا جا شدن مدل قابل ادعا باشد.

وزن Q8 حدود ۱۲۳٫۴۹ GiB، یعنی ۳۹٫۲۷ GiB بیشتر از Q5 است. Q5 ممکن است فشار حافظه/پهنای‌باند را
کم کند، اما رفتار کوانتیزه‌سازی و بازگشایی آن روی CPU سنجیده شود؛ سرعت یا درستی تضمین نیست.
کش فایل که پیش‌تر حساب شده، ممکن است اوج cgroup را کمتر از مصرف کامل نشان دهد. RSS/PSS، مصرف
جاری/اوج cgroup، حافظهٔ در دسترس مهمان، swap و فشار با هم دیده و کش مشترک دوباره‌شماری نشود.
با فشار منابع، افت خط مبنا یا شکست مهلت، آزمون متوقف و وضعیت تطبیق داده شود؛ سقف برای پنهان‌کردن
شکست بزرگ نشود.

### گام بعد، پذیرش، بازگشت و شواهد

ابزار آفلاین `scripts/prepare_122b_qualification.py` همان manifest و مجموعهٔ پرسش ثابت را کنترل
می‌کند؛ میزبان/مدل را فراخوانی، اعتبارنامه را دریافت یا نمایه را انتخاب نمی‌کند. ترتیب پیشنهادی،
پاسخ استاندارد، استدلال با خروجی صرفاً نهایی، زمینهٔ واقعیِ 16K و سپس 32K مشروط است. دادهٔ
پالایش‌شدهٔ RSS/PSS، cgroup، حافظه/swap مهمان و PSI فقط مشاهده‌اند، نه پذیرش مصرف کامل. بازبینی
محدود، معیار کدنویسیِ بدون اجرای کد تولیدشده و کنترل حریم خصوصی پاسخ نهاییِ موجود را به‌کار می‌گیرد.
گزارش، فایل تازهٔ محافظت‌شده و بیرون Git است. فرمان بخش انگلیسی با محیط آمادهٔ مخزن و مسیر
مطلقِ خصوصیِ تازه اجرا شود؛ کد خروج ۲ یعنی آماده‌سازی، نه پذیرش. آزمون محدودِ ناموفقِ ورودی، کد
خروج ۱ دارد. گزینه‌های `--resources` و `--trial` فقط فایل ورودیِ محدود و محافظت‌شده می‌پذیرند.

هویت typedِ 122B، کنترل سختِ قالب، نمایهٔ نامزد، اعتبارسنج هویت انتشار و مسیر استدلالِ واجد
پذیرش همچنان گام‌های کدیِ باقی‌اند؛ ابزار آن‌ها را دور نمی‌زند. پلکان 16K/32K پیشنهاد آزمون است،
نه ظرفیت زمینهٔ پذیرفته‌شده. هنگام توزیع، متن مجوز ثابتِ Apache، انتساب، اعلام تغییرهای لازم و
NOTICE احتمالیِ همراه حفظ شوند؛ در ریشهٔ نسخهٔ بررسی‌شدهٔ upstream، NOTICE یافت نشد. این
بررسی، commit دقیقِ تبدیلِ اعلام‌نشدهٔ کوانتیزه‌کننده یا انطباق جامع حقوقی را تأیید نمی‌کند.

۱. بخش‌های موجود دقیق تطبیق، ورود محدود تکمیل و اندازه/SHA-256 کاملِ هر فایل تأیید شود؛ تلاش
ناقص حفظ و هرگز انتخاب نشود.
۲. GGUF واقعیِ تأییدشده، tokenizer/قالب و سازگاری CPU با llama.cpp ثابتِ `v0.4.1` و commit
`b29c606e28a01b1bc8c1351026a0fa6e616bf6c4` پیش از بارگذاری محافظت‌شده بررسی شوند.
۳. مصرف کامل و پرسش‌های ثابتِ همسان دوزبانه برای پاسخ استاندارد، فنی و کدنویسی پذیرفته شوند؛ سپس
استدلال با خروجی صرفاً نهایی، حریم خصوصی و پذیرش زمینه در همان مهلت/صف سنجیده شوند.
۴. فقط پس از نتیجهٔ معنایی کاربردی، مسیر برنامه/API، مالکیت گفتگو، شاهد تازهٔ منبع انتخاب‌شده و
ممیزی، شاهد کهنه/ناقص/غایب/تزریق، خرابی/بازیابی وابستگی و صف، پاسخ تازه و restart با WAN مسدود،
شروع سرد VMِ قابل‌اعمال و بازگشت دقیق جدا پذیرفته شوند.

| معیار | نتیجه در زمان گزارش |
|---|---|
| فراداده/نسخهٔ ثابتِ مجوز آزاد وزن | موفق در همان دامنهٔ مجوز/فراداده |
| نمونهٔ native کدنویسی 27B با ۴۸ رشته | شکست مهلت؛ بدون پاسخ نهایی پذیرفته‌شده |
| manifest/schema/آزمون پسرفت Q5 | پیاده‌سازی در کد؛ آزمون کد، نه پذیرش مدل |
| ورود/هش کامل Q5 | آماده‌سازی ناقص؛ مجموعهٔ کامل تأیید نشده |
| metadata/قالب/بارگذاری CPU/مصرف کامل Q5 | اجرا‌نشده |
| معنا و زمان پاسخ استاندارد/استدلال/زمینهٔ دوزبانه Q5 | اجرا‌نشده |
| برنامه/شاهد/ممیزی/WAN/بازگشت Q5 | اجرا‌نشده |
| استدلال عمومی و انتخاب Q5 | غیرفعال؛ بدون گذار زنده |

مدل زنده `nextops-qwen3-5-35b-a3b-q4-k-m` است؛ runtime، حدود خط مبنا و خاموشی استدلال عمومی
ثابت‌اند. بازگشتِ آماده‌سازی فایل به restart نیاز ندارد؛ لینک/تنظیم زنده دست‌نخورده‌اند. فایل دقیق
خط مبنا و بخش‌های خصوصی حفظ شوند. تغییر زندهٔ بعدی به پذیرش ثبت‌شده، تنظیم دقیقِ محفوظ و بازگشت/
استقرار دوبارهٔ زمان‌دار نیاز دارد؛ حذف خودکار، downgrade پایگاه یا حفظ استدلال خصوصی مجاز نیست.
log انتقال، اعتبارنامه و موجودی خصوصی بیرون Git بمانند. وضعیت/فهرست جاری به این گزارش ارجاع دهند،
بدون بازنویسی پذیرش تاریخی یا موفق نامیدن معیار اجرا‌نشده.

</div>
