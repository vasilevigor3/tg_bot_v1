from db.models.models import RUSFigiModel, USDFigiModel


def insert_tickers_in_db():
    tickers_rus = open("/db/ticker_rub.txt", "r").readlines()
    tickers_usd = open("/db/ticker_usd.txt", "r").readlines()

    for ticker in tickers_rus:
        RUSFigiModel.get_or_create(ticker=ticker[:-1] + ".ME", defaults={'long_or_short': None})
    for ticker in tickers_usd:
        USDFigiModel.get_or_create(ticker=ticker[:-1], defaults={'long_or_short': None})
    print("finished")
