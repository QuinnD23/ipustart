from loader import dp

from aiogram.types import Message, ReplyKeyboardRemove

# db_commands
from handlers.db_commands import insert_db, update_db, select_db, delete_db

# st_commands
from handlers.st_commands import start

# state_machine
from states.statates import StateMachine

# marks
from kyeboards.marks import StartMenu, AcceptMenu


@dp.message_handler(content_types=["photo"], state=StateMachine.CheckPhoto)
async def send_photo(message: Message):
    user_id = str(message.from_user.id)
    index = str(await select_db("info", "user_id", "order_num", user_id)) + "$" + user_id

    photo_id = str(message.photo[-1].file_id)
    await update_db("orders", "index", "photo_id", index, photo_id)

    await message.answer("Вы уверены в правильности фото?", reply_markup=AcceptMenu)


@dp.message_handler(state=StateMachine.CheckPhoto)
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
        if status < 7:
            await update_db("info", "user_id", "status", user_id, 7)

        price = int(await select_db("orders", "index", "price", index))

        await message.answer(f"🏷 Цена заказа: {price} ₽", reply_markup=ReplyKeyboardRemove())
        await message.answer("Укажите адрес доставки:")

        await StateMachine.EnterPlace.set()

    if message.text == "Нет❌":
        await message.answer("Отправьте фото вашего рисунка:")
