from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.db_commands import insert_db, update_db, select_db, delete_db

# st_commands
from handlers.st_commands import start

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import StartMenu, CheckLevelMenu
from kyeboards.inline.in_buttons import InlineCheckLevel


@dp.message_handler(state=StateMachine.ColourSelect)
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

    if message.text == "Белый🤍":
        status = int(await select_db("info", "user_id", "status", user_id))
        if status < 4:
            await update_db("info", "user_id", "status", user_id, 4)

        await update_db("orders", "index", "colour", index, "Белый🤍")

        price = int(await select_db("orders", "index", "price", index))

        await message.answer(f"🏷 Цена заказа: {price} ₽", reply_markup=CheckLevelMenu)
        await message.answer("Выберите сложность вашего рисунка:\n"
                             "▪ 1 уровень - 300 ₽\n"
                             "◾ 2 уровень - 450 ₽\n"
                             "◼ 3 уровень - 700 ₽\n"
                             "⬛ 4 уровень - 1000 ₽\n"
                             "🔲 5 уровень - 1400 ₽")
        await message.answer("✨Чтобы понять, какого уровня ваш рисунок, взгляните на примеры", reply_markup=InlineCheckLevel)

        await StateMachine.CheckLevel.set()

    if message.text == "Черный🖤":
        status = int(await select_db("info", "user_id", "status", user_id))
        if status < 4:
            await update_db("info", "user_id", "status", user_id, 4)

        await update_db("orders", "index", "colour", index, "Черный🖤")

        price = int(await select_db("orders", "index", "price", index))
        price += 200
        await update_db("orders", "index", "price", index, price)

        await message.answer(f"🏷 Цена заказа: {price} ₽", reply_markup=CheckLevelMenu)
        await message.answer("Выберите сложность вашего рисунка:\n"
                             "▪ 1 уровень - 300 ₽\n"
                             "◾ 2 уровень - 450 ₽\n"
                             "◼ 3 уровень - 700 ₽\n"
                             "⬛ 4 уровень - 1000 ₽\n"
                             "🔲 5 уровень - 1400 ₽")
        await message.answer("✨Чтобы понять, какого уровня ваш рисунок, взгляните на примеры", reply_markup=InlineCheckLevel)

        await StateMachine.CheckLevel.set()
