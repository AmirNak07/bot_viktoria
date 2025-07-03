from typing import Any

from aiogram_dialog import DialogManager

from dialogs.feedback_menu.states import FeedbackStates
from dialogs.platform_search.states import PlatformSearchStates
from dialogs.useful_links.states import UserfulLinksStates


async def go_to_select_platforms(
    event: Any, handler: Any, dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(PlatformSearchStates.select_platform)


async def go_to_useful_links(
    event: Any, handler: Any, dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(UserfulLinksStates.select_link)


async def go_to_feedback(
    event: Any, handler: Any, dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(FeedbackStates.not_working_feedback)
