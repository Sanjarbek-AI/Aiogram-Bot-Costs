from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.users.default_keyboards.defaults import *
from keyboards.users.inline_keyboards.income import *
from loader import dp, _
from states.users.income import *
from utils.db_commands import *


@dp.message_handler(text=["Income 💸", "Доход 💸", "Kirim 💸"])
async def income(message: types.Message):
    text = _("Please, enter source of money which you want to enter.")
    await message.answer(text, reply_markup=await cancel_def())
    await GetIncome.source.set()


@dp.message_handler(state=GetIncome.source)
async def get_income_source(message: types.Message, state: FSMContext):
    await state.update_data({
        "source": message.text
    })

    text = _("Please, enter amount of money. (Sum)")
    await message.answer(text)
    await GetIncome.amount.set()


@dp.message_handler(state=GetIncome.amount)
async def get_amount_of_income(message: types.Message, state: FSMContext):
    await state.update_data({
        "amount": float(message.text)
    })
    data = await state.get_data()
    new_income = await insert_income(message, data)

    if new_income:
        text = _("Added to your income list.")
        await state.finish()
    else:
        text = _("Not added, please try again.")
        await state.finish()

    await message.answer(text, reply_markup=await user_menu_def())


@dp.message_handler(text=["Get Income 💸", "Получай доход 💸", "Kirimlar 💸"])
async def income(message: types.Message):
    text = _("How long do you want to see the income.")
    await message.answer(text, reply_markup=await income_menu_def())
