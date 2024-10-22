from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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