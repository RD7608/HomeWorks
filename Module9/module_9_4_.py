# Задача "Функциональное разнообразие"
from random import choice


# Вызов ламбда-функции и вывод результата
result = list(map(lambda x, y: [x[i] == y[i] for i in range(min(len(x), len(y)))],
                  'Мама мыла раму', 'Рамена мало было'))
print(result)


# Замыкание: функция для записи в файл
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as f:
            for item in data_set:
                if isinstance(item, str):
                    f.write(item + '\n')
                else:
                    f.write(str(item) + '\n')
    return write_everything


# Пример использования функции get_advanced_writer
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__: класс MysticBall
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


# Пример использования класса MysticBall
first_ball = MysticBall('Да', 'Нет', 'Наверное', "Может быть")
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
