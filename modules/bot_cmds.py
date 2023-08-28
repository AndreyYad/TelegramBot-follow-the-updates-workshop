'''Отправка сообщений'''

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup

from modules.config import TOKEN
from modules.localisation import _
from modules.found_arg import argument_parsing_obj

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

def get_text(func):
    '''
    Обёртка для получения текста(с возможностью форматирования)
    '''
    async def wrapper(*args, **kwargs):
        args_par = lambda arg: argument_parsing_obj(func, args, kwargs).argument_parsing_name(arg)
        format_data = kwargs.get('format')
        text = await _(await args_par('user_id'), await args_par('msgid'))
        if format_data != None:
            text = text.format(*format_data)
        await func(*args, **kwargs, text=text)
    return wrapper

@bot_setup
@get_text
async def send_msg(user_id, msgid, markup=InlineKeyboardMarkup(), format=None, **kwargs):
    await kwargs['dp'].bot.send_message(user_id, kwargs['text'], reply_markup=markup, parse_mode='html')

@bot_setup
@get_text
async def edit_msg(user_id, msg_id, msgid, markup=InlineKeyboardMarkup(), format=None, **kwargs):
    await kwargs['dp'].bot.edit_message_text(kwargs['text'], user_id, msg_id, reply_markup=markup, parse_mode='html')