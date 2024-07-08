import threading
import queue
import time
import random

s_print_lock = threading.Lock()


# добавил т.к. иногда print выводил в строку по несколько сообщений (добавление flush=True -  не помогло).
def s_print(*a, **b):
    with s_print_lock:
        print(*a, **b)


class Customer:
    def __init__(self, number, cafe):
        self.number = number
        self.cafe = cafe
        s_print("\033[92m" + f"Посетитель {number} прибыл" + "\033[0m")

    def service_customer(self, table):
#        ts = 5  # Задаем время обслуживания посетителя (по заданию)
        ts = random.randint(2, 8)  # Задаем случайное время обслуживания посетителя (более правдподобно)
        time.sleep(ts)  # Ждем обслуживание посетителя
        s_print("\033[1m" + f"Посетитель {self.number} покушал и ушёл." + "\033[0m")
        table.is_busy = False
        s_print("\033[3m" + f"Стол {table.number} освободился, время обслуживания - {ts}" + "\033[0m")
        self.cafe.waiting_message_shown = False


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.service_threads = []
        self.waiting_message_shown = False  # флаг для отслеживания вывода сообщения об ожидании

    def customer_arrival(self, max_customers):
        for i in range(1, max_customers + 1):
            time.sleep(1)  # Приход посетителя каждую секунду
            customer = Customer(i, self)
            self.serve_customer(customer)
            while not self.queue.empty():
                next_customer = self.queue.get()
                self.serve_customer(next_customer)

    def serve_customer(self, customer):
        free_table = next((table for table in self.tables if not table.is_busy), None)
        if free_table:
            free_table.is_busy = True
            s_print("\033[94m" + f"Посетитель {customer.number} сел за стол {free_table.number}." + "\033[0m")
            service_thread = threading.Thread(target=customer.service_customer, args=(free_table,))
            self.service_threads.append(service_thread)
            service_thread.start()
        else:
            self.queue.put(customer)
            if not self.waiting_message_shown and all(table.is_busy for table in self.tables):
                s_print("\033[91m" + f"Посетитель {customer.number} ожидает свободный стол." + "\033[0m")
                time.sleep(0.5)  # Ждем освобождения стола
                self.waiting_message_shown = True

    def wait_for_service_threads(self):
        for service_thread in self.service_threads:
            service_thread.join()


# Создаем три объекта Table
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Создаем объект Cafe
cafe = Cafe(tables)

# Запускаем поток для обслуживания 10 посетителей
arrival_thread = threading.Thread(target=cafe.customer_arrival, args=(20,))
arrival_thread.start()

arrival_thread.join()  # Ожидание завершения потока прихода посетителей
cafe.wait_for_service_threads()  # Ожидание завершения все потоков обслуживания посетителей

print(f"\nВсе посетители обслужены. Конец работы")
