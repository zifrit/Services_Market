from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from models.vpn import UserVPN
from crud.user import get_user


async def create_vpn(
    session: AsyncSession,
    price: str,
    country: str,
    tg_id: int,
) -> UserVPN:
    user = await get_user(session, tg_id)
    vpn = UserVPN(price=price, country=country, tg_user_id=user.id)
    session.add(vpn)
    await session.commit()
    return vpn


async def get_vpn(session: AsyncSession, _id: int) -> UserVPN:
    vpn = await session.scalar(select(UserVPN).where(UserVPN.id == _id))
    return vpn


async def count_get_user_vpn(
    session: AsyncSession,
    user: User,
) -> int:
    count_vpn = await session.scalar(
        select(func.count(UserVPN.id)).where(UserVPN.tg_user_id == user.id)
    )
    return count_vpn


async def get_user_vpn(
    session: AsyncSession,
    tg_id: int,
    limit: int = 5,  # page size
    offset: int = 1,  # page number
) -> tuple[list[UserVPN], int]:
    user = await get_user(session, tg_id)
    vpn = await session.scalars(
        select(UserVPN)
        .limit(limit)
        .offset(offset=(limit * (offset - 1)))
        .where(UserVPN.tg_user_id == user.id)
    )
    return list(vpn), await count_get_user_vpn(session, user)
