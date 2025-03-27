from aiogram.types import Message
from aiogram.filters import CommandStart
from loader import dp


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"HI {message.from_user.full_name}")