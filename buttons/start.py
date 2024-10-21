from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


start_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🛡️Купить VPN",
                callback_data="buy_vpn",
            ),
            InlineKeyboardButton(
                text="🛡️Мой VPN",
                callback_data="my_vpn",
            ),
        ],
        [
            InlineKeyboardButton(
                text="💰Пополнить",
                callback_data="replenish",
            ),
            InlineKeyboardButton(
                text="⚙️Аккаунт",
                callback_data="account",
            ),
        ],
        [
            InlineKeyboardButton(
                text="👥О нас",
                callback_data="about_us",
            ),
            InlineKeyboardButton(
                text="🆘Помощь",
                callback_data="user_help",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🤝Партнеры",
                callback_data="partners",
            ),
            InlineKeyboardButton(
                text="🧩Наши каналы",
                callback_data="user_help",
                url="https://ya.ru/",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📎Другие сервисы",
                callback_data="other_services",
            ),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


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
