# import tinvest
#
# from data import config
# import os
# os.path.abspath("C:/example/cwd/mydir/myfile.txt")
#
# ###### SETUP START######
# client = tinvest.SyncClient(config.TINKOFF_TOKEN)
#
# payload = client.get_market_stocks().payload
#
# figis = [(p.name, p.figi, p.currency) for p in payload.instruments]
# ###### SETUP END######
#
# ###### PREPEAR RUS AND USD LISTS OF FIGIS START######
# figis_usd_list = []
# figis_rub_list = []
#
# for candle in figis:
#     if candle[2] == "RUB":
#         figis_rub_list.append(candle[1])
#
# # with open(os.path.abspath("C:/Users/Igor_Vasiliev/Desktop/tg_bot_v1/tinkoff/figis_usd_list_200.txt")) as f:
# #     lines = f.readlines()
# #     for line in lines:
# #         figis_usd_list.append(line[:-1])
# ###### PREPEAR RUS AND USD LISTS OF FIGIS END######
