from datetime import date, datetime, timedelta

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from models.referral import Referral
from crud.user import get_user


async def create_referral(
    session: AsyncSession, referred_tg_id: int, referrer_tg_id: int
):
    referrer_user = await get_user(session, tg_id=referrer_tg_id)
    referred_user = await get_user(session, tg_id=referred_tg_id)
    print(referred_tg_id)
    print(referrer_tg_id)
    is_referral = await session.scalar(
        select(Referral).where(Referral.referred_user_id == referred_user.id)
    )
    if not is_referral:
        referral = Referral(
            referred_user_id=referred_user.id,
            referrer_id=referrer_user.id,
        )
        session.add(referral)
        await session.commit()
        return True
    return False


async def get_referral_statics(session: AsyncSession, tg_id: int) -> dict[str, int]:
    user = await get_user(session, tg_id=tg_id)
    count_referral = await session.scalar(
        select(func.count(Referral.id)).where(Referral.referred_user_id == user.id)
    )
    today = date.today()
    start_of_day = datetime.combine(today, datetime.min.time())
    end_of_day = start_of_day + timedelta(days=1)
    count_referral_today = await session.scalar(
        select(func.count(Referral.id)).where(
            Referral.created_at.between(start_of_day, end_of_day),
            Referral.referred_user_id == user.id,
        )
    )
    return {
        "count_referral": count_referral,
        "count_referral_today": count_referral_today,
    }
