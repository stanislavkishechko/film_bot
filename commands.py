from aiogram.filters import Command
from aiogram.types import BotCommand

FILMS_COMMAND = Command('films')
START_COMMAND = Command('start')
DESCRIPTION_COMMAND = Command('description')


FILMS_BOT_COMMAND = BotCommand(command='films', description="Перегляд списку фільмів")
START_BOT_COMMAND = BotCommand(command='start', description="Почати розмову")
