from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from dialogs.feedback_menu.states import FeedbackStates
from dialogs.platform_search.handlers import go_to_main_menu

dialog = Dialog(
    Window(
        Const("""К сожалению, обратная связь сейчас не работает(
Я не смогу тебе помочь с твоим вопрос. Попробуй позже"""),
        Button(text=Const("❌ Назад"), id="back_button", on_click=go_to_main_menu),
        state=FeedbackStates.not_working_feedback,
    )
)
