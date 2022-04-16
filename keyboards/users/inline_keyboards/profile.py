from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import _


async def profile_menu_def(income_notif, expense_notif):
    profile_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=_("First Name"), callback_data="change_first"),
                InlineKeyboardButton(text=_("Last Name"), callback_data="change_last"),
            ],
            [
                InlineKeyboardButton(text=_("Phone Number"), callback_data="change_phone"),
                InlineKeyboardButton(text=_("Language"), callback_data="change_language"),
            ],
            [
                InlineKeyboardButton(text=_("Country"), callback_data="change_country"),
                InlineKeyboardButton(text=_("City"), callback_data="change_city"),
            ],
            [
                InlineKeyboardButton(text=_("District"), callback_data="change_district"),
                InlineKeyboardButton(text=_("Village"), callback_data="change_village"),
            ],
            [
                InlineKeyboardButton(text=_(f"Income Notif ({income_notif})"), callback_data="change_income_notif"),
                InlineKeyboardButton(text=_(f"Expense Notif ({expense_notif})"), callback_data="change_expense_notif"),
            ],
        ]
    )
    return profile_menu


async def languages_def():
    languages = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=_("Uzbek 🇺🇿"), callback_data="uz"),
                InlineKeyboardButton(text=_("Russian 🇷🇺"), callback_data="ru"),
                InlineKeyboardButton(text=_("English 🇺🇸"), callback_data="en"),
            ]
        ]
    )
    return languages
