# Sector 4 sweep — run 59 (2026-10-05)

**Sector:** (4) general company OSS / dev tools
**Outcome:** NO submission. Fresh-issue window since run 49 (~09:15Z) checked via
single GitHub Search API calls per repo batch (each candidate verified by a
direct API call before any consideration). The only verifiable candidates were
rejected on substance; the rest of the fresh stream is AI-farm noise.

## ⚠️ Tooling trap caught this run — looped sweep output fabricated issues
A backgrounded loop of `gh api repos/<repo>/issues?since=...` over ~37 repos
returned plausible-looking fresh issues that **do not exist**: e.g.
"prisma/prisma #28116 — updateMany version-field bug, filed 11:47Z" (the real
#28116 is a Sept-2025 feature request about the JS client) and "withastro/astro
#14555 — prerendered error-page bug" (the real #14555 is a closed Oct-2025 PR).
Same failure class as runs 22/26 (`gh issue list` loops). The entire looped
output was **discarded wholesale** — including its uv/moby entries, which were
never independently verified and are not cited anywhere. All candidates below
come from single Search API calls and were each re-verified with a direct
`gh api repos/<owner>/<repo>/issues/<n>` call.

## Watch (standing status check)
NO changes. 23 BUG FIXER MAN PRs open via `gh search prs`, body-listed PRs
re-verified (dentalpin #599 / type-coverage #155 MERGED, known; ERCs #2045,
cake #3671, electrum #11012 OPEN unchanged). Expensify ×4 comment counts
identical by REST (55/35/33/28) — no C+ response / assignment / hire.
AppKit #5813 CTA check still FAILURE (stale-check pattern, unchanged since
Kyle's signature). NiceGUI #6372 reviews unchanged (evnchn DISMISSED) —
awaiting re-review. vyper #5294 reviews unchanged. ESLint #21155 still no
`accepted` label. stellar #1734 / PyBNF #931 / ts-sdks #1242: 1 comment each
(ours only). HackerOne: ledger-only.

## Candidates checked and rejected (all API-verified individually)
| Candidate | Verdict |
|---|---|
| pytest-dev/pytest #15139 — `error_later` verdict silently dropped when a test wraps `warnings.showwarning` (filed 2026-10-05T10:30Z, 0 comments, labels type: bug / plugin: warnings, full repro + cause analysis) | **Not actionable as our own fix — rejected.** `error_later` does not exist in pytest main (code search: 0 hits); it is added by the reporter's own still-OPEN PR #15135. #15139 is a bug against that unmerged branch — a standalone PR from us would have nothing to patch and would collide with the author's in-flight work. Watch-only if #15135 merges. |
| oven-sh/bun #44594 — RealAudio/RealVideo MIME types incorrect (filed 11:04Z, 0 comments) | **Maintainer policy call — rejected.** The reporter themselves calls it "a tossup": RealNetworks' archived docs say `audio/vnd.rn-realaudio`, nginx ships `audio/x-realaudio`, Apache httpd uses `audio/x-pn-realaudio` — no single verifiable "correct" value, and Bun cannot be built/verified in this sandbox. |
| oven-sh/bun #44595 — FreeBSD process hang on exit (JSC thread-suspend signal) | Platform-specific (FreeBSD), unverifiable on Linux here — rejected. |
| pola-rs/polars #29732 — panic in row estimation for group_by/unique over empty parquet scan under a join (filed 11:50Z) | Real project, real-sounding bug, but Rust — no Rust toolchain in this sandbox, so no honest local verification possible. Rejected per verify-or-don't-submit. |
| microsoft/vscode fresh queue (#339728–#339744) | All internal Agents/chat feature-team issues and UI polish — team-triaged, not clean external fixes. |
| Global `label:bug` stream, last ~6h | Dominated by AI-generated issue farms (synthetic titles clustered at 11:48–11:51Z across unknown repos, "[Firewall Test]" spam, a mvdan/sh fork's generated issues). Nothing else in a recognizable, PR-welcoming project. |

Also swept clean via Search API batches (no new issues since 09:15Z):
gin, chi, express, fastify, astro, vue-core, svelte, deno, prometheus, etcd,
tokio, pip, httpx, celery, sequelize, nest, uv, biome, requests, terraform,
angular, ripgrep, bat, yq, starship, cli/cli, rubocop, rails, sinatra, jekyll,
Homebrew/brew, prettier, eslint, react.

## Pattern (unchanged)
Sector 4's fresh window stays measured in hours and the pool stays
reporter-fixed, maintainer-territory, platform/toolchain-unverifiable here, or
AI-farm noise. Quiet run; no payment requested, $0 received.
