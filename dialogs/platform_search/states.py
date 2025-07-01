from aiogram.fsm.state import State, StatesGroup


class PlatformSearchStates(StatesGroup):
    select_platform = State()
    show_events = State()
