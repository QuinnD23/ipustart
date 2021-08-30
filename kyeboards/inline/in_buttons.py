from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from kyeboards.inline.in_datas import check_callback

InlineCheckLevel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1✨", url="https://t.me/level1art"),
            InlineKeyboardButton(text="2✨", url="https://t.me/level2art"),
            InlineKeyboardButton(text="3✨", url="https://t.me/level3art"),
            InlineKeyboardButton(text="4✨", url="https://t.me/level4art"),
            InlineKeyboardButton(text="5✨", url="https://t.me/level5art"),
        ],
    ],
    resize_keyboard=True
)