# Sector 1 (crypto wallets) sweep — run 151, 2026-10-06

**Result: NO submission.** Fresh wallet queues were direct-verified repo-by-repo (single `gh` calls only — batched scans have fabricated entries before). Everything fresh was already PR'd, ours, assigned/team-owned, backend/data-only, closed-source app-layer, or a design tradeoff for maintainers. $0 requested, $0 received.

## Deep-checked candidates

- **trustwallet/wallet-core #4860** — Solana Pay SPL-token amount shown 1000× (parsed with SOL's 9 decimals instead of the token's 6). Real, well-reported, unassigned, no competing PR. **Rejected: not fixable in this repo.** Code search of wallet-core finds no Solana Pay / `spl-token` URI parsing at all — the parsing lives in Trust Wallet's closed-source app layer (the reporter themselves filed here only because the app repos are closed). No in-scope code change exists to make.
- **BlueWallet/BlueWallet #8982** — iOS 27: BlueWallet becomes the default handler for JPEGs in Files. Reporter blamed the Info.plist Viewer registration for `public.jpeg`/`public.image`. **Verified in the actual plist:** the Image document type already carries `LSHandlerRank = Alternate` (not Default/Owner) — the obvious knob is already set correctly. The only remaining change (dropping the image types entirely) would remove the Open-In QR-import flow maintainer marcosrdz explicitly defended on the issue (2026-10-05, pointing at `hooks/useCompanionListeners.ts`), and no iOS verification is possible from this sandbox. A design tradeoff for the maintainers, not a verified fix. **Rejected.**
- **trezor/trezor-suite #33195** — "Unreachable data.trezor.io can break getTokenMetadata": title-only issue (empty body, 0 comments, filed by a team member) — no repro, no spec, nothing verifiable. **Rejected.**
- **ethers-io/ethers.js #5168** — `toUtf8String` per-byte allocation OOMs on large JSON-RPC responses. Real, but already has **two** open fix PRs (#5169, #5174) and the reporter states they are working on a PR. **Rejected (covered).**

## Queue scan (all direct-verified)

- viem #5195/#5191, wagmi #5256/#5248/#5233, safe-core-sdk #1438/#1425/#1424, appkit #5811: ours or already PR'd (standing).
- MetaMask extension fresh = team-owned Sev/data reports and yarn-audit bots; MetaMask/core fresh = incident report + team items; snaps/utils/accounts/WalletConnect monorepo: nothing actionable.
- Rabby #4157 backend data (standing), #4156 HELD (standing); rabby-mobile #1565 EIP-681 QR parsing — stale since Apr 2026, only a drive-by comment, heavy mobile repo, no maintainer engagement.
- BlueWallet #8994 assigned (marcosrdz); #8900 no repro/details. Cake Wallet fresh = features or Flutter device bugs (#3659 WalletConnect Solana, no Flutter toolchain here). Electrum: org has blocked the account — venue closed. OneKey/Argent X/Starknet.js/TrustWallet queues stale or feature-shaped.
- Held re-checked: SatoshiPortal/bullbitcoin-mobile #2902 still labels=["bug"] only, assignees=[] — HELD stands (venue requires a maintainer 'ready' label).

## Watch note

One change elsewhere in the portfolio (not sector 1): ansible/ansible PR #87642 received peer design feedback from contributor pkingstonxyz (2026-10-06T16:24Z) suggesting `-q`/`-qq` or `--reportformat json` instead of line-filtering in `get_lvm_facts`, plus pinning fields with `-o`. No direct question and not a maintainer directive — no reply sent; the redesign direction is Kyle's call. All other watched items identical (see status-watch ledger).
