from aiogram import Bot, Dispatcher,F
import asyncio 
from handler import start_handler
from callback_handler import vibor,keybord_handler
from aiogram.filters import Command

TOKEN = '6348032181:AAGh3nrYTBpO_03WNaNFizomgKXqlHzVJvY'

async def start():

    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.message.register(start_handler, Command(commands='start'))
    dp.callback_query.register(keybord_handler, F.data == 'Магазин')
    dp.callback_query.register(vibor)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start()) 