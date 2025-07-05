from typing import Any

from aiogram_dialog import DialogManager

from dialogs.useful_links.mkpatch import get_links


async def get_links_data(
    dialog_manager: DialogManager, **kwargs: dict[Any, Any]
) -> dict[str, str | bool]:
    link_index = dialog_manager.dialog_data.get("current_link_index", 0)
    links = await get_links()
    current_link = links[link_index]
    return {
        "platform_name": current_link["Название"],
        "platform_description": current_link["Описание"],
        "platform_link": current_link["Перейти"],
        "has_prev": link_index > 0,
        "has_next": link_index < len(links) - 1,
    }
