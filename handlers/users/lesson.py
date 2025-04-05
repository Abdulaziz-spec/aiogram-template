import aiogram.types
from aiogram import F
from aiogram.types import Message
from loader import dp

@dp.message(F.text)
async def lesson_one(message: Message):
    if message.text == '1-music':
        await message.answer("<a href = 'https://www.youtube.com/watch?v=Eo-KmOd3i7s'>Deadpool Bye Bye Bye</a>")
    elif message.text == '2-music':
        await message.answer("<a href = 'https://www.youtube.com/watch?v=YVkUvmDQ3HY'>Eminem Without me</a>")
    elif message.text == '3-music':
        await message.answer("<a href = 'https://www.youtube.com/watch?v=qaZ0oAh4evU'>Alvaro Soler - Sofia</a>")
    elif message.text == '4-music':
        await message.answer("<a href = 'https://www.youtube.com/watch?v=a5oedjPzCUg'>Memphis Cult, GROOVE DEALERS, SPLYXER - 9MM</a>")
    elif message.text == 'music':
        await message.answer(f"hi {aiogram.types.User.full_name} What music do you want listen")
    else:
        await message.answer('404 Not found')
