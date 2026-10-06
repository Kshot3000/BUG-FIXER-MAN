# Sector 1 (crypto wallets) sweep — run 136, 2026-10-06

**Result: NO submission.** Every fresh wallet issue was checked individually (single direct `gh api` calls — no batched scans) and fell into a known reject class.

## Fresh queues checked
- **wevm/viem** — newest open bugs are #5195 (ours, PR #5196) and #5191 (already PR #5192). Nothing new.
- **wevm/wagmi** — newest is #5256 (already PR #5257). Nothing new.
- **ethers-io/ethers.js** — #5194/#5193 are ours (PR #5198 / report). Nothing new.
- **WalletConnect web3modal** — #5811 is ours (AppKit PR #5813). Nothing new.
- **MetaMask/metamask-extension** — NEW #46893 (filed today 13:16Z, mUSD-on-Monad fiat conversion shows $0 in the send flow): token price/metadata data issue served by MetaMask's price pipeline, no locally reproducible code defect identifiable from the report — same data/incident reject class as #46887/#46889 (internal, no-repro, still open).
- **RabbyHub/Rabby** — #4157 backend balance data (RPC healthy, known reject); #4156 EIP-712 Permit display issue remains the standing held candidate (large extension monorepo, not PoC-verifiable in one run).
- **cake-tech/cake_wallet, spesmilo/electrum, BlueWallet/BlueWallet, reown-com/appkit** — fresh issue queues empty.
- **leather-io/extension** — only #6404 (stale, March). 
- **safe-global/safe-core-sdk** — #1438 (connect() drops signer) already covered by our PR #1440; #1436 is a feature/pain-point post.
- **trezor/trezor-suite** — NEW #33218 (filed today): "Available to wrap" amount flickers from ellipsis overflow toggling — a visual CSS overflow artifact in the Suite UI, no functional defect, not verifiable in this sandbox.
- **MystenLabs/ts-sdks** — #1311 reporter-owned (reporter spelled the fix, PR follows; venue also previously blocked our PR creation on #1242); #1186 (Aug) is a docs-vs-code default mismatch for seal `verifyKeyServers` — which side is wrong is a maintainer security-default decision, not a clean bug fix.
- **bitcoinjs/bitcoinjs-lib** — #2350 known reject (CompactSize lives in the varuint-bitcoin dependency, no maintainer engagement).

## Held candidates — re-checked directly
- **SatoshiPortal/bullbitcoin-mobile #2902:** still `labels=["bug"]` only, `assignees=[]` — the repo's CONTRIBUTING gate requires a maintainer `ready` label before a fix PR; **HELD stands**.
- **sigp/lighthouse #10226:** still 1 comment (the claim), no PR — claim-stall watch continues.
- **formbricks/formbricks #9526:** still 3 comments (run 135's maintainer forward to engineering is the latest); no maintainer PR/cherry-pick of our ready branch yet.

## Status watch — NO changes
All items direct-verified identical to run 135: dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 OPEN c=1, cake #3671 OPEN c=0, electrum #11012 CLOSED unmerged (known); payload #18534 OPEN/MERGEABLE, supabase #51340 OPEN c=4, viem #5196 OPEN c=3, optimism #23214 OPEN c=0, diffy #89 OPEN c=0, prysm #17626 OPEN c=1 (CLA = Kyle's step), memos #6435 OPEN c=2, ansible #87642 OPEN c=1, vyper #5294 c=4 (PR endpoint); NiceGUI #6372 OPEN c=1, evnchn APPROVED stands. Expensify identical: #102072 60, #101684 42, #102044 30, #102226 38 — no selection/hire, no melvin-bot prompt to Kshot3000. HackerOne: ledger-only (no browser check this run).

Payment: $0 requested, $0 received.
