# rclone/rclone — failed SFTP upload leaks the remote file handle

- **Issue:** https://github.com/rclone/rclone/issues/10033 — "sftp: failed upload leaves the remote file handle open, so the server's space isn't freed" (filed 2026-10-03, label bug, unassigned, no competing PR at submission time)
- **PR:** https://github.com/rclone/rclone/pull/10042 — OPEN (2026-10-05)
- **Sector:** (4) general company OSS / dev tools — run 54

## Bug

In `backend/sftp/sftp.go`, `Object.Update` opens the remote file, then:

```go
_, err = file.ReadFrom(&sizeReader{Reader: in, size: src.Size()})
if err != nil {
    o.fs.putSftpConnection(&c, err)
    remove()
    return fmt.Errorf("Update ReadFrom failed: %w", err)
}
```

On a partway failure (the reporter hit a full server disk) the file was never
closed. `putSftpConnection` treats an `SSH_FX_FAILURE` status error as
recoverable and returns the connection to the pool — with the handle still
open — so the server kept the removed file's space allocated until the
connection died. In `rcd` / `mount` / `serve`, pooled connections live for the
life of the process.

## Proof (red → green, against a real SFTP protocol server)

Self-contained regression test `TestUpdateFailedUploadClosesRemoteFile`
(`backend/sftp/sftp_update_internal_test.go`, included in the PR): runs the
real backend against an in-process SSH/SFTP server (x/crypto/ssh +
pkg/sftp `NewRequestServer`) whose writer fails past a 1 MiB quota,
mimicking the full disk, and counts server-side open handles.

- **Unpatched:** 3 MiB upload fails with `Update ReadFrom failed: sftp: "no
  space left on device" (SSH_FX_FAILURE)`; partial file removed server-side;
  **1 handle left open** — the reported leak, reproduced exactly.
- **Patched:** same failure and removal; **0 handles open**.
- **Control:** a 100 KiB under-quota upload succeeds with 0 handles open on
  both versions.

Also: `go build .` OK (full `./...` build in this sandbox died only on the
512 MB /tmp tmpfs filling — unrelated packages, cache relocated and build
re-verified), `go vet ./backend/sftp/` OK, gofmt clean,
`go test ./backend/sftp/ -skip TestIntegration` passes. The `TestIntegration*`
fixtures fail identically on the pristine tree here (they need a provisioned
SFTP test server) — disclosed in the PR.

## Fix

One line — close the file before returning the connection to the pool (the
reporter's own suggested fix):

```go
if err != nil {
    _ = file.Close()
    o.fs.putSftpConnection(&c, err)
```

Venue note: rclone's CONTRIBUTING.md explicitly welcomes AI-assisted
contributions provided the fix is verified and tested against real code —
met here (bug reproduced first, test included, AI assistance disclosed in
the PR).

## Payment

No bounty posted on the issue; fix offered freely, tips welcome in the PR
footer. $0 requested, $0 received.
