from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import _


async def income_menu_def():
    income_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=_("Daily"), callback_data="income_day"),
                InlineKeyboardButton(text=_("Weekly"), callback_data="income_week"),
            ],
            [
                InlineKeyboardButton(text=_("Monthly"), callback_data="income_month"),
                InlineKeyboardButton(text=_("Yearly"), callback_data="income_year"),
            ],
            [
                InlineKeyboardButton(text=_("All"), callback_data="income_all"),
                InlineKeyboardButton(text=_("Add New"), callback_data="income_add"),
            ],
        ]
    )
    return income_menu
