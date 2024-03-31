my_list = ["Яблоко", "Груша", "Вишня", "Банан", "Абрикос", "Киви"]
print("List:", my_list)
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Sublist:", my_list[2:5])
my_list[2] = "Лимон" #заменяем в списке третий элемент "Вишня" на "Лимон"
print("Modified list:", my_list)
print()
my_dict = {"Яблоко": "Apple", "Груша": "Pear", "Вишня": "Cherry", "Банан": "Banana", "Абрикос": "Apricot"}
print("Dictionary:", my_dict)
print("Translation:", my_dict["Вишня"])
my_dict["Киви"] = "Kiwi" #добавляем в словарь ключ "Киви" со значением "Kiwi"
print("Modified dictionary:", my_dict)
