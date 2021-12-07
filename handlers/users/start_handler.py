from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

import yahoo.yahoo_data
from keyboards.inline import inline_menu
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hi, {message.from_user.full_name} ! Choose the strategy",
                         reply_markup=inline_menu.inline_kb_strategies)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('_'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data
    if code == "_rub":
        await bot.send_message(callback_query.from_user.id, '&#128202 - RUB MA50 1D\n')
        a = await yahoo.yahoo_data.get_long_or_short_rus()
        print(a[0])
        print(a[1])
        if a[0]:
            await bot.send_message(callback_query.from_user.id, "&#128200 <b>LONG: </b> " + "<i>" + str(a[0]) + "</i>")
        if not a[0]:
            await bot.send_message(callback_query.from_user.id, "There is no available data for long positions, please try tomorrow")
        if a[1]:
            await bot.send_message(callback_query.from_user.id, "&#128201 <b>SHORT: </b> " + "<i>" + str(a[1]) + "</i>")
        if not a[1]:
            await bot.send_message(callback_query.from_user.id, "There is no available data for short positions, please try tomorrow")
    elif code == "_usd":
        await bot.send_message(callback_query.from_user.id, '&#128202 - USD MA50 1D\n')
        a = await yahoo.yahoo_data.get_long_or_short_usd()
        print(a[0])
        print(a[1])
        if a[0]:
            await bot.send_message(callback_query.from_user.id, "&#128200 <b>LONG: </b> " + "<i>" + str(a[0]) + "</i>")
        if not a[0]:
            await bot.send_message(callback_query.from_user.id, "There is no available data for long positions, please try tomorrow")
        if a[1]:
            await bot.send_message(callback_query.from_user.id, "&#128201 <b>SHORT: </b> " + "<i>" + str(a[1]) + "</i>")
        if not a[1]:
            await bot.send_message(callback_query.from_user.id, "There is no available data for short positions, please try tomorrow")
    else:
        await bot.answer_callback_query(callback_query.id)
