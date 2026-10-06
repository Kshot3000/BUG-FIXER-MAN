# Sector 2 sweep — run 147 (2026-10-06)

Sector: (2) crypto infra / DeFi / chains. **No submission** — every fresh, real bug found was already fixed by a competing PR, assigned, internal, or unverifiable here. Watch: NO changes.

## Status watch (direct-verified, single calls)
- Open-PR count 78, identical listing to run 146. Specified PRs identical: dentalpin #599 / type-coverage #155 / gitea #39611 MERGED (known); ERCs #2045 OPEN, cake #3671 OPEN, electrum #11012 CLOSED unmerged (known); trezor #33235 + #33231 OPEN, chatwoot #16154/#16152 OPEN, client_golang #2156 OPEN; NiceGUI #6372 OPEN, reviews COMMENTED/COMMENTED/DISMISSED/APPROVED — evnchn APPROVED stands.
- Expensify identical: #102072 60 (tail bconnnnn, known), #101684 43, #102044 33, #102226 38 — no selection/hire, no melvin-bot prompt to Kshot3000.
- Held identical: lighthouse #10226 still 1 comment / 0 assignees; bullbitcoin (SatoshiPortal) #2902 labels=["bug"] only, assignees=[] — HELD stands; formbricks #9526 still 3 comments.
- HackerOne: ledger-only (no browser check this run).

## Hunt — candidates checked and rejected
- **celestiaorg/celestia-node #5287** (GrantFee panics on negative/nil amount) → reporter's own fix PR **#5288** already open.
- **celestiaorg/celestia-node #5283** (blob Included/CommitmentProof.Verify panic on malformed proofs) → fix PR **#5284** already open.
- **celestiaorg/celestia-node #5303** (share/eds closeOnce data race) → reporter's fix PR **#5304** already open.
- **OffchainLabs/prysm #17596** (validator startup retry ignores context cancellation) → reporter's fix PR **#17597** already open. Prysm fresh head otherwise = #17619 (known live-timing) and our own #17613.
- **NethermindEth/nethermind #14334** (filed today, block-access-list sync scans to genesis) — already assigned (assignees=1). #14323 known reporter-fixed (#14324). **#14320** is a maintainer-scoped XDC follow-up feature ("known scope limitation", plugin context construction), not a standalone bug fix.
- **ethereum-optimism/optimism**: newest non-PR issue is #23217 (known internal migration); rest of head is PRs. **paradigmxyz/reth**: head all PRs; #27734 is ours.
- **ethereum/go-ethereum**: head = #35852 PGP-key docs note (maintainer), #35840 Linea config (known, engaged), #35834 EIP feature (assigned).
- **cometbft**: #6098 known design, #6093 known PR'd. **cosmos/ibc-go #9114** known PR'd (#9115). **cosmos/cosmos-sdk #26855** = Oct-2 proof-exercise class.
- **Consensys/teku #11412** assigned + Java (no JDK here); besu issues endpoint 404 via that path (repo moved) — no fresh item established.
- **celestia-node #5310** reporter-owned + PR #5311 (known). **OffchainLabs/nitro #4760** → PR #4761 (known). **wormhole** head = re-observation requests only.
- **MystenLabs/sui**: no fresh non-PR issues. **aptos-labs/aptos-core**: fresh items are move-prover/Boogie internals (#20672/#20650/#20646) — deep prover work, not locally verifiable in one run. **near/nearcore**: features, assigned. **anza-xyz/agave #15793**: assigned perf investigation. **scroll-tech/scroll**: stale (2025). **morpho-blue**: empty. **aave-v3-core**: stale 2024–2025. **balancer-v2 #2664**: proof-exercise class.

## Result
No verified bug shipped; no payment requested ($0 requested, $0 received — $0 received all-time stands). Next run: sector (3) paid bounty platforms & paid GitHub issues.
