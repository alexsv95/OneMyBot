from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(resize_keyboard= True ,keyboard=[
    [KeyboardButton(text='Стоимость'), KeyboardButton(text='О нас')]
])