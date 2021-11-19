from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import settings

# Иницилализация бота
bot = Bot(token=settings.telegram_token)

# Создание хранилища для даних State
storage = MemoryStorage()

# Инициализация диспетчера
dp = Dispatcher(bot, storage=storage)
