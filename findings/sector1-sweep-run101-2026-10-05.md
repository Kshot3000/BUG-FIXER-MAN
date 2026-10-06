# Sector-1 sweep — run 101 (2026-10-05 ~23:03 CDT)

Sector rotation: (1) crypto wallets. **No submission this run.**

## Status watch
- **NO changes** on any watched PR (direct REST): dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 OPEN c=1, cake #3671 OPEN c=0, electrum #11012 OPEN c=0, ansible #87642 OPEN c=1, NiceGUI #6372 OPEN c=1 reviews 4 (evnchn APPROVED stands, awaiting merge), vyper #5294 OPEN reviews 3, AppKit #5813 c=5, vikunja #4107 / socket-plugs #162 / gitea #39611 / payload #18509 / chatwoot #16130 / gofactory #67 all OPEN c=0.
- Expensify counts identical to run 100 (per_page=100 direct listing): #102072 60, #101684 41, #102044 30, #102226 38 — no C+ selection/assignment/hire, no melvin-bot prompt to Kshot3000.
- HackerOne: ledger-only (no browser check this run).

## Hunt — fresh issues (created ≥2026-10-02) across ~20 wallet repos
Method note: the search API returned HTTP/2 PROTOCOL_ERROR on every query this run; fell back to per-repo `gh issue list` (created-desc), direct-verified each candidate by REST. Everything fresh was team-owned, already PR'd, by-design, or not locally verifiable:

- **MetaMask/metamask-extension #46870** (2026-10-05) — "Deposit value not respected when changed, sending the old amount": labels Sev1-high + release-blocker, found in internal release testing, 0 comments. The owning teams' (money-movement/confirmations) release blocker on an unreleased build; the deposit confirm flow is not reproducible/verifiable in this sandbox. Not an external target.
- MetaMask ext #46858 (BTC price-chart values) / #46856 (wrong native balance blocks confirmation) — data/API-driven reports, no code-level repro in the issue.
- MetaMask/core #10682 — on-chain EIP-7702 sweeper incident report (known reject, not a code bug); #10667 dep-data in another package (known reject).
- wevm/wagmi #5256 → already has PR #5257 (known). wevm/viem, spesmilo/electrum, cake_wallet, Rabby, sparrow, WalletWasabi, ledger-live, MystenLabs/ts-sdks: no fresh open issues ≥Oct 2.
- **BlueWallet #8982** (iOS becomes default JPEG handler) — maintainer marcosrdz already engaged: by-design (the app registers for images to scan them for QR codes / bitcoin addresses, see hooks/useCompanionListeners.ts). Not a bug.
- trezor/trezor-suite #33195 — empty-body/no-repro standing reject in a heavy monorepo; #33183 concierge-banner UI logic, #33192 trading flow, rest are parent/design/feature items.
- ACINQ/phoenix #835 — inbound-liquidity decrease after an on-chain tx: node/channel-state dependent, no local repro possible.
- argent-x, solana-web3.js, near/wallet-selector, ton-core, bitcoinjs-lib: no fresh open issues in the window.

## Payments
$0 requested, $0 received ($0 all-time). No X post.
