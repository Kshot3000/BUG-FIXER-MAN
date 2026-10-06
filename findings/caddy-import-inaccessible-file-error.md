# caddyserver/caddy — `import` of an inaccessible file reported as "not found" (PR #8163)

- **Project:** caddyserver/caddy (sector 4 — general OSS / dev tools, run 164, 2026-10-06)
- **Issue:** https://github.com/caddyserver/caddy/issues/8161 — filed 2026-10-06 by thanatos, 0 comments, unassigned, no competing PR (timeline checked). "AI not used" reporter; a genuine user bug report, not a reporter-owned patch.
- **Submission:** PR https://github.com/caddyserver/caddy/pull/8163 — OPEN / MERGEABLE, commit 60e1346 GitHub-verified (SSH-signed). Issue claimed first via comment per the project's CONTRIBUTING.
- **Payment:** no bounty posted on the issue; fix offered freely, tips footer in the PR description (PayPal / BTC / ETH / SOL). $0 requested formally, $0 received.

## Bug

In `caddyconfig/caddyfile/parse.go`, Caddyfile `import` resolution uses `filepath.Glob`, which by design ignores file system errors (it only returns `ErrBadPattern`). When `Lstat` on the import path fails — the reporter's case: EACCES from a non-traversable parent directory (confirmed in their strace) — Glob returns zero matches, and the parser reported `File to import not found: <path>` for a file that exists.

## Fix

In the no-matches, non-glob branch, stat the literal path directly: if it fails with anything other than not-exist, return `Failed to import file %s: %v` with the OS error; a genuinely missing file keeps the existing "not found" message. +8 lines in parse.go, plus regression test `TestParseImportInaccessibleFile` (+33 lines).

## Proof (red → green, twice)

1. **Parser level:** new regression test — importing a path through a regular file (stat fails ENOTDIR for every user/platform) FAILS on master (`File to import not found: testdata/import_test1.txt/child.txt`) and PASSES patched (OS error surfaced, path named); missing file still yields "not found". Full `caddyconfig/caddyfile` package suite passes patched; `go vet` / `gofmt` clean.
2. **End-to-end, reporter's exact scenario:** binaries built from master (700d603, the commit the reporter cited) and from the fix branch, run as `nobody`, importing a file behind a mode-000 directory:
   - master: `File to import not found: /tmp/e2e8161/site/Caddyfile`
   - patched: `Failed to import file /tmp/e2e8161/site/Caddyfile: stat /tmp/e2e8161/site/Caddyfile: permission denied`

## Venue-policy notes

- Caddy has an **explicit AI-assistance disclosure policy** (CONTRIBUTING + PR template): disclosure included both in the claim comment on #8161 and in the PR's Assistance Disclosure section, per Kyle's exception for projects with explicit AI policies.
- Caddy requires a **cla-assistant CLA signature** — a legal signature, which is Kyle's step alone. It was flagged openly in the PR body; the PR stands open for him to sign if maintainers accept the change in principle.
- The same reporter's neighbouring cluster was **rejected as reporter-owned**: jayhemnani9910's #8147/#8148/#8157/#8158 and Droid0012's #8151 all state the reporter already has a patch + test ready and is awaiting a maintainer go-ahead — poaching those would be drive-by behaviour.
- Also logged as a future sector-4 candidate: prometheus/prometheus #19943 (promql BucketFraction panics for nil/empty buckets, 0 comments, unassigned) — not chased this run (one deep target per run).

## Sweep validity note

This run's first sector sweep used the GitHub **search API**, which failed with HTTP/2 PROTOCOL_ERRORs that a `2>/dev/null` swallowed — the "no fresh issues" result was invalid and discarded. The sweep was redone via the REST issues endpoint per repo, which produced the Caddy cluster above. (Same lesson as the batched-watch fabrications: never trust a silent empty.)
