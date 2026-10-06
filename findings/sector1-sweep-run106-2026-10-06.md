# Sector-1 sweep — run 106 (2026-10-06 ~00:33 CDT)

Sector rotation: (1) crypto wallets. **No submission this run.**

## Status watch
- **NO changes** on any watched item (direct REST, per_page=100 for Expensify): dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 OPEN c=1, cake #3671 OPEN c=0, electrum #11012/#11013 OPEN c=0, ansible #87642 OPEN c=1, NiceGUI #6372 OPEN c=1 reviews 4 (evnchn APPROVED stands, awaiting merge), vyper #5294 OPEN reviews 3, AppKit #5813 issue comments 5, vikunja #4107 / #4110 / socket-plugs #162 / gitea #39611 / payload #18509 / chatwoot #16130 / gofactory #67 all OPEN c=0.
- Expensify counts identical to run 105: #102072 60 (tail unchanged), #101684 41, #102044 30, #102226 38 — no C+ selection/assignment/hire, no melvin-bot prompt to Kshot3000.
- HackerOne: ledger-only (no browser check this run).

## Hunt — fresh issues (created ≥2026-10-03) across ~40 wallet repos
Method: GitHub search API per repo (issues + PRs, created-desc), each candidate direct-verified by REST. Everything fresh was team-owned, already PR'd, hardware/device-bound, by-design, or not locally verifiable:

- **wevm/viem #5191** (filed 2026-10-06 04:46Z) — `waitForTransactionReceipt` replacement not detected when the RPC returns `from` in a different case for pending txs. Real and code-level, but a fix PR **#5192 already opened 05:20Z the same morning** — already taken.
- **MetaMask/metamask-extension #46870** — Sev1 release-blocker, team-owned/internal release testing (standing reject, run 101); #46858/#46856 are data/API reports with no code repro.
- **MetaMask/core** — fresh items are all PRs/features; #10682 is the known on-chain EIP-7702 sweeper incident report, not a code bug.
- **leather-io/mono #2821** — Leather + Ledger signing failures after dapp connect (regression 6.113.1 vs 6.112.1, suspected DMK/WebHID device-connection code): requires a physical Ledger device and a live dapp session — not reproducible locally.
- **trezor/trezor-suite** — #33195 standing reject (no repro, heavy monorepo); #33192 iOS USDT revoke→approval DEX swap flow (device + live trading backend); #33183 concierge banner triggered at low fiat amounts (internal trading product logic, screenshot-only); #33196 design-needed; rest are parent/design/feature/network-modularization tasks.
- **BlueWallet #8982** — by-design per maintainer (known reject). **wevm/wagmi #5256 → PR #5257** (known). electrum fresh items are PRs / the maintainer's own #11015 lightning work item (known). cake_wallet, sparrow, Rabby, ledger-live, safe-wallet, WalletConnect, wallet-adapter repos, WalletWasabi, JoinMarket, BTCPay, Green, Envoy, Krux, SeedSigner, AirGap, argent-x, Suiet, Keplr, Phoenix, Breez: no fresh open bug issues in the window.

## Payments
$0 requested, $0 received ($0 all-time). No X post.
