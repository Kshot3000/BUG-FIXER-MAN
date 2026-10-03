# ZeusLN/zeus — swap rescue duplicates reverse swaps, never repairs missing preimages (#4821)

- **Project:** ZEUS (Bitcoin/Lightning wallet, React Native/TypeScript) — https://github.com/ZeusLN/zeus
- **Issue:** https://github.com/ZeusLN/zeus/issues/4821 (follow-up to merged #4460, which re-derives the preimage when rescuing reverse swaps)
- **PR:** https://github.com/ZeusLN/zeus/pull/4827 — OPEN, MERGEABLE (fork Kshot3000/zeus, branch `fix/swap-rescue-duplicates-4821`, commit bcac59e)

## Bug

`SwapStore.getRescuableSwaps` built `existingSwapIds` from `SWAPS_KEY` only. Rescued swaps are written to `SWAPS_KEY` whatever their type, and the next `fetchAndUpdateSwaps` re-files the reverse ones under `REVERSE_SWAPS_KEY`. A second rescue therefore:

- **Reverse swap already re-filed:** its ID is not in `SWAPS_KEY`, so it was imported again — both copies ended up under `REVERSE_SWAPS_KEY` with the same ID and both showed in the swap list.
- **Reverse swap still under `SWAPS_KEY`:** it was skipped, so nothing was updated — in particular a swap rescued before #4460, stored with no `preimage`, never got one, so every claim attempt kept failing and a second rescue (the obvious remedy) did not repair it.

## Proof (local, red → green)

Six new tests in `stores/SwapStore.rescue.test.ts` implementing the test list from the issue (in-memory Storage harness and pinned preimage vector already in that file from #4460):

- On upstream master (2b81e4e): the 4 bug tests **fail** (duplicate append, no repair under either key, no duplicate collapse); the 2 control tests pass.
- With the fix: `SwapStore.rescue.test.ts` + `SwapStore.test.ts` = **35/35 pass**; changed files clean under the project's own Prettier (2.4.1) and ESLint.
- Environment note: dependency install (yarn v1, frozen lockfile) initially failed repeatedly on registry 502s/network timeouts through the proxy and succeeded on the third resume from the yarn cache.

## Fix

In `getRescuableSwaps` (see `fixes/zeus-swap-rescue-duplicates-4821.patch`):

1. `existingSwapIds` is built from both `SWAPS_KEY` and `REVERSE_SWAPS_KEY`.
2. For a restored reverse swap whose ID is already stored and whose stored entry has no `preimage`, the re-derived preimage (same derivation as the rescue path — `deriveSwapPreimage` over the child key at `claimDetails.keyIndex`) is written onto that entry in whichever key holds it, preserving its other fields; no copy is appended.
3. Duplicate stored entries for the same rescued ID collapse to one, keeping the entry that has a preimage.
4. Submarine swaps unchanged: skipped when stored, no preimage added.

## Submission status / payment

- Submitted via fork PR #4827 on 2026-10-02. No bounty was posted on #4821; fix offered freely, tips pointer (PayPal/BTC) in the PR footer only. **Payment requested: none (no bounty). Received: none.**
- WATCH: maintainer review + CI (first-time-contributor workflow approval may be required before checks run).
