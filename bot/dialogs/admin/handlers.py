from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.admin.states import AdminState
from bot.services.notification.publisher import notificate_message


async def go_to_input_message(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    await dialog_manager.switch_to(AdminState.input_message)


async def on_message_input(
    message: Message,
    button: Button,
    dialog_manager: DialogManager,
    text: str,
) -> None:
    js = dialog_manager.middleware_data.get("js")
    notificate_subject = dialog_manager.middleware_data.get("notificate_subject")
    user_service = dialog_manager.middleware_data.get("user_service")

    user_ids = await user_service.get_all_user_ids()  # type: ignore

    for user_id in user_ids:
        await notificate_message(js, text, user_id, notificate_subject)  # type: ignore

    await dialog_manager.back()
