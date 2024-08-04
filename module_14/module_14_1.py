import sqlite3

# Создание файла базы данных и подключение к нему
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Проверка, если база данных не пустая, то очистить ее
cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Users'")
if cursor.fetchone()[0] > 0:
    cursor.execute("DELETE FROM Users")

# Создание таблицы Users, если она еще не создана
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
""")

# Заполнение таблицы 10 записями
users = [
    ("User1", "example1@gmail.com", 10, 1000),
    ("User2", "example2@gmail.com", 20, 1000),
    ("User3", "example3@gmail.com", 30, 1000),
    ("User4", "example4@gmail.com", 40, 1000),
    ("User5", "example5@gmail.com", 50, 1000),
    ("User6", "example6@gmail.com", 60, 1000),
    ("User7", "example7@gmail.com", 70, 1000),
    ("User8", "example8@gmail.com", 80, 1000),
    ("User9", "example9@gmail.com", 90, 1000),
    ("User10", "example10@gmail.com", 100, 1000)
]
cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", users)

# Обновление баланса у каждой 2ой записи, начиная с 1ой
for i, user in enumerate(users):
    if (i + 1) % 2 == 1:
        cursor.execute("UPDATE Users SET balance = 500 WHERE username = ?", (user[0],))

# Удаление каждой 3ей записи, начиная с 1ой
for i, user in enumerate(users):
    if (i + 1) % 3 == 1:
        cursor.execute("DELETE FROM Users WHERE username = ?", (user[0],))

# Выборка всех записей, где возраст не равен 60 и их вывод
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
for row in cursor.fetchall():
    username, email, age, balance = row
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
