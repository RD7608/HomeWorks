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

    return result, incorrect_data


def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple)):
        print('В numbers записан некорректный тип данных')
        return None

    try:
        sum_result, _ = personal_sum(numbers)
        avg = sum_result / len(numbers)
        return avg
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average(["1, 2, 3"])}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
