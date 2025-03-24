from aiogram.fsm.state import StatesGroup, State


class FilmForm(StatesGroup):
    name = State()
    description = State()
    rating = State()
    genre = State()
    actors = State()
    poster = State()
