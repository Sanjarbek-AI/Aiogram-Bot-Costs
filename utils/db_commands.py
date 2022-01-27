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

