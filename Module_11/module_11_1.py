# подключаем pandas и matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


# Считываем данные из CSV файла (продажи по годам)
df = pd.read_csv('data.csv')

# Выводим строку за 2023 год
print(df[(df["Год"] == 2023)].head())

# вычисляем среднее значение столбца "Продажи")
mean_value = df['Продажи'].mean()

# Выводим результаты анализа
print(f"\nСреднее значение продаж за {len(df)} лет :", mean_value)
# print(df.describe())


# Построим график продаж по годам с помощью matplotlib
# задаем стиль графика
mpl.style.use(['Solarize_Light2'])

# зададим цвет в зависимости от величины 'Продажи' (>1000 - зел, <500 - красный, иначе - синий)
df['Цвет'] = df['Продажи'].apply(lambda x: 'green' if x > 1000 else ('red' if x < 500 else 'blue'))

# Создаем график
fig, ax = plt.subplots(figsize=(10, 6))
# линейный
plt.plot(df['Год'], df['Продажи'], marker='o', color='green', linestyle='-', linewidth=2)

# столбчатый
bar = plt.bar(df['Год'], df['Продажи'], align='center', alpha=0.5, color=df['Цвет'])

# Добавляем заголовок и подписи к осям
plt.title('Динамика продаж по годам')
plt.xlabel('Год')
plt.ylabel('Продажи тыс. руб.')

# убиравем сетку на графике
plt.grid(False)

# добавляем значения на график в центр столбцов
ax.bar_label(bar, label_type='center')

# Отображаем график
plt.show()
