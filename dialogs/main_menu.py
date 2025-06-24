from aiogram.fsm.state import State, StatesGroup
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from dialogs.platform_search import PlatformSearchStates


class MainMenuStates(StatesGroup):
    main = State()


async def go_to_select_platforms(event, handler, dialog_manager: DialogManager):
    await dialog_manager.start(PlatformSearchStates.select_platform)


main_menu_dialog = Dialog(
    Window(
        Const("Выбирай, с чего начнём:"),
        Button(
            Const("Поиск по платформам 🔍"),
            id="search_platforms",
            on_click=go_to_select_platforms,
        ),
        Button(Const("Полезные ссылки 💻"), id="useful_links"),
        Button(Const("Обратная связь 📧"), id="feedback"),
        state=MainMenuStates.main,
    )
)
