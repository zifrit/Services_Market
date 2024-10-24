from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from models.referral import Referral
from crud.user import get_user


async def create_referral(
    session: AsyncSession, referred_tg_id: int, referrer_tg_id: int
):
    referrer_user = await get_user(session, tg_id=referrer_tg_id)
    referred_user = await get_user(session, tg_id=referred_tg_id)
    print(referrer_user)
    print(referred_user)
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
