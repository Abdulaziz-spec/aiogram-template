from aiogram import F
from loader import dp, bot
from aiogram.types import Message
from keyboards.inline.inline_key import inline_keyboards
@dp.message(F.text=='photo')
async def get_file_id(message: Message):
    await message.answer(text = 'Photos', reply_markup = inline_keyboards)


