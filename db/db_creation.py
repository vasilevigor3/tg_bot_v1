import asyncio
import asyncpg


async def create_db():
    create_rus_db_command = open("rus_figis.sql", "r").read()
    create_usd_db_command = open("usd_figis.sql", "r").read()

    conn: asyncpg.Connection = await asyncpg.connect('postgresql://postgres:example@localhost:6543/postgres')
    await conn.execute(create_rus_db_command)
    await conn.execute(create_usd_db_command)
    await conn.close()
    await insert_tickers_in_db()


async def insert_tickers_in_db():
    tickers_rus = open("C:/Users/Igor_Vasiliev/Desktop/tg_bot_v1/tinkoff/ticker_rub.txt", "r").readlines()
    tickers_usd = open("C:/Users/Igor_Vasiliev/Desktop/tg_bot_v1/tinkoff/ticker_usd.txt", "r").readlines()
    conn: asyncpg.Connection = await asyncpg.connect('postgresql://postgres:example@localhost:6543/postgres')
    for ticker in tickers_rus:
        insert = "INSERT INTO RUS_FIGIS (TICKER) VALUES ($1)"
        await conn.execute(insert, ticker[:-1] + ".ME")
    for ticker in tickers_usd:
        insert = "INSERT INTO USD_FIGIS (TICKER) VALUES ($1)"
        await conn.execute(insert, ticker[:-1])
    await conn.close()


async def create_pool():
    return await asyncpg.create_pool('postgresql://postgres:example@localhost:6543/postgres')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
