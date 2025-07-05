from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from dialogs.useful_links.getter import get_links_data


async def on_prev_click(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    current_index = dialog_manager.dialog_data.get("current_link_index", 0)
    if current_index > 0:
        dialog_manager.dialog_data["current_link_index"] = current_index - 1
        await dialog_manager.show()


async def on_next_click(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    current_index = dialog_manager.dialog_data.get("current_link_index", 0)
    events_info = await get_links_data(dialog_manager=dialog_manager)
    if current_index < len(events_info) - 1:
        dialog_manager.dialog_data["current_link_index"] = current_index + 1
        await dialog_manager.show()
