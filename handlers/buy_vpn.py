from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from buttons.start import back
from core.db_connections import db_helper
import logging
from buttons.buy_vpn import (
    buy_vpn_inline_buttons,
    choice_county_inline_buttons_builder,
    choice_tariff_inline_buttons_builder,
)
from crud import vpn as vpn_crud, order as order_crud, user as user_crud
from schematics.order import CreateOrderSchema

loger = logging.getLogger(__name__)


router = Router()


@router.callback_query(F.data.in_(["buy_vpn", "back_to_buy_vpn"]))
async def buy_vpn(call: CallbackQuery):
    await call.message.edit_text(
        text="""
Выберите VPN по цели использования или стране ⬇️\n
⚠️ Вы получите VPN той страны, в которой мы гарантируем работу выбранного вами направления.\n
Если же вам нужна конкретная страна VPN – жмите «Выбрать по стране».
        """,
        reply_markup=buy_vpn_inline_buttons,
    )


@router.callback_query(F.data.in_(["choice_county", "back_to_choice_county"]))
async def choice_county(call: CallbackQuery):
    async with db_helper.session_factory() as session:
        vpn_s = await vpn_crud.get_vpn_countries(session)
        vpn_data_list = [
            {"back_text": vpn.view_country, "back_callback_data": vpn.key_country}
            for vpn in vpn_s
        ]
    await call.message.edit_text(
        text="""
Выберите страну для вашего VPN ⬇️\n
⚠️ Если вам нужен VPN для соцсетей или торрентов – вернитесь назад и выберите цель использования. Ни в коем случае не используйте просто страновой VPN для скачивания с торрентов!\n
⛔️ Выбирая страну самостоятельно, мы НЕ гарантируем что ваш инстаграм будет работать в России с российского IP 😄
        """,
        reply_markup=choice_county_inline_buttons_builder(countries=vpn_data_list),
    )


@router.callback_query(F.data.startswith("country-"))
async def choice_county(call: CallbackQuery, state: FSMContext):
    async with db_helper.session_factory() as session:
        price_list, text = await vpn_crud.get_vpn_country_price(session, call.data)
        data_price_list = [
            {
                "back_text": f"🎟️{price.view_price}",
                "back_callback_data": f"{price.price_key}",
            }
            for price in price_list
        ]
        await state.update_data(country=text)
    await call.message.edit_text(
        text=f"""
{text}
💰 Лучший VPN по лучшей цене!

├ 1 мес: 100₽
├ 3 мес: 270₽
├ 6 год: 500₽
        """,
        reply_markup=choice_tariff_inline_buttons_builder(prices=data_price_list),
    )


@router.callback_query(F.data.startswith("tariff-"))
async def choice_county(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    key_price = call.data
    async with db_helper.session_factory() as session:
        price_id = await vpn_crud.get_price_id_by_price_key(session, key_price)
        tg_user_id = await user_crud.get_tg_user_id(session, tg_id=call.from_user.id)
        order_schema = CreateOrderSchema(
            price_id=price_id, tg_user_id=tg_user_id, status=True
        )
        order = await order_crud.create_order(
            session=session,
            order=order_schema,
        )
    await call.message.edit_text(
        text=f"""
Ваш заказ был принят✅

Информация о заказе:
Страна - {data['country']}
Цена - {order.price.view_price}
Срок - {order.price.term} {order.price.billing_period.value}
        """,
        reply_markup=back(back_text="🔙Назад", back_callback_data="back_to_start_menu"),
    )
