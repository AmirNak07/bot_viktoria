from typing import Any

from aiogram_dialog import DialogManager, StartMode

from dialogs.main_menu.states import MainMenuStates


async def go_to_main_menu(event: Any, handler: Any, manager: DialogManager) -> None:
    await manager.start(MainMenuStates.main, mode=StartMode.NEW_STACK)
