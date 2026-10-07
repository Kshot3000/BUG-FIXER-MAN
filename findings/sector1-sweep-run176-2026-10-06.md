# Sector 1 sweep — run 176 (2026-10-06)

**Sector:** (1) crypto wallets
**Result:** NO submission. Fresh wallet queues direct-verified repo-by-repo (REST issues endpoint, single calls) — every tractable item is ours, already PR'd, reporter-owned, assigned, team-tracked, backend-only, or a standing hold/reject.

## Watch
NO changes vs run 175. Open-PR count 85. dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 OPEN, cake #3671 OPEN, electrum #11012 CLOSED unmerged (known); chatwoot #16165, prometheus #19944, gitea #39646 (9bb973c) / #39650, caddy #8163 (5b88382), lodestar #10284, nats.go #2163 OPEN/MERGEABLE with identical heads; NiceGUI #6372 APPROVED stands. Expensify identical: #102072 61 (latest still melvin-bot 22:05Z overdue nudge to FitseTLT — NOT the contributor-details prompt; assignee FitseTLT only, Help Wanted stands), #101684 43, #102044 33, #102226 38 — no selection/hire/prompt. Held identical: lighthouse #10226 1 comment / 0 assignees; bullbitcoin (SatoshiPortal) #2902 labels=["bug"] only, assignees=0 — HELD stands; formbricks #9526 3 comments. HackerOne: ledger-only.

## Deep checks
- **MystenLabs/ts-sdks #1311** (walrus getFiles returns zeros when a quilt patch crosses into the next column, filed today, 1 comment) — REJECTED, reporter-owned: reporter 0xgdr's comment states "A fix with a test is on a branch" (0xgdr/ts-sdks@fix/walrus-quilt-patch-column-offset, commit 0451eed) because outside PRs can't be opened on that repo — the same permission-blocked venue as #1242. Nothing to add.
- **safe-global/safe-core-sdk #1438** (protocol-kit connect() drops the current signer when no signer is passed) — REJECTED, already fixed by open PR #1439 ("keep the signer in connect() when none is passed"), verified in the repo's open-PR list.
- **stellar/js-stellar-sdk #1783 / #1782** (filed today) — team placeholders by oceans404 (Q4 audit-remediation tracking; Protocol 30 scope TBD after the Oct 7 SDK sync). No bug to fix.
- **leather-io/extension #6404** (stx_callContract fee parameter ignored) — stale (March), Linear-tracked as LEA-3523 by the team. Not fresh, not unclaimed in practice.

## Rest of the sweep
- viem #5195 ours (PR #5196); #5191 → PR #5192 (known).
- wagmi #5256 → reporter's PR #5257 (known).
- ethers #5194 ours (PR #5198); #5193 RLP cluster known.
- MetaMask extension fresh = yarn-audit bot items (#46902/#46899); core #10682 = incident report (known).
- trezor #33233 ours (PR #33235).
- BlueWallet #8994 maintainer-assigned (marcosrdz), Apple-native (known reject).
- cake_wallet: no fresh issues. Rabby #4157 backend / #4156 HELD (known). appkit #5811 ours (PR #5813). WalletConnect monorepo fresh = spam/feature.
- cosmos/cosmjs #1982 → PR #1983 (known). bitcoinjs #2350 external-dep (varuint) cluster (known).
- XRPL fresh = dependency-vulnerability notices; near/wallet-selector, sparrow, rainbowkit, solana-web3.js, polkadot-js, starknet.js, argent-x, ton: stale / feature / platform-bound only.

## Payment
$0 requested, $0 received.
