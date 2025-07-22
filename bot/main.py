import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, setup_dialogs

from bot.config import settings
from bot.container import build_container
from bot.dialogs import dialogs
from bot.dialogs.start.states import StartStates
from bot.middlewares.service_middleware import ServiceMiddleware
from bot.middlewares.user_middleware import UserCheckMiddleware

container = build_container(settings.MONGO_URI, "mydatabase")

bot = Bot(
    token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
storage = RedisStorage.from_url(
    settings.REDIS_URL, key_builder=DefaultKeyBuilder(with_destiny=True)
)
dp = Dispatcher(storage=storage)

services = {
    "user_service": container["user_service"],
    "event_service": container["event_service"],
}

dp.update.outer_middleware(ServiceMiddleware(services))
dp.update.middleware(UserCheckMiddleware())


@dp.message(CommandStart())
async def command_start(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(StartStates.greeting, mode=StartMode.RESET_STACK)


async def main() -> None:
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        dp.include_routers(*dialogs)
        setup_dialogs(dp)
        await dp.start_polling(bot)
    finally:
        await container["mongo"].close()


if __name__ == "__main__":
    asyncio.run(main())
