from aiogram import types
from loader import bot
from handlers.users import help,jokes,lesson,music,start

async def set_default_commands():
    await bot.set_my_commands(
        [
            types.BotCommand(command="start", description="Running bot"),
            types.BotCommand(command="help", description="Getting some info about bot"),
            types.BotCommand(command="music",description="get anyone music in reply buttons"),
            types.BotCommand(command="jokes", description='generate random joke')
        ]
    )