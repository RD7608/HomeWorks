from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboards import *
from crud_functions import *

api = ''

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Инициализируем базу данных
    initiate_db()

    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb_start)


@dp.message_handler(text='Купить', state=None)
async def get_buying_list(message: types.Message):

    # Получаем список продуктов из базы данных
    products = get_all_products()

    for product in products:
        # Выводим информацию по продукту
        await message.answer(f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}")
        # Выводим фото продукта
        with open(product[4], 'rb') as photo:
            await message.answer_photo(photo)

    # Создаем клавиатуру с продуктами
    kb_products = types.InlineKeyboardMarkup()
    buttons = [types.InlineKeyboardButton(text=product[1], callback_data=f'product_buying_{product[0]}') for product in
               products]
    kb_products.add(*buttons)
    # Отправляем сообщение с клавиатурой
    await message.answer('Выберите продукт для покупки', reply_markup=kb_products)


@dp.callback_query_handler(text_startswith='product_buying_')
async def send_confirm_message(call: types.CallbackQuery):
    # Получаем информацию о продукте из базы данных
    product_id = int(call.data.split('_')[-1])
    product_info = get_product_by_id(product_id)

    if product_info:
        product_name, product_price = product_info
        await call.message.answer(f'Вы успешно приобрели продукт: {product_name} за {product_price} руб.')
    else:
        await call.message.answer('Произошла ошибка при получении информации о продукте.')
    await call.answer()


@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=kb_calc)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    formula = "Формула Миффлина-Сан Жеора:\n"
    formula += "Для мужчин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5"
    await call.message.answer(formula)
    await call.answer()


@dp.callback_query_handler(text='calories')
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


@dp.message_handler(text='Информация')
async def show_info(message: types.Message):
    info_text = "Бот позволяет рассчитать вашу суточную норму калорий " \
                "по упрощенной формуле Миффлина-Сан Жеора для мужчин. Для этого вам нужно " \
                "ввести ваш возраст, рост и вес." \
                "\nТакже Вы можете приобрести сопутствующие товары."
    await message.answer(info_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
