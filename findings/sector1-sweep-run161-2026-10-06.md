# Sector 1 sweep — run 161 (2026-10-06)

Sector: (1) crypto wallets. No submission this run.

## Watch (direct single API calls only)
NO changes vs run 160: open-PR count 81; dentalpin #599 / type-coverage #155 MERGED (known); ethereum/ERCs #2045 OPEN, cake_wallet #3671 OPEN, electrum #11012 CLOSED unmerged (known, org blocked — dropped per Kyle); lodestar #10284 / gitea #39646 (head 9bb973c, known Kyle-approved revision) / nats.go #2163 OPEN, mergeable_state=blocked (awaiting review); NiceGUI #6372 OPEN, evnchn APPROVED stands; ansible #87642 comments=2, latest still pkingstonxyz 2026-10-06T16:24Z (known peer feedback, Kyle's call). Expensify identical by direct per_page=100 listing: #102072 60, #101684 43, #102044 33, #102226 38 — no selection/hire, no melvin-bot contributor-details prompt. Held identical: lighthouse #10226 1 comment/0 assignees; SatoshiPortal/bullbitcoin-mobile #2902 labels=["bug"] only, assignees=[] — HELD stands; formbricks #9526 3 comments. HackerOne: ledger-only (no browser check this run).

## Hunt — fresh wallet queues, direct-verified repo by repo
- viem: only #5195 (ours, PR #5196) and #5191 (already PR #5192) open at head.
- wagmi: #5256 (already PR #5257), #5248 (already PR'd).
- ethers.js: #5194/#5193 = ours (PRs #5198 etc.).
- trezor-suite: head is #33233 = ours (PR #33235).
- MetaMask extension: fresh = Yarn audit advisories (team/CI).
- BlueWallet #8994 (filed today): iPad/macOS co-sign alert auto-dismisses / dead "Yes" on Apple second-signer path; Android control works. REJECTED — assigned to maintainer marcosrdz, native Apple UI behaviour, not verifiable in this sandbox.
- leather #6404 stale (Mar); Rabby #4157 backend balance data, #4156 HELD stands; safe-core-sdk #1438 already has a fix PR; stellar fresh = team audit/P30 work items + known dep-pin; cosmjs #1982 already fixed by open PR #1983 (run 156); bitcoinjs #2350 standing external-dep (varuint-bitcoin); sparrow = macOS env; Wasabi = user-support; argent-x = paymaster/backend; polkadot-js stale; cake / wallet-core / WalletConnect / MetaMask core / appkit heads empty of fresh bugs.

$0 requested, $0 received. Next run: sector (2) crypto infra / DeFi / chains.
