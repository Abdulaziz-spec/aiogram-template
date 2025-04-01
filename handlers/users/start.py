from aiogram.types import Message
from aiogram.filters import CommandStart
from loader import dp
from keyboards.default.menu import main_keyboard
from aiogram import F

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"HI {message.from_user.full_name}",
                         reply_markup=main_keyboard)



