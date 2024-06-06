class Building:
    total = 0

    def __init__(self):
        Building.total += 1


# Создание 40 объектов класса Building
b = {i: Building() for i in range(1, 41)}

# Вывод на экран созданных объектов класса Building
for i in range(1, 41):
    print(i, b[i])

# Вывод на экран количества созданных объектов класса Building
print(Building.total)
