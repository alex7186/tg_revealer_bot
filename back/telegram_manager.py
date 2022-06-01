from aiogram import Bot
from aiogram.dispatcher import Dispatcher


def generate_bot_dp(TOKEN):
    bot = Bot(token=TOKEN)
    dispatcher = Dispatcher(bot)
    return bot, dispatcher
