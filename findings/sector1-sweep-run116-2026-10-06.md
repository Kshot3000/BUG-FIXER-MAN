# Sector 1 (crypto wallets) sweep — run 116, 2026-10-06

**Result: NO submission.** Fresh wallet bugs across ~25 repos were all already PR'd, already ours, team/design-owned, or standing rejects.

## Checked and rejected
- **wevm/viem #5191** (waitForTransactionReceipt replacement detection) → already fixed by open PR #5192 (verified in run 111).
- **wevm/wagmi #5256** (disconnect() switches state.current) → already fixed by PR #5257.
- **ethers-io/ethers.js #5194 / #5193** (RLP decoder) — #5194 is the issue behind our own open PR #5198.
- **cake-tech/cake_wallet #3659** (WalletConnect Solana `solana_signAllTransactions` fails: `List<dynamic> as List<String>` cast throws, dApp gets "Malformed request parameters") — real and well-diagnosed by the reporter, but already covered by cross-referenced PRs #3660 and our own #3671. Nothing to add.
- **trezor/trezor-suite #33196** (Stellar custom-URL warning copy) — labeled `design needed`, cross-referenced by PR #32523; a UX-copy task, not a code bug.
- **trezor/trezor-suite #33195** — standing reject (no repro, heavy monorepo).
- **MetaMask/metamask-extension #46883** — bot-filed Yarn-audit advisory issue, team CI territory. #46870 Sev1 remains team-owned; MetaMask/core #10682 remains an on-chain incident report, not a code bug.
- **leather-io/extension #6404** (stx_callContract fee param ignored) — March 2026, stale.
- **BlueWallet** fresh queue: oldest item is July 2026 (#8812); #8982 by-design standing reject stands.
- **argent-x, unisat, aptos-wallet-adapter, MystenLabs/sui** — no fresh bug issues.

## Candidate held
- **rabbyhub/Rabby #4156** (filed 2026-10-01): a phishing site's EIP-712 payload hides a full-balance mETH Permit behind a decoy `string` type plus a chain of 110 synthetic struct types (S0…S110), and Rabby's sign dialog reportedly renders it as harmless. Genuine display-parsing security issue with a full repro payload in the issue, but the fix lives in Rabby's typed-data presentation layer inside a large extension monorepo — not locally verifiable to this loop's PoC bar in one run. Held for a dedicated session, not attempted half-verified.

## Watch
NO changes (see status-watch run 116): all open PR states and Expensify comment counts (60/42/30/38) identical to run 115; NiceGUI #6372 APPROVED stands, awaiting merge. $0 requested, $0 received.
