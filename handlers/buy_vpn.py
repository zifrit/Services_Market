from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from core.db_connections import db_helper
import logging
from buttons.start import (
    buy_vpn_inline_buttons,
    choice_county_inline_buttons,
    choice_tariff_inline_buttons,
)
from utils.countries import countries
from utils.price_list import price_list

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
    await call.message.edit_text(
        text="""
Выберите страну для вашего VPN ⬇️\n
⚠️ Если вам нужен VPN для соцсетей или торрентов – вернитесь назад и выберите цель использования. Ни в коем случае не используйте просто страновой VPN для скачивания с торрентов!\n
⛔️ Выбирая страну самостоятельно, мы НЕ гарантируем что ваш инстаграм будет работать в России с российского IP 😄
        """,
        reply_markup=choice_county_inline_buttons,
    )


@router.callback_query(
    F.data.in_(
        [
            "germany_county",
            "france_county",
            "netherlands_county",
        ]
    )
)
async def choice_county(call: CallbackQuery, state: FSMContext):
    await state.update_data(country=countries[call.data])
    await call.message.edit_text(
        text=f"""
{countries[call.data]}
💰 Лучший VPN по лучшей цене!

├ 1 мес: 100₽
├ 3 мес: 270₽
├ 6 год: 500₽
        """,
        reply_markup=choice_tariff_inline_buttons,
    )


@router.callback_query(
    F.data.in_(
        [
            "1_moth_tariff",
            "3_moth_tariff",
            "6_moth_tariff",
        ]
    )
)
async def choice_county(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.message.edit_text(
        text=f"""
Ваш заказ:

Страна - {data['country']}
Цена - {price_list[call.data]}
Была успешна принята.
        """,
    )
