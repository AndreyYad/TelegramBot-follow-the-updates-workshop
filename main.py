from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message, InlineKeyboardMarkup

from asyncio import new_event_loop

from modules.markups import *
from modules.config import TOKEN
from modules.sql_cmds import *
from modules.bot_cmds import *
from modules.reguler import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

print('Бот запущен!')

@dp.message_handler(commands = ['start'])
async def start_func(msg: Message):
    await set_user_info(msg.chat.id)
    await set_status(msg.chat.id, 'none')
    await send_msg(msg.chat.id, 'start', await markup_start(msg.chat.id))

@dp.message_handler(commands = ['lang'])
async def start_func(msg: Message):
    await send_msg(msg.chat.id, 'lang', await markup_lang())

@dp.message_handler()
async def user_enter(msg: Message):

    match await get_status(msg.chat.id):
        case 'add_work':
            work_id = await search_id(msg.text)
            if work_id != None:
                pass
            else:
                await send_msg(msg.chat.id, 'work_not_found')

@dp.callback_query_handler()
async def callback(call):
    user_id = call.message.chat.id
    msg_id = call.message.message_id

    edit_this = lambda msgid, markup=InlineKeyboardMarkup(): edit_msg(user_id, msg_id, msgid, markup)

    match call.data:
        case 'start':
            await set_status(user_id, 'none')
            await edit_this('start', await markup_start(user_id))
        case 'add_work':
            await set_status(user_id, 'add_work')
            await edit_this('add_work_text', await markup_cancel(user_id))
        case _:
            if call.data.startswith('lang_'):
                await set_lang(user_id, call.data[-2:])
                await edit_this('lang_changed')


if __name__ == '__main__':
    loop = new_event_loop()
    loop.run_until_complete(born_of_db())
    executor.start_polling(dp)