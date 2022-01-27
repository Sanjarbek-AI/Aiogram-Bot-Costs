from aiogram.dispatcher.filters.state import StatesGroup, State


class GetExpense(StatesGroup):
    reason = State()
    price = State()