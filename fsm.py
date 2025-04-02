from aiogram.fsm.state import StatesGroup, State


class FilmForm(StatesGroup):
    name = State()
    description = State()
    rating = State()
    genre = State()
    actors = State()
    poster = State()

class MovieStates(StatesGroup):
    search_query = State()
    filter_criteria = State()
    filter_by_actor = State()
    delete_query = State()
    edit_query = State()
    edit_description = State()
