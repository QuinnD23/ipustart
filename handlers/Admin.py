from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Command

# config
from data.config import admin_id

# db_commands
from handlers.db_commands import insert_db, update_db, select_db, delete_db

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import AdminCheckMenu, AdminMenu


@dp.message_handler(state=StateMachine.Admin)
async def mess(message: Message):

    # ----- start
    if message.text == "/start":
        await message.answer("Привет, хозяин😎", reply_markup=AdminMenu)
        await StateMachine.Admin.set()
    # -----

    if message.text == "Запустить рекламу☀":
        await message.answer("Введите текст рекламы:", reply_markup=ReplyKeyboardRemove())
        await StateMachine.CheckAdmin.set()


@dp.message_handler(state=StateMachine.CheckAdmin)
async def mess(message: Message):

    # ----- start
    if message.text == "/start":
        await message.answer("Привет, хозяин😎", reply_markup=AdminMenu)
        await StateMachine.Admin.set()
    # -----

    else:
        ads_text = message.text
        await update_db("ads", "user_id", "ads_text", admin_id, ads_text)
        await message.answer("Сообщение сохранено⚡\n"
                             "Осталось только отправить...", reply_markup=AdminCheckMenu)

        await StateMachine.SendAdmin.set()


@dp.message_handler(state=StateMachine.SendAdmin)
async def mess(message: Message):

    # ----- start
    if message.text == "/start" or message.text == "Отменить⬅":
        await message.answer("Привет, хозяин😎", reply_markup=AdminMenu)
        await StateMachine.Admin.set()
    # -----

    if message.text == "Отправить✅":
        ads_text = str(await select_db("ads", "user_id", "ads_text", admin_id))
        j = 1
        while True:
            try:
                user_id = str(await select_db("info", "user_num", "user_id", j))
            except:
                break
            await dp.bot.send_message(user_id, ads_text)
            j += 1

        await message.answer("Отправка завершена✅", reply_markup=AdminMenu)
        await StateMachine.Admin.set()
