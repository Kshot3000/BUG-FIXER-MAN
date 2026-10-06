# Sector 2 (crypto infra / DeFi / chains) sweep — run 127, 2026-10-06

**Outcome: NO submission.** Every fresh item individually verified was already PR'd, claimed within minutes, a known standing item, or toolchain-gated (Java/.NET, no JDK/dotnet here). Watch: NO changes.

## Methodology warning (important)

Two batched multi-repo loop scans this run returned **fabricated entries** — plausible titles attached to real-looking numbers that do not exist or belong to other items:

- paradigmxyz/reth "#27759 op-reth --dev mode" and "#27763 forkchoice" — both 404 on direct check; reth's real head is #27753.
- OffchainLabs/prysm "#17628 Slashing Protection Interchange Format Fails to Import" — #17628 is actually a PR, "Add builder_index and block_hash to the Gloas block event".
- sigp/lighthouse "#10220 BN Tracking issue: several nodes lagging" — #10220 is a Mergify merge-queue PR.
- The DeFi second-tier scan (chainlink/aave/eigenlayer/balancer entries) was discarded wholesale for the same reason.

Every item below was re-verified with a **single direct API call** (the method validated across prior runs). Batched loop output is never trusted without a direct check.

## Candidate checked deep — sigp/lighthouse #10226 (real, but claimed)

Filed 2026-10-06T09:58Z by jimmygchen (Lighthouse core), labels `gloas`, `v9.0.0`, unassigned: Gloas proposer prep picks the parent from the head's payload status, while bid validation / block production use `should_build_on_full` (which also weighs PTC votes). When the payload is Full but the PTC voted it late/unavailable, `payload_attributes` tells external builders to build on it and their bids are then ignored with `BidNotCompatibleWithHead`. Reporter observed it on a local devnet (all PTC votes `payload_present=false`, every gossip bid ignored). Fix is spelled out in the issue: use `should_build_on_full` for the proposal slot in proposer prep, matching the spec's `prepare_execution_payload`.

**Why not taken:** claimed 17 minutes after filing — NikhilSharmaWe commented "I can open a PR for this" (10:15Z) and a maintainer applied labels at 10:39Z. Racing a claimed, maintainer-labelled issue whose fix a core dev has already designed would produce a duplicate PR. WATCH #10226: if the claimant's PR does not appear / stalls, it becomes a candidate for a later sector-2 run (Rust toolchain permitting — Lighthouse is heavy).

## Other queues, individually verified

- ethereum-optimism/optimism: fresh #23217 is an internal opgeth-decoupling migration task, not a bug; #23211 → PR #23212 (known); #23213/#23214 are ours (PR open).
- celestiaorg/celestia-node: #5310 known reporter-owned + PR #5311 open; all other fresh items are PRs (#5312/#5314/#5315/#5318).
- cometbft/cometbft: #6098 known protocol-design item (Oct 1); #6093 → PR #6094.
- OffchainLabs/prysm: fresh items all PRs, incl. our #17626. paradigmxyz/reth: fresh items all PRs, incl. our #27735.
- hyperledger/besu: fresh items all PRs; Java, no JDK here regardless. Consensys/teku: #11412 standing reporter-claimed (Java); rest PRs/spec/test-format items.
- NethermindEth/nethermind: fresh items all PRs (.NET, no toolchain).
- OffchainLabs/nitro: #4760 → PR #4761 (known). wormhole-foundation/wormhole: only live-network re-observation requests (standing reject class).
- ethereum/go-ethereum, cosmos/ibc-go: fresh items all PRs / dependency bumps.

## Watch

NO changes — all PRs direct REST-verified identical to run 126: dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 OPEN c=1, cake #3671 OPEN c=0, electrum #11012 + trilium #11920 CLOSED unmerged (known); viem #5196 OPEN, optimism #23214 OPEN c=0, diffy #89 OPEN c=0, prysm #17626 OPEN c=1 (CLA = Kyle's step), memos #6435 OPEN c=2, NiceGUI #6372 OPEN c=1 (evnchn APPROVED stands), vyper #5294 OPEN c=2, ansible #87642 OPEN c=1, vikunja #4107/#4110 OPEN c=0. `gh search prs --author Kshot3000 --state open` shows no unknown new PRs. Expensify identical by direct per_page=100 listing: #102072 60 (tail = bconnnnn's known proposal + melvin-bot template reply), #101684 42, #102044 30, #102226 38 — no selection/hire, no melvin-bot prompt to Kshot3000. HackerOne: ledger-only (no browser check this run).

$0 requested, $0 received. Next run: sector (3) paid bounty platforms & paid GitHub issues.
