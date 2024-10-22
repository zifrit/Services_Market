from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

account_inline_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💰Пополнить баланс",
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
