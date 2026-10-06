# prometheus/client_golang — promhttp ReadFrom commits 200 before the source produces data

- **Project:** prometheus/client_golang (promhttp instrumentation)
- **Issue:** https://github.com/prometheus/client_golang/issues/2155 (filed 2026-10-06 by jgehrcke, 0 comments, unassigned, no competing PR; reporter explicitly deferred solutioning to maintainers)
- **Fix PR:** https://github.com/prometheus/client_golang/pull/2156 — OPEN / MERGEABLE, head `a357d91` (GitHub-verified), DCO signed-off
- **Bounty:** none posted on the issue; no payment requested (foundation project — PR kept free of payment info).

## Bug

`readerFromDelegator.ReadFrom` called `WriteHeader(StatusOK)` *before* delegating to the underlying `io.ReaderFrom`. The underlying ReadFrom bypasses the delegator, so that eager call was the only chance to register the status — but it committed a 200 to the client even when the source failed before producing a single byte. A handler doing `io.Copy(w, failingReader)` then `http.Error(w, ..., 502)` produced a client-visible **200** (plus a `superfluous response.WriteHeader` server log) while the metric recorded `code="502"`.

## Proof (reporter's repro, verbatim)

Pristine `main` (de866d6):

```
client status: 502                     <- plain handler
client status: 200                     <- promhttp-instrumented handler (wrong)
requests_total{code="502"} 1           <- metric claims 502 the client never saw
```

Patched: both handlers → **502**, metric `code="502"`, no superfluous-WriteHeader log.

## Fix (mirrors net/http's `(*response).ReadFrom`, the approach the issue links)

Probe-copy the first ≤512 bytes through `Write` (sends 200 implicitly once data actually flows; keeps `written`/`observeWriteHeader` accurate), then delegate the remainder to the underlying `ReadFrom` with the original reader so optimized copy paths survive for the bulk. A source that fails or is exhausted before producing anything leaves the header unwritten. If the header was already committed (or the reader is nil), delegate directly as before.

Disclosed in the PR: TimeToWriteHeader now observes the header when it is genuinely written (first byte); a copy failing before any byte yields no observation instead of a bogus instant-200; empty bodies still sanitize to `code="200"`.

## Tests

- New `TestReaderFromDelegatorErrorBeforeData` + `TestReaderFromDelegatorCopiesData` (0/5/512/1536-byte bodies): **fail on the old body** ("no status must be committed… got [200]"), **pass patched**.
- `go test ./prometheus/promhttp/` and `-race` pass; `go vet`/`gofmt` clean; existing `TestInterfaceUpgrade` passes unchanged.
- Honest limitation disclosed in the PR: the core `prometheus` package's go-collector runtime-metrics tests fail in this sandbox on a Go-version metrics-set mismatch (`fips140ems` cardinality) — verified identical on unmodified `main`, unrelated.

## Sector-4 sweep rejects this run (run 144)

- spf13/cobra #2520 (man pages one-line) — reporter-owned ("fix ready, will open PR"; their PR #2522 cross-referenced).
- hashicorp/hcl #851 (newIdentToken validation) — reporter-owned (patch existed as PR #850, offered to reopen).
- spf13/afero #685 (MemMapFs rename race) — reporter's fix PR #686 already open.
- golang-jwt/jwt #542 (CR/LF in signature) — maintainer engaged + cross-referenced PR #543.
- urllib3/urllib3 #5294 (NaN timeouts) — three competing PRs (#5295/#5296/#5303) + a claim comment.
- sveltejs/svelte #18936 (hydratable after await) — reporter's own PR #18927.
- pnpm/pnpm #16655 (.npmrc registry ignored) — claimed, fix PR #16657 open.
- agronholm/anyio #1385 (TLSStream cancel corruption) — maintainer actively designing the fix in-thread.
- denoland/deno #36972 (OTel Latin-1) — real and unclaimed, but deno cannot be built/verified in this sandbox.
- celery/celery #10760 assigned; fsnotify #783 kqueue-only (not verifiable on Linux); nats-io/nats.go #2162 (drain goroutine) left as a follow-up candidate — viable but timing-based goleak repro, promhttp was the cleaner verified target.
