# Sector 2 sweep — run 67 (2026-10-05)

Sector: (2) crypto infra / DeFi / chains. **No submission** — every candidate was verified individually via the GitHub API (no search-index claims trusted) and rejected for a concrete reason.

## Status watch (no changes)
25 BUG FIXER MAN PRs open (unchanged). Body-listed PRs re-verified directly: dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045, cake #3671, electrum #11012/#11013 OPEN unchanged. Expensify counts identical (55/38/38/28) — no C+ response, assignment, or hire. NiceGUI #6372 reviews unchanged (evnchn DISMISSED, awaiting re-review); vyper #5294 reviews unchanged. HackerOne: ledger-only.

## Candidates checked and rejected
- **cosmos/cosmos-sdk** bug queue: #25843 / #24634 — assigned, stale.
- **aptos-labs/aptos-core** #20650 (Move prover soundness — rejected in earlier runs), #20457 compiler-v2 equality bytecode — heavy Move toolchain, no local verification path here.
- **cometbft/cometbft** #6098 protocol-design (known reject); #6031/#6030 privval/evidence consensus-critical signing safety — heavy, disclosure-sensitive, not a sandbox-verifiable fix.
- **cosmos/cosmjs** #1982 → reporter's fix PR #1983 already open (known reject).
- **near/near-api-js** #1639 → fix PRs #2000/#1999 already open (known reject).
- **safe-global/safe-eth-py** #2765/#2764 → reporter's PRs #2767/#2766 already open (known rejects).
- **freqtrade/freqtrade** #13635 (FreqAI live-retrain dtype crash, filed 2026-10-04): maintainer xmatthias labeled the issue "AI Slop" and posted the repo AI-policy warning demanding a full reproduction from the reporter — venue is actively hostile to AI-assisted contributions; root cause also needs live candle-data retrain flow. REJECT.
- **OffchainLabs/nitro** #4760 (RestfulClient ignores context cancellation, filed today): reporter's own fix PR #4761 already open and cross-referenced. REJECT — already PR'd.
- **Uniswap/smart-order-router** #968 (L1 fee scoring bias + serialized candidate evaluation): performance/design optimization whose "possible direction" is a routing-behavior change; verification requires LocalStack OP-Stack benchmarks. Maintainer territory. REJECT.
- **wormhole-foundation/wormhole-sdk-ts** #1039 (checkAndCompleteTransfer drops updated receipt): maintainer MarkFeder confirmed the diagnosis and landed fix PR #1044. REJECT — already fixed.
- **Berachain/beacon-kit** #3166 (RangeDB prune re-walks from index 0): persistence design change in a heavy Go monorepo; no clean sandbox verification. Deprioritized.
- Queues with no fresh verifiable bugs: MystenLabs/sui, near/nearcore, ethereum/go-ethereum, paradigmxyz/reth (bug-label), xrpl.js / algorand / hedera SDKs (stale), Uniswap v3-sdk (stale), driftpy / hyperliquid-python-sdk (docs/questions only), polymarket/py-clob-client (live-service sig-type/version issues, not local code bugs).

Next run: sector (3) paid bounty platforms & paid GitHub issues.
