# подключаем numpy, pandas и matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# создаем массив на 10 лет
y = 2014
years = np.arange(y, y+10, 1)

# добавляем к годам продажи (здесь случайные значения в диапазоне)
sales_dict = {"Год": years,
              "Продажи": np.random.randint(400, 1300, size=len(years))}

# создаем таблицу из продаж
sales = pd.DataFrame(sales_dict)

# записываем таблицу в файл
sales.to_csv('data.csv', index=False)

# Считываем данные из CSV файла (продажи по годам)
df = pd.read_csv('data.csv')

# Выводим строку за 2023 год
print(df[(df["Год"] == 2023)].head())

# вычисляем среднее значение столбца "Продажи")
mean_value = df['Продажи'].mean()

# Выводим результат
print(f"\nСреднее значение продаж за {len(df)} лет :", mean_value)

# print(df.describe())


# Построим график продаж по годам с помощью matplotlib
# задаем стиль графика
mpl.style.use(['Solarize_Light2'])

# зададим цвет в зависимости от величины в колонке 'Продажи' (>1000 - зел, <500 - красный, иначе - синий)
df['Цвет'] = df['Продажи'].apply(lambda x: 'green' if x > 1000 else ('red' if x < 500 else 'blue'))

# Создаем график
fig, ax = plt.subplots(figsize=(10, 6))
# линейный
plt.plot(df['Год'], df['Продажи'], marker='o', color='black', linestyle='-', linewidth=2)
# столбчатый
bar = plt.bar(df['Год'], df['Продажи'], width=0.6, align='center', alpha=0.5, color=df['Цвет'])

# Добавляем заголовок и подписи к осям
plt.title('Динамика продаж по годам')
plt.xlabel('Год')
plt.ylabel('Продажи тыс. руб.')

# убираем сетку на графике
plt.grid(False)

# добавляем значения 'Продажи' на график в центр столбцов
ax.bar_label(bar, label_type='center')

# настраиваем подписи столбцов
plt.xticks(years, fontsize=14, rotation=60)

# Отображаем график
plt.show()
