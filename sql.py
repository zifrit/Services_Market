from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload


from core.db_connections import db_helper
from models.vpn import VPN, Price, AssociationVPNPrice
import asyncio


async def create_vpn_with_price():
    vpn_1 = VPN(country="germany", country_view_text="Германия")
    vpn_2 = VPN(country="france", country_view_text="Франция")

    price_1 = Price(price="100", price_view_text="100₽")
    price_2 = Price(price="200", price_view_text="200₽")
    price_3 = Price(price="300", price_view_text="300₽")

    async with db_helper.session_factory() as session:
        session.add(vpn_1)
        session.add(vpn_2)
        session.add(price_1)
        session.add(price_2)
        session.add(price_3)
        await session.commit()

        vpn_1_ = await session.scalar(
            select(VPN).options(selectinload(VPN.price)).where(VPN.id == vpn_1.id)
        )
        vpn_2_ = await session.scalar(
            select(VPN).options(selectinload(VPN.price)).where(VPN.id == vpn_2.id)
        )

        vpn_1_.price.append(price_1)
        vpn_1_.price.append(price_2)
        vpn_2_.price.append(price_3)

        await session.commit()


async def mina():
    await create_vpn_with_price()


if __name__ == "__main__":
    asyncio.run(mina())
