from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


async def back_main_menu_def():
    back_main_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=_("Back"), callback_data="back_main_menu")
            ]
        ]
    )
    return back_main_menu
