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

# date
import datetime

# admin
from data.config import admin_id


@dp.message_handler(state=StateMachine.Finally)
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

    if message.text == "Заказать🔥":
        status = int(await select_db("info", "user_id", "status", user_id))
        if status < 10:
            await update_db("info", "user_id", "status", user_id, 10)

        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).strftime("%d-%m-%Y")
        await update_db("orders", "index", "date", index, now)

        url_name = str(await select_db("info", "user_id", "url_name", user_id))
        place = str(await select_db("info", "user_id", "place", user_id))

        clothes = str(await select_db("orders", "index", "clothes", index))
        colour = str(await select_db("orders", "index", "colour", index))
        level = str(await select_db("orders", "index", "level", index))
        price = str(await select_db("orders", "index", "price", index))
        await dp.bot.send_message(admin_id, f"🍀 Поступил новый заказ от {now}\n"
                                            f"\n"
                                            f"🔹 Telegram: @{user_name}\n"
                                            f"🔹 Имя: {url_name}\n"
                                            f"🔹 Адрес: {place}\n"
                                            f"\n"
                                            f"🔸 Одежда: {clothes}\n"
                                            f"🔸 Цвет: {colour}\n"
                                            f"🔸 Уровень: {level}\n"
                                            f"\n"
                                            f"🏷 Цена заказа: {price} ₽\n"
                                            f"🚙 Цена доставки: 200-400 ₽")

        photo_id = str(await select_db("orders", "index", "photo_id", index))
        await dp.bot.send_photo(admin_id, photo_id, caption=f"🔹 Telegram: @{user_name}")

        order_num = int(await select_db("info", "user_id", "order_num", user_id)) + 1
        await update_db("info", "user_id", "order_num", user_id, order_num)

        await message.answer("Заказ создан✅", reply_markup=StartMenu)
        await message.answer("Скоро с вами свяжется наш менеджер @sotnicova1 и уточнит все дальнейшие действия☁")

        await StateMachine.Start.set()
