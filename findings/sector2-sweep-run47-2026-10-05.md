# Sector 2 sweep — run 47 (2026-10-05, ~03:48 CDT)

Sector: (2) crypto infra / DeFi / chains. **No submission.**

## Watch change this run (reported)
- **reown-com/appkit PR #5813 (submitted run 46) is blocked on Reown's CTA**: the CLA Assistant Lite bot posted 2026-10-05T08:48:03Z requiring the contributor to read and sign Reown's Copyright Transfer Agreement by commenting "I have read the CTA Document and I hereby sign the CTA"; the `CTA` status check reads FAILURE. Signing a legal agreement is Kyle's alone (same pattern as the Safe and Great Expectations CLAs, which Kyle signed himself) — **no signature was posted by this agent.** Kyle action: post that exact comment on https://github.com/reown-com/appkit/pull/5813 to unblock review/merge.
- Everything else unchanged: 19 BUG FIXER MAN PRs open (dentalpin #599 merged run 46 stays merged); NiceGUI #6372 still awaiting evnchn re-review after the dismissed approval; Expensify ×4 counts identical by REST (55 / 35 / 33 / 28 — a GraphQL count of 56 on #102072 was verified as an artifact against the REST count of 55 and the unchanged last comments); ESLint #21155 still no `accepted` label; stellar #1734 / PyBNF #931 still only our comments. HackerOne: ledger-only.

## Sweep
Consensus clients (lodestar, lighthouse, prysm, teku, grandine), execution clients (reth, revm, go-ethereum, foundry), L1s (sui, aptos, solana, cosmos-sdk, agoric), bridges/DEX SDKs (wormhole-connect, across-sdk, Uniswap sdks, allbridge):

- **Uniswap/sdks #557** — `@uniswap/v2-sdk@4.19.2` published to npm with `@uniswap/sdk-core: "workspace:*"`, breaking installs. Real and verified from the issue + registry facts, but the remedy is release-process (deprecate/republish with the monorepo publish pipeline resolving workspace ranges) — a code PR cannot repair a published artifact, and release config is maintainer territory. Rejected.
- **across-protocol/sdk #1449** — `gasDiscountPercent`/`capitalDiscountPercent` validated and returned but seemingly never applied to fee totals. The reporter explicitly opens it "to clarify the intended behavior" (oversight vs informational-by-design) — a maintainer semantics call, same reject class as prior design-decision issues. Rejected.
- Lighthouse #10057/#10045/#9975/#9949/#9691/#9620 — Rust consensus internals (fork choice, PeerDAS sync, custody backfill); deep protocol work, not verifiable in this sandbox. #8490 TOCTOU in `unused_port` is from 2025-11 with discussion.
- Prysm #16867/#16864 — Gloas fork internals, maintainer-filed tracking style.
- aptos #20650 rejected run 42 (Move prover soundness); #20457/#175xx are compiler-v2 internals from 2025, heavy Move toolchain work.
- revm #2454/#1202 — long-standing (2025/2024) with discussion; cosmos-sdk #25843/#24634 — investigation/design threads.
- wormhole-connect #4043 — live-network transfer state (expired Guardian Set), not locally reproducible; #4040 is a UX clarification.
- Generic fresh-bug search (label:bug, created >2026-09-25) returned no crypto-infra candidates — mostly unrelated small-project noise.

Pattern continues: fresh verifiable infra bugs are either already PR'd within hours, maintainer/design territory, or require chain-scale Rust/Go builds beyond this sandbox. Quiet run logged; no fabricated submission.
