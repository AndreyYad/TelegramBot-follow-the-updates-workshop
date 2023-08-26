'''Отправка сообщений'''

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup

from modules.config import TOKEN
from modules.localisation import _

def bot_setup(func):
    async def wrapper(*args, **kwargs):
        bot = Bot(token=TOKEN)
        dp = Dispatcher(bot)
        await func(*args, **kwargs, dp=dp)
        session = await bot.get_session()
        await session.close()
    return wrapper

@bot_setup
async def send_msg(user_id, msgid, markup=InlineKeyboardMarkup(), dp=None):
    text = await _(user_id, msgid)
    await dp.bot.send_message(user_id, text, parse_mode='html', reply_markup=markup)