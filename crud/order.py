from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from models.order import Payment, Order, PaymentsStatus
from models.vpn import Price
from crud.vpn import get_price
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


async def create_payment(session: AsyncSession, order_id: int, price_id: int) -> int:
    price = await get_price(session, price_id)
    payment_schema = CreatePaymentSchema(
        currency=price.currency,
        status=PaymentsStatus.completed,  # todo пока по дефолту стоит что пополнение произошло, но потом нужно будет поставить в процессе и переключить после принятия оплаты по хуку
        amount=price.price,
        order_id=order_id,
    )
    payment = Payment(**payment_schema.model_dump())
    session.add(payment)
    await session.commit()
    return payment.id
