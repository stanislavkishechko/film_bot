import json


def get_films(file_path: str = "data.json", film_id: int | None = None) -> list[dict] | dict:
    with open(file_path, 'r') as file:
        films = json.load(file)
        if film_id and film_id < len(films):
            return films[film_id]
        return films
