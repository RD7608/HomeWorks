import threading
import time
import queue


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
        for customer_number in range(1, 5):
            customer = Customer(customer_number)
            self.queue.put(customer)
            print(f"Посетитель номер {customer_number} прибыл.")
            time.sleep(1)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.number} сел за стол {table.number}.")
                time.sleep(5)  # время обслуживания 5 секунд
                table.is_busy = False
                print(f"Посетитель номер {customer.number} покушал и ушёл.")
                return
        print(f"Посетитель номер {customer.number} ожидает свободный стол. (помещение в очередь)")

    def register_customer(self, customer):
        self.queue.put(customer)
        print(f"Посетитель {customer} добавлен в очередь")

    def start_serving_customers(self):
        while not self.queue.empty():
            customer = self.queue.get()
            self.serve_customer(customer)

    def print_table_status(self):
        for table in self.tables:
            status = "занят" if table.is_busy else "свободен"
            print(f"Стол {table.number}: {status}")


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()


time.sleep(2)  # Подождем немного перед запуском обслуживания

cafe.start_serving_customers()
cafe.print_table_status()
