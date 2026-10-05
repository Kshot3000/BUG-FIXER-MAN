# ChainSafe/lodestar — scoped sync committee poll clobbers the whole period duty map

- **Issue:** https://github.com/ChainSafe/lodestar/issues/10210 (filed 2026-09-29 by lodekeeper, 0 comments, unassigned, no competing PR at check time)
- **PR:** https://github.com/ChainSafe/lodestar/pull/10264 — OPEN / MERGEABLE, base `unstable` (submitted run 42, 2026-10-05)
- **Bounty:** none posted on the issue; fix offered freely. No payment requested.

## Bug

`SyncCommitteeDutiesService.pollSyncCommitteesForEpoch` (packages/validator/src/services/syncCommitteeDuties.ts) built a fresh duty map from only the indices the poll requested and then replaced the entire cached map for the period with it:

```ts
this.dutiesByIndexByPeriod.set(period, dutiesByIndex);
```

`runDutiesTasks` runs two polls concurrently per epoch: a full poll for all local indices, and an incremental poll for just the indices `pollValidatorIndices()` newly discovered. If the incremental poll lands last, the period map is replaced by the subset result. When a newly discovered validator is not in the sync committee, the incremental result is empty and the period's cached duties are wiped entirely until the next epoch's full poll rebuilds them. This is the sync committee sibling of the attester and PTC duty merge bugs fixed upstream in #10213 and #10197, with a different mechanism (unconditional full replace, no merge gate), tracked separately in #10210.

## Fix

Merge the poll result into the cached period map, scoped to the indices the poll requested: overwrite entries the poll returned, delete entries for requested indices it did not return, and keep every other entry. A full poll requests every local index, so it stays authoritative for the whole period and the redundant-duties behavior from #3572 is preserved (the existing `should remove redundant duties` test passes unchanged). Commit `fcb0c12` on fork branch `fix/10210-sync-committee-duties-scoped-merge`.

## Proof (red → green, local, Node 24.20.0)

New regression test in `packages/validator/test/unit/services/syncCommitteDuties.test.ts` drives `pollSyncCommitteesForEpoch` through a full poll, an empty incremental poll, a merging incremental poll, and a final authoritative full poll:

- Unpatched: the test fails at the empty-incremental-poll assertion, expected `{4: duty}` got `{}` (the wipe, exactly as #10210 describes); the other 5 tests in the file pass.
- Patched: full file 6/6 pass, including the existing #3572 test.
- `pnpm --filter @lodestar/validator check-types` passes; Biome check on both changed files clean.

Environment note (disclosed in the PR): the sandbox blocks node-gyp tarball extraction (`EPERM fchown` in `classic-level`, an unrelated beacon-node dependency), so dependencies were installed with `pnpm install --ignore-scripts` and only the validator's workspace dependencies were built. CI is authoritative for the standard environment.

## Same-run sector-2 rejects

- celestiaorg/celestia-node #5305 and #5303: reporter's own PRs #5306 / #5304 already open.
- paradigmxyz/reth #27649: PR #27731 already open (also, reth cannot build in this sandbox).
- stellar/js-stellar-sdk #1763: PR #1774 already open; #1762 (duplicate spec types) is a design-level consistency question and that repo only accepts PRs on maintainer invitation.
- vyperlang/vyper #5289: maintainer security patch tracking (GHSA), not an outside fix target.
- aptos-labs/aptos-core #20650: Move prover soundness, far outside a verifiable local fix here.
