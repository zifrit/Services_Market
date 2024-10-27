from aiogram import F, Router
from aiogram.enums import ParseMode

from buttons.start import back
from aiogram.types import Message, CallbackQuery
from aiogram.utils.deep_linking import create_start_link
import logging
from core.db_connections import db_helper
from crud import referral as crud_referral


loger = logging.getLogger(__name__)


router = Router()


@router.callback_query(F.data == "partners")
async def referral(call: CallbackQuery):
    link = await create_start_link(call.bot, f"{call.from_user.id}", encode=True)
    async with db_helper.session_factory() as session:
        statistics = await crud_referral.get_referral_statics(
            session, call.from_user.id
        )
    await call.message.edit_text(
        f"""
Реферальная ссылка: `{link}`

Статистика📊
Рефералов за все время: {statistics['count_referral']}
Рефералов за сегодня: {statistics['count_referral_today']}
Активные рефералы:
            """,
        reply_markup=back("🔙Назад", "back_to_start_menu"),
        parse_mode=ParseMode.MARKDOWN,
    )
