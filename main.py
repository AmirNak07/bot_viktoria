import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, setup_dialogs

from config import settings
from dialogs.main_menu.windows import main_menu_dialog
from dialogs.platform_search.windows import platform_search_dialog
from dialogs.start.states import StartStates
from dialogs.start.windows import start_dialog
from dialogs.useful_links.window import dialog as useful_link_dialog

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(StartStates.greeting, mode=StartMode.RESET_STACK)


async def main() -> None:
    dp.include_router(start_dialog)
    dp.include_router(main_menu_dialog)
    dp.include_router(platform_search_dialog)
    dp.include_router(useful_link_dialog)
    setup_dialogs(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
