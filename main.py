import threading
import time
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 5:
            time.sleep(1)
            print(f"Посетитель номер {customer_number} прибыл.")
            customer = Customer(customer_number, self)
            customer.start()
            customer_number += 1

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.number} сел за стол {table.number}.")
                time.sleep(5)  # Время обслуживания 5 секунд
                table.is_busy = False
                print(f"Посетитель номер {customer.number} покушал и ушёл.")
                break
        else:
            self.queue.put(customer)
            print(f"Посетитель номер {customer.number} ожидает свободный стол.")


class Customer(threading.Thread):
    def __init__(self, number, cafe):
        threading.Thread.__init__(self)
        self.number = number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
