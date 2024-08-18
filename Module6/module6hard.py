import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self._sides = list(sides)
        if not self.__is_valid_sides(*sides):
            self.create_default_sides()

        self.__color = list(color)
        if not self.__is_valid_color(color[0], color[1], color[2]):
            self.set_color(0, 0, 0)

        self.filled = False

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    @staticmethod
    def __is_valid_color(r, g, b):
        # Проверяем, что все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно)
        if not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int):
            print(f"не корректные значения цвета {r, g, b}")
            return False
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            print(f"не корректные значения цвета  {r, g, b}")
            return False
        return True

    def __is_valid_sides(self, *new_sides):
        # Проверяем, что все стороны целые положительные числа и кол-во новых сторон совпадает с текущим
        for side in new_sides:
            if not isinstance(side, int) or side <= 0:
                print(f"не корректные значения сторон {new_sides}")
                return False

        if len(new_sides) != self.sides_count:
            print(f"Количество сторон {len(new_sides)} {new_sides} не совпадает с количеством сторон фигуры"
                  f" {self.__class__.__name__} ({self.sides_count})")
            return False

        return True

    def get_sides(self):
        return self._sides

    def __len__(self):
        # Возвращаем периметр фигуры
        return sum(self._sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            new_sides = self.fill_sides(list(new_sides), new_sides[0])
        if self.__is_valid_sides(*new_sides):
            self._sides = list(new_sides)
            self.sides_count = len(self._sides)

    def create_default_sides(self):
        self._sides = [1] * self.sides_count
        print(f"Заданы стороны по умолчанию: {self._sides}")

    def fill_sides(self, sides, value):
        while len(sides) < self.sides_count:
            sides.append(value)
        return sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    @property
    def _sides(self):
        return self.__sides

    @_sides.setter
    def _sides(self, value):
        self.__sides = value
        self.__radius = self.set_radius()

    def set_radius(self):
        return self._sides[0] / (math.pi * 2)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return (self._sides[0] ** 2) / (4 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = self.fill_sides(list(sides), sides[0])

        super().__init__(color, *sides)

        if not self.is_possible():
            print(f"Не возможно ли построить треугольник с заданными сторонами {self._sides}")
            self.create_default_sides()

    def get_square(self):
        # Используем формулу Герона для расчета площади треугольника
        a = self._sides[0]
        b = self._sides[1]
        c = self._sides[2]
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def is_possible(self):
        # Проверяем, что сумма длин любых двух сторон больше третьей стороны
        a = self._sides[0]
        b = self._sides[1]
        c = self._sides[2]
        return (a + b > c) and (b + c > a) and (c + a > b)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = self.fill_sides(list(sides), sides[0])

        super().__init__(color, *sides)

        if not self.is_correct():
            print(f"Не возможно построить куб с заданными сторонами {self._sides}")
            self.create_default_sides()

    @property
    def _sides(self):
        return self.__sides

    @_sides.setter
    def _sides(self, value):
        self.__sides = value
        self.__side_length = self.__sides[0]

    def get_volume(self):
        return self.__side_length ** 3

    def is_correct(self):
        if len(self._sides) == self.sides_count:
            return all(side == self._sides[0] for side in self._sides)
        else:
            return True


# Пример использования
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
print(circle1.get_sides(), len(circle1), circle1.get_radius())

cube1 = Cube((222, 35, 130), 6)
print(cube1.get_sides(), len(cube1), cube1.get_volume())

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color(), len(cube1), cube1.get_volume())

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides(), len(cube1), cube1.get_volume())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides(), circle1.get_radius())

# Проверка периметра (круга), это и есть длина
print(len(circle1))


# Проверка объёма (куба)
print(cube1.get_volume(), "\n")


triangle1 = Triangle((200, 200, 100), 3, 4, 5)
print(triangle1.get_sides(), len(triangle1), triangle1.get_square(), "\n")


# Проверка на корректность
circle2 = Circle((200, 200, 100), 10, 15, 6)
print(circle2.get_sides(), circle2.get_radius(), len(circle2), "\n")

triangle2 = Triangle((200, 200, 100), 10, 6)
print(triangle2.get_sides(), len(triangle2), triangle2.get_square(), "\n")

cube2 = Cube((200, 200, 100), 9)
print(cube2.get_sides(), len(cube2), cube2.get_volume(), "\n")

cube2.set_sides(8)
print(cube2.get_sides(), len(cube2), cube2.get_volume(), "\n")

cube2 = Cube((200, 200, 100), 9, 12)
print(cube2.get_sides(), len(cube2), cube2.get_volume(), "\n")


triangle3 = Triangle((200, 200, 100), 1, 2, 10)
print(triangle3.get_sides(), len(triangle3), triangle3.get_square(), "\n")

triangle3 = Triangle((200, 200, 100), 5)
print(triangle3.get_sides(), len(triangle3), triangle3.get_square(), "\n")


cube4 = Cube((200, 200, 100), 9, 12, 23, 34, 45, 56, 67, 78, 89, 90, 123, 123)
print(cube4.get_sides(), len(cube4), cube4.get_volume())
