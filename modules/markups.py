'''Наборы inline-кнопок'''

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from modules.localisation import _

async def markup_lang():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton('🇷🇺', callback_data='lang_ru'),
        InlineKeyboardButton('🇬🇧', callback_data='lang_en')
    )       
    return markup

async def markup_start(user_id):
    loc = lambda msgid: _(user_id, msgid)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(await loc('list_works'), callback_data='list_works'))
    markup.add(InlineKeyboardButton(await loc('add_work'), callback_data='add_work'))
    return markup

async def markup_cancel(user_id):
    loc = lambda msgid: _(user_id, msgid)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(await loc('cancel'), callback_data='start'))
    return markup