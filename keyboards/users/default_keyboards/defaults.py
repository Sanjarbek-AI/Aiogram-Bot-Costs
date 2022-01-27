from loader import _

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def user_menu_def():
    user_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Income 💸")),
                KeyboardButton(text=_("Expense 💶"))
            ],
            [
                KeyboardButton(text=_("Get Income 💸")),
                KeyboardButton(text=_("Get Expense 💶"))
            ],
            [
                KeyboardButton(text=_("Suggestion 🤓")),
                KeyboardButton(text=_("Profile 👤"))
            ]
        ],
        resize_keyboard=True
    )
    return user_menu


async def cancel_def():
    cancel_key = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Cancel ❌"))
            ]
        ],
        resize_keyboard=True
    )
    return cancel_key

