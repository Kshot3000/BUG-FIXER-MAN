# Sector-2 sweep — run 122 (2026-10-06, crypto infra / DeFi / chains)

**Outcome: NO submission.** Fresh bug queues swept across ~40 infra/DeFi/chain repos (direct per-repo issue listings, created ≥2026-10-03, candidates cross-checked for competing PRs and assignment). Every candidate was already ours, already PR'd, assigned/reporter-owned, maintainer/ZK/design territory, Java/.NET (no toolchain in this sandbox), or a live-network request.

## Candidates assessed

- **celestiaorg/celestia-node #5310** (shrex getter: empty-block short-circuit skips index validation — `GetRow` returns an unverifiable empty row for any index instead of `ErrOutOfBounds`; `GetSamples` with a negative row panics) — the best fresh candidate this run, with a precise location and expected behaviour. **Rejected: assigned to the reporter (Shailu-s), who states "I have a fix with tests ready and will open a PR," and PR #5311 is already cross-referenced.** Reporter-owned.
- **ethereum-optimism/optimism #23208** (ZKDisputeGame: a respected game can use an unrespected game as its parent) — assigned to maintainer Inphi, competing PR #23210 already open. **#23204/#23206/#23207/#23209** (kona-sp1 / kona-interop ZK proof items) — deep ZK prover internals, maintainer territory. #23213 is ours (PR #23214), #23211 already has PR #23212.
- **foundry-rs/foundry #17388** (`cast call` prompts for a keystore password even with `ETH_FROM` set) — assigned (stevencartavia) with competing PR #17404 already open. **#17313** (anvil storage read for the head block answered from the next block while it is being built) — a timing race in a huge Rust workspace; not deterministically verifiable here. #17405 is a CI flaky-test notice.
- **Consensys/teku #11412** (primitive progressive list serialization includes padding after backing-node reload) — standing reject: reporter-claimed with a patch offered in-thread, and Java with no JDK in this sandbox. Rest are spec-version/testing chores.
- **hyperledger/besu #11474/#11475/#11480** — all Java, no JDK here; #11480 additionally self-spells its fix pattern (standing reject class).
- **sigp/lighthouse #10214** (SSE channel capacity drops `payload_attestation_message` events) — standing design/devnet item. **OffchainLabs/prysm #17619** — live validator timing, not locally verifiable; #17613 is ours (PR #17626). **OffchainLabs/nitro #4760** — already fixed by PR #4761 (standing). **paradigmxyz/reth** fresh queue is only our own #27734.
- **wormhole-foundation/wormhole #5021–#5028** — all live-network re-observation requests (expired guardian sets), not code bugs. **NethermindEth/nethermind** fresh = Docker-page link, ignored/flaky tests, and #14235 (discv4, C# — no .NET toolchain here). **Consensys/linea-monorepo** fresh = internal design/review tickets (#4134/#4126/#4122). **smartcontractkit/chainlink #23896** — internal [SMRT] deployment ticket. **stacks** fresh = flaky signer tests; **aptos #20672** = Move-prover/Boogie crash (heavy prover toolchain); **celestia-app** fresh = flaky nightly races + a perf item.
- Queues empty of fresh bugs: cometbft, cosmos-sdk, ibc-go, go-ethereum, agave (feature/perf tasks), sui, nearcore, zksync-era, scroll, LayerZero-v2, safe-contracts, snowbridge, axelar-core, aave-v3-core, Uniswap v3-core/sdks, balancer-v2, hyperlane, morpho-blue, compound-protocol, superfluid, socket-plugs (only our own history), berachain/beacon-kit, mev-boost, cosmos/evm, evmos.

## Status watch (run 122)

**ONE substantive change + one minor maintainer exchange; bot-only comments on two new PRs.**

- **spesmilo/electrum PR #11012 CLOSED unmerged** (2026-10-06T09:31Z) by f321x with the sole comment "slop, replaced by https://github.com/spesmilo/electrum/pull/11017". The maintainer replaced our fix with their own PR. No reply sent (closed PR; no arguing/nagging per standing rules). This closes the electrum watch pair: #11013 was closed unmerged in run 117, #11012 now likewise.
- **vyperlang/vyper PR #5294 comments 1 → 2:** charles-cooper replied (09:44Z) to Sporarum's run-113 scope question ("how can line feeds break comments? maybe we should actually not be using splitlines or something?") — a maintainer-to-maintainer design exchange, not directed at Kshot3000; no reply sent.
- **Bot-only activity (not changes):** wevm/viem PR #5196 gained vercel[bot] / changeset-bot / pkg-pr-new comments (no human review); TriliumNext/Trilium PR #11920 gained a greptile-apps[bot] summary (no human review).
- All other PRs direct REST-verified identical to run 121: dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 OPEN c=1, cake #3671 OPEN c=0; optimism #23214 OPEN c=0, diffy #89 OPEN c=0, prysm #17626 OPEN c=1 (CLA-assistant not-signed = Kyle's step), memos #6435 OPEN c=2, NiceGUI #6372 OPEN c=1 (evnchn APPROVED stands — awaiting merge), ansible #87642 OPEN c=1, vikunja #4107/#4110 OPEN c=0.
- Expensify identical (direct listings, per_page=100): #102072 60 (tail unchanged — github-actions[bot] + bconnnnn, known), #101684 42, #102044 30, #102226 38 — no selection/hire, no melvin-bot prompt to Kshot3000.
- HackerOne: ledger-only (no signed-in browser check this run; ID-verification confirmation still pending — Kyle's step).

$0 requested, $0 received this run. Next run: sector (3) paid bounty platforms & paid GitHub issues.
