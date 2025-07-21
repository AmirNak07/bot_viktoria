from bot.dialogs.feedback_menu.window import dialog as feedback_dialog
from bot.dialogs.main_menu.windows import dialog as main_menu_dialog
from bot.dialogs.platform_search.windows import dialog as platform_search_dialog
from bot.dialogs.start.windows import dialog as start_dialog
from bot.dialogs.useful_links.window import dialog as useful_links_dialog

__all__ = [
    "feedback_dialog",
    "main_menu_dialog",
    "platform_search_dialog",
    "start_dialog",
    "useful_links_dialog",
]

dialogs = [
    start_dialog,
    main_menu_dialog,
    platform_search_dialog,
    useful_links_dialog,
    feedback_dialog,
]
