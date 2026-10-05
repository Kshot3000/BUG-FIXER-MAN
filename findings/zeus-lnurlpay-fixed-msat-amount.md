# ZeusLN/zeus — LNURL-pay fixed amounts that are not whole sats are sent rounded down (#4828)

- **Project:** ZEUS (Bitcoin/Lightning wallet, React Native/TypeScript) — https://github.com/ZeusLN/zeus
- **Issue:** https://github.com/ZeusLN/zeus/issues/4828 (filed 2026-10-03 by TheSeydiCharyyev, labels Bug/LNURL/LNURL-Pay/Amounts, unassigned, 0 comments, no competing PR; full jest repro supplied in the issue)
- **Submission:** **BLOCKED BY VENUE — ZeusLN has blocked the Kshot3000 GitHub account.** `gh pr create` returned `GraphQL: User is blocked (createPullRequest)` and a single issue comment offering the branch returned `GraphQL: User is blocked (addComment)`. No PR, no comment, no other channel attempted (no DMs, no alt accounts — a block is a final answer). This also retroactively explains PR #4827 being closed unmerged by the maintainer on 2026-10-03. **Zeus is a closed venue for this program — do not hunt there again.**
- **Ready branch (verified fix, on Kyle's fork):** `Kshot3000/zeus@fix/lnurlpay-fixed-msat-amount` — commits `2ae34dc` (fix) + `5983762` (tests), based on upstream master `2bf5a6c`. Patch: `fixes/zeus-lnurlpay-fixed-msat-4828.patch`.

## Bug

A fixed LNURL-pay request (`minSendable = maxSendable`) is denominated in msat and is not always a whole number of sats. In `views/LnurlPay/LnurlPay.tsx`:

- `stateFromProps` computed `Math.floor(lnurl.minSendable / 1000)` and used it for both the locked input and `state.satAmount`.
- `sendValues` converted back with `satAmount * 1000`.

So 12618500 msat → the callback was called with `amount=12618000` (500 msat below `minSendable`; a range-checking server rejects it), 1001 msat → `amount=1000`, and a fixed 500 msat request floored to 0 sats, which kept Confirm disabled — unpayable. Rounding up instead would not help either: for a fixed non-whole-sat amount there is no whole-sat value inside the range. The only correct amount is `minSendable` itself.

## Proof (local, red → green)

Five new tests in `views/LnurlPay/LnurlPay.test.ts` press Confirm against a mocked callback fetch and assert the exact `amount` in the callback URL (the issue's own repro approach):

- On master `2bf5a6c`: the state-precision test and all three sub-sat callback tests **fail** exactly as reported (floored state `12618`, callback `12618000` / `1000`, 500 msat Confirm disabled); the whole-sat control passes; all 20 pre-existing tests pass.
- With the fix: **views/LnurlPay suites 35/35**; **full jest suite 2190/2190 tests pass** (106/107 suites — `stores/startupWalletSelection.test.ts` fails to load in this sandbox on the `LndMobile` NativeEventEmitter invariant, byte-identical on the clean tree with postinstall skipped; unrelated env artifact). `tsc --noEmit`, ESLint, and Prettier clean on the changed files.
- Environment notes: `/tmp` (512M shared tmpfs) filled and wiped the first clone mid-run — work moved to the goal's hidden_files on the home filesystem with `TMPDIR=~/.cache/bfm-tmp`; yarn 1.22 via npx, `--ignore-scripts` install (skips pod-install/native setup).

## Fix

In `views/LnurlPay/LnurlPay.tsx` (see `fixes/zeus-lnurlpay-fixed-msat-4828.patch`):

1. `stateFromProps` fixed branch: keep the exact value `lnurl.minSendable / 1000` sats (fractional sats included) for the locked input and `state.satAmount`, instead of the floored `minSendableSats`. ZEUS already renders fractional sats (msat display support in `AmountUtils.processSatsAmount`); whole-sat fixed requests are byte-for-byte unchanged.
2. `sendValues`: `qs.amount = Math.round(parseFloat(satAmount.toString()) * 1000)` — msat is the smallest unit the callback takes, and rounding keeps float error out of the URL (`1.001 * 1000 = 1000.9999999999999` in JS, which the old `Number((...).toString())` passed through verbatim). Variable requests are unaffected: their amounts are entered in whole sats.
3. No Confirm-logic change needed: with satAmount `0.5` for a 500 msat request, the existing `!satAmount || satAmount == 0` disabled check is naturally false.

## Submission status / payment

- Submitted: **nowhere — venue blocked the account at the GitHub level** (verified twice, 2026-10-04 run 21). Verified branch stands on the fork if the block is ever lifted or the fix is wanted elsewhere.
- No bounty was posted on #4828. **Payment requested: none. Received: none.**
- Venue intel: **ZeusLN/zeus is closed to Kshot3000** (org block). Do not target again; do not attempt contact through other channels.
