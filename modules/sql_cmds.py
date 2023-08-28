'''Методы связаные с работой с базами данных'''

from aiosqlite import connect

from asyncio import run

async def born_of_db():
    async with connect('database/users.sql') as conn:
        cur = await conn.cursor()
        await cur.execute("CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, status varchar(20), lang varchar(2))")
        await cur.execute("CREATE TABLE IF NOT EXISTS works (id INTEGER PRIMARY KEY AUTOINCREMENT, user int, work int)")
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

async def get_status(user_id):
    async with connect('database/users.sql') as conn:
        cur = await conn.cursor()
        await cur.execute("SELECT status FROM users WHERE id = ?", (user_id,))
        result = (await cur.fetchall())[0][0]
    return result

async def set_status(user_id, status):
    async with connect('database/users.sql') as conn:
        cur = await conn.cursor()
        await cur.execute("UPDATE users SET status = ? WHERE id = ?", (status, user_id,))
        await conn.commit()

async def add_work(user_id, work_id):
    async with connect('database/users.sql') as conn:
        cur = await conn.cursor()
        await cur.execute("INSERT INTO works (user, work) VALUES (?, ?)", (user_id, work_id,))
        await conn.commit() 

async def get_user_works(user_id):
    async with connect('database/users.sql') as conn:
        cur = await conn.cursor()
        await cur.execute("SELECT work FROM works WHERE user = ?", (user_id,))
        result = [work[0] for work in await cur.fetchall()]
    return result

if __name__ == '__main__':
    print(run(get_user_works(1170048051)))