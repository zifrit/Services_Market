from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from core.db_connections import db_helper
import logging
from crud import user

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
    await message.answer("Привет новый пользователь")
