from aiogram.dispatcher.filters.state import StatesGroup, State


class ExampleForm(StatesGroup):
    SongList = State()
