import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, setup_dialogs

from config import settings
from dialogs.main_menu import main_menu_dialog
from dialogs.start import StartStates, start_dialog

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(StartStates.greeting, mode=StartMode.RESET_STACK)


async def main() -> None:
    dp.include_router(start_dialog)
    dp.include_router(main_menu_dialog)
    setup_dialogs(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
