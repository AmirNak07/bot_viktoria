from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.platform_search.states import PlatformSearchStates


async def on_prev_click(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    current_index = dialog_manager.dialog_data.get("current_index", 0)
    if current_index > 0:
        dialog_manager.dialog_data["current_index"] = current_index - 1
        await dialog_manager.show()


async def on_next_click(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    current_index = dialog_manager.dialog_data.get("current_index", 0)
    if current_index < dialog_manager.dialog_data["events_count"] - 1:
        dialog_manager.dialog_data["current_index"] = current_index + 1
        await dialog_manager.show()


async def go_to_main_menu(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
    **kwargs: dict[str, Any],
) -> None:
    await dialog_manager.done()


async def go_to_platform_select(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
    **kwargs: dict[str, Any],
) -> None:
    await dialog_manager.back()
    dialog_manager.dialog_data["current_index"] = 0


async def on_platform_selected(
    callback: CallbackQuery,
    widget: Button,
    dialog_manager: DialogManager,
    selected_id: str,
) -> None:
    platforms = dialog_manager.dialog_data["platforms"]
    selected_platform = next(p for p in platforms if p["id"] == int(selected_id))

    dialog_manager.dialog_data["current_platform"] = selected_platform
    await dialog_manager.switch_to(PlatformSearchStates.show_events)
