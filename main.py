import asyncio


from commands import FILMS_COMMAND, START_COMMAND, DESCRIPTION_COMMAND, FILM_CREATE_COMMAND, BOT_COMMANDS
from data import get_films, add_film

from aiogram import Bot, Dispatcher, html
from aiogram.fsm.context import FSMContext
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery, URLInputFile, ReplyKeyboardRemove

from decouple import config

from fsm import FilmForm
from keyboards import films_keyboard_markup, FilmCallback
from models import Film

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


@dp.callback_query(FilmCallback.filter())
async def callb_film(callback: CallbackQuery, callback_data: FilmCallback) -> None:
    film_id = callback_data.id
    film_data = get_films(film_id=film_id)
    film = Film(**film_data)

    text = f"Фільм: {film.name}\n" \
           f"Опис: {film.description}\n" \
           f"Рейтинг: {film.rating}\n" \
           f"Жанр: {film.genre}\n" \
           f"Актори: {', '.join(film.actors)}\n"

    await callback.message.answer_photo(
        caption=text,
        photo=URLInputFile(
            film.poster,
            filename=f"{film.name}_poster.{film.poster.split('.')[-1]}"
        )
    )

@dp.message(FILM_CREATE_COMMAND)
async def film_create(message: Message, state: FSMContext) -> None:
   await state.set_state(FilmForm.name)
   await message.answer(
       f"Введіть назву фільму.",
       reply_markup=ReplyKeyboardRemove(),
   )


@dp.message(FilmForm.name)
async def film_name(message: Message, state: FSMContext) -> None:
   await state.update_data(name=message.text)
   await state.set_state(FilmForm.description)
   await message.answer(
       f"Введіть опис фільму.",
       reply_markup=ReplyKeyboardRemove(),
   )


@dp.message(FilmForm.description)
async def film_description(message: Message, state: FSMContext) -> None:
   await state.update_data(description=message.text)
   await state.set_state(FilmForm.rating)
   await message.answer(
       f"Вкажіть рейтинг фільму від 0 до 10.",
       reply_markup=ReplyKeyboardRemove(),
   )


@dp.message(FilmForm.rating)
async def film_rating(message: Message, state: FSMContext) -> None:
   await state.update_data(rating=float(message.text))
   await state.set_state(FilmForm.genre)
   await message.answer(
       f"Введіть жанр фільму.",
       reply_markup=ReplyKeyboardRemove(),
   )


@dp.message(FilmForm.genre)
async def film_genre(message: Message, state: FSMContext) -> None:
   await state.update_data(genre=message.text)
   await state.set_state(FilmForm.actors)
   await message.answer(
       text=f"Введіть акторів фільму через роздільник ', '\n"
       + html.bold("Обов'язкова кома та відступ після неї."),
       reply_markup=ReplyKeyboardRemove(),
   )


@dp.message(FilmForm.actors)
async def film_actors(message: Message, state: FSMContext) -> None:
   await state.update_data(actors=[x for x in message.text.split(", ")])
   await state.set_state(FilmForm.poster)
   await message.answer(
       f"Введіть посилання на постер фільму.",
       reply_markup=ReplyKeyboardRemove(),
   )


@dp.message(FilmForm.poster)
async def film_poster(message: Message, state: FSMContext) -> None:
   data = await state.update_data(poster=message.text)
   film = Film(**data)
   add_film(film.model_dump())
   await state.clear()
   await message.answer(
       f"Фільм {film.name} успішно додано!",
       reply_markup=ReplyKeyboardRemove(),
   )


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await bot.set_my_commands(BOT_COMMANDS)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
