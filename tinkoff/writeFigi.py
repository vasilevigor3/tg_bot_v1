# import os
# from time import sleep
#
# import tinvest
#
# from data import config
# from tinkoff import setup
#
#
# def close_price(number_of_candle, params): return params.payload.candles[number_of_candle].c
#
#
# def get_ticker_and_name(figi):
#     ticker = setup.client.get_market_search_by_figi(figi).payload.ticker
#     return ticker
#
#
# client = tinvest.SyncClient(config.TINKOFF_TOKEN)
#
# payload = client.get_market_stocks().payload
#
# figis = [(p.name, p.figi, p.currency) for p in payload.instruments]
#
# figis_rub_list = []
# ticker_rub_list = []
# figis_usd_list = []
# ticker_usd_list = []
#
# # for candle in figis:
# #     if candle[2] == "RUB":
# #         figis_rub_list.append(candle[1])
# #         ticker_rub_list.append(get_ticker_and_name(candle[1]))
# #         sleep(0.1)
#
# # for candle in figis:
# #     if candle[2] == "USD":
# #         figis_usd_list.append(candle[1])
# #         ticker_usd_list.append(get_ticker_and_name(candle[1]))
#
#
# # with open(os.path.abspath("C:/Users/Igor_Vasiliev/Desktop/tg_bot_v1/tinkoff/figis_usd_list_200.txt")) as f:
# #     lines = f.readlines()
# #     for line in lines:
# #         figis_usd_list.append(line[:-1])
# #         ticker_usd_list.append(get_ticker_and_name(line[:-1]))
# #         sleep(0.3)
#
# file = open("ticker_usd.txt", "w")
# for element in ticker_usd_list:
#     file.write(element + "\n")
# file.close()
