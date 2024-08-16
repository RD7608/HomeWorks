from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

import crud_functions
import handlers
import config

api = config.API

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Инициализируем базу данных
crud_functions.initiate_db()

# Регистрация handler'ов
dp.message_handler(commands=['start'])(handlers.start)
dp.message_handler(text='Информация')(handlers.show_info)
dp.message_handler(text='Регистрация', state=None)(handlers.sing_up)
dp.message_handler(state=handlers.RegistrationState.username)(handlers.set_user_name)
dp.message_handler(state=handlers.RegistrationState.email)(handlers.set_user_email)
dp.message_handler(state=handlers.RegistrationState.age)(handlers.set_user_age)
dp.callback_query_handler(text='cancel_registration', state='*')(handlers.cancel_registration)

dp.message_handler(text='Купить')(handlers.get_buying_list)
dp.callback_query_handler(text_startswith='product_buying_')(handlers.send_confirm_message)

dp.message_handler(text='Рассчитать')(handlers.main_menu)
dp.callback_query_handler(text='calories')(handlers.set_age)
dp.message_handler(state=handlers.UserState.age)(handlers.set_growth)
dp.message_handler(state=handlers.UserState.growth)(handlers.set_weight)
dp.message_handler(state=handlers.UserState.weight)(handlers.send_calories)

dp.callback_query_handler(text='formulas')(handlers.get_formulas)

dp.message_handler(content_types=types.ContentTypes.ANY)(handlers.unknown_message)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
