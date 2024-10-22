import asyncio
import logging
import logging.config
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from core.settings import bot_settings
from core.logger import LOGGING
from handlers import (
    start,
    buy_vpn,
    account,
)

commands = [
    types.BotCommand(command="start", description="запуск бота"),
]


async def main():
    bot = Bot(
        token=bot_settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(
        start.router,
        buy_vpn.router,
        account.router,
    )
    await bot.set_my_commands(commands=commands)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.config.dictConfig(LOGGING)
    asyncio.run(main())
