from aiogram import executor

import middlewares
import filters
import handlers

from loader import dp
from utils.notify_admins import notify_admins
from utils.default_commands import set_default_commands
from main.database import database


async def on_startup(dispatcher):
    await database.connect()

    await set_default_commands(dispatcher)
    await notify_admins(dispatcher)


async def on_shutdown(dispatcher):
    await database.disconnect()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)


