from main.database import database
from main.models import *
import logging


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
            created_at=message.date,
            updated_at=message.date
        )
        await database.execute(query=query)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False
