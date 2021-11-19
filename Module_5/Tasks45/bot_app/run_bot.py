from aiogram.utils import executor

from .bot import dp


def run_bot() -> None:
    executor.start_polling(dp, skip_updates=True)