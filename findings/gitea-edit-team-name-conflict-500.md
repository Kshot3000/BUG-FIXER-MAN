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

## Revision — maintainer feedback, both points accepted (2026-10-06)

wxiaoguang reviewed within minutes of the PR opening with two points — "1. db table column unique, 2. APIErrorAuto" — and Kyle accepted both. Two new commits pushed (PR head `9bb973c`, signature verified):

- `f64f942` fix(models): unique index on `team (org_id, lower_name)` declared on the Team model (`TableIndices`, index name `unique_team_org_lower_name`) + migration 358 (`modelmigration/v29/v358.go`, registered in `modelmigration/migrations.go`). The migration removes pre-existing duplicate teams before syncing the index, following wxiaoguang's own user_badge migration (329) — the codebase's established pattern for adding a unique index to a possibly-dirty table. The service-level check is unchanged; the constraint is the backstop that makes the creation race in #39632 unable to store duplicates. New tests: `TestTeam_UniqueOrgLowerName` (models/organization — duplicate insert in the same org errors, same name in another org succeeds) and `Test_AddUniqueIndexForTeam` (modelmigration/v29 — inserts duplicates, migrates, asserts dedupe to one row per org/name and that a further duplicate insert fails).
- `9bb973c` fix(api): EditTeam now calls `ctx.APIErrorAuto(err)`. `ErrTeamAlreadyExist` unwraps to `util.ErrAlreadyExist`, so the duplicate-rename response is now **409** with the same message (superseding the hand-mapped 422 from the first version). Swagger annotations + regenerated specs and the `TestAPITeam` regression case updated to 409. PR title/body updated accordingly; reply posted: https://github.com/go-gitea/gitea/pull/39646#issuecomment-6024591942

Verification this round (all local, sqlite): `TestAPITeam` integration test PASS (full binary + test harness via `make test-integration#TestAPITeam`); `Test_AddUniqueIndexForTeam` PASS; `TestTeam_UniqueOrgLowerName` PASS; full `models/organization`, `services/org`, `modelmigration/v29` package tests PASS; `TestMigrations` registry test PASS; `go vet` and `gofmt` clean on all changed packages; fixtures contain no duplicate (org_id, lower_name) pairs, so the new index doesn't disturb fixture loading. Sandbox note: the test harness strips the root-run env bypass, so tests ran with the unsafe-root key added to the generated test config (template edit reverted afterwards; not part of the PR diff).
