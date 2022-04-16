from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.users.default_keyboards.defaults import cancel_def, user_menu_def, main_menu_def
from keyboards.users.inline_keyboards.profile import *
from loader import dp, _, bot
from states.users.common import Profile
from utils.db_commands import *


async def return_profile_text(user):
    text = f"""
{_("First Name")}: {user["first_name"]}
{_("Last Name")}: {user["last_name"]}
{_("Phone Number")}: {user["phone_number"]}
{_("Country")}: {user["country"]}
{_("City")}: {user["city"]}
{_("District")}: {user["district"]}
{_("Village")}: {user["village"]} \n
{_("Language")}: {user["language"]}
{_("Income Notification")}: {_("On") if user["income_notif"] == "on" else _("Off")}
{_("Expense Notification")}: {_("On") if user["expense_notif"] == "on" else _("Off")}
"""
    return text


@dp.message_handler(text=["Profile 👤", "Профиль 👤", "Profil 👤"])
async def income(message: types.Message):
    user = await get_user(message.from_user.id)
    text = await return_profile_text(user)
    await message.answer(text, reply_markup=await profile_menu_def(user["income_notif"], user["expense_notif"]))


@dp.callback_query_handler(text="change_first")
async def profile_change(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    text = _("Please, enter your first name.")
    await call.message.answer(text, reply_markup=await cancel_def())
    await Profile.first_name.set()


@dp.message_handler(state=Profile.first_name)
async def profile_change(message: types.Message, state: FSMContext):
    text = _("First name updated.")
    await message.answer(text, reply_markup=await user_menu_def())
    await update_first_name(message)
    await state.finish()
    user = await get_user(message.from_user.id)
    profile_text = await return_profile_text(user)
    await message.answer(profile_text, reply_markup=await profile_menu_def(user["income_notif"], user["expense_notif"]))


@dp.callback_query_handler(text="change_last")
async def profile_change(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    text = _("Please, enter your last name.")
    await call.message.answer(text, reply_markup=await cancel_def())
    await Profile.last_name.set()


@dp.message_handler(state=Profile.last_name)
async def profile_change(message: types.Message, state: FSMContext):
    text = _("Last name updated.")
    await message.answer(text, reply_markup=await user_menu_def())
    await update_last_name(message)
    await state.finish()
    user = await get_user(message.from_user.id)
    profile_text = await return_profile_text(user)
    await message.answer(profile_text, reply_markup=await profile_menu_def(user["income_notif"], user["expense_notif"]))


@dp.callback_query_handler(text="change_phone")
async def profile_change(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    text = _("Please, enter your number. Example: 99 001 58 51")
    await call.message.answer(text, reply_markup=await cancel_def())
    await Profile.phone_number.set()


@dp.message_handler(state=Profile.phone_number)
async def profile_change(message: types.Message, state: FSMContext):
    text = _("Phone number updated.")
    await message.answer(text, reply_markup=await user_menu_def())
    await update_phone_number(message)
    await state.finish()
    user = await get_user(message.from_user.id)
    profile_text = await return_profile_text(user)
    await message.answer(profile_text, reply_markup=await profile_menu_def(user["income_notif"], user["expense_notif"]))


@dp.callback_query_handler(text="change_country")
async def profile_change(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    text = _("Please, enter country.")
    await call.message.answer(text, reply_markup=await cancel_def())
    await Profile.country.set()


@dp.message_handler(state=Profile.country)
async def profile_change(message: types.Message, state: FSMContext):
    text = _("Country updated.")
    await message.answer(text, reply_markup=await user_menu_def())
    await update_country(message)
    await state.finish()
    user = await get_user(message.from_user.id)
    profile_text = await return_profile_text(user)
    await message.answer(profile_text, reply_markup=await profile_menu_def(user["income_notif"], user["expense_notif"]))


@dp.callback_query_handler(text="change_city")
async def profile_change(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    text = _("Please, enter your city name.")
    await call.message.answer(text, reply_markup=await cancel_def())
    await Profile.city.set()


@dp.message_handler(state=Profile.city)
async def profile_change(message: types.Message, state: FSMContext):
    text = _("City name updated.")
    await message.answer(text, reply_markup=await user_menu_def())
    await update_city(message)
    await state.finish()
    user = await get_user(message.from_user.id)
    profile_text = await return_profile_text(user)
    await message.answer(profile_text, reply_markup=await profile_menu_def(user["income_notif"], user["expense_notif"]))


@dp.callback_query_handler(text="change_district")
async def profile_change(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    text = _("Please, enter your district name.")
    await call.message.answer(text, reply_markup=await cancel_def())
    await Profile.district.set()


@dp.message_handler(state=Profile.district)
async def profile_change(message: types.Message, state: FSMContext):
    text = _("District name updated.")
    await message.answer(text, reply_markup=await user_menu_def())
    await update_district(message)
    await state.finish()
    user = await get_user(message.from_user.id)
    profile_text = await return_profile_text(user)
    await message.answer(profile_text, reply_markup=await profile_menu_def(user["income_notif"], user["expense_notif"]))


@dp.callback_query_handler(text="change_village")
async def profile_change(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    text = _("Please, enter your village name.")
    await call.message.answer(text, reply_markup=await cancel_def())
    await Profile.village.set()


@dp.message_handler(state=Profile.village)
async def profile_change(message: types.Message, state: FSMContext):
    text = _("Village name updated.")
    await message.answer(text, reply_markup=await user_menu_def())
    await update_village(message)
    await state.finish()
    user = await get_user(message.from_user.id)
    profile_text = await return_profile_text(user)
    await message.answer(profile_text, reply_markup=await profile_menu_def(user["income_notif"], user["expense_notif"]))


@dp.callback_query_handler(text="change_language")
async def profile_change(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    text = _("Please, select new language.")
    await call.message.answer(text, reply_markup=await languages_def())
    await Profile.language.set()


@dp.callback_query_handler(state=Profile.language)
async def profile_change(call: types.CallbackQuery, state: FSMContext):
    await update_language(call.message, call.data, call.from_user.id)
    text = _("Language updated.")
    await call.message.answer(text, reply_markup=await main_menu_def())
    await state.finish()
    user = await get_user(call.message.from_user.id)
    profile_text = await return_profile_text(user)
    await call.message.answer(profile_text,
                              reply_markup=await profile_menu_def(user["income_notif"], user["expense_notif"]))


@dp.callback_query_handler(text="change_income_notif")
async def change_income_notification(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await update_income_notification(call.message, call.from_user.id)

    user = await get_user(call.from_user.id)
    if user:
        profile_text = await return_profile_text(user)
        await call.message.answer(profile_text,
                                  reply_markup=await profile_menu_def(user["income_notif"], user["expense_notif"]))


@dp.callback_query_handler(text="change_expense_notif")
async def change_income_notification(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await update_expense_notification(call.message, call.from_user.id)

    user = await get_user(call.from_user.id)
    if user:
        profile_text = await return_profile_text(user)
        await call.message.answer(profile_text,
                                  reply_markup=await profile_menu_def(user["income_notif"], user["expense_notif"]))
