from aiogram import Dispatcher

# state_machine
from states.statates import StateMachine

# db_commands
from handlers.db_commands import insert_db, update_db, select_db, delete_db

# marks
from kyeboards.marks import StartMenu


async def start(user_id, user_name, dp: Dispatcher):
    index = str(await select_db("info", "user_id", "order_num", user_id)) + "$" + user_id
    try:
        await update_db("orders", "index", "price", index, 0)
    except:
        pass
    await dp.bot.send_message(user_id, f"Привет, {user_name}!\n"
                                       f"Самые крутые кастомы здесь🔥", reply_markup=StartMenu)
    await StateMachine.Start.set()
