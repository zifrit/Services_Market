from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from core.db_connections import db_helper
import logging
from crud import user
from buttons import start

loger = logging.getLogger(__name__)


router = Router()


@router.message(F.text == "/start")
async def start_handler(message: Message):
    async with db_helper.session_factory() as session:
        if not await user.get_user(session, message.from_user.id):
            await user.create_users(
                session,
                message.from_user.username,
                message.from_user.id,
            )
    await message.answer(
        """
🔥 Наши серверы не имеют ограничений по скорости и трафику, VPN работает на всех устройствах, YouTube в 4К – без задержек!\n
🔥 Максимальная анонимность и безопасность, которую не даст ни один VPN сервис в мире.\n
✅ Наш канал: 
    """,
        reply_markup=start.start_inline_button,
    )


@router.callback_query(F.data == "back_to_start_menu")
async def start_handler(call: CallbackQuery):
    await call.message.edit_text(
        """
🔥 Наши серверы не имеют ограничений по скорости и трафику, VPN работает на всех устройствах, YouTube в 4К – без задержек!\n
🔥 Максимальная анонимность и безопасность, которую не даст ни один VPN сервис в мире.\n
✅ Наш канал: 
    """,
        reply_markup=start.start_inline_button,
    )
