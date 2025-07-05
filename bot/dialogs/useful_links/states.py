from aiogram.fsm.state import State, StatesGroup


class UserfulLinksStates(StatesGroup):
    select_link = State()
