from aiogram import F, Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.utils.deep_linking import decode_payload
from aiogram.types import Message, CallbackQuery
from core.db_connections import db_helper
import logging
from crud import user
from buttons import start
from crud.referral import create_referral

loger = logging.getLogger(__name__)


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, command: CommandObject):
    async with db_helper.session_factory() as session:
        if not await user.get_user(session, message.from_user.id):
            await user.create_users(
                session,
                message.from_user.username,
                message.from_user.id,
            )
        if command.args is not None:
            if message.from_user.id != int(decode_payload(command.args)):
                status = await create_referral(
                    session=session,
                    referrer_tg_id=message.from_user.id,
                    referred_tg_id=int(decode_payload(command.args)),
                )
                if status:
                    await message.answer(
                        "Рефиралка принята",
                    )
                else:
                    await message.answer(
                        "Уже есть рефиралка",
                    )
    await message.answer(
        """
Шмель-VPN🐝: Летим без ограничений!
Привет, друзья! Шмель-VPN – это ваш надежный спутник в мире без ограничений! Безлимитный трафик, никаких замедлений скорости – просто летите, куда хотите! 
Все ваши любимые соцсети работают без сбоев, а выбор стран – на любой вкус!  Летим вместе с Шмель-VPN!
    """,
        reply_markup=start.start_inline_button,
    )


@router.callback_query(F.data == "back_to_start_menu")
async def start_handler(call: CallbackQuery):
    await call.message.edit_text(
        """
Шмель-VPN🐝: Летим без ограничений!
Привет, друзья! Шмель-VPN – это ваш надежный спутник в мире без ограничений! Безлимитный трафик, никаких замедлений скорости – просто летите, куда хотите! 
Все ваши любимые соцсети работают без сбоев, а выбор стран – на любой вкус!  Летим вместе с Шмель-VPN!
    """,
        reply_markup=start.start_inline_button,
    )
