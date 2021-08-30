from loader import dp

from aiogram.types import CallbackQuery


@dp.callback_query_handler()
async def check_pictures(call: CallbackQuery):
    await call.answer()
