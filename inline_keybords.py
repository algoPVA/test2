from aiogram.utils.keyboard import InlineKeyboardBuilder
from random import choice
from aiogram.utils.keyboard import InlineKeyboardBuilder
from store import store
                      



znachkis = ['💎' , '🗿', '💵', '🎰', '🥚', '☠️', '💤']
# znachkis = ['💎' , '🗿']
targets = []
for znack in znachkis:
    targets.append(znack*3)

def get_inline_keybords():
    kb = InlineKeyboardBuilder()
    callback_data = choice(znachkis) + choice(znachkis) + choice(znachkis)

    if callback_data in targets:
        store.change_score(1)
    kb.button(text='Игровой автомат 🎰',callback_data=callback_data)
    kb.button(text='Магагзин🏦', callback_data= 'Магазин')
    return kb.as_markup()

def get_inline_keybords1():
    kb = InlineKeyboardBuilder()
    score = store.get_score()
    if score > 0:
        callback_data = 'Поздравляю!'
        store.change_score(-1)

    #     callback_data = 'Поздравляю! Теперь вы можете расслабиться'
    # что-то не так со строкой выше...скорее всего какие-то старнные символы

    else:
        callback_data = 'У вас не хватает денег :('
    kb.button(text='Расслабляющий напиток🧉 - стоит 1₽', callback_data=callback_data)
    return kb.as_markup()

