from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.countries import countries

buy_vpn_inline_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🌏Выбор по стране",
                callback_data="choice_county",
            )
        ],
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data="back_to_start_menu",
            )
        ],
    ]
)

choice_county_inline_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🇩🇪Германия",
                callback_data="germany_county",
            )
        ],
        [
            InlineKeyboardButton(
                text="🇫🇷Франция",
                callback_data="france_county",
            )
        ],
        [
            InlineKeyboardButton(
                text="🇳🇱Нидерланды",
                callback_data="netherlands_county",
            )
        ],
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data="back_to_buy_vpn",
            )
        ],
    ]
)


def choice_county_inline_buttons_builder(countries: list[dict]):
    builder = InlineKeyboardBuilder()
    for county in countries:
        builder.row(
            InlineKeyboardButton(
                text=county["back_text"],
                callback_data=county["back_callback_data"],
            )
        )
    builder.row(
        InlineKeyboardButton(
            text="🔙 Назад",
            callback_data="back_to_buy_vpn",
        )
    )
    return builder.as_markup()


choice_tariff_inline_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🎟️ 1 месяц",
                callback_data="1_moth_tariff",
            ),
            InlineKeyboardButton(
                text="🎟️ 3 месяц",
                callback_data="3_moth_tariff",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🎟️ 6 месяц",
                callback_data="6_moth_tariff",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data="back_to_choice_county",
            )
        ],
    ]
)


def choice_tariff_inline_buttons_builder(prices: list[dict]):
    builder = InlineKeyboardBuilder()
    for price in prices:
        builder.row(
            InlineKeyboardButton(
                text=price["back_text"],
                callback_data=price["back_callback_data"],
            )
        )
    builder.row(
        InlineKeyboardButton(
            text="🔙 Назад",
            callback_data="back_to_choice_county",
        )
    )
    return builder.as_markup()


def list_user_vpn_inline_buttons(
    back_text: str, back_callback_data: str
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text=back_text, callback_data=back_callback_data), width=1
    )
    return builder.as_markup()
