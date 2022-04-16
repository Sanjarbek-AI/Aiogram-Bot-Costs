from aiogram.dispatcher.filters.state import StatesGroup, State


class Suggestion(StatesGroup):
    text = State()


class Profile(StatesGroup):
    first_name = State()
    last_name = State()
    phone_number = State()
    language = State()
    country = State()
    street = State()
    district = State()
    city = State()
    village = State()
