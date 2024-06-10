def math_func(operation):
    if operation == 'add':
        def add(x, y):
            return x + y
        return add
    elif operation == 'subtract':
        def subtract(x, y):
            return x - y
        return subtract
    elif operation == 'multiply':
        def multiply(x, y):
            return x * y
        return multiply
    elif operation == 'divide':
        def divide(x, y):
            if y == 0:
                return "Ошибка: Деление на ноль"
            else:
                return x / y
        return divide
    else:
        return None


# Пример использования
add_func = math_func('add')
sub_func = math_func('subtract')
mult_func = math_func('multiply')
div_func = math_func('divide')

print(add_func(2, 3))
print(sub_func(2, 3))
print(mult_func(2, 3))
print(div_func(2, 0))


# Использование лямбда-функции для возведения числа в квадрат
square = lambda x: x**2
print(square(4))


# То же самое с использованием def
def square(x):
    return x**2
print(square(4))


# Использование вызываемого объекта для вычисления площади прямоугольника
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


# Пример использования
rectangle = Rect(2, 4)
print(f"Стороны: {rectangle.a}, {rectangle.b}")
print("Площадь:", rectangle())
