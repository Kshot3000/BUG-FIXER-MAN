# Sector 2 sweep — run 87 (2026-10-05)

**Sector:** (2) crypto infra / DeFi / chains
**Result:** NO submission — no fresh, unclaimed, locally verifiable bug found.

## Status watch
NO changes. Body-listed PRs direct-verified unchanged: dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 OPEN c=1, cake #3671 OPEN c=0, electrum #11012/#11013 OPEN c=0. Spot checks identical: NiceGUI #6372 c=1 r=3; vyper #5294 r=3; AppKit #5813 c=5; gitea #39611 c=0; payload #18509 c=0; socket-plugs #162 c=0; chatwoot #16130 c=0; vikunja #4107 c=0; gofactory #67 OPEN; eslint #21391 CLOSED (known). Expensify counts identical (per_page listing): #102072 55, #101684 38, #102044 29, #102226 38 — no C+ selection/assignment/hire, no melvin-bot prompt to Kshot3000. HackerOne: ledger-only (no browser check this run).

## Candidates checked and rejected
- **celestiaorg/celestia-app #8031** (`WithParallelQueueSize` ignored at tx-queue start, filed 2026-09-30, 0 comments) — already fixed by the reporter's OPEN PR #8032 ("fix(user): honor WithParallelQueueSize when starting tx queue", myetcd). Not duplicated.
- **cometbft/cometbft #6098** (consensus halt via unbounded Block.MaxBytes, 2026-10-01) — protocol-design / maintainer territory, not a clean code fix.
- cometbft rest: #6023→PR #6024 and #5902→PR #6090 (known); #6031/#6030 FilePV/evidence internals are heavy validator-state work.
- **wormhole-foundation/wormhole** fresh queue is entirely user re-observation requests for stuck transfers (live-network operations, not code bugs).
- **sigp/lighthouse / NethermindEth/nethermind / offchainlabs/prysm** fresh bugs are deep consensus/client internals (fork-choice scoring, custody backfill amplification, FlatDb sync) — not locally verifiable in this sandbox.
- **Lidofinance/core** bug queue stale (newest Mar 2026, a disputed critical claim) or old precision/design items.
- **aptos-labs/aptos-core #20672/#20650/#20646** — Move prover soundness/spec issues, prover-toolchain territory (previously rejected class).
- **Uniswap/sdks #720/#557, aave-v3-core, chainlink, compound, spark, morpho-blue, across, balancer-v2, hyperlane** — queues empty, stale (2020–2025), spam, or design clarifications.
- **MystenLabs/sui, near/nearcore, stellar/go, zcash, monero, hydra, cardano-wallet** — newest items are features, tracking issues, assigned work, or heavy Haskell/Rust internals with no clean local repro.

No payment requested, none received. Next run: sector (3) paid bounty platforms & paid GitHub issues.
