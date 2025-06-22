from aiogram.fsm.state import State, StatesGroup
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const


class MainMenuStates(StatesGroup):
    main = State()


main_menu_dialog = Dialog(
    Window(
        Const("Выбирай, с чего начнём:"),
        Button(Const("Поиск по платформам 🔍"), id="search_platforms"),
        Button(Const("Полезные ссылки 💻"), id="useful_links"),
        Button(Const("Обратная связь 📧"), id="feedback"),
        state=MainMenuStates.main,
    )
)
