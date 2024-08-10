from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


api = ''

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

start_kb = ReplyKeyboardMarkup(resize_keyboard=True)



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Рассчитать', 'Информация']
    keyboard.add(*[KeyboardButton(text) for text in buttons])
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=keyboard)


@dp.message_handler(text = 'Рассчитать')
async def main_menu(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
        InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
    ]
    keyboard.add(*buttons)
    await message.answer('Выберите опцию:', reply_markup=keyboard)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula = "Формула Миффлина-Сан Жеора:\n"
    formula += "Для мужчин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5"
    await call.message.answer(formula)
    await call.answer()


@dp.callback_query_handler(text = 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()



@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()

    # Вычисление нормы калорий по упрощенной формуле Миффлина-Сан Жеора для мужчин
    if data['growth'] > 0 and data['weight'] > 0 and data['age'] > 0:
        calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
        await message.answer(f'Ваша норма калорий: {int(calories)} ккал/день')
    else:
        await message.answer('Не удалось рассчитать норму калорий. Проверьте введенные данные.')

    await state.finish()


@dp.message_handler(lambda message: message.text == 'Информация')
async def show_info(message: types.Message):
    info_text = "Бот позволяет рассчитать вашу суточную норму калорий " \
                "по упрощенной формуле Миффлина-Сан Жеора для мужчин. Для этого вам нужно " \
                "ввести ваш возраст, рост и вес."
    await message.answer(info_text)\

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
