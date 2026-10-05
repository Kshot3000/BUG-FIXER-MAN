# SocketDotTech/socket-plugs — yield-limit retry cache stores consumed shares as pending (run 77, 2026-10-05)

- **Issue:** https://github.com/SocketDotTech/socket-plugs/issues/161 (filed 2026-09-13 by chenshj73, 0 comments, unassigned, no competing PR — open-PR list and issue timeline checked)
- **PR:** https://github.com/SocketDotTech/socket-plugs/pull/162 — OPEN / MERGEABLE, base main, head e1446a0
- **Sector:** (2) crypto infra / DeFi / chains

## Bug
`Controller_YieldLimitExecHook.dstPostHookCall` (contracts/hooks/Controller_YieldLimitExecHook.sol) splits a partially pending destination mint into consumed/pending shares, but computed:

```solidity
// totalShares * consumedU / totalU
uint256 consumedShares = (params_.transferInfo.amount *
    pendingUnderlying) / depositUnderlying;   // pending, not consumed
pendingShares = params_.transferInfo.amount - consumedShares;
```

so `consumedShares` actually held the pending portion and `pendingShares` the consumed one. Downstream, all three consumers were swapped: `identifierCache` cached the consumed shares as the retry amount (a later `preRetryHook` would release them a second time and the truly pending shares would never be released), `connectorCache` grew by the consumed amount, and `TokensPending` reported the two swapped. The `transfer(receiver, consumedUnderlying)` release uses the underlying amount directly and was unaffected. Pattern cross-checked against the base `LimitExecutionHook`/`LimitHook`, which cache the pending amount directly.

## Fix
One word: `pendingUnderlying` → `consumedUnderlying` in the formula, exactly as the inline comment states. Regression test `testDstPostHookForDepositPartiallyPending` added to test/hooks/YieldTokenLimitExecutionHook.t.sol.

## Proof (red → green, Foundry, solc 0.8.13)
Setup's receiving limit is 100; a 150 deposit splits 100 consumed / 50 pending, shares 1:1.
- Unpatched: new test fails — cached pendingShares **100** (expected 50), connectorCache `abi.encode(100)` (expected 50). (Balance assertions were dropped from the test: the yield token revalues balances when dstPre adds underlying, so they are conversion-dependent and noisy on both versions.)
- Patched: new test passes; `TestController_YieldLimitExecHook` 20/20; full repo `forge test` **103 passed / 0 failed**.

## Payment
No bounty posted on #161; fix offered freely, tips welcome via the hub README. $0 requested, $0 received.

## Same-run sector-2 rejects
- cometbft #5902 (evidence hash 1 byte off) → reporter's PR #6090 already open; #6023 (unbuffered WS subscription stall) → PR #6024 already open.
- celestia-node/app queues: flaky tests, audit-tracking fibre items (maintainer territory), #8031 reporter's pattern.
- wormhole main repo queue: re-observation requests only. hyperlane bugs stale (2024–25). eigenlayer/morpho/aave bug queues empty.
- Nethermind fresh bugs are C# node internals (no tractable local verification here); lighthouse/prysm fresh bugs claimed by existing contributors; stacks/hiero/flow queues heavy protocol/live-network or maintainer-contested (flow #8476 already rejected run 72); OZ #5793 theoretical overflow/design.
- snarkjs/circomlib/0x/dydx/rainbowkit/wagmi bug queues empty; LI.FI/Across gh calls errored (repo resolution), not pursued after the socket-plugs find verified.
