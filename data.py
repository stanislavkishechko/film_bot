import logging
import json


logger = logging.getLogger(__file__)

def get_films(file_path: str = "data.json", film_id: int | None = None) -> list[dict] | dict:
    with open(file_path, 'r') as file:
        films = json.load(file)
        if film_id and film_id < len(films):
            return films[film_id]
        return films

def add_film(film: dict, file_path: str = "data.json") -> None:
    films = get_films(file_path, film_id=None)
    if films:
        films.append(film)
        with open(file_path, 'w') as file:
            json.dump(films, file, indent=4, ensure_ascii=False)

def edit_film(film_data: dict, film_name: str, file_path: str = "data.json") -> None:
    films = get_films(file_path, film_id=None)
    if films:
        for film in films:
            if film_name == film['name']:
                film['description'] = film_data['description']
                break
        with open(file_path, 'w') as file:
            json.dump(films, file, indent=4, ensure_ascii=False)

def delete_film(film: dict, file_path: str = "data.json") -> None:
    films = get_films(file_path, film_id=None)
    if films:
        films.remove(film)
        with open(file_path, 'w') as file:
            json.dump(films, file, indent=4, ensure_ascii=False)
