from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.users.default_keyboards.defaults import *
from loader import dp, _


@dp.callback_query_handler(text="back_main_menu")
async def cancel(call: types.CallbackQuery, state: FSMContext):
    text = _("Main menu.")
    await call.message.answer(text, reply_markup=await user_menu_def())
    await state.finish()
