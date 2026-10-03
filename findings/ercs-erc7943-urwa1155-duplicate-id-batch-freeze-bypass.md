# ethereum/ERCs — ERC-7943 uRWA1155 duplicate-id batch transfer bypasses the frozen-balance check

- **Project:** ethereum/ERCs (ERC-7943 "Universal RWA Interface" reference implementation, Final since 2026-05-27)
- **Issue:** https://github.com/ethereum/ERCs/issues/1814 (reported by MavenRain, with a public PoC)
- **Sector:** crypto infra / DeFi / chains
- **Date:** 2026-10-02

## Bug
`uRWA1155._update` validated each element of a batch transfer in isolation against the *pre-transfer* balance and unfrozen balance, but the debit happens once, in `super._update`, after the loop. Repeating a `tokenId` in one `safeBatchTransferFrom` passed the `value <= unfrozenBalance` check once per element against the same stale figure, so a whitelisted holder could move up to `unfrozen × N` tokens — draining the frozen portion of a partially frozen balance (the core ERC-7943 compliance feature), while `canTransfer` correctly returned `false` for the same total, and `getFrozenTokens` stayed stale afterwards. The burn branch shared the root cause: `_excessFrozenUpdate` got per-element amounts, so a duplicate-id `burnBatch` under-adjusted the frozen balance.

## Proof (local, Foundry 1.3.6 / solc 0.8.29 / OpenZeppelin v5.1.0)
PoC test (in `fixes/ercs-erc7943-urwa1155-duplicate-id-poc.t.sol`): balance 100, frozen 60 → 40 unfrozen; batch `[1, 1] × [40, 40]`:
- **Pre-fix:** succeeded — 80 moved to the destination, holder left with 20 and `getFrozenTokens == 60` (stale). PoC test PASSED against the vulnerable code (asserting the buggy outcome).
- **Post-fix:** the same batch reverts with `ERC7943InsufficientUnfrozenBalance(holder, 1, 80, 40)`.

## Fix
Cumulative per-id accounting inside `_update`: transfer checks validate the cumulative amount per `tokenId` within the batch; the burn branch passes cumulative amounts to `_excessFrozenUpdate`. Patch: `fixes/ercs-erc7943-urwa1155-duplicate-id-batch.patch`. Three regression tests added to the project's own `test/uRWA1155.t.sol` (duplicate-id revert, duplicate-id within-unfrozen success, duplicate-id burn frozen adjustment). Full `assets/erc-7943` suite: **222 passed, 0 failed**.

## Submission
- **PR (OPEN):** https://github.com/ethereum/ERCs/pull/2045 — fork `Kshot3000/ERCs`, branch `fix/erc7943-1155-duplicate-id-batch-freeze-bypass` (commit c069b43), base `master`.
- Disclosure note: the bug and PoC were already public in issue #1814 by the original reporter; this PR is the fix, credited to the reporter in the PR body.

## Payment
- None requested — ethereum/ERCs is a standards repo with no bounty program for asset fixes. No payment received.
