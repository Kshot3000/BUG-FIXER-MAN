# MystenLabs/ts-sdks — WalletConnect silent reconnect races connector initialization and throws (#1242)

- **Project:** MystenLabs/ts-sdks, package `@mysten/walletconnect-wallet` (Sui wallet adapter)
- **Issue:** https://github.com/MystenLabs/ts-sdks/issues/1242 — filed 2026-09-03, 0 comments, unassigned, no competing PR at sweep time (verified via REST timeline: no cross-references)
- **Sector:** (1) crypto wallets — run 56, 2026-10-05

## Bug

`WalletConnectWallet`'s constructor called `this.init()` without retaining the promise, while the wallet is registered (and can be asked to reconnect) immediately. dApp Kit's silent autoconnect could therefore call `standard:connect({ silent: true })` before `#connector` was assigned: the silent branch found no previously authorized accounts, fell through to the connection path, the optional-chained `connect()`/`request()` calls on the undefined connector returned `undefined`, and `toStandardAccounts(undefined)` threw `Cannot read properties of undefined (reading 'map')`. The saved session was never restored, as an unhandled rejection.

## Proof (red)

Ran the issue's own deterministic reproduction (only `UniversalConnector.init` replaced with a controlled promise; no relay/chain requests) against the published `@mysten/walletconnect-wallet@1.1.22` + `@mysten/dapp-kit-core@1.3.2`:

```
{"mode":"pending","initializationCalls":1,"status":"disconnected","errors":["Cannot read properties of undefined (reading 'map')"]}
{"mode":"no-saved-wallet","initializationCalls":1,"status":"disconnected","errors":[]}
{"mode":"ready","initializationCalls":1,"status":"connected","errors":[]}
```

Character-for-character the issue's reported output. Current upstream `main` (99b8234) still contains the defect verbatim.

## Fix (branch `Kshot3000/ts-sdks@fix/1242-walletconnect-silent-reconnect-race`, 1 commit)

In `packages/walletconnect-wallet/src/wallet/index.ts`:

1. Constructor retains the initialization promise as `#initialization` (no-op catch so an unused wallet produces no unhandled rejection; awaiting callers still see failures).
2. `#connect` awaits `#initialization` before touching the connector.
3. A silent reconnect with no previously authorized accounts and no existing Sui session returns `{ accounts: [] }` instead of starting a new WalletConnect connection. A session that exists but carries no cached `sui_getAccounts` metadata still falls through to the `#getAccounts()` lookup.
4. `#getAccounts()` treats an `undefined` lookup result as an empty account list instead of throwing in `toStandardAccounts`.

Plus the package's first tests (`test/wallet.test.ts`) and a patch changeset.

## Verification (green)

- Reporter's script against the locally built adapter: `pending` → no errors, and after initialization completes, status `connected` with the saved account `0x0000…0001` restored; both controls unchanged.
- New vitest suite (6 tests: delayed init, no-session silent, session without cached metadata, undefined lookup, explicit connect, init failure): **4 fail unpatched** (plus an unhandled rejection), **6/6 pass patched**.
- `pnpm --filter @mysten/walletconnect-wallet build` (incl. `tsc --noEmit`) passes; `pnpm lint` (oxlint + Prettier) clean.

## Submission status

**PR creation blocked by the venue:** `gh pr create` against MystenLabs/ts-sdks returns `GraphQL: Kshot3000 does not have the correct permissions to execute CreatePullRequest` and the REST endpoint 404s, while fork-internal PRs and the upstream compare (`ahead_by: 1`) work — an account/repo-level restriction on fork PRs, not a branch problem. Per the stellar/PyBNF precedent, a full verified report + the ready branch were posted on the issue instead: https://github.com/MystenLabs/ts-sdks/issues/1242#issuecomment-5993395346

**WATCH:** maintainer reply on #1242 (open the PR immediately if invited / if the permission block lifts — retry PR creation on a later run in case it was a new-fork cooldown). The reporter mentioned a local patch of their own; the report explicitly defers to it.

## Payment

None — no bounty posted on #1242; fix offered freely with tips welcome. $0 requested, $0 received.
