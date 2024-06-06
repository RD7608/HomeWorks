class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print("Количество этажей изменено на:", self.numberOfFloors)


# Пример использования класса
my_house = House()
print("Изначальное количество этажей:", my_house.numberOfFloors)

my_house.setNewNumberOfFloors(2)
my_house.setNewNumberOfFloors(5)
