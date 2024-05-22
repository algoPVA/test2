from aiogram import Bot
from aiogram.types import CallbackQuery
from inline_keybords import get_inline_keybords, get_inline_keybords1
# from inline_keybords import koshelok
from store import store


async def vibor(call: CallbackQuery, bot: Bot):
    score = store.get_score()
    await call.message.answer(text=f'{call.data} - ваш кошелёк-{score}₽', reply_markup=get_inline_keybords())
    await call.answer()

async def keybord_handler(call: CallbackQuery, bot: Bot):
    await call.message.answer("Салам! Я бот, где ты можешь получить зависимость к крутке слотов! Начинаем?",reply_markup=get_inline_keybords1()) 
    await call.answer()

                           
