#import requests

# Отправляем GET-запрос к API
#response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Проверяем статус код ответа
#if response.status_code == 200:
#    data = response.json()  # Преобразуем полученный ответ в формат JSON
#    for post in data:
#        print(f"Post #{post['id']}: {post['title']}")  # Выводим название каждого поста в консоль
#else:
#    print("Ошибка при запросе данных. Статус код:", response.status_code)

import pandas as pd

# Считываем данные из CSV файла
df = pd.read_csv('data.csv')  # Замените 'data.csv' на название вашего файла

# Выводим первые несколько строк данных для предварительного анализа
print("Первые строки данных:")
print(df.head())
print(df.columns.tolist ())

# Выполняем простой анализ данных (например, вычисляем среднее значение числового столбца)
mean_value = df['Продажи'].mean()  # Замените 'column_name' на название столбца, который вы хотите проанализировать

# Выводим результаты анализа
print("\nСреднее значение числового столбца:", mean_value)


import matplotlib.pyplot as plt

# Считываем данные из CSV файла
#df = pd.read_csv('data.csv')  # Убедитесь, что файл содержит столбцы 'Год' и 'Продажи'

# Создаем график линий
#plt.figure(figsize=(10, 6))
#plt.plot(df['Year'], df['Sales'], marker='o', color='b', linestyle='-', linewidth=2)

# Добавляем заголовок и подписи к осям
#plt.title('Динамика продаж по годам')
#plt.xlabel('Year')
#plt.ylabel('Sales')

# Добавляем сетку на график
#plt.grid(True)

# Отображаем график
#plt.show()