# cli/cli — cursor stays hidden after Ctrl+C during the spinner (#14601)

**Project:** cli/cli (GitHub CLI)
**Sector:** (4) general company OSS / dev tools — run 64, 2026-10-05
**Issue:** https://github.com/cli/cli/issues/14601 (filed 2026-10-05, needs-triage,
1 comment — the cli-triage bot traced the same mechanism; unassigned, no competing PR)
**PR:** https://github.com/cli/cli/pull/14602 — OPEN (base `trunk`) — no bounty, tips welcome.

## Bug
Commands showing the progress spinner (e.g. `gh issue view` while its request is in
flight) hide the terminal cursor: briandowns/spinner writes `\x1b[?25l` on `Start()`
and restores it (`\x1b[?25h`) only on `Stop()`. `IOStreams` stops the spinner on the
normal path, but Ctrl+C kills the process immediately, so the cursor stays hidden in
the user's shell.

## Proof (red → green, end-to-end in a PTY)
A Python PTY harness ran the real `gh issue view 300 --repo cli/cli` with the child as
session leader, waited for the hide-cursor sequence, then sent SIGINT:

- **Unpatched** (base 6fc1c29): output contains `\x1b[?25l` at byte 0, spinner frames,
  process exits by SIGINT, and **`\x1b[?25h` never appears** — bug reproduced exactly.
- **Patched**: output ends `…\x1b[?25h\r\x1b[K`, `show_cursor_at=57 > hide_cursor_at=0`,
  process still exits by SIGINT (termination semantics unchanged).
- **Control**: patched binary run to completion without interrupt hides the cursor
  during load and restores it afterwards; the issue view renders normally (20 KB output).

Environment notes: Go 1.26.6 workspace toolchain; `/tmp` (512 MB shared tmpfs) filled
mid-build twice and a killed build poisoned the cache (ABIInternal relocation errors) —
resolved with `GOTMPDIR`/`TMPDIR` on the home filesystem + `go clean -cache`, per the
workspace AGENTS.md lessons. `pkg/iostreams` tests pass; gofmt/vet clean.

## Fix
`pkg/iostreams/iostreams.go` (+35 lines, 1 file, commit cfe1130 on
`Kshot3000/cli@fix/14601-spinner-cursor-on-interrupt`): while a real spinner runs,
`StartProgressIndicatorWithLabel` installs an `os.Interrupt` watcher (the pattern the
same file already uses for the alternate screen buffer). On interrupt it stops the
progress indicator — restoring the cursor — then re-delivers the signal so the
process terminates as it would have without the handler. `StopProgressIndicator`
removes the handler and closes a done channel releasing the watcher goroutine when
the spinner stops normally. The textual-indicator (spinner-disabled) path never
hides the cursor and is untouched.

## Submission status
PR #14602 OPEN. The cli/cli PR template's authorship section is answered honestly
(agent-written independently; agent drafts review replies for @Kshot3000 to read
first). Payment: none requested — no bounty on #14601; fix offered freely.
