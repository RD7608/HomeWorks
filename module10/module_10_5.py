from multiprocessing import Process, Manager


class WarehouseManager:
    def __init__(self):
        self.data = Manager().dict()

    def process_request(self, request):
        product, action, amount = request

        if action == "receipt":
            if product in self.data:
                self.data[product] += amount
            else:
                self.data[product] = amount
        elif action == "shipment":
            if product in self.data and self.data[product] >= amount:
                self.data[product] -= amount

    def process_requests(self, requests):
        processes = []
        for request in requests:
            p = Process(target=self.process_request, args=(request,))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()


# Пример использования
if __name__ == '__main__':
    manager = WarehouseManager()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.process_requests(requests)

    sorted_data = dict(sorted(manager.data.items()))
    print(sorted_data)
