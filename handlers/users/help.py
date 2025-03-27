from aiogram.types import Message
from loader import dp, bot
from aiogram.filters import Command

@dp.message(Command("help"))
async def help_function(message: Message):
    await message.answer(text = f"{message.from_user.first_name} what can i help you?")
