from aiogram import F
from aiogram.types import Message
from loader import dp

@dp.message(F.text)
async def lesson_one(message: Message):
    if message.text == '1-lesson':
        await message.answer("<a href = 'https://www.youtube.com/watch?v=4xqVv2lTo40'>This Lesson 1</a>")
    elif message.text == '2-lesson':
        await message.answer("<a href = 'https://www.youtube.com/watch?v=4xqVv2lTo40'>This lesson 2</a>")
    elif message.text == '3-lesson':
        await message.answer('This lesson 3')
    elif message.text == '4-lesson':
        await message.answer('This lesson 4')
    else:
        await message.answer('Bunday dars yo')
