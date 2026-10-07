# Sector 1 (crypto wallets) sweep — run 171, 2026-10-06

**Result: NO submission.** Fresh wallet queues direct-verified repo-by-repo via the
REST issues endpoint (per-repo, newest first); every tractable fresh bug is already
ours, already PR'd, maintainer-assigned, a team item, backend-only, or held.

## Deep-check
- **wevm/wagmi #5256** (filed 2026-10-04, 0 comments at sweep start, unassigned):
  `disconnect()` of a non-current connector switches `state.current` to the first
  remaining connection, silently changing the active account for
  `getConnection`/`sendTransaction`. Reporter-diagnosed in both
  `packages/core/src/actions/disconnect.ts` and the `createConfig.ts` disconnect
  handler, with a full repro. **REJECTED — already fixed by open PR #5257**
  ("Preserve the active connection when another connector disconnects"), the
  reporter's own fix he offered on the issue.

## Rest of the sweep (all direct-verified)
- wevm/viem: #5195 is ours (PR #5196); #5191 already fixed by open PR #5192.
- BlueWallet/BlueWallet #8994: still maintainer-assigned (marcosrdz), native
  Apple co-sign UI — not verifiable here (standing rejection).
- trezor/trezor-suite #33233: ours (PR #33235).
- rabbyhub/rabby: #4157 backend balance data, #4156 HELD (standing).
- MetaMask/metamask-extension fresh head: yarn-audit bot advisories only.
- safe-global/safe-wallet-monorepo: no fresh issues.
- stellar/js-stellar-sdk #1783/#1782: team items ("Audit remediation", "P30 work").
- bitcoinjs/bitcoinjs-lib #2350: external-dependency encoding item (standing).
- MystenLabs/ts-sdks #1311: reporter-owned walrus item (standing).
- cosmos/cosmjs #1982: already fixed by open PR #1983.
- reown-com/appkit #5811: ours (PR #5813).
- leather-io/extension head: stale (March).

## Status watch (this run)
NO external changes. Open-PR count 85 (unchanged). Expensify comment counts
identical by direct listing: #102072 61, #101684 43, #102044 33, #102226 38 —
no selection/hire, no melvin-bot contributor-details prompt; #102072's latest is
still the known 22:05Z overdue nudge to FitseTLT. NiceGUI #6372 OPEN, evnchn
APPROVED stands. gitea #39646 (head 9bb973c) / #39650, prometheus #19944,
chatwoot #16165, caddy #8163, lodestar #10284, nats.go #2163 all OPEN.
Caddy #8163's head/comment movement is Kyle's own parallel-session work (CLA
signed by Kyle himself; Windows CI test fix 5b88382). Held items identical:
lighthouse #10226 (1 comment, 0 assignees), SatoshiPortal/bullbitcoin #2902
(labels=["bug"] only, 0 assignees), formbricks #9526 (3 comments).
HackerOne: ledger-only.

Payment: none requested, none received ($0 all-time stands).
