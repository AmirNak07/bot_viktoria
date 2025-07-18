from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Column, Row, Select
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.platform_search.getters import get_platform_info, get_platforms
from bot.dialogs.platform_search.handlers import (
    go_to_main_menu,
    go_to_platform_select,
    on_next_click,
    on_platform_selected,
    on_prev_click,
)
from bot.dialogs.platform_search.states import PlatformSearchStates
from bot.dialogs.platform_search.utils.for_text import DynamicFormat

choose_platform_window = Window(
    Const("Выбери платформу:"),
    Column(
        Select(
            text=Format("{item[name]}"),
            id="platform_select",
            item_id_getter=lambda item: str(item["id"]),
            items="platforms",
            on_click=on_platform_selected,  # type: ignore
        ),
        Button(text=Const("⬅️ Назад"), id="back_button", on_click=go_to_main_menu),
    ),
    state=PlatformSearchStates.select_platform,
    getter=get_platforms,
)

platform_info_window = Window(
    Format("Проект: {platform_name}"),
    DynamicFormat(
        "{event_text}", fallback="Нет информации о мероприятии в данный момент"
    ),
    Row(
        Button(
            Const("⬅️ Предыдущий"),
            id="prev",
            on_click=on_prev_click,
            when="has_prev",
        ),
        Button(
            Const("➡️ Следующий"),
            id="next",
            on_click=on_next_click,
            when="has_next",
        ),
    ),
    Button(
        Format("{current_event_index}/{max_event_index}"),
        id="counter",
        on_click=None,
        when="has_events",
    ),
    Button(text=Const("❌ Назад"), id="back_button", on_click=go_to_platform_select),
    state=PlatformSearchStates.show_events,
    getter=get_platform_info,
)


platform_search_dialog = Dialog(choose_platform_window, platform_info_window)
