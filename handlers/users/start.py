from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

import yahoo.yahoo_data
from keyboards.inline import inline_menu
from loader import dp, bot
# from tinkoff.tinkoff_test import get_figi_data_for_tg


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hi, {message.from_user.full_name} ! Choose the strategy",
                         reply_markup=inline_menu.inline_kb_strategies)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('s'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    print(callback_query.data)

    code = callback_query.data
    if code == "s_rub":
        await bot.send_message(callback_query.from_user.id, '&#128202 - RUB MA50 1D\n')
        a = await yahoo.yahoo_data.get_long_or_short_rus()
        print(a[0])
        print(a[1])
        if a[0]:
            await bot.send_message(callback_query.from_user.id, "&#128200 <b>LONG: </b> " + "<i>" + str(a[0]) + "</i>")
        if not a[0]:
            await bot.send_message(callback_query.from_user.id, "There is no avalible data for long positions, please try tomorrow")
        if a[1]:
            await bot.send_message(callback_query.from_user.id, "&#128201 <b>SHORT: </b> " + "<i>" + str(a[1]) + "</i>")
        if not a[1]:
            await bot.send_message(callback_query.from_user.id, "There is no avalible data for short positions, please try tomorrow")
    # elif code == "s_rub_short":
    #     await bot.answer_callback_query(callback_query.id, text='RUB MA50 SHORT 1D')
    #     await bot.send_message(callback_query.from_user.id, 'PLEASE WAIT FOR DATA LOADING - RUB MA50 SHORT 1D\n')
    #     await bot.send_message(callback_query.from_user.id, get_figi_data_for_tg(code))
    elif code == "s_usd":
        # await bot.answer_callback_query(callback_query.id, text='USD MA50 1D')
        await bot.send_message(callback_query.from_user.id, '&#128202 - USD MA50 1D\n')
        a = await yahoo.yahoo_data.get_long_or_short_usd()
        print(a[0])
        print(a[1])
        if a[0]:
            await bot.send_message(callback_query.from_user.id, "&#128200 <b>LONG: </b> " + "<i>" + str(a[0]) + "</i>")
        if not a[0]:
            await bot.send_message(callback_query.from_user.id, "There is no avalible data for long positions, please try tomorrow")
        if a[1]:
            await bot.send_message(callback_query.from_user.id, "&#128201 <b>SHORT: </b> " + "<i>" + str(a[1]) + "</i>")
        if not a[1]:
            await bot.send_message(callback_query.from_user.id, "There is no avalible data for short positions, please try tomorrow")

    # elif code == "s_usd_short":
    #     await bot.answer_callback_query(callback_query.id, text='USD MA50 SHORT 1D')
    #     await bot.send_message(callback_query.from_user.id, 'PLEASE WAIT FOR DATA LOADING - USD MA50 SHORT 1D\n')
    #     await bot.send_message(callback_query.from_user.id, get_figi_data_for_tg(code))
    # elif code == "s_usd_short":
    #     await bot.answer_callback_query(
    #         callback_query.id,
    #         text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    # await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')