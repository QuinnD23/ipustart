from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Command

# config
from data.config import admin_id

# date
import datetime

# db_commands
from handlers.db_commands import insert_db, update_db, select_db, delete_db

# st_commands
from handlers.st_commands import start

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import StartMenu, ClothesMenu, AdminMenu


@dp.message_handler(Command("start"))
async def mess(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).strftime("%d-%m-%Y")

    if user_id != admin_id:
        try:
            await insert_db("info", "user_id", user_id)
        except:
            pass
        await update_db("info", "user_id", "user_name", user_id, user_name)
        await update_db("info", "user_id", "status", user_id, 1)
        await update_db("info", "user_id", "reg_date", user_id, now)

        await message.answer(f"Привет, {user_name}!\n"
                             f"Самые крутые кастомы здесь🔥", reply_markup=StartMenu)
        await StateMachine.Start.set()
    else:
        try:
            await insert_db("ads", "user_id", user_id)
        except:
            pass
        await message.answer("Привет, хозяин😎", reply_markup=AdminMenu)
        await StateMachine.Admin.set()


@dp.message_handler()
async def mess(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)

    if user_id != admin_id:
        check = True

        try:
            await select_db("info", "user_id", "order_num", user_id)
        except:
            check = False

        if check:
            await start(user_id, user_name, dp)
    else:
        check = True

        try:
            await select_db("ads", "user_id", "ads_text", user_id)
        except:
            check = False

        if check:
            await message.answer("Привет, хозяин😎", reply_markup=AdminMenu)
            await StateMachine.Admin.set()


@dp.message_handler(state=StateMachine.Start)
async def mess(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)

    # ----- start
    if message.text == "/start":
        await start(user_id, user_name, dp)
    # -----

    if message.text == "Составить заказ🥥":
        index = str(await select_db("info", "user_id", "order_num", user_id)) + "$" + user_id
        try:
            await insert_db("orders", "index", index)
        except:
            pass

        status = int(await select_db("info", "user_id", "status", user_id))
        if status < 2:
            await update_db("info", "user_id", "status", user_id, 2)

        price = str(await select_db("orders", "index", "price", index))
        await message.answer(f"🏷 Цена заказа: {price} ₽", reply_markup=ClothesMenu)
        await message.answer("Выберите одежду для кастома:\n"
                             "👕 Футболка - 500 ₽\n"
                             "🛍 Шопер - 300 ₽")

        await StateMachine.ClothesSelect.set()
