'''Отправка сообщений'''

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup

from inspect import signature, isfunction

from modules.config import TOKEN
from modules.localisation import _

def bot_setup(func):
    '''
    Обёртка с подключением и отключением сесии бота
    '''
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
    await dp.bot.send_message(user_id, text, reply_markup=markup, parse_mode='html')

@bot_setup
async def edit_msg(user_id, msg_id, msgid, markup=InlineKeyboardMarkup(), dp=None):
    text = await _(user_id, msgid)
    await dp.bot.edit_message_text(text, user_id, msg_id, reply_markup=markup, parse_mode='html')