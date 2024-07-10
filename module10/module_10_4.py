import threading
import queue
import time
import random

s_print_lock = threading.Lock()


def s_print(*args, **kwargs):
    with s_print_lock:
        print(*args, **kwargs)


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.customer_threads = []
        self.tables = tables
        self.total_service_time = 0
        self.total_customers = 0

    def customer_arrival(self, max_customers):
        for i in range(1, max_customers + 1):
            time.sleep(1)
            customer = Customer(i, self)
            customer_thread = threading.Thread(target=customer.service_customer)
            customer_thread.start()
            self.customer_threads.append(customer_thread)

    def wait_for_customer_threads(self):
        for customer_threads in self.customer_threads:
            customer_threads.join()

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
        self.in_queue = False
        s_print(f"\033[92mПосетитель {number} прибыл\033[0m")

    def service_customer(self):
        served = False
        service_time = random.randint(2, 8)

        while not served:
            for table in self.cafe.tables:
                if not table.is_busy:
                    table.is_busy = True
                    s_print(f"\033[94mПосетитель {self.number} сел за стол {table.number}.\033[0m")
                    time.sleep(service_time)
                    table.is_busy = False
                    s_print(f"\033[1mПосетитель {self.number} покушал и ушёл.\033[0m")
                    self.cafe.update_total_service_time(service_time)
                    self.cafe.update_total_customers()
                    served = True
                    break
            if not served:
                if not self.in_queue:
                    s_print(f"\033[91mПосетитель {self.number} ожидает свободный стол.\033[0m")
                    self.cafe.queue.put(self)
                    self.in_queue = True
#                    time.sleep(0.5)

# Создаем три объекта Table
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

arrival_thread = threading.Thread(target=cafe.customer_arrival(20))
arrival_thread.start()
arrival_thread.join()  # Ожидание завершения потока прихода посетителей

cafe.wait_for_customer_threads()  # Ожидание завершения всех потоков обслуживания посетителей

print(f"\nВсе посетители обслужены.\n")

total_service_time = cafe.total_service_time
total_customers = cafe.total_customers
print(f"Общее время обслуживания {total_customers} посетителей: {total_service_time} секунд")
print(f"Среднее время обслуживания одного посетителя: {total_service_time/total_customers} секунд")
