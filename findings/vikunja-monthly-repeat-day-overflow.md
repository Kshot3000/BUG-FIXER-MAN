# Vikunja — monthly repeat on the 31st skips a month (Jan 31 → Mar 3)

- **Project:** go-vikunja/vikunja (self-hosted to-do app, Go)
- **Issue:** [#4104](https://github.com/go-vikunja/vikunja/issues/4104) — filed 2026-10-05, unassigned, no competing PR (timeline cross-references empty; the only comment is an unrelated AI-tooling remark)
- **PR:** [#4107](https://github.com/go-vikunja/vikunja/pull/4107) — OPEN (2026-10-05, base main)
- **Bounty:** none posted; fix offered freely, tips welcome via the PR footer.

## Bug

`addOneMonthToDate` (`pkg/models/tasks.go`) built the next occurrence with the
original day of the month:

```go
time.Date(d.Year(), d.Month()+1, d.Day(), ...)
```

Go normalizes a day that doesn't exist in the target month into the month
after next. A task due **January 31, 2027** with repeat mode **Monthly**
therefore moved to **March 3, 2027** when marked done: February got no
occurrence at all, and because the day was now the 3rd, every later
occurrence stayed on the 3rd — the original day was lost for good.
`setTaskDatesMonthRepeat` routes the due date, all reminders, and the
start/end dates through the same helper, so all of them overflowed the same
way (March 31 → May 1, October 31 → December 1).

## Fix

Clamp the day to the number of days in the target month (last day computed
via `time.Date(year, month+1, 0, ...)`), with explicit December → January
year rollover. January 31 now repeats to February 28 (February 29 in a leap
year) — exactly the expected behavior stated in the issue. Later occurrences
continue from the clamped day; remembering the original day across
occurrences would need persisted state and is a separate design decision
(the issue raises and accepts this).

## Proof (red → green)

New `TestAddOneMonthToDate` (`pkg/models/tasks_test.go`, 7 cases):

- Unpatched: the 4 overflow cases fail with exactly the reported dates —
  Jan 31 2027 → **Mar 3** (want Feb 28), Jan 31 2028 → **Mar 2** (want
  Feb 29), Mar 31 → **May 1** (want Apr 30), Oct 31 → **Dec 1** (want
  Nov 30). Regular-day, December-rollover, and Feb 28 controls pass.
- Patched: 7/7 pass; full `go test ./pkg/models/ -count=1` passes;
  `gofmt` / `go vet` clean. (One test-authoring note: the helper returns
  times in `config.GetTimeZone()`, so the test builds expectations in that
  location instead of `time.UTC`.)

## Same-run sector-5 rejects

- **navidrome #6270** (smart-playlist `dateAdded` vs birth time): mechanism
  verified in code — `dateadded` → `media_file.created_at` (import time) is
  *consistent* with the song-level `recently_added` sort and
  `mediaFileCreatedAt`; the reporter's "recently added" page is the
  album list, whose `created_at` is birth-time-derived since #1350.
  Remapping would break song-level consistency — a maintainer design call,
  not a clean fix. **Rejected.**
- **navidrome #6273** (add-to-playlist list incomplete): UI requests
  `perPage: -1`; traced UI → ra-data-json-server → deluan/rest → persistence
  — `Max=0` means no limit anywhere. No repro data (playlist count/ownership
  mix unknown). **Rejected as unverifiable.**
- **chatwoot #16122** (conversation list 500 on deleted assignee): already
  has competing PR #16123. **Rejected.**
- **chatwoot #16133** (widget `status_changed_at=` NoMethodError): instance
  schema quirk on 4.17.1, migrations all "up" — not a code bug. **Rejected.**
- **linkding #1510** (quoted acronym substring search): feature request for
  a whole-word option — design call. **Rejected.**
- **jellyfin #18306** (version-prefix brackets): no .NET toolchain in this
  sandbox; 4 comments of ongoing discussion. **Rejected.**
- **twenty #27249** (currency default ignored in creation form): huge
  monorepo, full-stack repro not feasible here. **Rejected for this run.**
- **formbricks #9504** (`private.icloud.com` missing from personal-domain
  list): one-word data addition with a reporter already offering a PR.
  **Rejected (too thin / claimed in spirit).**
