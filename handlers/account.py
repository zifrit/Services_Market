from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from core.db_connections import db_helper
from buttons.account import account_inline_buttons
from buttons.pagination import vpn_pagination, Pagination
import logging
from crud import vpn as crud_vpn

loger = logging.getLogger(__name__)


router = Router()


@router.callback_query(
    F.data.in_(
        [
            "account",
        ]
    )
)
async def user_account(call: CallbackQuery):
    await call.message.edit_text(
        text=f"""
Личный кабинет

🆔:{call.from_user.id}
        """,
        reply_markup=account_inline_buttons,
    )


@router.callback_query(
    F.data.in_(
        [
            "my_vpn",
        ]
    )
)
async def user_vpn(call: CallbackQuery):
    async with db_helper.session_factory() as session:
        vpn, count_count = await crud_vpn.get_user_vpn(
            session=session, tg_id=call.from_user.id, limit=2
        )
        count_page = count_count // 2 + 1 if count_count % 2 != 0 else count_count // 2
        list_data = []
        for data in vpn:
            list_data.append(
                {
                    "text": f"{data.country} {data.price}",
                    "callback_data": f"{data.id}_{data.tg_user_id}",
                }
            )
        if count_count <= 2:
            await call.message.edit_text(
                text="some text",
                reply_markup=vpn_pagination(
                    list_data=list_data,
                    count_page=count_page,
                    back_callback_data="back_to_start_menu",
                ),
            )
        elif count_count > 2:
            await call.message.edit_text(
                text="some text",
                reply_markup=vpn_pagination(
                    list_data=list_data,
                    count_page=count_page,
                    name_nex_action="next_page_user_vpn",
                    back_callback_data="back_to_start_menu",
                ),
            )


@router.callback_query(
    Pagination.filter(F.action.in_(["prev_page_user_vpn", "next_page_user_vpn"]))
)
async def paginator_service(call: CallbackQuery, callback_data: Pagination):
    left = "prev_page_user_vpn"
    right = "next_page_user_vpn"
    if callback_data.action == "prev_page_user_vpn":
        if callback_data.page > 1:
            page = callback_data.page - 1
            if page <= 1:
                left = None
                right = "next_page_user_vpn"
        else:
            page = callback_data.page
            left = None
            right = "next_page_user_vpn"
    elif callback_data.action == "next_page_user_vpn":
        if callback_data.page < callback_data.count_page:
            page = callback_data.page + 1
            if page >= callback_data.count_page:
                left = "prev_page_user_vpn"
                right = None
        else:
            page = callback_data.page
            left = "prev_page_user_vpn"
            right = None

    async with db_helper.session_factory() as session:
        vpn, count_count = await crud_vpn.get_user_vpn(
            session=session,
            tg_user_id=call.from_user.id,
            limit=2,
            offset=page,
        )
        count_page = count_count // 2 + 1 if count_count % 2 != 0 else count_count // 2
        list_data = []
        for data in vpn:
            list_data.append(
                {
                    "text": f"{data.country} {data.price}",
                    "callback_data": f"{data.id}_{data.tg_user_id}",
                }
            )
        await call.message.edit_text(
            text="some text",
            reply_markup=vpn_pagination(
                list_data=list_data,
                count_page=count_page,
                page=page,
                name_prev_action=left,
                name_nex_action=right,
                back_callback_data="back_to_start_menu",
            ),
        )
