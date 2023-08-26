'''Наборы inline-кнопок'''

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def markup_lang():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton('🇷🇺', callback_data='lang_ru'),
        InlineKeyboardButton('🇬🇧', callback_data='lang_en')
    )       
    return markup