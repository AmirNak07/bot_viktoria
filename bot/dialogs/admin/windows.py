from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Back, Button, Column
from aiogram_dialog.widgets.text import Const

from bot.dialogs.admin.handlers import go_to_input_message, on_message_input
from bot.dialogs.admin.states import AdminState

admin_menu_window = Window(
    Const("Админ панель:"),
    Column(
        Button(
            Const("Сообщение для всех пользователей"),
            id="notify_all",
            on_click=go_to_input_message,
        )
    ),
    state=AdminState.menu,
)

notificate_window = Window(
    Const("Введите сообщение для рассылки:"),
    TextInput(
        id="message_input",
        on_success=on_message_input,  # type: ignore
    ),
    Back(Const("⬅️ Назад")),
    state=AdminState.input_message,
)

dialog = Dialog(admin_menu_window, notificate_window)
