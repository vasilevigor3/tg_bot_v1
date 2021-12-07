import yahoo
from loader import bot


async def main(user_id):
    a = await yahoo.yahoo_data.get_long_or_short_rus()
    if a[0]:
        await bot.send_message(user_id, "&#128200 <b>LONG: </b> " + "<i>" + str(a[0]) + "</i>")
    if not a[0]:
        await bot.send_message(user_id, "There is no available data for long positions")
    if a[1]:
        await bot.send_message(user_id, "&#128201 <b>SHORT: </b> " + "<i>" + str(a[1]) + "</i>")
    if not a[1]:
        await bot.send_message(user_id, "There is no available data for short positions")

    await bot.send_message(user_id, '&#128202 - USD MA50 1D\n')
    a = await yahoo.yahoo_data.get_long_or_short_usd()
    if a[0]:
        await bot.send_message(user_id, "&#128200 <b>LONG: </b> " + "<i>" + str(a[0]) + "</i>")
    if not a[0]:
        await bot.send_message(user_id, "There is no available data for long positions")
    if a[1]:
        await bot.send_message(user_id, "&#128201 <b>SHORT: </b> " + "<i>" + str(a[1]) + "</i>")
    if not a[1]:
        await bot.send_message(user_id, "There is no available data for short positions")
