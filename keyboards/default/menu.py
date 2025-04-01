from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# main = ReplyKeyboardBuilder()
#
# main.add(
#     KeyboardButton(text = 'Text')
# )
# main.row(
#     KeyboardButton(text = 'Button'), width=2
# )

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = '1-lesson'),
            KeyboardButton(text = '2-lesson'),
        ],
        [
            KeyboardButton(text = '3-lesson'),
            KeyboardButton(text = '4-lesson'),
        ]
    ],resize_keyboard=True, input_field_placeholder='Writing....'
)





