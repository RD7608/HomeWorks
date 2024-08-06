import sqlite3

# Создание файла базы данных и подключение к нему
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

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

# если база данных не пустая, то очистить ее
cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Users'")
if cursor.fetchone()[0] > 0:
    cursor.execute("DELETE FROM Users")

# Заполнение таблицы 10 записями
users = [
    ("User{}".format(i+1), "example{0}@gmail.com".format(i+1), (i+1)*10, 1000)
    for i in range(10)
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
