from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher import FSMContext
import requests
from keyboards import *
from crud_functions import *

api = ' '

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Инициализируем базу данных
initiate_db()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb_start)


@dp.message_handler(text='Регистрация', state=None)
async def sing_up(message):
    await message.answer("Для начала регистрации введите имя пользователя (только латинский алфавит),")
    await message.answer("для прерывания регистрации введите слово 'отмена' на любом из этапов.")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if message.text.lower() == 'отмена':
        await state.finish()
        await message.answer("Регистрация отменена.")
        return

    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя")
        return
    if not is_valid_username(username):
        await message.answer("Неверное имя пользователя, введите другое имя")
        return

    async with state.proxy() as data:
        data['username'] = username
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    if message.text.lower() == 'отмена':
        await state.finish()
        await message.answer("Регистрация отменена.")
        return

    email = message.text
    if not is_valid_email(email):
        await message.answer("Неверный email, введите другой")
        return
    async with state.proxy() as data:
        data['email'] = email
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    if message.text.lower() == 'отмена':
        await state.finish()
        await message.answer("Регистрация отменена.")
        return

    try:
        age = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста, введите число.")
        return
    if age <= 0 or age > 120:
        await message.answer("Неверный возраст, введите > 0 и < 120.")
        return

    async with state.proxy() as data:
        data['age'] = age
    add_user(data['username'], data['email'], data['age'])
    await message.answer("Регистрация успешно завершена!")
    await state.finish()


@dp.message_handler(text='Купить', state=None)
async def get_buying_list(message):

    # Получаем список продуктов из базы данных
    products = get_all_products()

    for product in products:

        # Выводим информацию по продукту
        await message.answer(f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}")
        product_photo = product[4]
        # Проверяем, существует ли фотография

        if product_photo:
            try:
                # Проверяем, можно ли загрузить фото по URL-адресу
                response = requests.get(product_photo)
                if response.status_code == 200:
                    # Отправляем изображение
                    await message.answer_photo(photo=product_photo)
                else:
                    await message.answer(f"Фото продукта отсутствует 1")
            except requests.exceptions.RequestException:
                await message.answer(f"Фото продукта отсутствует 2")
        else:
            await message.answer(f"Фото продукта отсутствует")

    # Создаем клавиатуру с продуктами
    kb_products = types.InlineKeyboardMarkup()
    buttons = [types.InlineKeyboardButton(text=product[1], callback_data=f'product_buying_{product[0]}') for product in
               products]
    kb_products.add(*buttons)
    # Отправляем сообщение с клавиатурой
    await message.answer('Выберите продукт для покупки', reply_markup=kb_products)


@dp.callback_query_handler(text_startswith='product_buying_')
async def send_confirm_message(call):
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
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_calc)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    formula = "Формула Миффлина-Сан Жеора:\n"
    formula += "Для мужчин: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5"
    await call.message.answer(formula)
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
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
async def show_info(message):
    info_text = "Бот позволяет рассчитать вашу суточную норму калорий " \
                "по упрощенной формуле Миффлина-Сан Жеора для мужчин. Для этого вам нужно " \
                "ввести ваш возраст, рост и вес." \
                "\nТакже Вы можете приобрести сопутствующие товары."
    await message.answer(info_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
