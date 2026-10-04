# Great Expectations — ExpectTableColumnsToMatchSet(column_set=None) crashes on SQL backends

- **Project:** fivetran/great_expectations — https://github.com/fivetran/great_expectations
- **Issue:** #12288 — "ExpectTableColumnsToMatchSet with column_set=None raises on SQL backends but is treated as an empty set on pandas" https://github.com/fivetran/great_expectations/issues/12288 (filed 2026-10-04, unclaimed, no competing fix PR)
- **Submission:** verified diagnosis + root cause + fix posted on the issue: https://github.com/fivetran/great_expectations/issues/12288#issuecomment-5983797548 — tested patch ready on fork branch `Kshot3000/great_expectations@fix/match-set-none-sql` (commit d42d0e4). **PR NOT opened yet: the repo's AGENTS.md makes the Contributor License Agreement a hard stop for agents — Kyle must sign the GE CLA personally (Google form linked from the repo CLA.md) before the PR can be opened; then it opens from that branch immediately.**
- **Bounty:** none — standards/OSS fix offered freely.
- **Status:** AWAITING KYLE (CLA) + maintainer triage of #12288.

## Bug

`column_set` is typed `Union[list, set, SuiteParameterDict, None]`, so `None` is an allowed value. The generic (pandas/Spark) validation path in `expect_table_columns_to_match_set.py` guards it:

```python
expected_column_set = set(expected_column_list) if expected_column_list is not None else set()
```

`_validate_sqlalchemy` did not:

```python
expected_column_set = set(self._get_success_kwargs().get("column_set"))
```

So on every SQL backend, `column_set=None` raised `'NoneType' object is not iterable` instead of returning a verdict.

## Proof (red → green)

Reporter's exact SQLite repro, run locally on `develop` @ 7d52570:

| Backend | exact_match=True (default) | exact_match=False |
|---|---|---|
| SQLite (pre-fix) | `False`, exception `'NoneType' object is not iterable` | `False`, same exception |
| Pandas (pre-fix) | `False`, no exception (mismatched: unexpected a, b) | `True`, no exception |
| SQLite (post-fix) | `False`, no exception | `True`, no exception |

Regression tests added to `tests/integration/data_sources_and_expectations/expectations/test_expect_table_columns_to_match_set.py`, parameterized over pandas + SQLite, asserting `raised_exception is False` and the expected verdict for both `exact_match` modes: the SQLite cases **fail unpatched and pass patched**; the full pandas+SQLite selection for the file passes **22/22**; ruff check + format clean. (Cloud-backend parameterizations — postgres/snowflake/etc. — error locally for missing credentials/deps, a local-env limit; CI covers them. The fix is in the shared SQLAlchemy path all SQL backends use.)

## Fix

Mirror the generic path in `_validate_sqlalchemy`: `None` becomes an empty set. One behavioral change, no API change. The alternative direction (rejecting `None` at construction) was deliberately not taken — the field type explicitly allows `None` and the non-SQL backends already define its semantics; the issue comment says so and offers to adjust if maintainers prefer it.
