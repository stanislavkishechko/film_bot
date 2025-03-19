import asyncio

from commands import FILMS_COMMAND, START_COMMAND, DESCRIPTION_COMMAND, START_BOT_COMMAND, FILMS_BOT_COMMAND
from data import get_films

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message

from decouple import config

from keyboards import films_keyboard_markup

TOKEN = config("BOT_TOKEN")

dp = Dispatcher()


@dp.message(START_COMMAND)
async def start(message: Message) -> None:
    await message.answer(
        f"Вітаю, {message.from_user.full_name}! Я допоможу знайти тобі фільм."
    )


@dp.message(DESCRIPTION_COMMAND)
async def description(message: Message) -> None:
    await message.answer("Даний бот допоможе знайти вам фільм для перегляд")


@dp.message(FILMS_COMMAND)
async def films(message: Message) -> None:
    data = get_films()
    markup = films_keyboard_markup(films_list=data)
    await message.answer(
        f"Перелік фільмів. Натисніть на назву фільму для отримання деталей.",
        reply_markup=markup
    )


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await bot.set_my_commands(
        [
            FILMS_BOT_COMMAND,
            START_BOT_COMMAND
        ]
    )


if __name__ == "__main__":
    asyncio.run(main())
