# import time
# from . import date1
# from . import setup
# from tinvest import CandleResolution
# # from date1 import today_day, today_month, today_year, calculate_date_for_MA
# # from setup import figis_usd_list, figis_rub_list, client
#
# print(setup.figis_usd_list)
# print(setup.figis_rub_list)
#
#
# def getparams(figi, limit):
#     date = date1.calculate_date_for_MA(limit)
#     return setup.client.get_market_candles(figi
#                                      , f"{date}T00:00:00+03:00"
#                                      , f"{date1.today_year}-{date1.today_month}-{date1.today_day}T00:00:00+03:00",
#                                      CandleResolution.day)
#
#
# def get_ticker_and_name(figi):
#     ticker = setup.client.get_market_search_by_figi(figi).payload.ticker
#     return ticker
#
#
# def getMA(params):
#     summ = 0
#     for i in range(len(params.payload.candles)):
#         summ = summ + close_price(i, params)
#     return summ / len(params.payload.candles)
#
#
# def close_price(number_of_candle, params): return params.payload.candles[number_of_candle].c
#
#
# def high_price(number_of_candle, params): return params.payload.candles[number_of_candle].h
#
#
# def low_price(number_of_candle, params): return params.payload.candles[number_of_candle].l
#
#
# def open_price(number_of_candle, params): return params.payload.candles[number_of_candle].o
#
#
# # for candle in getparams("BBG002W2FT69", 50).payload.candles:
# #     print(candle.c)
#
# # print(getMA("BBG002W2FT69", 200))
# list_rub_buy_to_send = []
# list_rub_sell_to_send = []
# list_usd_buy_to_send = []
# list_usd_sell_to_send = []
#
#
# # with open('figis_usd_list_200.txt') as f:
# #     lines = f.readlines()
# #     for line in lines:
# #         figis_usd_list.append(line[:-1])
#
#
# # print(getparams("BBG002W2FT69", 50).payload.candles[47])
# def get_figi_data_for_tg(code):
#     if code == "s_rub":
#         get_data(setup.figis_rub_list, code)
#         return list_rub_buy_to_send, list_rub_sell_to_send
#     elif code == "s_usd":
#         get_data(setup.figis_usd_list, code)
#         return list_usd_buy_to_send, list_usd_sell_to_send
#
#
# def get_data(list, code):
#     for i in list:
#         try:
#             lim = 50
#             can_lim = 50 - 2
#             params = getparams(i, lim)
#             ma = getMA(params)
#             print(open_price(can_lim, params))
#             print(ma)
#             print(close_price(can_lim, params))
#
#             print(get_ticker_and_name(i))
#
#             if open_price(can_lim, params) < ma < close_price(can_lim, params):
#                 if code == "s_rub":
#                     list_rub_buy_to_send.append(get_ticker_and_name(i))
#                     print(get_ticker_and_name(i))
#                     print("BUY")
#                 if code == "s_usd":
#                     list_usd_buy_to_send.append(get_ticker_and_name(i))
#                     print(get_ticker_and_name(i))
#                     print("SELL")
#             if open_price(can_lim, params) > ma > close_price(can_lim, params):
#                 if code == "s_rub":
#                     list_rub_buy_to_send.append(get_ticker_and_name(i))
#                     print(get_ticker_and_name(i))
#                     print("BUY")
#                 if code == "s_usd":
#                     list_usd_sell_to_send.append(get_ticker_and_name(i))
#                     print(get_ticker_and_name(i))
#                     print("SELL")
#             time.sleep(0.3)
#         except Exception as ex:
#             print(ex)
#
#
# # print(list_rub_buy_to_send)
# # print(list_rub_sell_to_send)
# # get_figi_data_for_tg("s_rub_long")
