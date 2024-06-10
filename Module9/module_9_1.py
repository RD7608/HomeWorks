# функция для фильтрации нечетных чисел
def is_odd(x):
    return x % 2 != 0

# функция для возведения числа в квадрат
def square(x):
    return x ** 2

# Входные данные
numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

# Фильтрация нечетных чисел и возведение их в квадрат
filtered_numbers = filter(is_odd, numbers)
result = map(square, filtered_numbers)

# Преобразование результата в список
result_list = list(result)

print(result_list)