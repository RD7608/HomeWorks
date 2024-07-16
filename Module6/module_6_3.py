class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


# Пример работы программы
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()


#  в Примечании к заданию п.2 указано:
#  Заметьте, что Pegasus издаёт звук "I train, eat, sleep, and repeat",
#  т.к. по порядку сначала идёт наследование от Horse, а после от Eagle.
#
#  но т.к. первым идет Horse, то звук получился 'Frrr'
print('\n', p1.__class__.__mro__)