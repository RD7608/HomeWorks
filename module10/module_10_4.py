import threading
import time
import queue
import random

s_print_lock = threading.Lock()
def s_print(*a, **b):
    with s_print_lock:
        print(*a, **b)


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer:
    def __init__(self, number):
        self.number = number


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for customer_number in range(1, 11):
            customer = Customer(customer_number)
            self.queue.put(customer)
            s_print(f"Посетитель номер {customer_number} прибыл.")
            time.sleep(1)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                s_print(f"Посетитель номер {customer.number} сел за стол {table.number}. (начало обслуживания)")
#                time.sleep(5)  # время обслуживания 5 секунд
                time.sleep(random.randint(2, 5))  # для большей наглядности
                table.is_busy = False
                s_print(f"Посетитель номер {customer.number} покушал и ушёл. (конец обслуживания)")
                return
        s_print(f"Посетитель номер {customer.number} ожидает свободный стол. (помещение в очередь)")


def serve_customers(cafe):
    while True:
          customer = cafe.queue.get()
          cafe.serve_customer(customer)
          cafe.queue.task_done()
          print(cafe.queue.empty())

if __name__ == "__main__":
    table1 = Table(1)
    table2 = Table(2)
    table3 = Table(3)
    tables = [table1, table2, table3]

    cafe = Cafe(tables)

    # Создаем поток для обслуживания посетителей из очереди
    customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()

    # Создаем потоки для обслуживания посетителей за столами
#    worker_threads = []
#    for _ in range(len(tables)):
#        worker_thread = threading.Thread(target=serve_customers, args=(cafe,))
#        worker_thread.start()
#        worker_threads.append(worker_thread)


# Ждем завершения потока, добавляющего посетителей в очередь
    customer_arrival_thread.join()


# Ждем завершения всех потоков, обслуживающих посетителей за столами
#for worker_thread in worker_threads:
#    worker_thread.join()
#    print ( "Все посетители обслужены. Завершение работы кафе." )

