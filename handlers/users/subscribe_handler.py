from aiogram import types
from db.models.subscribed_user_model import SubscribedUserModel
from keyboards.inline import inline_menu
from loader import dp, bot


@dp.callback_query_handler(lambda c: c.data and c.data == 'subscribe')
async def process_callback_btn_subscribe(callback_query: types.CallbackQuery):
    subscribed_user_id = callback_query.from_user.id
    user = SubscribedUserModel.get_or_none(user_id=subscribed_user_id)
    if user is None:
        await bot.send_message(callback_query.from_user.id,
                               reply_markup=inline_menu.inline_kb_strategies,
                               text="You have been successfully subscribed.\n"
                                    "Data will automatically sent after stock exchange wil close")
        user = SubscribedUserModel(user_id=subscribed_user_id)
        SubscribedUserModel.save(user)
    else:
        await bot.send_message(callback_query.from_user.id,
                               reply_markup=inline_menu.inline_kb_strategies,
                               text="You're already subscribed")
