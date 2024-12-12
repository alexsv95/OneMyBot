import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config
from config import *
from keyboards import *
import texts

logging.basicConfig(level=logging.INFO)
API = config('TOKEN')
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start(message):
    await message.answer(texts.start, reply_markup= start_kb)

@dp.message_handler(text= 'О нас')
async def price(message):
    await message.answer(texts.about, reply_markup= start_kb)

@dp.message_handler(text = 'Стоимость')
async def info(message):
    await message.answer('Что вас интересует?', reply_markup= catalog_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)