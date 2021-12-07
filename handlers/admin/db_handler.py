from aiogram import types
from data.config import admin_id
import cron
from keyboards.inline import inline_menu
from loader import dp, bot
from db import fullfilment


@dp.callback_query_handler(lambda c: c.data and c.data == 'fulfillment', user_id=admin_id)
async def process_callback_btn_fulfillment(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'DB Updating starts...')
    fullfilment.insert_tickers_in_db()
    await bot.send_message(callback_query.from_user.id, 'DB Updating finished!',
                           reply_markup=inline_menu.inline_kb_strategies)


@dp.callback_query_handler(lambda c: c.data and c.data == 'data_refresh', user_id=admin_id)
async def process_callback_btn_data_refresh(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'DB Updating starts...')
    await cron.update_figi.main()
    await bot.send_message(callback_query.from_user.id, 'DB Updating finished!')
