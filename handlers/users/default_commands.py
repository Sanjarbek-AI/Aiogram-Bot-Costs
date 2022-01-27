from aiogram import types

from loader import dp, _
from keyboards.users.default_keyboards.defaults import *
from utils.db_commands import *


@dp.message_handler(commands=["start"])
async def user_start(message: types.Message):
    user = await get_user(message.from_user.id)
    if user:
        text = _("Welcome !!!")
        await message.answer(text, reply_markup=await user_menu_def())
    else:
        new_user = await insert_user(message)

        if new_user:
            text = _(
                "Welcome to our service bot ! \n\n This bot can help to you to calculating all your incomes and"
                "expenses day by day. If you want to take more information, /help",
                locale=message.from_user.language_code)
        else:
            text = _("Try again later, Please")

        await message.answer(text, reply_markup=await user_menu_def())


@dp.message_handler(commands=["help"])
async def user_help(message: types.Message):
    text = _("""My service 🤖 \n 
1. Taking incomes and giving them as a list. \n
2. Giving incomes daily, weekly, monthly and yearly. \n
3. Taking expenses and giving them as a list. \n
4. Giving expenses daily, weekly, monthly and yearly. \n
5. Giving changes in your costs. \n
6. Giving statistics what you  spend more. \n
7. Planning your costs and giving notification about it. \n\n
And giving you more great mood. Smile 😁 \n""")

    await message.answer(text, reply_markup=await user_menu_def())
