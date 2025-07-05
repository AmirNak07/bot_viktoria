from aiogram.fsm.state import State, StatesGroup


class FeedbackStates(StatesGroup):
    not_working_feedback = State()
