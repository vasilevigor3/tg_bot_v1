#!/usr/bin/env python
import asyncio

import asyncpg
import yfinance as yf

data = yf.download("OKEY.ME", period="50d")
print(data["Open"].values.tolist()[0])

tickers_usd_list, tickers_rus_list, list_rub_buy_to_send, list_usd_buy_to_send, list_rub_sell_to_send, list_usd_sell_to_send = [], [], [], [], [], []
update_rus = "update rus_figis set LONG_OR_SHORT = $2 where TICKER = $1"
update_usd = "update usd_figis set LONG_OR_SHORT = $2 where TICKER = $1"


def close_price(number_of_candle, params): return params["Close"].values.tolist()[number_of_candle]


def open_price(number_of_candle, params): return params["Open"].values.tolist()[number_of_candle]


def getMA(params):
    summ = 0

    for i in range(len(params)):
        summ = summ + close_price(i, params)
    return summ / len(params)


def get_params(ticker):
    return yf.download(ticker, period="50d")


async def push_data_to_db(request, ticker, l_or_s):
    conn: asyncpg.Connection = await asyncpg.connect('postgresql://postgres:example@localhost:5432/postgres')
    await conn.execute(request, ticker, bool(l_or_s))
    await conn.close()


async def get_all_tickers():
    conn: asyncpg.Connection = await asyncpg.connect('postgresql://postgres:example@localhost:5432/postgres')
    select_rus = "select TICKER from rus_figis"
    select_usd = "select TICKER from usd_figis"

    rec_rus = await conn.fetch(select_rus)
    rec_usd = await conn.fetch(select_usd)
    for v in rec_rus:
        tickers_rus_list.append(v["ticker"].strip())
    for v in rec_usd:
        tickers_usd_list.append(v["ticker"].strip())
    await conn.close()


async def get_data(ticker_list, code):
    for i in ticker_list:
        try:
            can_lim = 50 - 1
            params = get_params(i)
            ma = getMA(params)
            print(i)
            print(open_price(can_lim, params))
            print(ma)
            print(close_price(can_lim, params))

            if open_price(can_lim, params) < ma < close_price(can_lim, params):
                if code == "s_rub":
                    list_rub_buy_to_send.append(i)
                    print("BUY")
                    await push_data_to_db(update_rus, i, True)
                if code == "s_usd":
                    list_usd_buy_to_send.append(i)
                    print("BUY")
                    await push_data_to_db(update_usd, i, True)
            if open_price(can_lim, params) > ma > close_price(can_lim, params):
                if code == "s_rub":
                    list_rub_sell_to_send.append(i)
                    print("SELL")
                    await push_data_to_db(update_rus, i, False)
                if code == "s_usd":
                    list_usd_sell_to_send.append(i)
                    print("SELL")
                    await push_data_to_db(update_usd, i, False)
        except Exception as ex:
            print(ex)


async def main():
    await get_all_tickers()
    await get_data(tickers_rus_list, "s_rub")
    await get_data(tickers_usd_list, "s_usd")


asyncio.run(main())

print(list_rub_buy_to_send)
print(list_usd_buy_to_send)
print(list_rub_sell_to_send)
print(list_usd_sell_to_send)
