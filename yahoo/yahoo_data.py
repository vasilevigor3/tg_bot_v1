from db.models.models import RUSFigiModel, USDFigiModel


async def get_long_or_short_rus():
    tickers_rus_list_long, tickers_rus_list_short = [], []
    query = RUSFigiModel.select(RUSFigiModel.ticker).where(RUSFigiModel.long_or_short == True)
    result = query.execute()
    for i in result:
        print(i.ticker)
        tickers_rus_list_long.append(i.ticker[:-3])

    query = RUSFigiModel.select(RUSFigiModel.ticker).where(RUSFigiModel.long_or_short == False)
    result = query.execute()
    for i in result:
        print(i.ticker)
        tickers_rus_list_short.append(i.ticker[:-3])
    return tickers_rus_list_long, tickers_rus_list_short


async def get_long_or_short_usd():
    tickers_usd_list_long, tickers_usd_list_short = [], []
    query = USDFigiModel.select(USDFigiModel.ticker).where(USDFigiModel.long_or_short == True)
    result = query.execute()
    for i in result:
        print(i.ticker)
        tickers_usd_list_long.append(i.ticker)

    query = USDFigiModel.select(USDFigiModel.ticker).where(USDFigiModel.long_or_short == False)
    result = query.execute()
    for i in result:
        print(i.ticker)
        tickers_usd_list_short.append(i.ticker)
    return tickers_usd_list_long, tickers_usd_list_short

# asyncio.run(get_long_or_short_rus())
