from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message

from asyncio import new_event_loop

from modules.markups import *
from modules.config import TOKEN
from modules.sql_cmds import *
from modules.send_msg import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

print('Бот запущен!')

@dp.message_handler(commands = ['start'])
async def start_func(msg: Message):
    await set_user_info(msg.chat.id)

@dp.message_handler(commands = ['lang'])
async def start_func(msg: Message):
    await send_msg(msg.chat.id, 'lang', await markup_lang())

@dp.callback_query_handler()
async def callback(call):

    user_id = call.message.chat.id

    match call.data:
        case _:
            if call.data.startswith('lang_'):
                await set_lang(user_id, call.data[-2:])


if __name__ == '__main__':
    loop = new_event_loop()
    loop.run_until_complete(born_of_db())
    executor.start_polling(dp)