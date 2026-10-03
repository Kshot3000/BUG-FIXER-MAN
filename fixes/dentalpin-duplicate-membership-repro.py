"""Repro: duplicate clinic_memberships rows break membership existence checks.

Uses the REAL DentalPin service functions against an in-memory-style SQLite
DB containing ONLY the clinic_memberships table (mirroring production,
where clinic_memberships has NO unique (clinic_id, user_id) constraint —
see dentalpin issue #590).
"""
import asyncio
import os
import sys
from uuid import uuid4

os.environ.setdefault("TESTING", "true")
os.environ.setdefault("SECRET_KEY", "test-secret-key-for-ci-1234567890")
os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:////home/hatch/.cache/bfm/repro.db")

sys.path.insert(0, "/path/to/dentalpin/backend")

from sqlalchemy import select  # noqa: E402
from sqlalchemy.exc import MultipleResultsFound  # noqa: E402
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine  # noqa: E402

from app.core.auth.models import ClinicMembership  # noqa: E402

# Import all model modules so SQLAlchemy relationships resolve (mirrors tests/conftest.py)
import app.modules.agenda.models  # noqa: E402,F401
import app.modules.billing.models  # noqa: E402,F401
import app.modules.budget.models  # noqa: E402,F401
import app.modules.catalog.models  # noqa: E402,F401
import app.modules.clinical_notes.models  # noqa: E402,F401
import app.modules.india_gst.models  # noqa: E402,F401
import app.modules.media.models  # noqa: E402,F401
import app.modules.odontogram.models  # noqa: E402,F401
import app.modules.patients.models  # noqa: E402,F401
import app.modules.payments.models  # noqa: E402,F401
import app.modules.periodontogram.models  # noqa: E402,F401
import app.modules.recalls.models  # noqa: E402,F401
import app.modules.schedules.models  # noqa: E402,F401
import app.modules.treatment_plan.models  # noqa: E402,F401
import app.modules.verifactu.models  # noqa: E402,F401
from app.modules.agenda.service import AppointmentService  # noqa: E402
from app.modules.schedules.services.professional_hours import ProfessionalHoursService  # noqa: E402
from app.modules.treatment_plan.service import _validate_professional_in_clinic  # noqa: E402


async def main() -> int:
    if os.path.exists("/home/hatch/.cache/bfm/repro.db"):
        os.remove("/home/hatch/.cache/bfm/repro.db")
    engine = create_async_engine("sqlite+aiosqlite:////home/hatch/.cache/bfm/repro.db")
    async with engine.begin() as conn:
        await conn.run_sync(ClinicMembership.__table__.create)
    maker = async_sessionmaker(engine, expire_on_commit=False)

    clinic_id, user_id, stranger_id = uuid4(), uuid4(), uuid4()
    admin_id = uuid4()
    async with maker() as s:
        # ONE user, TWO membership rows for the same clinic (the exact
        # state issue #590 reports in real installs).
        s.add_all([
            ClinicMembership(id=uuid4(), user_id=user_id, clinic_id=clinic_id, role="dentist"),
            ClinicMembership(id=uuid4(), user_id=user_id, clinic_id=clinic_id, role="dentist"),
            # A second user with TWO admin rows (for the auth-router check).
            ClinicMembership(id=uuid4(), user_id=admin_id, clinic_id=clinic_id, role="admin"),
            ClinicMembership(id=uuid4(), user_id=admin_id, clinic_id=clinic_id, role="admin"),
        ])
        await s.commit()

    failures = 0

    async def check(name, coro_factory, expect_ok):
        nonlocal failures
        async with maker() as s:
            try:
                result = await coro_factory(s)
                status = f"returned {result!r}"
                ok = expect_ok(result)
            except MultipleResultsFound as e:
                status = f"RAISED MultipleResultsFound: {e}"
                ok = False
            except ValueError as e:
                status = f"raised ValueError({e})"
                ok = expect_ok(e)
            print(f"{name}: {status} -> {'OK' if ok else 'BUG/FAIL'}")
            if not ok:
                failures += 1

    # 1. treatment_plan professional validation (duplicate rows)
    await check(
        "treatment_plan._validate_professional_in_clinic (dup)",
        lambda s: _validate_professional_in_clinic(s, clinic_id, user_id),
        lambda r: r is None,
    )
    # 2. schedules professional_hours is_professional (duplicate rows)
    await check(
        "professional_hours.is_professional (dup)",
        lambda s: ProfessionalHoursService.is_professional(s, clinic_id, user_id),
        lambda r: r is True,
    )
    # 3. agenda validate_professional_access (duplicate rows)
    await check(
        "agenda.validate_professional_access (dup)",
        lambda s: AppointmentService.validate_professional_access(s, clinic_id, user_id),
        lambda r: r is True,
    )
    # 4. auth router cross-clinic admin check — exact query from
    #    app/core/auth/router.py create_user() (inline in the endpoint)
    async def admin_check(s):
        result = await s.execute(
            select(ClinicMembership.id)
            .where(
                ClinicMembership.user_id == admin_id,
                ClinicMembership.clinic_id == clinic_id,
                ClinicMembership.role == "admin",
            )
            .limit(1)
        )
        return result.scalar_one_or_none() is not None

    await check("auth/router caller_is_admin query (dup admin rows -> expect True, not crash)",
                admin_check, lambda r: r is True)

    # Negative controls: stranger with no membership at all
    await check(
        "treatment_plan._validate_professional_in_clinic (no membership -> ValueError)",
        lambda s: _validate_professional_in_clinic(s, clinic_id, stranger_id),
        lambda r: isinstance(r, ValueError),
    )
    await check(
        "professional_hours.is_professional (no membership -> False)",
        lambda s: ProfessionalHoursService.is_professional(s, clinic_id, stranger_id),
        lambda r: r is False,
    )
    await check(
        "agenda.validate_professional_access (no membership -> False)",
        lambda s: AppointmentService.validate_professional_access(s, clinic_id, stranger_id),
        lambda r: r is False,
    )

    await engine.dispose()
    print(f"\nRESULT: {'ALL OK' if failures == 0 else f'{failures} failing check(s)'}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
