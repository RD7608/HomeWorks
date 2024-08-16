import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config

api = config.API

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb_start = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kb_start.row(KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация'))
    kb_start.add(KeyboardButton(text='Купить'))
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb_start)


@dp.message_handler(text='Купить', state=None)
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        await message.answer(f'Название: Продукт {i} | Описание: описание {i} | Цена: {i * 100}')
        # Выводим фото
        with open(f'photos/product{i}.jpg', 'rb') as photo:
            await message.answer_photo(photo)

    kb_catalog = InlineKeyboardMarkup(row_width=4, resize_keyboard=True)
    row = []
    for i in range(1, 5):
        row.append(InlineKeyboardButton(text=f"Продукт {i}", callback_data='product_buying'))
    kb_catalog.row(*row)
    kb_catalog.add(InlineKeyboardButton(text='Назад', callback_data='main_menu'))

    await message.answer('Выберите продукт для покупки :', reply_markup=kb_catalog)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text='main_menu')
async def return_to_main_menu(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer('Вы вернулись в главное меню')
    await start(call.message)


@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):

    kb_calc = InlineKeyboardMarkup(resize_keyboard=True)
    kb_calc.row(InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
                InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas'))
    kb_calc.add(InlineKeyboardButton(text='Назад', callback_data='main_menu'))
    await message.answer('Выберите опцию:', reply_markup=kb_calc)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    formula = "Формула Миффлина-Сан Жеора:\n"
    formula += "Для мужчин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5"
    await call.message.answer(formula)
    await call.answer()


@dp.message_handler(state='*', commands=['cancel'])
async def cancel_input(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Ввод данных отменен. Начнем сначала')
#    await set_age(call=types.CallbackQuery(message=message, id='cancel'))
    await main_menu(message)


@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer(f'Введите свой возраст:\n /cancel - отмена')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer(f'Введите свой рост:\n /cancel - отмена')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer(f'Введите свой вес:\n /cancel - отмена')
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

@dp.message_handler(text='Информация')
async def show_info(message: types.Message):
    info_text = "Бот позволяет рассчитать вашу суточную норму калорий " \
                "по упрощенной формуле Миффлина-Сан Жеора для мужчин. Для этого вам нужно " \
                "ввести ваш возраст, рост и вес." \
                "\nТакже Вы можете приобрести сопутствующие товары."
    await message.answer(info_text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
