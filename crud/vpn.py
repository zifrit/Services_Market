from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from models import User
from models.vpn import UserVPN, VPN, Price
from crud.user import get_user

term = {
    "day": "день",
    "month": "месяц",
    "year": "год",
}


async def create_user_vpn(
    session: AsyncSession,
    key_price: str,
    tg_id: int,
) -> UserVPN:
    user = await get_user(session, tg_id)
    price = await get_price_by_key_price(session, key_price)
    country = await get_vpn_by_id(session, price.vpn_id)
    vpn = UserVPN(
        price_id=price.id,
        tg_user_id=user.id,
        view=f"{country.country_view_text} {price.price_view_text} {price.quantity} {term.get(price.term.value)}",
    )
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


async def get_user_vpn_s(
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


async def get_vpn_by_id(session: AsyncSession, _id: int) -> VPN:
    vpn = await session.scalar(select(VPN).where(VPN.id == _id))
    return vpn


async def get_vpn_key_country(session: AsyncSession, key_country: str) -> VPN:
    vpn = await session.scalar(select(VPN).where(VPN.key_country == key_country))
    return vpn


async def get_price_by_key_price(session: AsyncSession, key_price: str) -> Price:
    price = await session.scalar(select(Price).where(Price.key_price == key_price))
    return price


async def get_vpn_prices(
    session: AsyncSession, key_county: str
) -> tuple[list[Price], str]:
    vpn = await get_vpn_key_country(session, key_county)
    prices = await session.scalars(select(Price).where(Price.vpn_id == vpn.id))
    return list(prices), vpn.country_view_text
