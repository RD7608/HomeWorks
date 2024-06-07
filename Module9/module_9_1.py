# Входные данные
numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

# Фильтрация нечётных чисел и возведение их в квадрат
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))

print(result)  # Вывод результата