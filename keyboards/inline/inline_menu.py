from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_1 = InlineKeyboardButton('RUB MA50 1D', callback_data='s_rub')
inline_btn_2 = InlineKeyboardButton('USD MA50 1D', callback_data='s_usd')
inline_kb_strategies = InlineKeyboardMarkup(row_width=2).add(inline_btn_1, inline_btn_2)

