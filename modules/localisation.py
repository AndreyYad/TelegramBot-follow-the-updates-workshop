'''Возвращение текста в нужном языке'''

from gettext import translation

from modules.sql_cmds import get_lang

async def _(user_id, msgid):
    translations = translation(localedir='localisation', languages=[await get_lang(user_id)],  domain='bbb_text')
    translations.install()
    return translations.gettext(msgid)