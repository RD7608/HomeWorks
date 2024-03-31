immutable_var = "Строка", 2, True, 4
print("Immutable tuple:", immutable_var)
#immutable_var[1] = 10
#TypeError: 'tuple' object does not support item assignment
#Объект «кортеж» не поддерживает назначение элементов

mutable_list = ["Строка", 2, True, 4]
mutable_list [1] = 10
print("Mutable list:", mutable_list)