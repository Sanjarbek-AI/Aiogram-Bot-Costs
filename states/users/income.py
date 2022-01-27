from aiogram.dispatcher.filters.state import StatesGroup, State


class GetIncome(StatesGroup):
    source = State()
    amount = State()