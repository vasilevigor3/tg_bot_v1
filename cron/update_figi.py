#!/usr/bin/env python
import asyncio
import yfinance as yf

from db.models.models import RUSFigiModel, USDFigiModel
from . import subscriber_job

tickers_usd_list, tickers_rus_list, list_rub_buy_to_send, list_usd_buy_to_send, list_rub_sell_to_send, list_usd_sell_to_send = [], [], [], [], [], []


def close_price(number_of_candle, params): return params["Close"].values.tolist()[number_of_candle]


def open_price(number_of_candle, params): return params["Open"].values.tolist()[number_of_candle]


def getMA(params):
    summ = 0

    for i in range(len(params)):
        summ = summ + close_price(i, params)
    return summ / len(params)


def get_params(ticker):
    return yf.download(ticker, period="50d")


async def clean_data(model):
    query = model.update(long_or_short=None).where(model.long_or_short is not None)
    query.execute()


async def push_data_to_db(model, ticker, l_or_s):
    query = model.update({model.long_or_short: l_or_s}).where(
        model.ticker == ticker)
    query.execute()


async def get_all_tickers():
    query = RUSFigiModel.select(RUSFigiModel.ticker)
    result = query.dicts().execute()
    for artist in result:
        for k, v in artist.items():
            tickers_rus_list.append(v)
    query = USDFigiModel.select(USDFigiModel.ticker)
    result = query.dicts().execute()
    for artist in result:
        for k, v in artist.items():
            tickers_usd_list.append(v)


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
                    await push_data_to_db(RUSFigiModel, i, True)
                if code == "s_usd":
                    list_usd_buy_to_send.append(i)
                    print("BUY")
                    await push_data_to_db(USDFigiModel, i, True)
            if open_price(can_lim, params) > ma > close_price(can_lim, params):
                if code == "s_rub":
                    list_rub_sell_to_send.append(i)
                    print("SELL")
                    await push_data_to_db(RUSFigiModel, i, False)
                if code == "s_usd":
                    list_usd_sell_to_send.append(i)
                    print("SELL")
                    await push_data_to_db(USDFigiModel, i, False)
        except Exception as ex:
            print(ex)


async def main():
    await clean_data(RUSFigiModel)
    await clean_data(USDFigiModel)
    await get_all_tickers()
    await get_data(tickers_rus_list, "s_rub")
    await get_data(tickers_usd_list, "s_usd")
