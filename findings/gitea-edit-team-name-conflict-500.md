# Gitea — EditTeam API returns 500 when the new team name is already taken

- **Project:** go-gitea/gitea
- **Issue:** https://github.com/go-gitea/gitea/issues/39632 (filed 2026-10-06: duplicate teams creatable via a creation race, and a subsequent `PATCH /api/v1/teams/{id}` on one of them returns an unhandled 500)
- **PR:** https://github.com/go-gitea/gitea/pull/39646 — OPEN / MERGEABLE, commit `0595ef7` GitHub-verified
- **Payment:** none posted on the issue; fix offered freely, tips welcome via the PR footer. Not a bounty request.

## Bug (the deterministic slice of #39632)

`PATCH /api/v1/teams/{id}` with a name that another team in the same organization already holds returned **HTTP 500** instead of a client error. No race is needed to reproduce it: with teams `alpha` and `beta` in one org, renaming `beta` to `alpha` is enough.

Root cause, traced through the code at upstream `2647540`:

- `services/org.UpdateTeam` checks for a conflicting team (`org_id` + `lower_name`, excluding self) and returns `organization.ErrTeamAlreadyExist`.
- The web UI create and edit handlers and the API `CreateTeam` handler all special-case that error (form error / HTTP 422).
- The API `EditTeam` handler (`routers/api/v1/org/team.go`) was the only one of the four call sites that mapped **every** `UpdateTeam` error to `ctx.APIErrorInternal(err)` — a 500.

## Fix

Mirror `CreateTeam` in the same file: map `organization.IsErrTeamAlreadyExist(err)` to `422 Unprocessable Entity`, keep `APIErrorInternal` for everything else, add the `422` response to the EditTeam swagger docs, and regenerate the swagger files (`make generate-swagger`, +6 lines across the two generated files). A regression case is added to the existing `TestAPITeam` integration test: create a third team, rename the second team to its name, expect 422 and an unchanged team, then clean up.

Scope note: this fixes the 500 half of #39632. The duplicate-creation race itself (check-then-insert without a uniqueness constraint) is a larger change and is called out as separate in the PR. Another contributor (manenim) had asked on the issue about investigating the race; this PR does not touch that part.

## Proof (red → green, end-to-end against locally built servers)

The sandbox runs as root and Gitea's integration-test harness strips the root-run env bypass, so verification was done with real `gitea web` servers (patched and unpatched binaries, fresh SQLite DBs, same API sequence: create org → create teams `alpha`/`beta` → `PATCH` beta's name to `alpha`):

- **Unpatched:** `HTTP 500` — `{"message":"team already exists [org_id: 2, name: alpha]"}`
- **Patched:** `HTTP 422` — same message, correct status; control rename `beta` → `gamma` still returns `200`.

Also: `go build ./routers/api/v1/org/` and `go vet` clean, gofmt clean, regenerated swagger committed per the repo's AGENTS.md (which also requires the `Assisted-by` commit trailer — included). The added integration-test case compiles (the integration package builds); CI is authoritative for its execution.
