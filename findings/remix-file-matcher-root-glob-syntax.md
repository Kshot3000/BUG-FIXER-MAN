# remix-run/remix — asset file matcher treats the root directory name as glob syntax

- **Issue:** https://github.com/remix-run/remix/issues/11970 (`allowFiles`/`denyFiles` never match when the project path contains parentheses; filed 2026-10-05, 0 comments, unassigned, no competing PR at submission time)
- **PR:** https://github.com/remix-run/remix/pull/11973 — OPEN / MERGEABLE, head `be78de5` (GitHub-verified), branch `kshot3000/fix-asset-file-matcher-root-glob`
- **Sector:** (4) general company OSS / dev tools — run 139, 2026-10-06

## Bug

`createFileMatcher` (`packages/assets/src/lib/file-matcher.ts`) resolves a user's
`allowFiles`/`denyFiles` pattern against `rootDir` and compiles the joined string with
picomatch. Glob syntax in the root directory's own name is therefore compiled as part of
the glob: in `…/app (copy)/app/**/public/**`, `(copy)` is a group that matches `copy`
without the parentheses. A project in a folder like `app (copy)`, `project (1)`, or
`Dropbox (Company)` fails asset-server startup with `FILE_NOT_ALLOWED` for its own
files, while the de-parenthesized path wrongly matches. Bracket/brace characters in a
directory name have the same class of problem (a `[a]` class matches the single letter).

## Proof (local, from public code)

Standalone harness around the real `file-matcher.ts` + `paths.ts` (Node 24 type
stripping, picomatch 4.0.7 — the version the issue cites), harness kept at
`hidden_files/remix-11970-repro.mjs` in the goal workspace:

- Unpatched: 5 of 13 checks fail — parens root rejects its own file and accepts the
  de-parenthesized path, `[a] and (b)` root rejects its own file, pattern character
  classes break under a parens root.
- Patched: 13/13 pass.

The PR's own `file-matcher.test.ts` (7 tests, repo `@remix-run/test`/`assert` style)
was also executed under a node:test shim: 3 fail on pristine `file-matcher.ts`,
7/7 pass patched. Standalone `tsc --noEmit` on the two touched source files is clean.
The full pnpm workspace test suite was not run in this sandbox (monorepo install);
that limitation is disclosed here, and the changed function is covered by the new
unit tests plus the harness above.

## Fix

Escape glob syntax in the root-directory portion of the resolved pattern before
compiling with picomatch, so only the user-supplied pattern is treated as a glob.
Absolute patterns are used verbatim (their glob syntax is the user's own), and
patterns resolving outside the root (`../packages/**`) are unchanged. Includes a
`patch` change file for `@remix-run/assets` per the repo's `.changes` convention.

## Payment

No bounty posted on the issue; fix offered freely, tips welcome via the PR footer.
$0 requested, $0 received.
