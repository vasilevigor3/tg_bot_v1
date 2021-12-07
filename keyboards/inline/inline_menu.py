from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_1 = InlineKeyboardButton('RUB MA50 1D', callback_data='_rub')
inline_btn_2 = InlineKeyboardButton('USD MA50 1D', callback_data='_usd')

inline_btn_3 = InlineKeyboardButton('REFRESH DATA', callback_data='data_refresh')
inline_btn_4 = InlineKeyboardButton('DB FULFILMENT', callback_data='fulfillment')

inline_btn_5 = InlineKeyboardButton('admin', callback_data='admin')

inline_btn_6 = InlineKeyboardButton('SUBSCRIBE', callback_data='subscribe')
inline_btn_7 = InlineKeyboardButton('UNSUBSCRIBE', callback_data='unsubscribe')

inline_kb_strategies = InlineKeyboardMarkup(row_width=2)\
    .add(inline_btn_1, inline_btn_2)\
    .add(inline_btn_6, inline_btn_7)\
    .add(inline_btn_5)

inline_admin = InlineKeyboardMarkup(row_width=2)\
    .add(inline_btn_4, inline_btn_3)\
