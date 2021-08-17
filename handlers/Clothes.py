from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.db_commands import insert_db, update_db, select_db, delete_db

# st_commands
from handlers.st_commands import start

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import StartMenu, ColourMenu


@dp.message_handler(state=StateMachine.ClothesSelect)
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

    if message.text == "Шопер🛍":
        status = int(await select_db("info", "user_id", "status", user_id))
        if status < 3:
            await update_db("info", "user_id", "status", user_id, 3)

        await update_db("orders", "index", "clothes", index, "Шопер🛍")

        price = int(await select_db("orders", "index", "price", index))
        price += 300
        await update_db("orders", "index", "price", index, price)

        await message.answer(f"🏷 Цена заказа: {price} ₽", reply_markup=ColourMenu)
        await message.answer("Выберите цвет одежды:\n"
                             "🤍 Белый - 0 ₽\n"
                             "🖤 Черный - 200 ₽")
        await message.answer("Черный цвет требует дополнительные затраты краски")

        await StateMachine.ColourSelect.set()

    if message.text == "Футболка👕":
        status = int(await select_db("info", "user_id", "status", user_id))
        if status < 3:
            await update_db("info", "user_id", "status", user_id, 3)

        await update_db("orders", "index", "clothes", index, "Футболка👕")

        price = int(await select_db("orders", "index", "price", index))
        price += 500
        await update_db("orders", "index", "price", index, price)

        await message.answer(f"🏷 Цена заказа: {price} ₽", reply_markup=ColourMenu)
        await message.answer("Выберите цвет одежды:\n"
                             "🤍 Белый - 0 ₽\n"
                             "🖤 Черный - 200 ₽")
        await message.answer("Черный цвет требует дополнительные затраты краски")

        await StateMachine.ColourSelect.set()