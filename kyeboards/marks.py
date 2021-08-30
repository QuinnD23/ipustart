from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

StartMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Составить заказ🥥"),
        ],
    ],
    resize_keyboard=True
)

ClothesMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Шопер🛍"),
            KeyboardButton(text="Футболка👕"),
        ],
        [
            KeyboardButton(text="Отменить⬅"),
        ],
    ],
    resize_keyboard=True
)

ColourMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Белый🤍"),
            KeyboardButton(text="Черный🖤"),
        ],
        [
            KeyboardButton(text="Отменить⬅"),
        ],
    ],
    resize_keyboard=True
)

CheckLevelMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Указать сложность✅"),
        ],
        [
            KeyboardButton(text="Отменить⬅"),
        ],
    ],
    resize_keyboard=True
)

EnterLevelMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1️⃣"),
            KeyboardButton(text="2️⃣"),
            KeyboardButton(text="3️⃣"),
            KeyboardButton(text="4️⃣"),
            KeyboardButton(text="5️⃣"),
        ],
        [
            KeyboardButton(text="Отменить⬅"),
        ],
    ],
    resize_keyboard=True
)

AcceptMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да✅"),
            KeyboardButton(text="Нет❌"),
        ],
        [
            KeyboardButton(text="Отменить⬅"),
        ],
    ],
    resize_keyboard=True
)

FinallyMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Заказать🔥"),
        ],
        [
            KeyboardButton(text="Отменить⬅"),
        ],
    ],
    resize_keyboard=True
)

AdminMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Запустить рекламу☀"),
        ],
    ],
    resize_keyboard=True
)

AdminCheckMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить✅"),
        ],
        [
            KeyboardButton(text="Отменить⬅"),
        ],
    ],
    resize_keyboard=True
)
