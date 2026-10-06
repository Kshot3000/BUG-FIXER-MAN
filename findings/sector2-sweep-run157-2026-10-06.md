# Sector-2 sweep — run 157 (2026-10-06)

Sector: (2) crypto infra / DeFi / chains. **No submission** — every fresh candidate was direct-verified singly and rejected below. Watch: NO changes (open-PR count 81; all named PRs identical; Expensify 60/43/33/38; held items identical).

## Deep-checks

- **Consensys/teku #11431** (filed today by tbenr): DiscV5Service builds the initial ENR with the TCP port even when TCP is disabled; the address-update handler respects `isTcpEnabled()`, so a QUIC-only node advertises a dead TCP port until discovery changes its address. Real bug, fully diagnosed — REJECTED: the issue itself carries an explicit release gate ("Do not ship this before #11420 is widely deployed" — removing TCP would hide the node from pre-#11420 receivers), it is one of a coordinated maintainer series (#11427–#11431, same reporter), and it is Java with no JDK in this sandbox (standing gate). #11427–#11430 are diagnostics/feature-shaped items from the same series.
- **lidofinance/core #1984** (filed today by avsetsin): `Lido.getFeeDistribution()` returns treasury/operator proportions swapped (router returns `(modulesFee, treasuryFee)`, Lido assigns them reversed). Root cause fully spelled out by the reporter — REJECTED: the issue itself states the impact is "incorrect output from a deprecated view; core reward distribution does not use this getter," and the code lives in the frozen legacy `contracts/0.4.24/` directory. No competing PR, but a drive-by variable swap on a deprecated getter in a frozen legacy contract is not a submittable fix here.

## Queue scan (all direct-verified)

- celestia-node, lighthouse, reth, geth, nethermind, prysm, sui, nearcore, agave, lodestar, morpho, scroll, polkadot-sdk: fresh-issue heads empty.
- cosmos/ibc-go #9114: known — already fixed by PR #9115.
- cometbft #6098 / #6093: known design / known PR'd items.
- ethereum-optimism/optimism #23234: kona-interop ZK-proofs internal item.
- hyperledger/besu #11496 / #11493 / #11492: fresh but Java snap-sync/BFT internals — no JDK here, deep sync machinery not verifiable in one run.
- aptos-core #20689: Move prover internals (opaque-callee purity) — not locally verifiable.
- wormhole: re-observation requests only.
- cosmos-sdk #26855, zksync-era #4952, Uniswap v4-core #1078, balancer #2664: Oct-2 "machine-proven" proof-exercise batch.
- compound-protocol fresh head: bounty-claim/audit spam (#315/#308/#307/#306).
- aave-v3-core: stale 2025 items only.
- linea-monorepo #4134: assigned design item.
- OffchainLabs/nitro #4760: known (→ PR #4761).

## Held items re-checked (unchanged)

- sigp/lighthouse #10226: still 1 comment, 0 assignees — claim watch continues.
- SatoshiPortal/bullbitcoin-mobile #2902: labels=["bug"] only, assignees=[] — HELD stands (venue 'ready'-label gate).
- formbricks/formbricks #9526: still 3 comments.

Payment: none requested, none received. $0 all-time received stands.
