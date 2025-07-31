import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, setup_dialogs

from bot.config import settings
from bot.container import build_container
from bot.dialogs import dialogs
from bot.dialogs.admin.states import AdminState
from bot.dialogs.start.states import StartStates
from bot.middlewares.service_middleware import ServiceMiddleware
from bot.middlewares.user_middleware import UserCheckMiddleware
from bot.utils.start_consumers import start_notificate_consumer

bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
storage = RedisStorage.from_url(
    settings.REDIS_URL, key_builder=DefaultKeyBuilder(with_destiny=True)
)
dp = Dispatcher(storage=storage)


@dp.message(CommandStart())
async def command_start(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(StartStates.greeting, mode=StartMode.RESET_STACK)


@dp.message(Command("admin"), F.from_user.id.in_(settings.ADMIN_IDS))
async def start_admin(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(AdminState.menu, mode=StartMode.RESET_STACK)


async def main() -> None:
    try:
        container = await build_container(settings.MONGO_URI, "mydatabase")

        services = {
            "user_service": container["user_service"],
            "event_service": container["event_service"],
        }

        nc = container["nc"]
        js = container["js"]

        dp.update.outer_middleware(ServiceMiddleware(services))
        dp.update.middleware(UserCheckMiddleware())

        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        dp.include_routers(*dialogs)
        setup_dialogs(dp)
        await asyncio.gather(
            dp.start_polling(bot, js=js, notificate_subject=settings.NATS_SUBJECT),
            start_notificate_consumer(
                nc=nc,
                js=js,
                bot=bot,
                subject=settings.NATS_SUBJECT,
                stream=settings.NATS_STREAM,
                durable=settings.NATS_NOTIFICATE_DURABLE_NAME,
            ),
        )
    finally:
        await container["mongo"].close()
        await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
