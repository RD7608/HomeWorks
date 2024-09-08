def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Вызов с разным числом параметров
print_params()
print_params(10, "привет", False)
print_params(5, c=False)
print_params(b="---------------")

# Проверка
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров
values_list = [55, "СТР", 77.77]
values_dict = {"a": 66, "b": 'AAA', "c": 5555}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [99.99, "СТРОКА"]
print_params(*values_list_2, 42)
