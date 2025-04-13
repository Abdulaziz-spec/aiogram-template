import random
from aiogram import types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp

jokes = [
    "Почему программисты не любят ходить в лес? Потому что они боятся багов.",
    "Как программисты делают уборку? Они пишут программу для очистки мусора.",
    "Какая разница между программистом и врачом? Программист исправляет ошибки, а врач их находит.",
    "Почему программисты не доверяют лестницам? Потому что они всегда спотыкаются о баги.",
    "Что сказал один программист другому? Слушай, тебе нужно разобраться с этим кодом!"
]


@dp.message(Command("jokes"))
async def jokes_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Get a joke", callback_data="get_joke")]
        ]
    )
    await message.answer("Click the button to get a random joke:", reply_markup=keyboard)


@dp.callback_query(lambda c: c.data == "get_joke")
async def send_joke(callback_query: types.CallbackQuery):
    joke = random.choice(jokes)
    await callback_query.message.answer(joke)
    await callback_query.answer()
