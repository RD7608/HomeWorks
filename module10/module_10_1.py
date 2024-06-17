from threading import Thread, Lock
from time import sleep


s_print_lock = Lock()

# добавил т.к. иногда print выводил в строку по 2 символа, добавление flush=True -  не помогало.
def s_print(*a, **b):
    with s_print_lock:
        print(*a, **b)


def print_num():
    for i in range(1, 11):
        s_print(i)
        sleep(1)


def print_let():
    for c in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'):
        s_print(c)
        sleep(1)


thread1 = Thread(target=print_num)
thread2 = Thread(target=print_let)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
