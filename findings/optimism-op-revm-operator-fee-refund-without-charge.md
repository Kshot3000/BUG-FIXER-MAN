# ethereum-optimism/optimism — op-revm refunds an operator fee that was never charged

- **Issue:** https://github.com/ethereum-optimism/optimism/issues/23213 (filed 2026-10-06 by ariescodescream, 0 comments, unassigned, no competing PR at submission time)
- **PR:** https://github.com/ethereum-optimism/optimism/pull/23214 — OPEN / MERGEABLE, base `develop`, commit 47168b1 (GitHub-verified signature, valid)

## Bug

`L1BlockInfo::operator_fee_charge` returns zero when the transaction's enveloped bytes are empty (or a deposit), but `operator_fee_refund` never looked at the envelope — it always refunded `fee(gas_limit) − fee(gas_used)`. op-reth builds RPC transactions with `enveloped_tx: Some(Bytes::new())`, and `eth_simulateV1` does not set `disable_fee_charge`, so after Isthmus every simulated call credited the sender an operator fee it never paid, and later calls in the same simulation saw the inflated balance. Block execution is unaffected (real transactions carry a non-empty envelope; deposits are excluded in `reimburse_caller`).

## Proof (red → green, on `develop` dfe4f947ca — the exact commit the issue names)

- Issue's handler-level regression test, unpatched: **fails** — `sender gained 7946 from an operator fee it never paid` (balance 1,000 after charge → 8,946 after refund; gas limit 100,000, spent 21,000, scalar 10,000,000, constant 50).
- Patched: balance after refund equals balance after charge; test passes.
- New unit test `test_operator_fee_refund_without_charge` (empty and `0x7E`-prefixed inputs refund zero).
- Full suite: `cargo test -p op-revm --lib` — **91 passed, 0 failed** (operator-fee subset 6/6, including the updated deposit/dyn-fee handler cases).

## Fix

Mirror the charge guard in the refund: `operator_fee_refund` now takes the enveloped bytes (`input: &[u8]`) and returns zero for an empty or deposit-prefixed input — the same condition `operator_fee_charge` applies. `OpHandler::reimburse_caller` passes `tx.enveloped_tx()` through (missing envelope treated as empty). Note: this is a signature change to a public op-revm API, disclosed as a breaking change in the PR; in-repo callers are confined to `rust/op-revm`.

## Sector-2 sweep notes (run 117, no other submission)

- optimism #23211 (static peer re-dial) already has the reporter's PR #23212; #23209 is a maintainer ZK proof-cost design item.
- lighthouse #10214 known SSE-capacity design; besu #11474/#11475 are deep EVM/snap items in Java (no JDK in this sandbox); prysm bug queue is stale May gloas items; cometbft #6098 protocol design, #6023 already PR'd; celestia #8031 already fixed by PR #8032; wormhole fresh items are live-network re-observation requests, not code bugs.
- DeFi queues: Uniswap v4 #1078 / balancer #2664 / lido #1981 are machine-proof exercise posts; compound queue is bounty-claim spam; morpho/chainlink/hyperlane/sui/ibc-go queues empty.

## Payment

No bounty posted on #23213; fix offered freely with tips welcome via the PR footer. $0 requested, $0 received.
