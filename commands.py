from aiogram.filters import Command
from aiogram.types import BotCommand

FILMS_COMMAND = Command('films')
START_COMMAND = Command('start')
DESCRIPTION_COMMAND = Command('description')
FILM_CREATE_COMMAND = Command('create_film')

BOT_COMMANDS = [
    BotCommand(command='films', description="Перегляд списку фільмів"),
    BotCommand(command='start', description="Почати розмову"),
    BotCommand(command="create_film", description="Додати новий фільм")
]
