import hashlib
from typing import List

import aiosqlite


async def add_user(ip: str):
    async with aiosqlite.connect('weather.db') as db:
        value = hashlib.md5(ip.encode()).hexdigest()
        async with db.execute('SELECT * FROM users WHERE hash=?', (value,)) as cursor:
            v = await cursor.fetchone()
        if v is None:
            await db.execute('INSERT INTO Users (hash, history) VALUES (?, ?)', (value, ""))
            await db.commit()


async def set_history(ip: str, city: str):
    async with aiosqlite.connect('weather.db') as db:
        value = hashlib.md5(ip.encode()).hexdigest()
        async with db.execute('SELECT history FROM Users WHERE hash=?', (value,)) as cursor:
            v = await cursor.fetchone()
            hist = v[0] if v else ""
        if hist == "":
            hist = city
        else:
            hist += f";{city}"
        await db.execute('UPDATE Users SET history=? WHERE hash=?', (hist, value))
        await db.commit()


async def add_stat(city: str):
    async with aiosqlite.connect('weather.db') as db:
        async with db.execute('SELECT count FROM City WHERE name=?', (city,)) as cursor:
            v = await cursor.fetchone()
            count = v[0] if v else None
        if isinstance(count, int):
            await db.execute('UPDATE City SET count=? WHERE name=?', (count + 1, city))
        else:
            await db.execute('INSERT INTO City (name) VALUES(?)', (city,))
        await db.commit()


async def get_stat(city: str) -> int:
    async with aiosqlite.connect("weather.db") as db:
        async with db.execute('SELECT count FROM City WHERE name=?', (city,)) as cursor:
            v = await cursor.fetchone()
            count = v[0] if v else ""
        return count


async def last_city(ip: str) -> str:
    async with aiosqlite.connect('weather.db') as db:
        value = hashlib.md5(ip.encode()).hexdigest()
        async with db.execute('SELECT * FROM Users WHERE hash=?', (value,)) as cursor:
            v = await cursor.fetchone()
            if v is None:
                hist = ""
            else:
                hist = v[1]
            last = hist.split(";")[-1] if hist else ""
        return last
