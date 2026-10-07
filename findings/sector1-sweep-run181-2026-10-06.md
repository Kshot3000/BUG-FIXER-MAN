# Sector-1 sweep — run 181 (2026-10-06)

Rotation: (1) crypto wallets. **No submission.**

Fresh wallet queues direct-verified repo-by-repo via per-repo REST listings
(no batched search — that class of scan has fabricated pairs before and is
discarded wholesale when it appears).

## Deep-checks

- **stellar/js-stellar-sdk #1762** (`contract.Spec` / `jsonSchema()` handle
  duplicate spec type names inconsistently — struct `Foo` and enum `Foo` in
  one spec silently collide): real and well-reproduced, but filed by
  leighmcculloch (Stellar core maintainer) and the expected behaviour is an
  API-design decision (throw on spec load vs. disambiguate names). A
  maintainer design call, not a clean outsider fix. Rejected.
- **MystenLabs/ts-sdks #1185 / #1186** (seal docs import a non-exported
  `seal`/`SealOptions`; `verifyKeyServers` docs/code default mismatch):
  reporter spelled the exact fix and deferred it from their own PR review
  (#1184) — reporter-owned; this venue also permission-blocks outside PR
  creation for this account (the #1242 precedent). Rejected.
- **stellar/js-stellar-sdk #1763**: known — already addressed by closed
  PR #1774 (run 156).

## Rest of the sweep (all known classes)

- viem #5195 ours, #5191 → PR #5192; wagmi #5256 → reporter's PR #5257,
  #5248 dataSuffix feature-class.
- MetaMask fresh = yarn-audit bot advisories + a Sev1 team-yield-display bug
  (team-confirmations, release-blocker).
- BlueWallet #8994 maintainer-assigned (Apple-native); #8982 known Alternate.
- trezor #33233 / #33224 = ours (PRs #33235 / #33231).
- safe-core-sdk #1438 → PR #1439; #1425 ours (PR #1440); #1436 backend task.
- cosmjs #1982 → PR #1983; #1976 test-coverage task.
- ts-sdks #1311 reporter-owned (fix on reporter's branch).
- stellar #1783/#1782 team placeholders (audit tracking / P30 scope).
- appkit #5811 ours (PR #5813).
- Rabby #4157 backend data, #4156 HELD (phishing-display security UX).
- leather #6404 stale + Linear-tracked; #6396 assigned/stale.
- WalletConnect fresh = chain-addition requests; solana-web3.js legacy
  advisory/feature; bitcoinjs #2350 known consensus-policy/external-dep
  class, rest of its head is spam.
- cake_wallet head unchanged (our PR #3671 open).

## Watch (run 181)

NO changes, direct-verified: open-PR count 85; dentalpin #599 /
type-coverage #155 MERGED (known); ERCs #2045, cake #3671 OPEN; electrum
#11012 CLOSED unmerged (known, org blocked — never retarget); chatwoot
#16165, prometheus #19944, gitea #39646/#39650, caddy #8163, lodestar
#10284, nats.go #2163 OPEN/MERGEABLE at known heads; NiceGUI #6372 APPROVED
stands. Expensify identical (61/43/33/38; #102072 latest still the
melvin-bot overdue nudge — NOT the contributor-details prompt; no
selection/hire). Held identical: lighthouse #10226 1 comment/0 assignees;
formbricks #9526 3 comments. HackerOne: ledger-only.

$0 requested, $0 received. Next run: sector (2) crypto infra/DeFi/chains.
