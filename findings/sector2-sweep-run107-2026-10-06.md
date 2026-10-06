# Sector-2 sweep — run 107 (2026-10-06, crypto infra / DeFi / chains)

**Outcome: NO submission.** Fresh bug queues swept across ~35 infra/DeFi/chain repos (direct per-repo REST issue listings, created ≥2026-10-03, cross-checked for competing PRs). Every candidate was already PR'd, reporter-claimed, maintainer-territory/design, live-network, or not locally verifiable in this sandbox.

## Candidates assessed

- **sigp/lighthouse #10216** → already fixed by open PR #10217. **#10214** (Default SSE channel capacity 16 drops `payload_attestation_message` events during Gloas PTC bursts) — capacity/design call needing devnet-scale reproduction; not a clean local fix.
- **Consensys/teku #11412** (primitive progressive list serialization includes padding after backing-node reload) — reporter-claimed: the reporter offered a patch in-thread and a maintainer asked the assignee (tbenr) to triage whether the reporter's patch is acceptable. Also Java — no JDK in this sandbox, so no local verification path regardless. **#11405** builder-payment ordering is spec/design work.
- **hyperledger/besu #11480** (`unsafeStoreHeader`/`unsafeSetChainHead` publish chain head before storage commit) — the issue itself spells the exact fix pattern (stage in locals, publish after `updater.commit()`, mirroring PR #10842). A drive-by copy of a maintainer-spelled pattern fix in a race-ordering area we cannot test (no JDK toolchain here) would be low-substance; held/rejected as in run 102.
- **prysmaticlabs/prysm #17619** (v7.2.0 REST validator misses attestations, ~500 ms attestation-data read window) — live validator timing behaviour; not locally reproducible/verifiable here.
- **OffchainLabs/nitro #4760** (RestfulClient `HealthCheck`/`ExpirationPolicy` ignore context cancellation, use `http.Get`) — already fixed by open PR #4761 (re-verified this run via search).
- **ChainSafe/lodestar #10262** — feature/telemetry (record Fulu block timeliness), not a bug.
- **wormhole-foundation/wormhole #5022–#5027** — all live-network re-observation requests (expired guardian sets), not code bugs.
- **stacks-network/stacks-core #7704/#7705** — flaky signer tests, heavy Rust integration suite; not a product bug.
- **celestiaorg/celestia-app #8082** flaky nightly race tests (maintainer territory), **#8078** perf optimisation, **cosmos/cosmos-sdk #26855 / balancer #2664 / lido #1981 / Uniswap v4 #1078 / superfluid #2240** — "machine-proven math" proof exercises, not reported defects; **compound-protocol** fresh items are bounty-claim/audit-spam threads.
- Queues empty of fresh bugs: reth (only our own #27734), Nethermind, cometbft (latest Oct 1, protocol-design), aptos-core, nearcore, go-ethereum, ibc-go, hyperlane, morpho-blue, aave-v3-core (stale 2025), across (Oct 1 perf items).

## Status watch (run 107)

**NO changes.** Direct REST verification (issue-comment listings, not the PR-endpoint `comments` field — that field read NiceGUI #6372 as 3 and lodestar #10264 as 1 this run; direct listings prove 1 and 0 respectively, identical to run 106 — artifact caught and discarded):

- dentalpin/dentalpin #599 and plantain-00/type-coverage #155: MERGED (known).
- OPEN, unchanged: ethereum/ERCs #2045 (c=1), cake-tech/cake_wallet #3671 (c=0), spesmilo/electrum #11012/#11013 (c=0), ansible/ansible #87642 (c=1), zauberzeug/nicegui #6372 (c=1, reviews 4 — evnchn APPROVED stands, awaiting merge), vyperlang/vyper #5294 (reviews 3), go-vikunja/vikunja #4107/#4110 (c=0), SocketDotTech/socket-plugs #162 (c=0), go-gitea/gitea #39611 (c=0), payloadcms/payload #18509 (c=0), chatwoot/chatwoot #16130 (c=0), maranqz/gofactory #67, reown-com/appkit #5813 (issue comments 5), ChainSafe/lodestar #10264 (c=0, reviews 0).
- Expensify/App comment counts identical: #102072 = 60, #101684 = 41, #102044 = 30, #102226 = 38 — no C+ selection/assignment/hire on the live three, no melvin-bot prompt to Kshot3000.
- HackerOne: ledger-only (no browser check this run; ID-verification confirmation still pending a signed-in check — Kyle's step, not performed).

$0 requested, $0 received this run. Next run: sector (3) paid bounty platforms & paid GitHub issues.
