import os
from aiogram import types
from aiogram.utils import executor
from aiogram.utils.markdown import text, code

# backend default modules
from back.config_manager import get_config
from back.token_manager import get_token
from back.telegram_manager import generate_bot_dp
from back.print_manager import Logger


SCRIPT_PATH = "/".join(os.path.realpath(__file__).split("/")[:-1])

CONFIG = get_config(SCRIPT_PATH)
TG_TOKEN = get_token(SCRIPT_PATH)
APP_NAME = CONFIG["APP_NAME"]

bot, dp = generate_bot_dp(TG_TOKEN)

logger = Logger(SCRIPT_PATH)


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):

    s = text(
        "Привет!",
        "Этот бот отправляет telegram ID для каждого пользователя",
        "Просто отправьте любое сообщение",
        sep="\n\n",
    )

    await bot.send_message(message.from_user.id, s)


@dp.message_handler()
async def process_answer(message: types.Message):
    logger.mprint(
        f"INCOME : from {message.from_user.id} ::: {message.text}", print_std=False
    )

    s = text("Ваш telergam ID :", code(message.from_user.id), sep="\n\n")
    await bot.send_message(message.from_user.id, s)

    logger.mprint(APP_NAME + f" : reacted to {message.from_user.id}", print_std=False)


if __name__ == "__main__":
    logger.mprint(APP_NAME + " : bot started")
    executor.start_polling(dp)
