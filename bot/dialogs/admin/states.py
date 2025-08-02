from aiogram.fsm.state import State, StatesGroup


class AdminState(StatesGroup):
    menu = State()
    input_message = State()
