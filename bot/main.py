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
from pymongo import AsyncMongoClient

from bot.config import settings
from bot.dialogs import dialogs
from bot.dialogs.start.states import StartStates
from bot.middlewares.service_middleware import ServiceMiddleware
from bot.repositories.event_repo import EventsRepository
from bot.services.event_service import EventService

bot = Bot(
    token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
storage = RedisStorage.from_url(
    settings.REDIS_URL, key_builder=DefaultKeyBuilder(with_destiny=True)
)
dp = Dispatcher(storage=storage)


client = AsyncMongoClient(settings.MONGO_URI)  # type: ignore
db = client.mydatabase
collection = db.events

event_repo = EventsRepository(collection)
event_service = EventService(event_repo)
dp.update.middleware(ServiceMiddleware(event_service))


@dp.message(CommandStart())
async def command_start(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(StartStates.greeting, mode=StartMode.RESET_STACK)


async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.include_routers(*dialogs)
    setup_dialogs(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
