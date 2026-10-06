# trezor/trezor-suite — EIP-7708 pseudo-token trips the fake-token phishing filter

- Issue: https://github.com/trezor/trezor-suite/issues/33233 (filed 2026-10-06, 0 comments, unassigned, no competing PR; cross-reference is the upstream data issue trezor/blockbook#1845, not a fix)
- PR: https://github.com/trezor/trezor-suite/pull/33235 — OPEN / MERGEABLE, commit `b0703a2` (GitHub-verified)

## Bug
EIP-7708 (Glamsterdam) makes every nonzero ETH transfer emit an ERC-20-shaped `Transfer` log from the system address `0xfffffffffffffffffffffffffffffffffffffffe`. Blockbook indexes it as a token transfer of an unnamed pseudo-contract. Suite's `filterTokenTransfers` kept it, so:
- an ETH receipt through a contract call (top-level `amount: '0'`, ETH arriving as an internal transfer, exactly one "token" transfer — the pseudo one) was flagged by `isFakeTokenPhishing` and hidden by default on every network with `coin-definitions`;
- plain ETH transfers gained an unnamed token line.

## Fix
`filterTokenTransfers` (`packages/blockchain-link-utils/src/blockbook.ts`) drops transfers whose `contract` is the EIP-7708 system address (case-insensitive; exported as `EIP7708_SYSTEM_ADDRESS`). This is the Suite-side filter the issue proposes — safe regardless of the Blockbook version Suite talks to. The ETH movement stays represented by amount/targets and `internalTransfers`.

## Proof (red → green, real sources)
Standalone tsx harness loading the REAL `blockbook.ts` plus the REAL fake-token detector from `@suite-common/token-definitions` (two faithful one-function shims for `@mobily/ts-belt` `D.isEmpty` and the wallet-utils NFT-standard set / contract-address lowercasing):
- Pristine: pseudo-token kept (incl. checksummed case), transformed tx `tokens=[pseudo]`, detector `isPhishing: true` — 4/4 checks FAIL.
- Patched: pseudo-token dropped, real token kept, `tokens=[]`, `isPhishing: false` — 4/4 PASS.
- Repo `blockbook.test.ts` executed in the same harness: 53/53 pass (incl. 2 new fixtures).
- Honest limitation disclosed in the PR: full workspace jest NOT run (no monorepo install in sandbox) — CI authoritative. Repo AGENTS.md followed: PR description carries the required agent prefix; no comments posted; nothing approved/merged.

## Payment
No bounty posted on #33233; fix offered freely with tips welcome via the PR footer. $0 requested, $0 received.
