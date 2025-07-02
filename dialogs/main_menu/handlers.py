from typing import Any

from aiogram_dialog import DialogManager

from dialogs.platform_search.states import PlatformSearchStates


async def go_to_select_platforms(
    event: Any, handler: Any, dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(PlatformSearchStates.select_platform)
