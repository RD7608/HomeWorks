import requests

# удаление всех пользователей и заданий
response = requests.delete('http://127.0.0.1:8000/user/delete-all')
print(0, response.json())

# Создание пользователей
response = requests.post('http://127.0.0.1:8000/user/create',
                         json={'username': 'user1', 'firstname': 'Pasha', 'lastname': 'Technique', 'age': 40})
print(1, response.json())

response = requests.post('http://127.0.0.1:8000/user/create',
                         json={'username': 'user2', 'firstname': 'Roza', 'lastname': 'Syabitova', 'age': 62})
print(2, response.json())

response = requests.post('http://127.0.0.1:8000/user/create',
                         json={'username': 'user3', 'firstname': 'Alex', 'lastname': 'Unknown', 'age': 25})
print(3, response.json())

# изменение пользователей
response = requests.put('http://127.0.0.1:8000/user/update', params={'user_id': 3},
                        json={"firstname": "Bear", "lastname": "Grylls", "age": 50})
print(4, response.json())

# удаление
response = requests.delete('http://127.0.0.1:8000/user/delete', params={'user_id': 2})
print(5, response.json())


# проверка на исключения
# удаляем несуществующего пользователя
response = requests.delete('http://127.0.0.1:8000/user/delete', params={'user_id': 10})
print(6, response.json())

# обновляем несуществующего пользователя
response = requests.put('http://127.0.0.1:8000/user/update', params={'user_id': 10},
                        json={"firstname": "Bear", "lastname": "Grylls", "age": 50})
print(7, response.json())

# создаем пользователя с уже существующим именем
response = requests.post('http://127.0.0.1:8000/user/create',
                         json={'username': 'user1', 'firstname': 'Pasha', 'lastname': 'Technique', 'age': 40})
print(8, response.json())

