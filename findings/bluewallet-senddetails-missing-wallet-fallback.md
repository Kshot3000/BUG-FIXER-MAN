# BlueWallet — Send silently falls back to another wallet when the requested wallet ID is missing

- **Project:** BlueWallet/BlueWallet — https://github.com/BlueWallet/BlueWallet
- **Issue:** #8879 — "FIX: Send falls back to another wallet when the given wallet ID is missing" https://github.com/BlueWallet/BlueWallet/issues/8879 (open, unassigned, 0 comments; filed as the follow-up to merged #8861, which fixed the derivation-path ID change that used to trip this fallback)
- **Submission:** **PR #8985 OPEN (2026-10-04): https://github.com/BlueWallet/BlueWallet/pull/8985** (fork branch `Kshot3000/BlueWallet@fix/send-details-missing-wallet-id`, commit 1c470e5)
- **Bounty:** none — OSS fix offered freely, tips welcome.
- **Status:** PR #8985 OPEN, awaiting maintainer review + CI.

## Bug

In the mount effect of `screen/send/SendDetails.tsx` (master a7fe068, line 258):

```ts
const newWallet = (routeParams.walletID && wallets.find(w => w.getID() === routeParams.walletID)) || suitable[0];
```

If Send is opened with a `walletID` that matches no wallet, `find` returns `undefined` and the expression silently selects `suitable[0]` — the first spendable on-chain wallet, which can be completely unrelated (the reporter gives: a hot wallet while the user was acting on a watch-only wallet). The Send screen shows that wallet's name, but there is no error and nothing tells the user they are about to spend from a different wallet than the one they opened.

## Fix

Per the issue's stated expected behavior:

- `walletID` given but not found → error haptic + alert (new string `send.details_wallet_not_found`: "The requested wallet could not be found.") + `navigation.goBack()`, mirroring the existing no-suitable-wallet handling directly above. The string is added to `loc/en.json` only; `loc` is typed via `LocalizedStrings<typeof enJson>`, so it is picked up automatically.
- No `walletID` (payment-URI flow) → unchanged, defaults to `suitable[0]`.
- `walletID` matches → that wallet, exactly as before (the found wallet is still looked up across all wallets, not just suitable ones — watch-only send flows are untouched).

Diff: `screen/send/SendDetails.tsx` (+11/−1), `loc/en.json` (+1).

## Verification

- **Logic harness (red→green):** the verbatim pre-fix expression and the post-fix logic were run against mock wallets. Pre-fix: a bogus `walletID` selected `suitable[0]` (the wrong hot wallet) — the reported bug. Post-fix: bogus `walletID` → error + goBack, nothing selected; valid `walletID` → that wallet; no `walletID` → first suitable; no suitable wallets → the pre-existing `details_wallet_before_tx` error. All non-bug cases identical pre/post.
- **Syntax:** `SendDetails.tsx` passes a TypeScript `transpileModule` check (typescript 5.9.2) with 0 diagnostics; `loc/en.json` parses as JSON; the repo's `scripts/find-unused-loc.js` passes (the new key is used).
- **Honest limitation:** the full `npm ci` (and therefore the repo `tsc`/jest/eslint suite) could not be run in this sandbox — npm's git-dependency preparation fails deterministically here with `EPERM` on a `chown` syscall inside the `expo-module-scripts` git dependency (reproduced 3×, unrelated to this change; the first attempt also hit a root-owned `~/.npm` cache). This is disclosed in the PR; BlueWallet CI is the authoritative suite run.

## Same-run rejects (sector 1, crypto wallets)

- **spesmilo/electrum #10908** (swapserver reverse swap never claimed after locktime expiry): maintainer ecdsa has already ruled the core behavior **not a bug** (revealing the preimage near expiry risks the client settling the LN payment *and* refunding; only the per-block warning spam "might need to be investigated"). The intentional-behavior ruling plus an ambiguous spam-only scope makes a fix PR a poor bet — skipped.
- **BlueWallet #8882** (same key in different forms double-counts balance): the reporter themselves flags it may be by design (seed wallet + watch-only copy of its own xpub is a wanted setup) and suggests at most a warning — no clean fix to ship.
- **cake-tech/cake_wallet fresh bugs** (#3622 Nano work-server 402, #3613 ZEC viewkey import, #3495 notes lost on restart): all need a Flutter/Dart toolchain + device/node state to verify honestly; not feasible in this sandbox this run.
