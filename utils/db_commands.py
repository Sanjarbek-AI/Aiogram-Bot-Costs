import logging

from main.database import database
from main.models import *


async def get_user(telegram_id):
    try:
        query = Users.select().where(Users.c.telegram_id == telegram_id)
        user = await database.fetch_one(query=query)
        return user
    except Exception as exc:
        logging.exception(exc)
        return False


async def insert_income(message, data):
    try:
        query = Income.insert().values(
            telegram_id=message.from_user.id,
            source=data.get("source"),
            amount=data.get("amount"),
            status=IncomeStatus.active,
            created_at=message.date,
            updated_at=message.date
        )
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False


async def get_all_incomes(telegram_id):
    try:
        query = Users.select().where(Income.c.telegram_id == telegram_id)
        incomes = await database.fetch_all(query=query)
        return incomes
    except Exception as exc:
        logging.exception(exc)
        return False


async def insert_expense(message, data):
    try:
        query = Expense.insert().values(
            telegram_id=message.from_user.id,
            reason=data.get("reason"),
            price=data.get("price"),
            status=ExpenseStatus.active,
            created_at=message.date,
            updated_at=message.date
        )
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False


async def insert_user(message):
    try:
        query = Users.insert().values(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            language=message.from_user.language_code,
            status=UserStatus.active,
            income_notif=IncomeNotif.off,
            expense_notif=ExpenseNotif.on,
            created_at=message.date,
            updated_at=message.date
        )
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False


async def insert_suggestion(message):
    try:
        query = Suggestions.insert().values(
            feedback=message.text,
            status=SuggestionStatus.active,
            created_at=message.date,
            updated_at=message.date
        )
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False


async def update_first_name(message):
    try:
        query = Users.update().values(
            first_name=message.text,
            updated_at=message.date
        ).where(Users.c.telegram_id == message.from_user.id)
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False


async def update_last_name(message):
    try:
        query = Users.update().values(
            last_name=message.text,
            updated_at=message.date
        ).where(Users.c.telegram_id == message.from_user.id)
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False


async def update_phone_number(message):
    try:
        query = Users.update().values(
            phone_number=message.text,
            updated_at=message.date
        ).where(Users.c.telegram_id == message.from_user.id)
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False


async def update_country(message):
    try:
        query = Users.update().values(
            country=message.text,
            updated_at=message.date
        ).where(Users.c.telegram_id == message.from_user.id)
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False


async def update_district(message):
    try:
        query = Users.update().values(
            district=message.text,
            updated_at=message.date
        ).where(Users.c.telegram_id == message.from_user.id)
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False


async def update_village(message):
    try:
        query = Users.update().values(
            village=message.text,
            updated_at=message.date
        ).where(Users.c.telegram_id == message.from_user.id)
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False


async def update_city(message):
    try:
        query = Users.update().values(
            city=message.text,
            updated_at=message.date
        ).where(Users.c.telegram_id == message.from_user.id)
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False


async def update_language(message, lang, user_id):
    try:
        query = Users.update().values(
            language=lang,
            updated_at=message.date
        ).where(Users.c.telegram_id == user_id)
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False


async def update_income_notification(message, user_id):
    try:
        user = await get_user(user_id)
        if user["income_notif"] == IncomeNotif.on:
            query = Users.update().values(
                income_notif=IncomeNotif.off,
                updated_at=message.date
            ).where(Users.c.telegram_id == user_id)
        else:
            query = Users.update().values(
                income_notif=IncomeNotif.on,
                updated_at=message.date
            ).where(Users.c.telegram_id == user_id)
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False


async def update_expense_notification(message, user_id):
    try:
        user = await get_user(user_id)
        if user["expense_notif"] == ExpenseNotif.on:
            query = Users.update().values(
                expense_notif=ExpenseNotif.off,
                updated_at=message.date
            ).where(Users.c.telegram_id == user_id)
        else:
            query = Users.update().values(
                expense_notif=ExpenseNotif.on,
                updated_at=message.date
            ).where(Users.c.telegram_id == user_id)
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False
