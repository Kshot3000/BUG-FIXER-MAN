# viem — `waitForUserOperationReceipt` never resolves after concurrent waits (#5175)

- **Project:** wevm/viem (Ethereum TypeScript client library — crypto infra)
- **Issue:** https://github.com/wevm/viem/issues/5175 (filed 2026-10-02, unassigned, no competing PR at claim check)
- **Fix PR:** https://github.com/wevm/viem/pull/5176 — OPEN, submitted 2026-10-02
- **Patch:** fixes/viem-wait-for-user-operation-receipt-stale-listener.patch

## Bug
After two concurrent `waitForUserOperationReceipt` calls for the same hash on the same bundler client resolve, a later call for that hash never resolves and sends no request.

## Root cause
Concurrent calls share one observer via `observe()` (`src/utils/observe.ts`). The poller's `done()` only calls the first caller's `unobserve`, so the second caller's listener stays in `listenersCache` forever. A later `observe()` with the same observer id sees the stale listener, returns early without running the poll function, and its promise never settles — its timeout is never even armed, because the timeout is created inside the poll function.

## Fix
Each caller removes its own listener when its promise settles: the action captures its own `unobserve` handle and returns `promise.finally(() => unobserve())`. `unobserve` is idempotent, so the existing `done()` cleanup is unaffected, and concurrent callers still share a single poll (1 request per batch). Changeset (`patch`) included. A regression test was added to the project's bundler test harness (two concurrent waits, then a later wait for the same hash must resolve).

## Proof (all local, 2026-10-02)
- Reporter's exact snippet against the published `viem@2.57.2` build: concurrent waits resolved with 1 request; later wait sent no request and never settled. With the fix applied to that build, the later wait polls again (2nd request) and resolves.
- Reject path on the patched build: two concurrent waits that time out both reject with `WaitForUserOperationReceiptTimeoutError` and clean up; a later wait then resolves; a single wait still works.
- Red/green against the TypeScript source (sparse clone of `main` @ 26d5bd2) with a stub `custom` transport: regression test hangs on unpatched source (failed at the 60s test timeout — the promise never settles) and passes with the fix; `src/utils/observe.test.ts` 10/10 pass; `tsc --noEmit -p src/tsconfig.json` clean; Biome clean on changed files.
- Honest gap: the harness regression test added to the PR needs the anvil/bundler fork setup and was not run locally; it relies on CI. The equivalent scenario was run red/green locally as described above.

## Payment
None requested — viem has no bounty program for this issue; fix offered freely, tips welcome via the hub README. Nothing received.
