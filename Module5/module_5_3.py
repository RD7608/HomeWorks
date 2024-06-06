class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


# Пример использования класса Building
building1 = Building(5, "Жилой")
building2 = Building(5, "Офисный")

# Проверка на равенство
print(building1 == building2)  # Выводит False, так как различаются типы зданий

# меняем тип building2 на такой же как building1
building2.buildingType = "Жилой"
print(building1 == building2) # Выводит True, так как количество этажей и тип здания совпадают
