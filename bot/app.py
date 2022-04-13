from aiogram import executor

from config import admin_id
from database import create_db
from load_all import bot


async def on_startup(dp):
    await create_db()
    await bot.send_message(admin_id, 'Я запущений!')


if __name__ == '__main__':
    # from admin_panel import dp
    from hendlers import dp
    from inline_hendlers import dp
    executor.start_polling(dp, on_startup=on_startup)
