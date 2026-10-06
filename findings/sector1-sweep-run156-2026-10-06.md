# Sector 1 (crypto wallets) sweep — run 156, 2026-10-06

**Result: NO submission.** Every fresh wallet queue was direct-verified repo-by-repo via single `gh` calls; all candidates are already PR'd, ours, maintainer-assigned, team/backend-only, or standing held items.

## Deep-checks
- **cosmos/cosmjs #1982** (`fromBech32` throws `RangeError` with `@scure/base >= 2.3.0`, clean install resolves 2.4.0; filed 2026-09-19, 0 comments, unassigned): real and locally reproducible in principle, but already fixed by open PR **#1983** ("fix(encoding): Stop passing Infinity as bech32 decode limit", cross-referenced on the issue timeline). Rejected — competing PR exists.
- **stellar/js-stellar-sdk #1763** (ledger-absence errors in three incompatible shapes across `getLedgerEntry` / `getContractInstance` / `getAccount`): already addressed by PR **#1774** ("fix(rpc): unify missing-ledger-entry errors across lookup helpers", closed). Rejected.
- **trezor/trezor-suite #33196** (Stellar custom-URL warning): cross-referenced by closed PR #32523. **#33192** (USDT revoke → approval DEX swap flow): app/device flow, not locally verifiable. **#33212**: visual clipping. Rest of the trezor head = ours (#33233/#33224), assigned (#33218), or architecture work (#33204).

## Queues checked (all known/closed classes)
- viem #5195 ours (PR #5196), #5191 → PR #5192; wagmi #5256/#5248/#5233 all PR'd previously.
- ethers.js: #5194/#5193 ours, #5178/#5168 PR'd, #5172/#5165/#5137 assigned to ricmoo.
- Rabby #4157 backend-data, #4156 HELD stands. BlueWallet #8994 assigned marcosrdz, #8982 rejected run 151. Cake #3659 = Dart/Flutter cast bug (no toolchain here; our #3671 already open in that repo).
- MetaMask extension fresh = team Sev/data/internal release-testing reports. Safe #1438/#1424 PR'd, #1425 ours. AppKit #5811 ours; #5801/#5782/#5778 are live-wallet device flows, not locally verifiable. bitcoinjs #2350 standing external-dep reject. WalletConnect monorepo head = chain-addition requests + a spam URI issue. starknet.js head stale (2025). MetaMask/core #10682 is an incident report, #10667 a data/registry gap.

## Held items re-checked
- SatoshiPortal/bullbitcoin-mobile #2902: labels=["bug"] only, assignees=[] — HELD stands (venue requires a maintainer 'ready' label).
- sigp/lighthouse #10226: still 1 comment / 0 assignees.
- formbricks/formbricks #9526: still 3 comments.

## Watch note (characterized this run)
- **go-gitea/gitea PR #39646** carries a maintainer comment from wxiaoguang (2026-10-06T18:22Z, minutes after submission): "1. db table column unique / 2. APIErrorAuto" — terse shorthand pointing at a DB-level unique constraint + auto error mapping, i.e. the creation-race half of #39632 rather than the EditTeam 500 our PR fixes. CI is fully SUCCESS and the PR is OPEN/MERGEABLE. No reply sent: whether to expand scope toward the reviewer's implied approach is Kyle's maintainer-direction call.

## Payments
$0 requested, $0 received. All-time received remains $0.
