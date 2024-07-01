# подключаем pandas и matplotlib
import pandas as pd
import matplotlib.pyplot as plt


# Считываем данные из CSV файла (продажи по годам)
df = pd.read_csv('data.csv')

# Выводим строку за 2023 год
print(df[(df["Год"] == 2023)].head())

# вычисляем среднее значение столбца "Продажи")
mean_value = df['Продажи'].mean()

# Выводим результаты анализа
print(f"\nСреднее значение продаж за {len(df)} лет :", mean_value)


# Построим график продаж по годам с помощью matplotlib
# Создаем график линий
plt.figure(figsize=(10, 6))
plt.plot(df['Год'], df['Продажи'], marker='o', color='b', linestyle='-', linewidth=2)

# Добавляем заголовок и подписи к осям
plt.title('Динамика продаж по годам')
plt.xlabel('Год')
plt.ylabel('Продажи тыс. руб.')

# Добавляем сетку на график
plt.grid(True)

# Отображаем график
plt.show()
