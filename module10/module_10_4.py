import threading
import queue
import time
# import random

s_print_lock = threading.Lock()


def s_print(*args, **kwargs):
    with s_print_lock:
        print(*args, **kwargs)


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.total_service_time = 0
        self.total_customers = 0
        self.start_time = time.time()

    def customer_arrival(self, max_customers=20):
        for i in range(1, max_customers + 1):
            customer = Customer(i)  # Создаем нового посетителя
            self.queue.put(customer)  # Добавляем посетителя в очередь
            if self.free_tables() is None:  # Если нет свободных столов, то выводим сообщение об ожидании
                s_print(f"\033[93mПосетитель {customer.number} ожидает свободный стол\033[0m")

            serve_customer_thread = threading.Thread(target=cafe.serve_customers)
            serve_customer_thread.start()  # Запускаем поток для обслуживания посетителя
            time.sleep(1)

    def serve_customers(self):
        while not self.queue.empty():
            table = self.free_tables()
            if table is None:
                break  # Если нет свободных столов, то выходим из цикла
            customer = self.queue.get()  # Берем первого посетителя из очереди
            service_time = 5  # random. randint(2, 8)
            table.serve_customer(customer, service_time)  # Садим посетителя за стол
            self.queue.task_done()

            self.update_total_service_time(customer.service_time)
            self.update_total_customers()

    def wait_for_customers(self):
        self.queue.join()

    def free_tables(self):
        for table in self.tables:
            if not table.is_busy:
                return table

    def update_total_service_time(self, service_time):
        self.total_service_time += service_time

    def update_total_customers(self):
        self.total_customers += 1

    def get_average_service_time(self):
        if self.total_customers > 0:
            return self.total_service_time / self.total_customers
        else:
            return 0


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
        self.lock = threading.Lock()

    def serve_customer(self, customer, service_time):
        with self.lock:
            if not self.is_busy:
                self.is_busy = True
                s_print(f"\033[94mПосетитель {customer.number} сел за стол {self.number}.\033[0m")
                time.sleep(service_time)
                self.is_busy = False
                customer.set_service_time()
                s_print(f"\033[1mПосетитель {customer.number} покушал и ушёл.\033[0m",
                        f"\n\033[3mСтол {self.number} свободен,", "Время обслуживания", customer.service_time, "секунд\033[0m")


class Customer:
    def __init__(self, number):
        self.number = number
        self.start_time = time.time()
        self.service_time = 0
        print(f"\033[92mПосетитель {number} прибыл\033[0m")

    def set_service_time(self):
        self.service_time = round(time.time() - self.start_time, 2)
        return self.service_time


# Создаем три объекта Table
# table1 = Table(1)
# table2 = Table(2)
# table3 = Table(17_3)
# tables = [table1, table2, table3]

# Создаем столики в кафе
tables = []
for i in range(1, 4):
    table = Table(i)
    tables.append(table)


cafe = Cafe(tables)  # Создаем кафе

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()  # Запускаем поток прибытия посетителей

customer_arrival_thread.join()  # Ожидаем прибытия всех посетителей

cafe.wait_for_customers()  # Ожидаем обслуживания всех посетителей

print(f"\nВсе посетители обслужены.\n")

# Выводим общее время обслуживания и среднее время обслуживания
total_service_time = cafe.total_service_time
average_service_time = cafe.get_average_service_time()
print(f"Обслужено посетителей: {cafe.total_customers}, время обслуживания {total_service_time:.2f} секунд")
print(f"Среднее время обслуживания: {average_service_time:.2f} секунд")
