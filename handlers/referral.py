from aiogram import F, Router
from aiogram.enums import ParseMode

from buttons.start import back
from aiogram.types import Message, CallbackQuery
from aiogram.utils.deep_linking import create_start_link
import logging
from core.db_connections import db_helper


loger = logging.getLogger(__name__)


router = Router()


@router.callback_query(F.data == "partners")
async def referral(call: CallbackQuery):
    link = await create_start_link(call.bot, f"{call.from_user.id}", encode=True)
    await call.message.edit_text(
        f"`{link}`",
        reply_markup=back("🔙Назад", "back_to_start_menu"),
        parse_mode=ParseMode.MARKDOWN,
    )
