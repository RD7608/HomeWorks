import sqlite3
import re


def initiate_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Products
                (id INTEGER PRIMARY KEY, title TEXT NOT NULL, description TEXT, price INTEGER NOT NULL, photo TEXT)''')
    conn.commit()

    c.execute('''CREATE TABLE IF NOT EXISTS Users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT NOT NULL,
                      email TEXT NOT NULL,
                      age INTEGER NOT NULL,
                      balance INTEGER NOT NULL)''')
    conn.commit()

    conn.close()


def get_all_products():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Products")
    products = c.fetchall()
    conn.close()
    return products


def get_product_by_id(product_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT title, price FROM products WHERE id = ?", (product_id,))
    product_info = c.fetchone()
    conn.close()
    return product_info


def add_user(username, email, age):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Добавляем нового пользователя с балансом 1000
    c.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)", (username, email, age))

    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Проверяем, есть ли пользователь с таким именем в таблице
    c.execute("SELECT COUNT(*) FROM Users WHERE username = ?", (username,))
    count = c.fetchone()[0]

    conn.close()
    return count > 0


def is_valid_username(username):
    # Проверяем, что имя пользователя состоит только из латинских букв
    pattern = r'^[a-zA-Z]+$'
    return bool(re.match(pattern, username))


def is_valid_email(email):
    """
    Проверяет, является ли переданная строка корректным email-адресом.
    :param email: Строка, содержащая email-адрес.
    :return: True, если email-адрес корректен, иначе False.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

