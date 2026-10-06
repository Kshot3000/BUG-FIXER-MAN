# Sector 2 sweep — run 162 (2026-10-06)

Sector: (2) crypto infra / DeFi / chains. **No submission.**

Fresh queues direct-verified repo-by-repo (single calls only):

- **ethereum-optimism/optimism #23234** (filed today 19:19Z, 0 comments, unassigned, no competing PR): kona-interop should treat provider errors as fatal, not invalid messages. REJECTED as a submission target — it is a T-proofs team design task from today's internal kona audit series (sibling exploitable case already closed by team PR #23235; the issue prescribes the team's own change + test), same class as the previously rejected internal optimism items (#23217 migration, #23211/#23213 ours/internal). The Oct 5–6 kona-sp1/kona-interop head (#23209/#23207/#23206/#23204) is the same proof-team series.
- **celestiaorg/celestia-node #5310**: assigned (Shailu-s) and already fixed by PR #5311. The rest of the Sept celestia batch was PR'd in earlier runs.
- **OffchainLabs/nitro #4760**: already fixed by open PR #4761 (known).
- **cosmos/ibc-go #9114**: known, already fixed by PR #9115; older Sept batch all PR'd.
- **sigp/lighthouse**: #10226 HELD unchanged (1 comment, 0 assignees); #10214 known maintainer-committed design; rest Gloas team testing.
- **paradigmxyz/reth**: head is our own #27734 plus Sept engine internals; nothing fresh and tractable.
- **ethereum/go-ethereum**: head = EIP feature work, Linea config, PGP-docs note — no fresh tractable bug.
- **OffchainLabs/prysm**: #17613 is ours (PR #17626, CLA = Kyle's step); #17596 reporter's PR known; rest team items.
- **ChainSafe/lodestar**: no open bug-labelled issues; our PR #10284 stands.
- **wormhole-foundation/wormhole**: head is entirely VAA re-observation requests — not code bugs.
- **MystenLabs/sui / aptos-labs/aptos-core**: stale heads; aptos fresh = move-prover/Boogie internals, not verifiable in one run.
- **near/nearcore**: tracking/design issues only. **aave-v3-core**: stale (2025 and older). **morpho-blue**: no open issues.
- teku/besu remain Java/no-JDK gated; cometbft items are known design/security discussions.

Held re-checked: lighthouse #10226 still 1 comment / 0 assignees; SatoshiPortal/bullbitcoin-mobile #2902 labels=["bug"] only, assignees=[] — HELD stands; formbricks #9526 still 3 comments.

Watch: NO changes (see status-watch run 162). $0 requested, $0 received.
