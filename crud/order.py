from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from models.order import Payment, Order
from models.vpn import Price
from schematics.order import (
    CreateOrderSchema,
    CreatePaymentSchema,
    ShowOrderSchema,
    ShowPaymentSchema,
)


async def create_order(
    session: AsyncSession, order: CreateOrderSchema
) -> ShowOrderSchema:
    order = Order(**order.model_dump())
    session.add(order)
    await session.commit()
    return await get_order(session, order.id)


async def get_order(session: AsyncSession, order_id: int) -> ShowOrderSchema:
    order = await session.scalar(
        select(Order)
        .options(
            joinedload(Order.price).load_only(
                Price.view_price, Price.term, Price.billing_period
            )
        )
        .where(Order.id == order_id)
    )
    return ShowOrderSchema.model_validate(order)
