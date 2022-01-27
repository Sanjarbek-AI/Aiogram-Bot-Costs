from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import _


async def expense_menu_def():
    expense_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=_("Daily"), callback_data="expense_day"),
                InlineKeyboardButton(text=_("Weekly"), callback_data="expense_week"),
            ],
            [
                InlineKeyboardButton(text=_("Monthly"), callback_data="expense_month"),
                InlineKeyboardButton(text=_("Yearly"), callback_data="expense_year"),
            ],
            [
                InlineKeyboardButton(text=_("All"), callback_data="expense_all"),
                InlineKeyboardButton(text=_("Add New"), callback_data="expense_add"),
            ],
        ]
    )
    return expense_menu
