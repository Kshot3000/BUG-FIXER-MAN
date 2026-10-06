# Sector 1 (crypto wallets) sweep — run 166, 2026-10-06

**Result: NO submission.** Fresh wallet queues direct-verified repo-by-repo via the REST issues endpoint; every fresh tractable item is already ours, already PR'd, maintainer-assigned, or team/backend/hardware-bound.

## Deep-check
- **wevm/viem #5191** (filed today, 0 comments, unassigned): `waitForTransactionReceipt` replacement detection compares `from` as a raw string, so a checksummed pending `from` (Alchemy behaviour) never matches the lowercase mined `from` — replacement never detected, `onReplaced` never fires; the `to` comparison below has the same flaw for the `repriced` classification. Well-diagnosed by the reporter with a self-contained anvil repro. **REJECTED — already fixed by open PR #5192** ("fix: compare addresses case-insensitively in `waitForTransactionReceipt` replacement detection", cross-referenced on the issue timeline).

## Queue heads (all known / not actionable)
- viem #5195 = ours (PR #5196 open); wagmi #5256 → PR #5257; ethers #5194/#5193 = ours.
- trezor-suite head = #33233, ours (PR #33235 open).
- BlueWallet #8994 still maintainer-assigned (marcosrdz), native iPad/macOS co-sign UI — not verifiable here.
- Rabby #4157 backend data / #4156 HELD (unchanged); appkit #5811 ours; safe-core-sdk #1438 already PR'd (#1439).
- MetaMask extension fresh = Yarn-audit bot advisories (team); MetaMask/core and wallet-core heads empty of fresh bugs; stellar #1783/#1782 = team work items ("Audit remediation", "P30 work"); bitcoinjs #2350 standing external-dep reject.
- ts-sdks #1311 reporter-owned (known); argent-x / wallet-selector / polkadot-js extension / solana-web3.js / Keystone queues stale, feature, or hardware-bound.

## Status watch
- ONE minor change: **Expensify #102072 comments 60 → 61** — melvin-bot[bot] 2026-10-06T22:05:49Z posted an "Eep! 4 days overdue now" nudge to C+ reviewer FitseTLT. This is the bot's overdue ping to the reviewer, **not** the contributor-details prompt to Kshot3000; no selection/assignment/hire. Kyle's $250 proposal still awaits FitseTLT.
- Everything else identical: open-PR count 83; dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 / cake #3671 OPEN; electrum #11012 CLOSED unmerged (known, org blocked — never retarget); gitea #39646 (head 9bb973c) / #39650, caddy #8163, lodestar #10284, nats.go #2163 OPEN/MERGEABLE; NiceGUI #6372 evnchn APPROVED stands; ansible #87642 comments = 2 (known pkingstonxyz feedback, Kyle's call); Expensify #101684 43 / #102044 33 / #102226 38 identical; held items identical (lighthouse #10226 1 comment/0 assignees, bullbitcoin #2902 labels=["bug"] only, formbricks #9526 3 comments). HackerOne: ledger-only.

Payment requested: none. $0 requested, $0 received (all-time received still $0).
