# wevm/viem — `waitForCallsStatus` concurrent waits share the first call's options, and a later wait hangs

- **Project:** wevm/viem (TypeScript Ethereum client; crypto wallets sector)
- **Issue:** [#5195](https://github.com/wevm/viem/issues/5195) — filed 2026-10-06, 0 comments, unassigned, no competing PR at submission time
- **PR:** [#5196](https://github.com/wevm/viem/pull/5196) — OPEN / MERGEABLE, base `main`, commit `62eeb4c` (SSH-signed, GitHub-verified)

## Bug

Concurrent `waitForCallsStatus` calls for the same `id` on one client share one
observer via `observe()`, keyed only by `['waitForCallsStatus', client.uid, id]`:

1. **First call's options win for everyone.** The shared polling closure captures
   the first caller's `status`, `throwOnFailure`, `retryCount`, `retryDelay` and
   `pollingInterval`, and `emit.resolve` settles every joined caller with that
   closure's result — a default-status wait resolved with a pending (100) result
   because a concurrent wait passed `status: () => true`.
2. **A later wait hangs.** The poller's `done()` only calls the *first* caller's
   `unobserve`, so the other callers' listeners stay in `listenersCache` forever.
   A later `observe()` with the same id sees the stale listener, returns early
   without running the poll function, and sends no request — the wait only fails
   with `WaitForCallsStatusTimeoutError`.

Same pattern as viem #5176 (merged) fixed for `waitForUserOperationReceipt`, and
#5142, which keyed `waitForTransactionReceipt`'s observer by its options.

## Proof (red → green)

- Issue's standalone reproduction script (custom transport answering
  `wallet_getCallsStatus` from a status sequence), run with `tsx` against the
  repo source at 2.57.3:
  - Unpatched: `1. default status: 100` (expected 200);
    `2. later wait: WaitForCallsStatusTimeoutError, 0 requests` (expected 200).
  - Patched: `1. default status: 200`; `2. later wait: 200, 1 request`.
- New vitest regression tests in `src/actions/wallet/waitForCallsStatus.test.ts`
  (`behavior: concurrent waits resolve according to their own options`,
  `behavior: resolves a later wait after concurrent waits`):
  unpatched 2 failed / patched 2 passed (run with `SKIP_GLOBAL_SETUP=true` —
  the harness `beforeEach` otherwise requires a forked anvil this sandbox
  cannot reach; the new tests need no chain).
- `biome check` on both changed source files: clean.

## Fix

- Observer id now includes the behavior-defining options (`pollingInterval`,
  `retryCount`, `throwOnFailure`, and the `status`/`retryDelay` function
  sources), so concurrent calls with different options each run their own
  poll. `timeout` is excluded: it is enforced per caller by each call's own
  timer.
- The action returns `promise.finally(() => unobserve())`, so every caller
  removes its own listener when its promise settles.
- Changeset included (patch). The reporter's side question (retrying a failed
  bundle under `throwOnFailure`) is explicitly left untouched.

## Payment

None — no bounty posted on #5195; fix offered freely, tips welcome.
Tips (only where the channel allows): PayPal kyleblake0659@gmail.com ·
BTC 3GnR7TWBXAB3pPztBWpNF4LMNEX5yX8vZK ·
ETH 0xA1d3CEB7bD707847c3c6aB59d30D385FE8DD85Fc ·
SOL DLg1ua1ufewQ81J7dQomwWhXzhZreq4jEwTaQJR31Exb
Attribution: GitHub Kshot3000, X @kshot9000.
