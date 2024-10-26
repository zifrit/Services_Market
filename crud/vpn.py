from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from models import User
from models.vpn import UserVPN, VPN, Price
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


async def get_user_vpn(session: AsyncSession, _id: int) -> UserVPN:
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


async def get_vpn_s(session: AsyncSession) -> list[VPN]:
    vpn_s = await session.scalars(select(VPN))
    return list(vpn_s)


async def get_vpn(session: AsyncSession, _id: int) -> VPN:
    vpn = await session.scalar(select(VPN).where(VPN.id == _id))
    return vpn


async def get_vpn_price(session: AsyncSession, key_county: str) -> list[Price]:
    vpn_s = await session.scalar(
        select(VPN)
        .options(selectinload(VPN.prices))
        .where(VPN.key_country == key_county)
    )
    return vpn_s.prices
