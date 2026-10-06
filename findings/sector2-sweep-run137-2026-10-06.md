# Sector 2 sweep — run 137 (2026-10-06)

Sector: (2) crypto infra / DeFi / chains. **No submission.**

## Fresh queues checked (direct `gh api` per repo, newest open issues)

- **NethermindEth/nethermind #14323** (filed today 13:23Z by CPerezz, 0 comments, unassigned): restart replays genesis on an empty state and deletes the whole chain after importing a side branch. Serious and real — but the reporter cross-referenced his own fix PR **#14324** ("refuse a branch that reaches genesis without state") 23 minutes after filing. Reporter-owned; rejected.
- **cosmos/ibc-go #9114**: known — already fixed by PR #9115 (run 132).
- **Consensys/teku #11412**: known — assigned to reporter (tbenr), Java/no-JDK here.
- **celestiaorg/celestia-node #5310**: known — reporter-owned, PR #5311 open.
- **cometbft #6098 / #6093**: known design/security items from earlier runs.
- **ethereum-optimism/optimism**: #23217 internal migration; #23213 is ours (PR #23214).
- **wormhole-foundation/wormhole**: fresh items are re-observation requests only.
- **cosmos/cosmos-sdk #26855, Uniswap/v4-core #1078, balancer #2664, zksync-era #4952**: the Oct 2 "machine-proven math" proof-exercise postings — not bugs.
- **aave-v3-core**: freshest issues are from 2025 (stale).
- Empty fresh-issue heads (recent items all PRs): go-ethereum, reth, prysm, besu, sui, aptos-core, nearcore, agave, foundry, morpho-blue, lodestar, sway, scroll, revm, espresso, starknet-specs.
- FuelLabs/fuel-core #3340–#3342 (Sep 28): `std` transitive-dependency hygiene items, not runtime bugs; linea #4134 is a design doc.

## Held candidates re-checked

- sigp/lighthouse #10226: still 1 comment (claim only), no assignee, no PR — claim watch continues.
- SatoshiPortal/bullbitcoin-mobile #2902: still labels=["bug"] only, no assignees — 'ready'-label HELD stands.
- formbricks/formbricks #9526: still 3 comments, no maintainer PR.

## Status watch

ONE change (corrected after the delayed watch output landed): **Expensify #102044 comments 30 → 32** — C+ reviewer FitseTLT (13:47Z) asked MelvinBot whether similar Sentry issues were previously fixed by suppressing third-party noise, and MelvinBot (13:50Z) answered yes with four prior examples. This is reviewer activity on the issue where Kyle's $250 proposal sits in 'Reviewing'; no selection, assignment, or hire, and no reply was needed. All watched PRs direct-verified identical to run 136 (payload #18534 OPEN/MERGEABLE c=0, supabase #51340 OPEN c=4, viem #5196 OPEN c=3, optimism #23214 OPEN c=0, diffy #89 OPEN c=0, prysm #17626 OPEN c=1 CLA = Kyle's step, memos #6435 OPEN c=2, ansible #87642 OPEN c=1, NiceGUI #6372 OPEN c=1 with evnchn APPROVED standing, vyper #5294 OPEN — its 5th issue comment is Kshot3000's own rework note; dentalpin #599 / type-coverage #155 merged, electrum #11012 closed unmerged — all known). Other Expensify counts identical: #102072 60, #101684 42, #102226 38 — no melvin-bot prompt to Kshot3000. $0 requested, $0 received.
