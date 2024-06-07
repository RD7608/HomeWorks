class Car:
    price = 1000000

    def horse_powers(self):
        return 200


class Nissan(Car):
    price = 1200000

    def horse_powers(self):
        return 250


class Kia(Car):
    price = 900000

    def horse_powers(self):
        return 180


my_car = Car()
print(my_car.price, my_car.horse_powers())


my_car = Nissan()
print(my_car.price, my_car.horse_powers())

my_car = Kia()
print(my_car.price, my_car.horse_powers())


