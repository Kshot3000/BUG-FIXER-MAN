# Sector-2 sweep — run 177 (2026-10-06)

Sector: (2) crypto infra / DeFi / chains. Result: **no submission** — every fresh
tractable item across ~25 infra repos was already ours, PR'd, assigned,
team-owned, part of a coordinated audit-report series, or a re-observation
request. All candidates below were direct-verified singly via the REST issues
endpoint (no batched-scan artifacts used).

## Deep-checks / known items re-verified

- **cometbft/cometbft #6098** (Block.MaxBytes consensus halt, Oct 1, 0 comments,
  unassigned) — already fixed by open PR #6100 (run-172 rejection stands).
  #6093 (remote signer panic) — already fixed by open PR #6094 (run-167).
- **celestiaorg/celestia-node #5310** — assigned (Shailu-s) + PR #5311. Known.
- **cosmos/ibc-go #9114** (PFM fractional-retry truncation, filed today) —
  known, already PR'd.
- **Consensys/teku #11427–#11433** and **hyperledger/besu #11492/#11493/#11496**
  (filed today) — the coordinated Java audit-report series seen in runs
  167/172; deep client internals, not single-run verifiable.
- **OffchainLabs/prysm #17613** — ours (PR #17626, CLA is Kyle's step).
  #17596 → PR #17597. #17619 is a version/environment report.
- **sigp/lighthouse #10226** — HELD claim-watch item: still 1 comment,
  0 assignees. #10214 maintainer committed to the fix on-issue; #10201 engaged
  by another contributor with the solution spelled out.
- **OffchainLabs/nitro #4760** — already fixed by PR #4761. Known.
- **lidofinance/core #1984** (filed today, getFeeDistribution order) — known
  rejection (runs 157/172): deprecated view in frozen legacy 0.4.24 contracts,
  reporter-spelled; no viable fix venue.
- **aptos-labs/aptos-core #20689** — prover internals (opaque callee closure
  purity), not locally verifiable in a single run.
- **ava-labs/avalanchego #6077–#6079** — VM scaffolding / feature work, one
  assigned to a team member.
- **wormhole-foundation/wormhole #5023–#5029** — VAA re-observation requests
  only, not code bugs.

Empty fresh heads (newest page all PRs or nothing new): go-ethereum,
polkadot-sdk, sui, nearcore, celestia-app, reth, optimism, agave, lodestar
(ours is the newest work there), juno, morpho-blue, scroll, mev-boost,
cosmos-sdk (proof-exercise only).

## Standing watch (direct-verified, single calls)

NO changes vs run 176: open-PR count 85; dentalpin #599 / type-coverage #155
MERGED (known); ERCs #2045 OPEN, cake #3671 OPEN, electrum #11012 CLOSED
unmerged (known, org blocked); chatwoot #16165 (e09e711), prometheus #19944
(0639411), gitea #39646 (9bb973c) / #39650 (1cb955f), caddy #8163 (5b88382),
lodestar #10284 (a20fd5c), nats.go #2163 (a44728b) OPEN/MERGEABLE; NiceGUI
#6372 reviews COMMENTED/COMMENTED/DISMISSED/APPROVED — APPROVED stands.
Expensify identical: #102072 61 (assignee FitseTLT only, latest still the
melvin-bot 22:05Z overdue nudge — NOT the contributor-details prompt),
#101684 43, #102044 33, #102226 38 — no selection/hire. Held identical:
lighthouse #10226 1 comment/0 assignees; bullbitcoin #2902 labels=["bug"]
only, assignees=0 — HELD stands; formbricks #9526 3 comments. HackerOne:
ledger-only (no browser check this run).

Payment: $0 requested, $0 received (all-time received still $0).
Next run: sector (3) paid bounty platforms & paid GitHub issues.
