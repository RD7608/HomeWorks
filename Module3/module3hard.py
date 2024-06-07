def calculate_structure_sum(data_structure):
    def calculate(item):
        if isinstance(item, int):
            return item
        elif isinstance(item, str):
            return len(item)
        elif isinstance(item, (list, tuple, set)):
            return sum(calculate(subitem) for subitem in item)
        elif isinstance(item, dict):
            return sum(calculate(key) + calculate(value) for key, value in item.items())
        else:
            return 0

    return sum(calculate(item) for item in data_structure)


data_structure = [
   [1, 2, 3],
   {'a': 4, 'b': 5},
   (6, {'cube': 7, 'drum': 8}),
   "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
