# DentalPin — duplicate clinic memberships 500 four more membership checks (#590 follow-up)

- **Project / repo:** https://github.com/dentalpin/dentalpin (open-source dental clinic software, Python/FastAPI/SQLAlchemy, 84★, active)
- **Issue / bounty:** https://github.com/dentalpin/dentalpin/issues/590 (reported 500 in orthodontics; fixed there by PR #598 from another contributor). No bounty posted on the issue — fix offered freely, tips welcome. This find is the **same bug class in four unchecked locations** found by auditing the codebase for the identical query shape.
- **Found:** 2026-10-02
- **Severity / type:** correctness / availability (500 Internal Server Error on legitimate requests), one instance in an authorization path (cross-clinic admin check 500s instead of allowing a legit admin or returning a clean 403)
- **Bug:** `clinic_memberships` has no unique `(clinic_id, user_id)` constraint, so duplicate membership rows occur in real installs (#590). Four existence checks used `scalar_one_or_none()` on that non-unique query and raise `MultipleResultsFound`:
  1. `treatment_plan/service.py` — `_validate_professional_in_clinic`
  2. `schedules/services/professional_hours.py` — `ProfessionalHoursService.is_professional`
  3. `agenda/service.py` — `AppointmentService.validate_professional_access`
  4. `core/auth/router.py` — `create_user` cross-clinic admin check
- **Proof:** Local reproduction against the **real imported service functions** (SQLite session with only `clinic_memberships`, one user with two identical dentist rows, one with two admin rows): before the fix, all four checks raised `MultipleResultsFound: Multiple rows were found when one or none was required`; after the fix, all return correct results and non-member controls are unchanged. Repro script: `fixes/dentalpin-duplicate-membership-repro.py`. Note: the project's own suite needs Postgres (CI) — not available locally; the new pytest regression tests follow #598's style and are for CI to exercise.
- **Fix:** `.limit(1)` existence read at all four sites (identical to the approach in #598), regression tests in `backend/tests/test_duplicate_membership_checks.py`, module CHANGELOG entries. Patch: `fixes/dentalpin-duplicate-membership-existence-checks.patch`
- **Tests:** repro red → green (7/7 checks); `ruff check` + `ruff format --check` pass on all touched files; full project suite not run locally (needs Postgres — stated openly in the PR).
- **Submission:** PR https://github.com/dentalpin/dentalpin/pull/599 — submitted 2026-10-02, awaiting review. Fork: https://github.com/Kshot3000/dentalpin branch `fix/duplicate-membership-existence-checks` (commit 0b9ff96).
- **Payment:** requested: none (no bounty posted; tips welcome via hub README addresses) | received: none
- **Disclosure:** n/a — publicly reported bug class in the project's own issue tracker; no new vulnerability details.
