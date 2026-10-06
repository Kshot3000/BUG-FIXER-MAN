# prometheus/prometheus — BucketFraction panics on nil/empty buckets

- **Issue:** https://github.com/prometheus/prometheus/issues/19943 (filed 2026-10-06 by inanna-malick, 0 comments, unassigned, no competing PR)
- **PR:** https://github.com/prometheus/prometheus/pull/19944 — OPEN / MERGEABLE, commit `0639411` GitHub-verified (SSH) + DCO Signed-off-by
- **Patch:** `fixes/prometheus-bucket-fraction-empty.patch`
- **Payment:** none posted on the issue; foundation project — PR kept free of payment info. Not a bounty request.

## Bug

`promql.BucketFraction(lower, upper, buckets)` (promql/quantile.go) reads
`buckets[len(buckets)-1]` to check that the last bucket's upper bound is `+Inf`
before any length check, so a nil or empty `Buckets` slice panics with
`index out of range [-1]`. The issue is the maintainer-requested follow-up to
merged #19927, which fixed the identical last-element read in `BucketQuantile`
(@krajorama on #19927: "Please do BucketFraction as well").

## Proof (red → green, twice)

- Reporter's verbatim repro `BucketFraction(0, 1, nil)` on pristine upstream
  main `39c878f` (the #19927 merge): `panic: runtime error: index out of range
  [-1]` at `promql/quantile.go:544`.
- Fix: early `if len(buckets) == 0 { return math.NaN() }` after the sort,
  before the last-bucket read (+3 lines), mirroring #19927. `NaN` matches the
  function's own conventions (no `+Inf` last bucket → NaN; zero total count →
  NaN) and the native counterpart's zero-observation behavior.
- New tests (+36 lines in promql/quantile_test.go): `TestBucketFraction_EmptyBuckets`
  (nil/empty × finite, reversed, infinite, NaN bounds → all NaN; zero-count
  +Inf control) and `TestBucketFraction` (nonempty controls: interpolated
  fraction 5/30, full range 1.0, reversed bounds 0). Both FAIL (panic) with
  only the production change reverted, PASS with it restored.
- Full `go test ./promql` PASS (28.8s); gofmt clean; `go vet` shows only
  pre-existing findings in untouched files.

## Honest scope (stated in the PR, per repo AGENTS.md)

This corrects an exported-helper contract. The current PromQL call site
(`funcHistogramFraction`) guards empty bucket lists before calling the helper,
so no expression-evaluation/server failure is claimed; release-notes `NONE`
(same as #19927), no regression/backport framing. PR body carries an AI
assistance disclosure, matching #19927's accepted norm for this issue thread.

## Environment notes

- Workspace mode (`go.work`) hangs module resolution in this sandbox; build/test
  with `GOWORK=off GOPROXY=off` against the local module cache instead.
- Full-suite run needs `TMPDIR` off the shared 512M /tmp tmpfs (WAL tests fail
  with "no space left on device" there — environment artifact, not a failure).
