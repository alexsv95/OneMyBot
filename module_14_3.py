from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton ,InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config

key = config('TOKEN')
bot = Bot(token=key)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb_reply = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard= [[KeyboardButton(text= 'Рассчитать'), KeyboardButton(text='Информация')],
                                          [KeyboardButton(text= 'Купить')]
                                          ])

kb_inline = InlineKeyboardMarkup(resize_keyboard=True)
button_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inline.add(button_1, button_2)

kb_inline_buy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text= 'Витамин А', callback_data= 'product_buying'),
     InlineKeyboardButton(text='Витамин B', callback_data= 'product_buying'),
     InlineKeyboardButton(text='Витамин C', callback_data= 'product_buying'),
     InlineKeyboardButton(text='Витамин D', callback_data= 'product_buying')]
])


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb_reply)

@dp.message_handler(text= 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup= kb_inline)

@dp.callback_query_handler(text= 'formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5
    await message.answer(f'Ваша норма калорий {calories}')
    await state.finish()

@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        with open(f"images/img{i}.jpg", "rb") as img:
            await message.answer_photo(img, f"Название: Product{i} | Описание: описание {i} | Цена: {i*100}")
    await message.answer("Выберите продукт для покупки", reply_markup = kb_inline_buy)

@dp.callback_query_handler(text= 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
