import logging
from aiogram import Dispatcher

from main import config


async def notify_admins(dp: Dispatcher):
    for admin in config.ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot start to work")
        except Exception as exc:
            logging.exception(exc)
            # await dp.bot.send_message(admins, str(exc))
