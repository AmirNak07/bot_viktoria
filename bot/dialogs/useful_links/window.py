from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.platform_search.handlers import go_to_main_menu
from bot.dialogs.useful_links.getter import get_links_data
from bot.dialogs.useful_links.handlers import on_next_click, on_prev_click
from bot.dialogs.useful_links.states import UserfulLinksStates

dialog = Dialog(
    Window(
        Format("{platform_name}"),
        Format("Описание: {platform_description}"),
        Format("Перейти: {platform_link}"),
        Row(
            Button(
                Const("⬅️ Назад"),
                id="prev",
                on_click=on_prev_click,
                when="has_prev",
            ),
            Button(text=Const("❌ Назад"), id="back_button", on_click=go_to_main_menu),
            Button(
                Const("➡️ Вперед"),
                id="next",
                on_click=on_next_click,
                when="has_next",
            ),
        ),
        state=UserfulLinksStates.select_link,
    ),
    getter=get_links_data,
)
