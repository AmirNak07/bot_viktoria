from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, Column, Select
from aiogram_dialog.widgets.text import Const, Format

PLATFORMS = {
    "VK": [
        {
            "Название": "Разработчик C++",
            "Направление": "Другое дело",
            "Город": "Москва",
        },
        {"Название": "Web-разработчик", "Направление": "СМБ", "Город": "Москва"},
    ],
    "Россия - страна возможностей": [
        {
            "Название": "Стажер PR-менеджер",
            "Направление": "Государственная служба, некоммерческие организации",
            "Компания": "Ассоциация Добро.рф",
        },
        {
            "Название": "Стажер-аналитик данных",
            "Направление": "Государственная служба, некоммерческие организации",
            "Компания": "Ассоциация Добро.рф",
        },
    ],
    "Росмолодёжь": [],
}


class PlatformSearchStates(StatesGroup):
    select_platform = State()
    show_events = State()


async def get_platforms(dialog_manager: DialogManager, **kwargs):
    platforms = []
    platforms_names = list(PLATFORMS.keys())
    for i, platform in enumerate(platforms_names):
        platforms.append({"id": i, "name": platform})
    return {"platforms": platforms}


async def go_to_main_menu(
    callback: CallbackQuery, widget, dialog_manager: DialogManager, **kwargs
):
    await dialog_manager.done()


async def on_platform_selected(
    callback: CallbackQuery, widget, dialog_manager: DialogManager, selected_id: str
):
    print(f"Выбрана платформа: {selected_id}")
    await dialog_manager.switch_to(PlatformSearchStates.select_platform)


platform_search_dialog = Dialog(
    Window(
        Const("Выбери платформу:"),
        Column(
            Select(
                text=Format("{item[name]}"),
                id="platform_select",
                item_id_getter=lambda item: str(item["id"]),
                items="platforms",
                on_click=on_platform_selected,
            ),
            Button(text=Const("⬅️ Назад"), id="back_button", on_click=go_to_main_menu),
        ),
        state=PlatformSearchStates.select_platform,
        getter=get_platforms,
    ),
)
