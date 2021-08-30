from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.db_commands import insert_db, update_db, select_db, delete_db

# st_commands
from handlers.st_commands import start

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import StartMenu, EnterLevelMenu


@dp.message_handler(state=StateMachine.CheckLevel)
async def mess(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)

    index = str(await select_db("info", "user_id", "order_num", user_id)) + "$" + user_id

    # ----- start
    if message.text == "/start":
        await start(user_id, user_name, dp)
    # -----

    # ----- back
    if message.text == "Отменить⬅":
        await update_db("orders", "index", "price", index, 0)
        await message.answer("Отменяю...", reply_markup=StartMenu)
        await StateMachine.Start.set()
    # -----

    if message.text == "Указать сложность✅":
        status = int(await select_db("info", "user_id", "status", user_id))
        if status < 5:
            await update_db("info", "user_id", "status", user_id, 5)

        await message.answer("Укажите сложность:", reply_markup=EnterLevelMenu)

        await StateMachine.EnterLevel.set()


@dp.message_handler(state=StateMachine.EnterLevel)
async def mess(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)

    index = str(await select_db("info", "user_id", "order_num", user_id)) + "$" + user_id

    # ----- start
    if message.text == "/start":
        await start(user_id, user_name, dp)
    # -----

    # ----- back
    if message.text == "Отменить⬅":
        await update_db("orders", "index", "price", index, 0)
        await message.answer("Отменяю...", reply_markup=StartMenu)
        await StateMachine.Start.set()
    # -----

    if message.text == "1️⃣":
        status = int(await select_db("info", "user_id", "status", user_id))
        if status < 6:
            await update_db("info", "user_id", "status", user_id, 6)

        await update_db("orders", "index", "level", index, "1")

        price = int(await select_db("orders", "index", "price", index))
        price += 300
        await update_db("orders", "index", "price", index, price)

        await message.answer(f"🏷 Цена заказа: {price} ₽", reply_markup=ReplyKeyboardRemove())
        await message.answer("Отправьте фото вашего рисунка:")

        await StateMachine.CheckPhoto.set()

    if message.text == "2️⃣":
        status = int(await select_db("info", "user_id", "status", user_id))
        if status < 6:
            await update_db("info", "user_id", "status", user_id, 6)

        await update_db("orders", "index", "level", index, "2")

        price = int(await select_db("orders", "index", "price", index))
        price += 450
        await update_db("orders", "index", "price", index, price)

        await message.answer(f"🏷 Цена заказа: {price} ₽", reply_markup=ReplyKeyboardRemove())
        await message.answer("Отправьте фото вашего рисунка:")

        await StateMachine.CheckPhoto.set()

    if message.text == "3️⃣":
        status = int(await select_db("info", "user_id", "status", user_id))
        if status < 6:
            await update_db("info", "user_id", "status", user_id, 6)

        await update_db("orders", "index", "level", index, "3")

        price = int(await select_db("orders", "index", "price", index))
        price += 700
        await update_db("orders", "index", "price", index, price)

        await message.answer(f"🏷 Цена заказа: {price} ₽", reply_markup=ReplyKeyboardRemove())
        await message.answer("Отправьте фото вашего рисунка:")

        await StateMachine.CheckPhoto.set()

    if message.text == "4️⃣":
        status = int(await select_db("info", "user_id", "status", user_id))
        if status < 6:
            await update_db("info", "user_id", "status", user_id, 6)

        await update_db("orders", "index", "level", index, "4")

        price = int(await select_db("orders", "index", "price", index))
        price += 1000
        await update_db("orders", "index", "price", index, price)

        await message.answer(f"🏷 Цена заказа: {price} ₽", reply_markup=ReplyKeyboardRemove())
        await message.answer("Отправьте фото вашего рисунка:")

        await StateMachine.CheckPhoto.set()

    if message.text == "5️⃣":
        status = int(await select_db("info", "user_id", "status", user_id))
        if status < 6:
            await update_db("info", "user_id", "status", user_id, 6)

        await update_db("orders", "index", "level", index, "5")

        price = int(await select_db("orders", "index", "price", index))
        price += 1400
        await update_db("orders", "index", "price", index, price)

        await message.answer(f"🏷 Цена заказа: {price} ₽", reply_markup=ReplyKeyboardRemove())
        await message.answer("Отправьте фото вашего рисунка:")

        await StateMachine.CheckPhoto.set()
