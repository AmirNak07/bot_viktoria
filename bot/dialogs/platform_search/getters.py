from typing import Any

from aiogram_dialog import DialogManager

from bot.dialogs.platform_search.mkpatch import get_plarforms_info, get_platforms_name
from bot.dialogs.platform_search.utils.for_text import generate_event_text


async def get_platforms(
    dialog_manager: DialogManager, **kwargs: dict[Any, Any]
) -> dict[str, list[dict[str, Any]]]:
    platform_names = await get_platforms_name()
    platforms = []
    for i, platform in enumerate(platform_names):
        platforms.append({"id": i, "name": platform})
    return {"platforms": platforms}


async def get_platform_info(
    dialog_manager: DialogManager, **kwargs: dict[Any, Any]
) -> dict[str, Any]:
    platform_name = dialog_manager.dialog_data["current_platform"]["name"]
    events = await get_plarforms_info(platform_name)

    current_index = dialog_manager.dialog_data.get("current_index", 0)

    if not events:
        return {
            "platform_name": platform_name,
            "has_events": False,
            "has_prev": False,
            "has_next": False,
        }

    return {
        "platform_name": platform_name,
        "current_event_index": current_index + 1,
        "max_event_index": len(events),
        "current_event": events[current_index],
        "event_text": generate_event_text(events[current_index]),
        "has_events": True,
        "has_prev": current_index > 0,
        "has_next": current_index < len(events) - 1,
    }
