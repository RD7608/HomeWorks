def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    if not isinstance(numbers, (list, tuple)):
        print('В numbers записан некорректный тип данных')
        return None

    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы : {num}')

    return result, incorrect_data


def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple, str)):
        print('В numbers записан некорректный тип данных')
        return None

    if isinstance(numbers, str):
        numbers = list(numbers)

    try:
        sum_result, incorrect_data = personal_sum(numbers)
        n = len(numbers)
        if n - incorrect_data > 0:
            avg = sum_result / (n - incorrect_data)
        else:
            avg = sum_result / n
        return avg
    except ZeroDivisionError:
        print('numbers пустая')
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
print(f'Результат 5: {calculate_average([])}')
