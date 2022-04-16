from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.users.default_keyboards.defaults import *
from keyboards.users.inline_keyboards.expense import *
from loader import dp, _
from states.users.expense import GetExpense
from utils.db_commands import *


@dp.message_handler(text=["Expense 💶", "Расход 💶", "Chiqim 💶"])
async def income(message: types.Message):
    text = _("Please, enter what you spent money.")
    await message.answer(text, reply_markup=await cancel_def())
    await GetExpense.reason.set()


@dp.message_handler(state=GetExpense.reason)
async def get_expense_reason(message: types.Message, state: FSMContext):
    await state.update_data({
        "reason": message.text
    })

    text = _("Please, enter price of it. (Sum)")
    await message.answer(text)
    await GetExpense.price.set()


@dp.message_handler(state=GetExpense.price)
async def get_amount_of_income(message: types.Message, state: FSMContext):
    await state.update_data({
        "price": float(message.text)
    })
    data = await state.get_data()
    new_expense = await insert_expense(message, data)

    if new_expense:
        text = _("Added to your expense list.")
        await state.finish()
    else:
        text = _("Not added, please enter valid value.")
        await GetExpense.price.set()

    await message.answer(text, reply_markup=await user_menu_def())


@dp.message_handler(text=["Get Expense 💶", "Получите расход 💶", "Chiqimlar 💶"])
async def income(message: types.Message):
    text = _("How long do you want to see the expenses.")
    await message.answer(text, reply_markup=await expense_menu_def())
