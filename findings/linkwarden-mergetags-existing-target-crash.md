# linkwarden/linkwarden — merging tags into an existing tag name crashes (P2002); destination settings erased

- **Issue:** https://github.com/linkwarden/linkwarden/issues/1849 (filed 2026-09-28 by codeCraft-Ritik, label bug, 0 comments, unassigned, no competing PR at hunt time)
- **PR:** https://github.com/linkwarden/linkwarden/pull/1855 — OPEN (2026-10-05, run 50, sector 5 web/other OSS)
- **Fork branch:** Kshot3000/linkwarden@fix/1849-merge-tags-existing-target (7f4f7c0), base upstream main 952ac45

## Bug
`apps/web/lib/api/controllers/tags/mergeTags.ts` always deleted the source tags and then created a brand-new tag with `newTagName`:
1. If a tag with that name already existed for the user (the primary merge use case — e.g. `reactjs` → existing `react`), `tx.tag.create` violated `@@unique([name, ownerId])` → Prisma P2002 → transaction rollback → HTTP 500, merge fails completely.
2. If the destination tag was itself in `tagIds`, it was deleted and recreated with blank defaults, silently erasing `archiveAsScreenshot/Monolith/PDF/Readable/WaybackMachine` and `aiTag` settings.

## Fix
Resolve the destination inside the transaction first: `findUnique` on `name_ownerId`; if it exists, exclude it from `deleteMany` and `tag.update`-connect the affected links (row + settings preserved); otherwise create as before. `indexVersion` reset unchanged; lookup scoped by `ownerId` so another user's same-named tag is untouched. The issue's proposed approach, implemented and credited via `Fixes #1849`.

## Proof (red → green, real controller code)
No Postgres/pnpm in the sandbox, so the real `mergeTags.ts` (esbuild-transpiled verbatim, only its two imports stubbed) ran against an in-memory Prisma fake enforcing the unique constraint (P2002) with transaction rollback, plus a zod-faithful `MergeTagsSchema` stub:
- Unpatched: merge-into-existing throws `P2002` and rolls back (source tag survives, links unchanged); destination-in-`tagIds` succeeds but returns a NEW tag with `archiveAsPDF: null` / `aiTag: null` — both reported defects reproduced exactly.
- Patched: 8/8 checks pass — 200 + existing tag returned, settings preserved, only source tags deleted, links relinked, `indexVersion` nulled, other user's same-name tag untouched; fresh-name creation and 400 validation unchanged (controls pass on both variants).
- Repo-style integration tests added (`mergeTags.test.ts`, modeled on `importFromHTMLFile.test.ts`) for CI's Postgres; **not run locally (no DATABASE_URL) — disclosed in the PR.** Prettier clean on both files; esbuild syntax check clean.

## Submission status / payment
PR #1855 OPEN, awaiting CI + maintainer review. No bounty posted on #1849; fix offered freely, tips welcome in the PR footer. $0 requested, $0 received.
