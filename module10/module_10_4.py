# переделал с помощью использования пула потоков ThreadPoolExecutor из модуля concurrent.futures.
import concurrent.futures
import threading
import time
import random


s_print_lock = threading.Lock()


# добавил т.к. иногда print выводил в строку по несколько сообщений (добавление flush=True -  не помогло).
def s_print(*a, **b):
    with s_print_lock:
        print(*a, **b)


class Cafe:
    def __init__(self, tables):
        self.queue = []
        self.tables = tables
        self.total_service_time = 0
        self.total_customers = 0

    # Метод submit создает задачу для обслуживания каждого посетителя, а ThreadPoolExecutor автоматически
    # управляет выполнением этих задач в пуле потоков.
    def customer_arrival(self, max_customers):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for i in range(1, max_customers + 1):
                time.sleep(1)
                customer = Customer(i, self)
                executor.submit(customer.service_customer)

    def update_total_service_time(self, service_time):
        self.total_service_time += service_time

    def update_total_customers(self):
        self.total_customers += 1


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer:
    def __init__(self, number, cafe):
        self.number = number
        self.cafe = cafe
        self.in_queue = False  # признак ожидания в очереди
        s_print("\033[92m" + f"Посетитель {number} прибыл" + "\033[0m")

    def service_customer(self):
        served = False
        service_time = random.randint(2, 8)  # время обслуживания посетителя (для правдоподобности)
        # service_time = 5  # время обслуживания посетителя (по заданию)
        while not served:
            for table in self.cafe.tables:
                if not table.is_busy:
                    table.is_busy = True
                    s_print("\033[94m" + f"Посетитель {self.number} сел за стол {table.number}." + "\033[0m")
                    time.sleep(service_time)  # Ждем обслуживание посетителя
                    table.is_busy = False
                    # mess_o = "\033[3m" + f"\nСтол {table.number} освободился, время обслуживания - {service_time}" + "\033[0m"
                    s_print("\033[1m" + f"Посетитель {self.number} покушал и ушёл." + "\033[0m")
                    self.cafe.update_total_service_time(service_time)
                    self.cafe.update_total_customers()
                    served = True
                    break
            if not served:
                if not self.in_queue:  # проверяем ожидает ли посетитель в очереди
                    s_print("\033[91m" + f"Посетитель {self.number} ожидает свободный стол." + "\033[0m")
                    self.cafe.queue.append(self)  # добавляем посетителя в очередь
                    self.in_queue = True  # изменяем признак ожидания посетителя
                    time.sleep(0.5)


# Создаем три объекта Table
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Создаем объект Cafe
cafe = Cafe(tables)

#  запускаем процесс обслуживания 20 посетителей
cafe.customer_arrival(20)

print(f"\nВсе посетители обслужены.\n")

#  выводим справочную информацию
total_service_time = cafe.total_service_time
total_customers = cafe.total_customers
print(f"Общее время обслуживания {total_customers} посетителей: {total_service_time} секунд")
print(f"Среднее время обслуживания одного посетителя: {total_service_time/total_customers} секунд")
