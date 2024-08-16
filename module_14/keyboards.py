from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура для главного меню
kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')

        ],
        [
            KeyboardButton(text='Купить')
        ],
        [
            KeyboardButton(text='Регистрация')
        ]
    ], resize_keyboard=True
)

# Клавиатура для калькулятора
kb_calc = InlineKeyboardMarkup(
    inline_keyboard=[
         [
             InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
             InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
         ]
    ]
)

# Клавиатура для каталога
kb_catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
        ]
    ]
)

# Кнопка "Отмена"
kb_cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Отмена', callback_data='cancel_registration')
        ]
    ],
    resize_keyboard=True
)


def get_kb_products(products):
    kb_products = InlineKeyboardMarkup()
    buttons = [InlineKeyboardButton(text=product[1], callback_data=f'product_buying_{product[0]}') for product in products]
    kb_products.add(*buttons)
    return kb_products
