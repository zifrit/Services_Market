from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped
from models import UserVPNs, Country, Price
from schematics.vpn import (
    CreateUserVPNsSchema,
    ShowUserVPNsSchema,
    ShowCountriesSchema,
    ShowPricesSchema,
)



async def create_vpn_s(session: AsyncSession, user_vpn: CreateUserVPNsSchema) -> None:
    vpn = UserVPNs(**user_vpn.model_dump())
    session.add(vpn)
    await session.commit()


async def get_user_vpn(session: AsyncSession, _id: int) -> ShowUserVPNsSchema:
    vpn = await session.scalar(select(UserVPNs).where(UserVPNs.id == _id))
    return ShowUserVPNsSchema.model_validate(vpn)


async def get_vpn_countries(session: AsyncSession) -> list[ShowCountriesSchema]:
    countries = await session.scalars(select(Country))
    return [ShowCountriesSchema.model_validate(country) for country in countries]


async def get_vpn_country_price(
    session: AsyncSession, country_key: str
) -> tuple[list[ShowPricesSchema], Mapped[str]]:
    country = await session.scalar(
        select(Country).where(Country.key_country == country_key)
    )
    prices = await session.scalars(select(Price).where(Price.country_id == country.id))
    return [
        ShowPricesSchema.model_validate(price) for price in prices
    ], country.view_country


async def get_price_id_by_price_key(session: AsyncSession, price_key: str) -> int:
    price = await session.scalar(select(Price.id).where(Price.price_key == price_key))
    return price