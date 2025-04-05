from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = '1-music'),
            KeyboardButton(text = '2-music'),
        ],
        [
            KeyboardButton(text = '3-music'),
            KeyboardButton(text = '4-music'),
        ],
        [
            KeyboardButton(text='5-music'),
            KeyboardButton(text='6-music'),
        ],
        [
            KeyboardButton(text='7-music'),
            KeyboardButton(text='8-music'),
        ],
    ],resize_keyboard=True,
    input_field_placeholder='idk'
)





