# safe-global/safe-core-sdk — `TransactionOptions.nonce: 0` dropped when converting execution options

- **Project:** Safe{Wallet} Core SDK (`@safe-global/protocol-kit`)
- **Issue:** https://github.com/safe-global/safe-core-sdk/issues/1425 (filed 2026-09-06, unassigned; the 1 comment traced the conversion path but opened no surviving PR)
- **PR:** https://github.com/safe-global/safe-core-sdk/pull/1440 — OPEN (2026-10-04, run 22), base `development` per the repo CONTRIBUTING
- **Payment:** none posted on the issue; fix offered freely, tips welcome. **$0 requested, $0 received.**
- **Patch:** `fixes/safe-core-sdk-1425-nonce-zero.patch` (fork branch `Kshot3000/safe-core-sdk@fix/1425-nonce-zero`, commit ef0524f3)

## Bug

`createLegacyTxOptions` and `createTxOptions` in `packages/protocol-kit/src/utils/transactions/utils.ts` copied the caller's nonce only under a truthiness guard:

```ts
if (options?.nonce) {
  converted.nonce = options.nonce
}
```

`nonce: 0` is a valid EOA nonce — a fresh signer's first transaction, local/dev chains, deterministic tests — but `0` is falsy, so an explicit `nonce: 0` passed to `execTransaction` (which reaches these helpers via `BaseContract.convertTransactionOptions`) was silently dropped and the wallet/provider chose the nonce instead.

## Proof (red → green, on `development`)

Verified with the repo's pinned Node v20 (`.nvmrc`; the sandbox's default Node 24 makes mocha load tests as ESM and bypasses tsconfig-paths, breaking even the pre-existing suite — a Node 20.19.5 was installed alongside for this run):

- New unit tests `packages/protocol-kit/tests/unit/tx-options.test.ts` (9 tests: nonce 0 / non-zero / omitted for both converters + the `convertTransactionOptions` dispatcher).
- **Unpatched:** exactly the 4 nonce-0 tests fail — `AssertionError: expected undefined to equal +0`.
- **Patched:** full protocol-kit unit suite **49 passing, 0 failing** (40 pre-existing + 9 new). Prettier and ESLint clean on the changed files.

## Fix

Guard on `options?.nonce !== undefined` in both helpers (2 lines). A patch changeset for `@safe-global/protocol-kit` is included, per repo convention.

## Prior attempt, acknowledged in the PR

devtechedge's PR #1426 implemented the same fix with CI green and the CLA signed, then **closed it themselves, unmerged and unreviewed, on 2026-09-23** after a ping went unanswered. The bug is still on `development` and #1425 is still open, so #1440 re-submits the fix and explicitly defers to the original author if they would rather revive #1426.

## Open maintainer-side step

Safe uses CLA Assistant: the CLA signature comment on the PR is a legal agreement and is **Kyle's to post personally** (flagged in the PR body). Until then the CLA check may sit pending — no code action needed.

## WATCH

Maintainer review + CI on #1440; CLA prompt (Kyle action).

## Same-run sector-2 rejects / intelligence

- **MystenLabs/ts-sdks scan discarded:** a parallel `gh issue list` sweep returned plausible-looking issue numbers/titles for ts-sdks that do not exist — every number checked via the REST API (`#995/#1002/#1032/#979/#850`) is a PR with a different title, and title searches find nothing. Do not trust multi-repo `gh issue list` loop output without per-item API verification (same class as the run-19 lesson). No Mysten target was pursued on unverified data.
- wormhole-foundation/connect-sdk and across-protocol/sdk: no open `bug`-label issues at all.
- safe-core-sdk #1438 (connect() drops signer): reporter's own fix PR promised in the issue — taken. #1424 (generateHash hex-char truncation): reporter explicitly wants a maintainer decision before any behavior change, companion docs PR #1423 open — design territory, skipped.
