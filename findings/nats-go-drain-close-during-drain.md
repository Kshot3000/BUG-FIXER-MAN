# nats-io/nats.go — Close during Drain resurrects the connection and flushes a closed conn

- **Project:** nats-io/nats.go (NATS Go client)
- **Issue:** https://github.com/nats-io/nats.go/issues/2162 — filed 2026-10-06, 0 comments, unassigned, no competing PR at submission time
- **Submission:** PR https://github.com/nats-io/nats.go/pull/2163 — OPEN / MERGEABLE, commit a44728b (SSH-signed, DCO Signed-off-by per the repo's CONTRIBUTING)
- **Sector:** (4) general company OSS / dev tools — run 149

## Bug
`Conn.drainConnection` waits for subscriptions to drain, then unconditionally flips the connection to `DRAINING_PUBS` and calls `FlushTimeout(5s)`, without rechecking whether the connection was closed in the meantime. A `Close()` concurrent with `Drain()` is therefore undone: the closed connection is resurrected to `DRAINING_PUBS` and the drain goroutine starts a new 5-second flush on it, surviving long after `Close()` returned (the reporter's goleak failure).

## Proof (red → green)
- The reporter's standalone goleak reproducer (embedded nats-server, held async callback, Drain → wait for the drain goroutine's pending-subscription sleep → Close → release) against pristine main: **FAIL — "connection resurrected after Close: DRAINING_PUBS"**.
- New repo regression test `TestDrainConnectionCloseDuringDrain` (test/drain_test.go, same interleaving barrier): on pristine main **FAIL** at the same resurrection assertion; patched **PASS**.
- Patched: reporter's reproducer passes `-race -count=3`; the full drain suite passes with `-race` (10/10, incl. the new test); `go vet` clean; gofmt clean.

## Fix
In `drainConnection`, recheck `isClosed()` under the connection lock immediately before the `DRAINING_PUBS` flip; if already closed, return early — no state resurrection, no new flush. Patch: `fixes/nats-go-drain-close-race.patch`.

## Payment
No bounty posted on the issue; fix offered freely. Not a bounty request. $0 requested, $0 received.
