import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

from decouple import config


TOKEN = config("BOT_TOKEN")

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer(
        f"Вітаю, {message.from_user.full_name}! Я допоможу знайти тобі фільм."
    )


@dp.message(Command("description"))
async def description(message: Message) -> None:
    await message.answer("Даний бот допоможе знайти вам фільм для перегляд")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
