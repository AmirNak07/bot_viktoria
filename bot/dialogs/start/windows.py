from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from bot.dialogs.start.handlers import go_to_main_menu
from bot.dialogs.start.states import StartStates

greeting_window = Window(
    Const("""Ещё раз привет! 👋
Давай подробнее расскажу, с чем я могу тебе помочь:

- найти все актуальные проекты с платформ "Росмолодежь", "Россия - страна возможностей", "VK Education" и других
- найти любые проекты благодаря удобной сортировке по категориям и направлениям

Я прошла очень длинный путь активиста. который хочет успеть всё. И я знаю, как это тяжело, когда крутых проектов очень много, а времени и сил на их поиски и систематизацию нет. И я здесь, чтобы сделать этот процесс проще

Теперь тебе не надо выписывать дедлайны подачи заявок на листочек, не надо искать подходящий проект по telegram-каналам. Теперь у тебя есть я 💔"""),
    Button(
        text=Const("Выбирай, с чего начнем 👇"),
        id="go_btn",
        on_click=go_to_main_menu,
    ),
    state=StartStates.greeting,
)

start_dialog = Dialog(greeting_window)
