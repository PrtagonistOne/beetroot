import logging
import random

from aiogram import types
from aiogram.dispatcher import FSMContext

from config.loggers import get_message_logger
from .bot import dp
from .states import ExampleForm


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    # [deep_linking]-[BEGIN]
    # Also can be used for another commands while chatting
    split = message.text.split(maxsplit=1)
    token = split[1] if len(split) > 1 else None
    # [deep_linking]-[END]

    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
    if token:
        await message.answer(f'Your token: "{token}"')


# [example_state]-[BEGIN]
# You can use state '*' if you need to handle all states
@dp.message_handler(state='*', commands='cancel')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info(f'Cancelling state {current_state}')

    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['song_list', ])
async def start_state__example_state(message: types.Message):
    # Set current state to this.
    await ExampleForm.SongList.set()
    await message.reply("What's you favourite song?\nSend one song name, or multiple song names separated by comma.\n"
                        "In example: <Believer> or <Believer, Whorehouse Blues, Батарейка> )")


@dp.message_handler(state=ExampleForm.SongList)
async def example_state__process_name(message: types.Message, state: FSMContext):
    """
    Process user song lists
    """
    async with state.proxy() as data:
        songList = message.text.split(',')
        if len(songList) > 1:
            val = '\n'.join([song.strip() for song in songList])
            await message.reply(f"Your songs:\n{val}")
        else:
            data['SongList'] = message.text
            await message.reply(f"Your song: {data['SongList']}")
    await state.finish()


# [example_state]-[END]
@dp.message_handler()
async def echo(message: types.Message):
    logger = get_message_logger()
    logger.info('echo.before')
    await message.answer(message.text)
    await message.reply(message.text)
    logger.info('echo.after')
