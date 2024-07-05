class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

    def rename(self, newname):
        self.name = newname


# Создаем объект класса Person
person1 = Person("Анатолий", 48)
person1.rename("Гена")

# Выводим информацию о созданном объекте
print(person1)


def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = obj.__class__.__module__ if hasattr(obj, '__class__') else None

    introspection_data = f'\ntype: {obj_type}\nattributes: {attributes}\nmethods: {methods}\nmodule: {module}'

    return introspection_data


# Пример использования:
number_info = introspection_info(person1)
print(number_info)
