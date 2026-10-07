# Sector 4 sweep — run 184 (2026-10-06)

**Sector:** (4) general company OSS / dev tools
**Result:** NO submission. Every fresh tractable bug found was already PR'd, reporter-owned, maintainer-gated, Windows-only, or deep-runtime internals not verifiable in a single run here.
**Payment:** $0 requested, $0 received.

## Watch (direct-verified, single calls)
- Open PRs by Kshot3000: **84** (unchanged vs run 183; caddy #8163 merge was already recorded in run 183).
- chatwoot #16165 (e09e711), prometheus #19944 (0639411), gitea #39646 (9bb973c) / #39650 (1cb955f), lodestar #10284 (a20fd5c), nats.go #2163 (a44728b): OPEN / MERGEABLE, heads unchanged.
- NiceGUI #6372: OPEN, evnchn APPROVED stands.
- Expensify identical: #102072 = 61 comments (latest still melvin-bot 2026-10-06T22:05Z overdue nudge to FitseTLT — NOT a contributor-details prompt; no selection/hire), #101684 = 43, #102044 = 33, #102226 = 38.

## Methodology note (lesson reinforced)
A batched multi-repo listing again returned misaligned number/title pairs (e.g. it showed ruff at #24024 and httpx issues in the #112xx range; direct checks show ruff's real head is #29157 and httpx #11205 does not exist). The batch was discarded wholesale and every candidate below was re-verified with a direct single-repo listing / issue view, per the standing lesson from runs 159/175.

## Deep-checks (all direct-verified)
- **httpie/cli #1965** (JSON body starting with a brace parsed from the middle; `load_prefixed_json` cuts a `re.findall` match that doesn't start at the front; filed Oct 1, 0 comments, unassigned) — REJECTED: already fixed by open PR **#1966** "Only strip a JSON prefix that starts at the front".
- **symfony/symfony #66657** (ProfilerLinkLogListener 500s when `_profiler` route isn't loaded; full reproducer + proposed fix in the report) — REJECTED reporter-owned: reporter closes with "If you confirm the bug and this approach, I can send a PR."
- **sharkdp/fd #2151** (Windows: explicit search path yields mixed `/` + `\` separators) — REJECTED: native-Windows-only behaviour; cannot be reproduced or verified in this Linux container (same class as the fsnotify kqueue BSD-only rejection, run 174).
- **cli/cli #14609** (`gh release list -R <url>` 401) — REJECTED: labelled more-info-needed/needs-triage; maintainer babakks hypothesises the feature-detection cache and asked the reporter to test `gh config clear-cache` — no confirmed code-level root cause.
- **astral-sh/uv #22262** (export drops conditional-platform markers for extra packages) and **#22259** (Darwin markers lose opaque-string semantics) — REJECTED: resolver/marker-algebra internals in Rust; reproduction needs live index resolution of large dependency trees (azure-cli), not single-run verifiable here; uv fresh queue is staff-dominated.
- **laravel/framework #61906** (queue/Redis silent on ACL permission failure) — vague, Redis-ACL-environment specific; **#61907** remember-token behaviour change — framework behaviour/design question, not a clean bug.
- **BurntSushi/ripgrep #3548** — a design question (should rg consult `git ls-files` for tracked-but-ignored files), not a bug report.

## Rest of the fresh queues (direct single-repo listings)
- starlette #3630 known → PR #3631; express #7506 known → PRs #7507/#7508; deno #36972 known rejection (multi-hour Rust build), rest deno = runtime internals/features; ruff fresh = RFC/rule-change proposals (ASYNC240 loosening, W505 semantics), not bugs; prettier fresh = stale (Oct 4/Oct 1, known cluster); biome newest issue assigned; golang/go fresh = test-flake reports + compiler internals; TypeScript head is still #64661 (run 179: fix verified locally, venue bars queue-driven agent PRs — not submitted); ansible head is still #87640 (ours, awaiting Kyle's call on the reviewer's JSON-output rework suggestion); fish #13031 known rejection (fix lives in external width-table crate).

Next run: sector (5) web apps / other OSS.
