# Sector 1 sweep — run 51 (2026-10-05, crypto wallets)

## Watch changes (2)

1. **reown-com/appkit PR #5813 — Kyle signed the Reown CTA himself.** At
   2026-10-05T09:44:54Z Kyle posted "I have read the CTA Document and I hereby
   sign the CTA" on the PR, followed by "recheck" at 09:45:22Z (both via email
   reply, same pattern as his Safe CLA signature in run 23). The agent did not
   sign anything — legal signatures are Kyle's alone. The `CTA` status check
   still read **FAILURE** on re-check minutes later (09:5xZ) — likely the same
   stale-check pattern Safe #1440 showed after signing. Watch next run for the
   flip / a bot all-signed comment.
2. **linkwarden/linkwarden PR #1855 — `check-branches` FAILURE fixed by this
   run.** The repo's `check-branch.yml` policy: "Merge requests to main branch
   are only allowed from dev branch." Our PR targeted `main`. Retargeted the
   PR base `main` → `dev` (`gh pr edit 1855 --base dev`); the PR stayed
   MERGEABLE (no conflicts), the re-run `check-branches` check is **SUCCESS**,
   and `license/cla` is **SUCCESS**. The Playwright workflow shows
   `action_required` (maintainer approval needed for fork PRs — normal, not a
   failure). The old FAILURE entry in the rollup is the superseded main-base
   run.

All other watch items unchanged: 20 BUG FIXER MAN PRs open; Expensify ×4
comment counts identical by REST (55/35/33/28) — no C+ response / assignment /
hire on any; ESLint #21155 still `bug`/`repro:yes`, no `accepted`;
stellar #1734 / PyBNF #931 still 1 comment each (ours); NiceGUI #6372 still
awaiting evnchn re-review; vyper #5294 reviews unchanged (last is ours).
HackerOne: ledger-only (no logged-in check this run).

## Hunt (sector 1 — crypto wallets): NO submission

API-verified sweep (per-repo REST, newest-first) of ~25 wallet repos:
wevm/viem, wevm/wagmi, ethers-io/ethers.js, bitcoinjs/bitcoinjs-lib,
near/near-api-js, anza-xyz/kit, FuelLabs/fuels-ts, XRPLF/xrpl.js,
MystenLabs/ts-sdks, family/connectkit, rainbow-me/rainbowkit,
MetaMask/extension, MetaMask/core, MetaMask/snaps, spesmilo/electrum,
RabbyHub/Rabby, tahowallet/extension, hirosystems/connect, trezor-suite,
paulmillr/scure-* (btc-signer/bip32/bip39/starknet), safe-global/safe-core-sdk,
cake-tech/cake_wallet, BlueWallet/BlueWallet.

Every fresh verifiable bug is already PR'd or a standing reject:

- wagmi #5256 → reporter PR #5257 (run-41 resolution)
- ethers #5193 → PR #5197; #5194 is ours (PR #5198)
- connectkit #520/#521 → PRs #522/#523; #525 no repro (standing)
- rainbowkit #2700 → PR #2702
- safe-core-sdk #1438 → PR #1439; #1424 maintainer design decision (standing)
- bitcoinjs #2350 — defect lives in the varuint-bitcoin dependency (standing)
- xrpl.js #3523–#3528 — audit-spam pattern (rejected run 46)
- ts-sdks #1303 — design/feature (rejected run 37)
- viem #5048 (claimed + design debate), #5064 (no clean payoff — standing)
- Rabby #4156/#4157 — server/RPC-dependent (standing)
- scure-bip32 #29 held watch unchanged (open, 1 comment, updated 2026-09-24)

One genuinely new item checked deep: **MetaMask/metamask-extension #46858**
(filed today 2026-10-05T08:51Z, "Invalid price chart values for BTC") —
REJECTED: historical-price hover values wrong only inside the built extension
against live price APIs; no root cause stated and no local reproduction is
possible in this sandbox (same class as the run-46 #46856 reject).

Payments: $0 requested, $0 received. No X post.
Next run: sector (2) crypto infra / DeFi / chains.
