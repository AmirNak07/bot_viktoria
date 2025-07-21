from typing import Any

from aiogram_dialog import DialogManager

from bot.dialogs.platform_search.utils.for_text import generate_event_text
from bot.services.event_service import EventService


async def get_platforms(
    dialog_manager: DialogManager, service: EventService, **kwargs: dict[Any, Any]
) -> dict[str, list[dict[str, Any]] | bool]:
    platform_names = await service.get_creators()
    platforms = []
    if len(platform_names) != 0:
        for i, platform in enumerate(platform_names):
            platforms.append({"id": i, "name": platform})
        dialog_manager.dialog_data["platforms"] = platforms
        return {"platforms": platforms, "has_platforms": True}
    return {"platorms": platforms, "has_platforms": False, "dont_has_platforms": True}


async def get_platform_info(
    dialog_manager: DialogManager, service: EventService, **kwargs: dict[Any, Any]
) -> dict[str, Any]:
    platform_name = dialog_manager.dialog_data["current_platform"]["name"]
    events = await service.get_by_creator(platform_name)

    current_index = dialog_manager.dialog_data.get("current_index", 0)

    if not events:
        return {
            "has_events": False,
            "has_prev": False,
            "has_next": False,
        }

    dialog_manager.dialog_data["events_count"] = len(events)
    return {
        "current_event_index": current_index + 1,
        "max_event_index": len(events),
        "current_event": events[current_index],
        "event_text": generate_event_text(events[current_index]),
        "has_events": True,
        "has_prev": current_index > 0,
        "has_next": current_index < len(events) - 1,
    }
