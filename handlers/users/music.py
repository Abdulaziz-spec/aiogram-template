from aiogram.types import Message
from loader import dp, bot
from aiogram.filters import Command

@dp.message(Command("music"))
async def music_function(message: Message):
    await message.answer(text = f"{message.from_user.first_name} what music do you want listen")
