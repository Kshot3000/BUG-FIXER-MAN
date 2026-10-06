# Sector-2 sweep — run 132 (2026-10-06, crypto infra / DeFi / chains)

**Result: NO submission.** Every fresh bug queue across ~25 infra/DeFi repos was
already PR'd, already ours, claimed/reporter-owned, a known design item, or
gated by a toolchain this sandbox lacks (Java/.NET). All items below were
verified by single direct GitHub API calls (no batched-scan data used).

## Fresh candidate checked and rejected

- **cosmos/ibc-go #9114** (filed today 11:13Z, 0 comments, unassigned) —
  packet-forward middleware parses the memo `retries` field as JSON `float64`
  and casts to `uint8`, so `2.9` silently truncates to `2` instead of failing
  as malformed metadata. Real, small, locally verifiable — **but already
  fixed**: cross-referenced **PR #9115** ("fix(apps/pfm): reject fractional
  retries in forward metadata") is open. Nothing to add.

## Known / standing items re-verified

- **sigp/lighthouse #10226** — Gloas `payload_attributes`/PTC bid bug: still
  open, still only the 1 claim comment (NikhilSharmaWe), no assignee, no
  cross-referenced PR yet (~2.5h since filing — claim watch continues, not
  stalled). #10214 = known SSE-capacity design item.
- **ethereum-optimism/optimism** — #23213 is ours (PR #23214); #23211
  (op-node static peer re-dial) → PR #23212 (timeline-verified); #23217 =
  internal opgeth-decoupling migration; #23207–#23209 = ZK prover internals
  (known).
- **Consensys/teku #11412** — assigned (1 assignee), standing reporter claim,
  Java (no JDK here). **hyperledger/besu #11480** — known self-spelled
  pattern fix, Java (no JDK here).
- **celestiaorg/celestia-node #5310** — reporter-owned, assigned, PR #5311
  already open (known).
- **OffchainLabs/nitro #4760** → PR #4761 (known).
- **paradigmxyz/reth #27734** — ours (PR #27735).
- **OffchainLabs/prysm #17619** — live-validator timing, unverifiable here
  (known). **cometbft #6098/#6093** — design / PR'd (known).
- **wormhole-foundation/wormhole** — fresh items are all guardian
  re-observation requests (live-network actions, not code bugs).
- **ethereum/go-ethereum, NethermindEth/nethermind, MystenLabs/sui,
  anza-xyz/agave, near/nearcore, morpho-org/morpho-blue** — fresh open-issue
  heads empty of actionable bugs.
- **DeFi (aave-v3-core, Uniswap/v3-core, compound-protocol,
  balancer-v2-monorepo, cosmos/cosmos-sdk)** — only stale items, bounty-claim
  spam, or "machine-proven math" proof-exercise posts (cosmos-sdk #26855,
  balancer #2664, same-minute Oct 2 posts); aave #988 is a stale 2025
  rounding discussion. Nothing fresh and verifiable.

## Held candidates

- **BullBitcoin/bullbitcoin-mobile #2902** — repo moved to the
  **SatoshiPortal** org (SatoshiPortal/bullbitcoin-mobile); issue still open
  with labels=["bug"] only — the maintainer 'ready' label the repo's
  CONTRIBUTING requires is still absent, so the HELD decision stands.
- **formbricks/formbricks #9526** — unchanged: 2 comments, unassigned, no
  maintainer PR/cherry-pick of the ready branch yet.
- **sigp/lighthouse #10226** — claim-stall watch (see above).

## Status watch

NO changes. All watched PRs direct-verified identical to run 131 (dentalpin
#599 / type-coverage #155 merged; ERCs #2045, cake #3671, supabase #51340,
viem #5196, optimism #23214, diffy #89, prysm #17626, memos #6435, NiceGUI
#6372 with evnchn APPROVED, ansible #87642, vikunja #4107/#4110 open;
electrum #11012 and trilium #11920 closed unmerged, known). The PR-endpoint
comments field read viem #5196 as 4 — the direct issue-comment listing shows
the same 3 bot comments (vercel/changeset/pkg-pr-new); artifact discarded.
Expensify counts identical by direct listing: #102072 60, #101684 42,
#102044 30, #102226 38 — no selection/hire, no melvin-bot prompt to
Kshot3000. HackerOne: ledger-only (no browser check this run).

Payment: $0 requested, $0 received.
