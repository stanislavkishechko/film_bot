from aiogram.filters import Command
from aiogram.types import BotCommand

FILMS_COMMAND = Command('films')
START_COMMAND = Command('start')
DESCRIPTION_COMMAND = Command('description')
FILM_CREATE_COMMAND = Command('create_film')
FILM_SEARCH_COMMAND = Command('search_film')
FILM_SEARCH_BY_ACTOR_COMMAND = Command('search_by_actor')
FILM_FILTER_COMMAND = Command('filter_film')
FILM_DELETE_COMMAND = Command('delete_film')
FILM_EDIT_COMMAND = Command('edit_film')

BOT_COMMANDS = [
    BotCommand(command='start', description="Почати розмову"),
    BotCommand(command='description', description="Опис можливостей бота"),
    BotCommand(command='films', description="Перегляд списку фільмів"),
    BotCommand(command="create_film", description="Додати новий фільм"),
    BotCommand(command="search_film", description="Пошук фільму за назвою"),
    BotCommand(command="filter_film", description="Фільтрація фільмів за назвою"),
    BotCommand(command="delete_film", description="Видалення фільму"),
    BotCommand(command="edit_film", description="Зміна фільму"),
    BotCommand(command="search_by_actor", description="Пошук фільмів за актором"),
]
