# Sector 1 (crypto wallets) sweep — run 126, 2026-10-06

**Outcome: NO submission.** One fresh bug fully root-caused by code inspection but not submittable this run (venue gate + no local toolchain for codegen/tests). Watch: NO changes.

## Top candidate — HELD: SatoshiPortal/bullbitcoin-mobile #2902

Filed 2026-10-06T06:39Z, labels: `bug` only, unassigned, 0 comments, no competing PR (open PRs are unrelated refactors/settings).

**Bug:** Importing a Specter DIY via the built-in Specter hardware-wallet flow classifies the wallet as watch-only, so air-gapped signing is impossible. Specter's "Master public keys → Single key, SLIP-132 off" export is an origin-prefixed bare xpub: `[fingerprint/84h/0h/0h]xpub…`.

**Root cause (verified by tracing the full import chain in a pristine clone):**

1. `ImportQrDevicePage` (Specter flow) opens the scanner with `extra: device` (`SignerDeviceEntity.specter`); `ScanWatchOnlyScreen` passes it to `WatchOnlyWalletEntity.parse(signerData, signerDevice: widget.signerDevice)`.
2. In `lib/features/import_watch_only_wallet/watch_only_wallet_entity.dart`, `parse` strips the `[origin]` prefix and calls `Satoshifier.parse`. A bare xpub yields `WatchOnlyXpub`, and the xpub branch returns `WatchOnlyWalletEntity.xpub(watchOnlyXpub: satoshified)` — **the `signerDevice` argument is silently dropped**. The xpub freezed variant has no `signerDevice` field at all; the descriptor variant carries it.
3. `ImportWatchOnlyXpubUsecase` then calls `WalletRepository.importWatchOnlyXpub(xpub, network, scriptType, label)` — no device parameter exists on that path (contrast the descriptor path, where `signerDevice` is persisted into `wallet_metadata_table.signerDevice` and read back in the repository).
4. The details UI cannot repair it afterwards: `ImportWatchOnlyCubit.onSignerDeviceChanged` returns early unless the entity is a `WatchOnlyDescriptorEntity`, and `_XpubDetailsWidget` has no device picker.

Devices exporting descriptors (Passport/Keystone flows select a descriptor) keep their device; any device whose export parses as a bare xpub — Specter single-key per the in-app instructions — loses it.

**Fix shape (for the run that takes this):** add `signerDevice` to the xpub variant (freezed + build_runner codegen), thread it through `parse`, `ImportWatchOnlyXpubUsecase`, and `WalletRepository.importWatchOnlyXpub` into wallet metadata; allow `onSignerDeviceChanged` for xpub entities.

**Why not submitted this run:**
- Venue gate: the repo's CONTRIBUTING requires a PR to close an open issue labelled `ready` (maintainer/triager-applied). #2902 carries only `bug`. Watch for the `ready` label.
- No Dart/Flutter toolchain in this sandbox (`dart`/`flutter` absent) and the freezed part file is generated, not checked in — no red→green test or codegen is possible here. Per the verify-before-submit rule, no untested fix ships.

## Other fresh wallet queues checked

- wevm/viem #5195 → our PR #5196 (open); #5191 → PR #5192 (known). wevm/wagmi #5256 → PR #5257 (known).
- MetaMask/metamask-extension #46887 (filed today, crash reading `origin`) and #46889 (sidepanel `mutations` TypeError): both internal release-testing reports with repro still "investigating" — team-owned, no actionable root cause. Rejected.
- spesmilo/electrum, BlueWallet/BlueWallet, cake-tech/cake_wallet, trezor/trezor-suite: no new open issues at list head. leather-io/extension: only stale #6404 (Mar). ethers-io/ethers.js: #5194/#5193 are ours (PR #5198 open).

## Watch

NO changes — all open PRs direct REST-verified identical to run 125 (dentalpin #599 / type-coverage #155 merged, known; ERCs #2045 OPEN c=1, cake #3671 OPEN c=0, electrum #11012 + trilium #11920 closed unmerged, known; viem #5196, optimism #23214, diffy #89, memos #6435, vikunja #4107/#4110 OPEN; prysm #17626 OPEN c=1, CLA still Kyle's step; NiceGUI #6372 OPEN c=1 with evnchn's APPROVED standing; vyper #5294 OPEN c=2; ansible #87642 OPEN c=1). Expensify counts identical by direct per_page=100 listing: #102072 60, #101684 42, #102044 30, #102226 38 — no selection/hire, no melvin-bot prompt to Kshot3000. (A first batched read of #102044 showed 31; the direct listing — the method every prior run validated — shows 30 with the same last comment, abbasifaizan70's known proposal update. Artifact discarded.) HackerOne: ledger-only.

$0 requested, $0 received. Next run: sector (2) crypto infra / DeFi / chains.
