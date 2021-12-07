from aiogram import types
from data.config import admin_id
from keyboards.inline import inline_menu
from loader import dp, bot


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('admin'), user_id=admin_id)
async def process_callback_btn_admin(callback_query: types.CallbackQuery):

    await bot.send_message(callback_query.from_user.id, reply_markup=inline_menu.inline_admin, text="You entered as "
                                                                                                    "admin")
