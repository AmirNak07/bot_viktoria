from aiogram.fsm.state import State, StatesGroup


class StartStates(StatesGroup):
    greeting = State()
