from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.users.default_keyboards.defaults import *
from loader import dp, _
from states.users.common import Suggestion
from utils.db_commands import insert_suggestion


@dp.callback_query_handler(text="back_main_menu")
async def cancel(call: types.CallbackQuery, state: FSMContext):
    text = _("Main menu.")
    await call.message.answer(text, reply_markup=await user_menu_def())
    await state.finish()


@dp.message_handler(text=["Cancel ❌", "Bekor qilish ❌", "Отменить ❌"], state="*")
async def cancel(message: types.Message, state: FSMContext):
    text = _("Main menu.")
    await message.answer(text, reply_markup=await user_menu_def())
    await state.finish()


@dp.message_handler(text=["Suggestion 🤓", "Taklif 🤓", "Предложение 🤓"], state="*")
async def cancel(message: types.Message, state: FSMContext):
    text = _("Qanday taklif bildirmoqchisiz.")
    await message.answer(text, reply_markup=await cancel_def())
    await Suggestion.text.set()


@dp.message_handler(state=Suggestion.text)
async def cancel(message: types.Message, state: FSMContext):
    text = _("Taklifingiz uchun raxmat.")
    await message.answer(text, reply_markup=await user_menu_def())
    await insert_suggestion(message)
    await state.finish()


@dp.message_handler(text=["Main menu ⏹", "Asosiy menyu ⏹", "Главное меню ⏹"], state="*")
async def cancel(message: types.Message, state: FSMContext):
    text = _("Main menu.")
    await message.answer(text, reply_markup=await user_menu_def())
    await state.finish()
