# payloadcms/payload #18531 — image sizes built all at once, one decoded copy per size

- **Project:** payloadcms/payload (Payload CMS, sector 5 — web/other OSS)
- **Issue:** https://github.com/payloadcms/payload/issues/18531 (filed 2026-10-06, 0 comments, unassigned, no competing PR at check time)
- **Fix PR:** https://github.com/payloadcms/payload/pull/18534 — OPEN / MERGEABLE, head `07ca801` (GitHub-verified)
- **Payment:** no bounty posted on the issue; fix offered freely, tips welcome via the PR footer. $0 requested, $0 received.

## Bug

`createImageSizes` (`packages/payload/src/uploads/image-resizing/createImageSizes.ts`) built every configured `imageSizes` entry at once via `Promise.all(imageSizes.map(...))`. Each size pipeline clones the sharp base and decodes the whole source image, so one upload held one full decoded copy per size concurrently — peak ≈ `sizes × width × height × channels`. Reporter-measured on 3.90.1 (sharp 0.34.3): flat 7000×7000 PNG (~320 KB) with four WebP sizes grew the process ~591 MB (0 sizes: 4 MB; 1 size: 138 MB) — enough to OOM-kill memory-limited containers, and client retries then take down the next replica.

## Fix

Build the sizes sequentially (`for...of` in place of `Promise.all(map)`); the `omit` branch becomes `continue`. Peak stays at roughly one decoded copy (reporter's sequential measurement: ~162 MB). Side benefit: `sizeData`/`sizesToSave` are now collected in config order instead of completion order, and the focal-point branch's shared `resizeImageMeta` mutation is no longer racy.

Branch: `Kshot3000/payload fix/18531-image-sizes-sequential` @ `07ca801`.

## Proof (red → green)

New unit test in `createImageSizes.spec.ts` instruments the sharp mock so each pipeline's `toBuffer` records how many are in flight at once (3 configured sizes, real `createImageSizes` code path):

- Unpatched: max in flight = 3 — test fails (`expected 3 to be 1`); the 2 pre-existing tests pass.
- Patched: max in flight = 1 — full spec 3/3 passes (`vitest run --project unit`, repo-pinned toolchain via `pnpm install --filter payload...`).
- Prettier (repo config) clean on both changed files.

## Watch changes this run

- **formbricks/formbricks #9526 comments 2 → 3:** maintainer mattinannt (2026-10-06T13:02Z) forwarded the issue to the engineering team and told the other volunteer "We are currently not maintaining community contributions" — our ready branch stays linked on the issue for their team; no reply sent.
- Everything else identical: all watched PR states unchanged, Expensify counts 60/42/30/38, NiceGUI #6372 APPROVED stands, bullbitcoin (SatoshiPortal) #2902 still labels=["bug"] only (HELD stands), lighthouse #10226 still 1 comment / no PR.

## Also swept this run (all rejected, individually verified)

chatwoot #16122 → fix PR #16123 already open; listmonk #3250 → fix PR #3256; directus #28318 → fix PR #28319, #28322 internal/Linear-tracked relational-delta design; outline #13746 → PR #13750 closed; woodpecker #7198 feature-shaped (annotate orphaned repos).
