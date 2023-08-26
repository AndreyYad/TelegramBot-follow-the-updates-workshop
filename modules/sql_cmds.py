'''Методы связаные с работой с базами данных'''

from aiosqlite import connect

async def born_of_db():
    async with connect('database/users.sql') as conn:
        cur = await conn.cursor()
        await cur.execute("CREATE TABLE IF NOT EXISTS users (id int primary key, status varchar(50), lang varchar(2))")
        await conn.commit()

async def set_user_info(user_id):
    async with connect('database/users.sql') as conn:
        cur = await conn.cursor()
        await cur.execute("INSERT OR IGNORE INTO users VALUES (?, 'none', 'en')", (user_id,))
        await conn.commit()

async def get_lang(user_id):
    async with connect('database/users.sql') as conn:
        cur = await conn.cursor()
        await cur.execute("SELECT lang FROM users WHERE id = ?", (user_id,))
        result = (await cur.fetchall())[0][0]
    return result

async def set_lang(user_id, lang):
    async with connect('database/users.sql') as conn:
        cur = await conn.cursor()
        await cur.execute("UPDATE users SET lang = ? WHERE id = ?", (lang, user_id,))
        await conn.commit()