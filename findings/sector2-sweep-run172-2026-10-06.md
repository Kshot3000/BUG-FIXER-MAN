# Sector 2 sweep — run 172 (2026-10-06)

Sector: (2) crypto infra / DeFi / chains. **No submission** — every fresh queue item was direct-verified repo-by-repo and was already ours, already PR'd, maintainer-assigned, a coordinated team/audit series, or a non-code request.

## Direct-verified candidates and why each was rejected

- **cometbft/cometbft #6098** (Consensus Halt via Unbounded `Block.MaxBytes`, filed 2026-10-01, 0 comments, unassigned) — REJECTED: already fixed by open PR **#6100** ("enforce minimum Block.MaxBytes floor and handle small limits defensively"). #6093 (remote signer panic) remains fixed by open PR #6094 (known).
- **celestiaorg/celestia-node #5310** — maintainer-assigned (Shailu-s) with PR #5311 (known).
- **cosmos/ibc-go #9114** (PFM fractional-retries truncation, filed today) — known PR'd item from runs 162/167.
- **Consensys/teku #11427–#11433** and **hyperledger/besu #11492/#11493/#11496** (all filed today) — the same coordinated Java audit-report series rejected in runs 157/167: deep client internals, not single-run verifiable here.
- **OffchainLabs/nitro #4760** — already fixed by PR #4761 (known).
- **sigp/lighthouse #10226** — held claim-watch item: still 1 comment, 0 assignees (verified this run).
- **wormhole-foundation/wormhole #5025–#5029** — VAA re-observation requests only, not code bugs.
- **LidoFinance/lido-dao #1984** (`getFeeDistribution` order) — known rejection (run 157): deprecated view in frozen legacy 0.4.24 contracts, fix spelled out by reporter.
- **aptos-labs/aptos-core #20689** — Move prover internals (opaque callee / closure purity), not verifiable in one run.
- **babylonlabs-io/babylon** fresh heads are stale March items, maintainer-assigned.
- Empty / no fresh bug heads: optimism, prysm, lodestar, reth, geth, celestia-app, sui, nearcore, morpho-blue, scroll, nethermind, polkadot-sdk, espresso-network. cosmos-sdk #26855 and balancer #2664 / rocketpool #350 are machine-proof exercise posts, not bugs. aave-v3-core heads are stale 2025.

## Status watch (direct single calls, this run)

NO external changes vs run 171: open-PR count **85**; dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 OPEN, cake #3671 OPEN, electrum #11012 CLOSED unmerged (known); chatwoot #16165, prometheus #19944, gitea #39646 (head 9bb973c) / #39650, caddy #8163 (head 5b88382, Kyle's own), lodestar #10284, nats.go #2163 OPEN/MERGEABLE; NiceGUI #6372 OPEN with evnchn APPROVED standing. Expensify counts identical by direct listing: #102072 61, #101684 43, #102044 33, #102226 38 — no selection/hire, no melvin-bot contributor-details prompt (#102072 latest is still the known 22:05Z overdue nudge to FitseTLT). Held identical: lighthouse #10226 (1 comment / 0 assignees), SatoshiPortal/bullbitcoin #2902 (labels=["bug"] only, 0 assignees), formbricks #9526 (3 comments). HackerOne: ledger-only, no change reported.

Payment: $0 requested, $0 received (all-time received remains $0).
Next run: sector (3) paid bounty platforms & paid GitHub issues.
