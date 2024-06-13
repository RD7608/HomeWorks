import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = sides

        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    @staticmethod
    # def __is_valid_color(self, r, g, b):
    def __is_valid_color(r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)

        self.__radius = radius

    def get_square(self):
        return math.pi * self.__radius ** 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides)

        self.__sides = sides

    def get_volume(self):
        return self.__sides ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверяем изменение цветов
circle1.set_color(55, 66, 77)
cube1.set_color(300, 70, 15)

print(circle1.get_color())
print(cube1.get_color())

# Проверяем изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)
circle1.set_sides(15)

print(cube1.get_sides())
print(circle1.get_sides())

# Проверяем периметр (длину) круга
print(len(circle1))

# Проверяем объем куба
print(cube1.get_volume())
