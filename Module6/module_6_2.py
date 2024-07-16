class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 1000000

    def horse_powers(self):
        return 200  # у всех автомобилей 200 лошадиных сил


class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.vehicle_type = "легковой универсал"
        self.price = 1500000  # переопределяем цену для Nissan

    def horse_powers(self):
        return 250  # переопределяем ЛС для Nissan


nissan = Nissan()
print(nissan.vehicle_type, nissan.price)

print("ЛC:", nissan.horse_powers())
