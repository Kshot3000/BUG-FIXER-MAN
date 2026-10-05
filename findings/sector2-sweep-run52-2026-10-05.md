# Sector-2 sweep — run 52 (2026-10-05, crypto infra / DeFi / chains)

**Result: NO submission.** Per-repo server-side search (REST `search/issues`,
every candidate API-verified — no `gh issue list` loop output trusted) across
~30 repos. Every fresh verifiable bug was already PR'd, team-tracked,
feature-branch audit work, or protocol/security maintainer territory.

## Candidates checked and rejected

| Repo / issue | Why rejected |
|---|---|
| cometbft/cometbft #6098 — Consensus Halt via Unbounded `Block.MaxBytes` | Consensus-critical security bug, `needs-triage`, no assignee but a protocol-design fix (where the bound belongs is a maintainer call); not a local clean fix |
| sigp/lighthouse #10193/#10189/#10069/#10062/#10057/#10045/#9975 | Gloas/PTC fork-boundary team tracking tasks with comments/reviews already in flight |
| celestiaorg/celestia-app #7814/#7816/#7817 (fibre audit F03/F05/F28) | All on feature branch `feat/fibre-r2-adapter` @ ddaca69, cross-referenced by tracking PR #7827; #7816 assigned to rootulp — audit remediation in progress by the team |
| celestiaorg/celestia-app #8031 — `WithParallelQueueSize` ignored at tx-queue start | Reporter's ecosystem PR #8032 ("fix(user): honor WithParallelQueueSize…", myetcd, 2026-09-30) already open |
| celestiaorg/celestia-node #5237 | Flaky tastora restart test — CI flake, not a product bug |
| graphprotocol/graph-node #6726 — `loadRelated` stale children while blocks queued | Reporter madumas opened fix PR #6727 two minutes after the issue |
| graphprotocol/graph-node #6725 | Is itself a PR (trigger-ordering sort panics), not an open issue |
| livepeer/go-livepeer #4100 — remote-signer Kafka queue drops `create_signed_ticket` events | Design/queue-policy call (drop vs block vs spill), `status: triage`; #4101 is itself a PR |
| wormhole-foundation/wormhole #5021–#5024 | Guardian re-observation operational requests for stuck bridge transfers — not code bugs |
| aptos-labs/aptos-core #20650 | Move prover soundness — standing reject (run 42) |
| stellar/stellar-core #5451 | Windows `build_rust.bat` env issue, 1 comment, not verifiable on Linux here |
| matter-labs/zksync-era #4946 | "External mainnet node not working" — live-network/support, no local repro |
| aave-v3-core, compound-protocol, Uniswap/v4-core, smartcontractkit/chainlink, balancer-v2-monorepo, rocketpool, curve-contract, LayerZero-v2, hop-protocol/contracts, flashbots/mev-boost, ethereum/consensus-specs, ethereum/execution-specs, foundry-rs/foundry, crytic/slither, cosmos-sdk, cometbft (other), go-ethereum, reth, prysm, nimbus-eth2, beacon-kit, nitro, optimism, scroll, taiko-mono, anza/agave, polkadot-sdk, sui, nearcore, rippled | No fresh open `bug`-label issues in the Sep 1+ window |

Note: the GitHub search API rate limit was hit at the end of the sweep
(2026-10-05 10:06Z); the last three queries (morpho-blue, pendle-core-v2,
etherfi smart-contracts) returned no data and are **not** counted as checked.

## Watch (run 52)
NO changes. 20 BUG FIXER MAN PRs open. AppKit #5813 CTA check still FAILURE
after Kyle's own signature (2026-10-05T09:44:54Z) — stale-check pattern, watch
for the flip. Expensify ×4 REST counts identical (55/35/33/28), no
C+/assignment/hire. NiceGUI #6372 awaiting evnchn re-review; vyper #5294
reviews unchanged (Sporarum COMMENTED + our two replies, latest = the
parallel session's rework note 09:14Z). ESLint #21155 no `accepted`;
stellar #1734 / PyBNF #931 still ours-only. Linkwarden #1855 base=dev,
checks from run 51 stand. HackerOne: ledger-only, no logged-in check.

Payments: $0 requested, $0 received. No X post.
Next run: sector (3) paid bounty platforms & paid GitHub issues.
