from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from dialogs.main_menu.handlers import go_to_select_platforms
from dialogs.main_menu.states import MainMenuStates

main_menu_window = Window(
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

main_menu_dialog = Dialog(main_menu_window)
