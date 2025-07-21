from collections.abc import Sequence
from typing import Any

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.text import Format


class DynamicFormat(Format):
    def __init__(
        self,
        text_template: str,
        fallback: str = "Не указано",
        when: WhenCondition = None,
    ):
        super().__init__(text=text_template, when=when)
        self.fallback = fallback

    async def _render_text(self, data: dict[str, Any], manager: DialogManager) -> str:
        try:
            return await super()._render_text(data, manager)
        except (KeyError, TypeError):
            return self.fallback


def generate_event_text(event: dict[str, Any]) -> str:
    lines = []
    del event["Платформа"]
    lines.append(f"📌 {event.pop('Название')}")
    for key, value in event.items():
        if value:
            if isinstance(value, str):
                lines.append(f"<b>{key}</b>: {value}")
            elif isinstance(value, Sequence):
                lines.append(f"<b>{key}</b>: \n- {'\n- '.join(value)}")
        else:
            lines.append(f"{key}: 'Нет информации'")
    return "\n".join(lines) if lines else "Нет информации о мероприятии"
