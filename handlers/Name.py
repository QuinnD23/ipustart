from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.db_commands import insert_db, update_db, select_db, delete_db

# st_commands
from handlers.st_commands import start

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import StartMenu, AcceptMenu, FinallyMenu


@dp.message_handler(state=StateMachine.EnterName)
async def mess(message: Message):
    user_id = str(message.from_user.id)
    user_name = str(message.from_user.username)

    # ----- start
    if message.text == "/start":
        await start(user_id, user_name, dp)
    # -----

    else:
        url_name = str(message.text)

        await update_db("info", "user_id", "url_name", user_id, url_name)

        await message.answer(f"Вы уверены в правильности имени?", reply_markup=AcceptMenu)

        await StateMachine.CheckName.set()


@dp.message_handler(state=StateMachine.CheckName)
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

    if message.text == "Да✅":
        status = int(await select_db("info", "user_id", "status", user_id))
        if status < 9:
            await update_db("info", "user_id", "status", user_id, 9)

        price = int(await select_db("orders", "index", "price", index))

        await message.answer("Заказ успешно заполнен🌷", reply_markup=FinallyMenu)
        await message.answer(f"🏷 Цена заказа: {price} ₽\n"
                             f"🚙 Цена доставки: 200-400 ₽")
        await message.answer("Нажмите: Заказать🔥\n"
                             "И ожидайте ответа")

        await StateMachine.Finally.set()

    if message.text == "Нет❌":
        await message.answer("Укажите ваше имя:", reply_markup=ReplyKeyboardRemove())

        await StateMachine.EnterName.set()
