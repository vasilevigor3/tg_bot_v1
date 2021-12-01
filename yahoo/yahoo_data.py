import asyncpg


async def get_long_or_short_rus():
    tickers_rus_list_long, tickers_rus_list_short = [], []
    conn: asyncpg.Connection = await asyncpg.connect('postgresql://postgres:example@localhost:5432/postgres')
    select_rus_long = "select TICKER from rus_figis where LONG_OR_SHORT = true"
    select_rus_short = "select TICKER from rus_figis where LONG_OR_SHORT = false"
    rec_rus_long = await conn.fetch(select_rus_long)
    rec_rus_short = await conn.fetch(select_rus_short)
    for i in rec_rus_long:
        tickers_rus_list_long.append(i["ticker"].strip()[:-3])
    for i in rec_rus_short:
        tickers_rus_list_short.append(i["ticker"].strip()[:-3])
    await conn.close()
    return tickers_rus_list_long, tickers_rus_list_short


async def get_long_or_short_usd():
    tickers_usd_list_long, tickers_usd_list_short = [], []
    conn: asyncpg.Connection = await asyncpg.connect('postgresql://postgres:example@localhost:5432/postgres')
    select_usd_long = "select TICKER from usd_figis where LONG_OR_SHORT = true"
    select_usd_short = "select TICKER from usd_figis where LONG_OR_SHORT = false"
    rec_usd_long = await conn.fetch(select_usd_long)
    rec_usd_short = await conn.fetch(select_usd_short)
    for i in rec_usd_long:
        tickers_usd_list_long.append(i["ticker"].strip())
    for i in rec_usd_short:
        tickers_usd_list_short.append(i["ticker"].strip())
    await conn.close()
    return tickers_usd_list_long, tickers_usd_list_short
