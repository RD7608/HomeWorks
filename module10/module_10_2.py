import threading
import time

s_print_lock = threading.Lock()


def s_print(*a, **b):
    with s_print_lock:
        print(*a, **b)


class Knight(threading.Thread):
    def __init__(self, name, skill):
        super(Knight, self).__init__()
        self.name = name
        self.skill = skill

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies_left = 100
        day = 1
        while enemies_left > 0:
            enemies_left -= self.skill
            time.sleep(1)  # Задержка в 1 секунду
            s_print(f"{self.name}, сражается {day} день(дня)..., осталось {enemies_left} воинов.")
            day += 1

        print(f"{self.name} одержал победу спустя {day - 1} дней!")


# Создание рыцарей
knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)

# Запуск потоков
knight1.start()
knight2.start()

# Ожидание окончания битвы
knight1.join()
knight2.join()

print("Все битвы закончились!")
