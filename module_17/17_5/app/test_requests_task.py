import requests


def create_tasks():
    # Создание заданий (2 для user_id = 1, 2 для user_id = 3)
    response = requests.post('http://127.0.0.1:8000/task/create', params={'user_id': 1},
                             json={'title': 'FirstTask', 'content': 'Content1', 'priority': 0})
    print(1, response.json())

    response = requests.post('http://127.0.0.1:8000/task/create', params={'user_id': 1},
                             json={'title': 'SecondTask', 'content': 'Content2', 'priority': 2})
    print(2, response.json())

    response = requests.post('http://127.0.0.1:8000/task/create', params={'user_id': 3},
                             json={'title': 'ThirdTask', 'content': 'Content3', 'priority': 4})
    print(3, response.json())

    response = requests.post('http://127.0.0.1:8000/task/create', params={'user_id': 3},
                             json={'title': 'FourthTask', 'content': 'Content4', 'priority': 6})
    print(4, response.json())


def delete_task_and_user():
    # удаление задания 3
    response = requests.delete('http://127.0.0.1:8000/task/delete', params={'task_id': 3})
    print(5, response.json())

    # удаление пользователя 1
    response = requests.delete('http://127.0.0.1:8000/user/delete', params={'user_id': 1})
    print(6, response.json())


def task_error():
    # получение несуществующего задания
    response = requests.get('http://127.0.0.1:8000/task/task_id', params={'task_id': 100})
    print(7, response.json())

    # удаление несуществующего задания
    response = requests.delete('http://127.0.0.1:8000/task/delete', params={'task_id': 100})
    print(8, response.json())

    # создание задания с уже существующим идентификатором
    response = requests.post('http://127.0.0.1:8000/task/create', params={'user_id': 3},
                             json={'title': 'FourthTask', 'content': 'Content4', 'priority': 8})
    print(9, response.json())

    # создание задания для не существующего пользователя
    response = requests.post('http://127.0.0.1:8000/task/create', params={'user_id': 100},
                             json={'title': 'FiftyTask', 'content': 'Content5', 'priority': 0})
    print(10, response.json())


if __name__ == '__main__':
    # удаление всех заданий
    response = requests.delete('http://127.0.0.1:8000/task/delete-all')
    print(0, response.json())

    create_tasks()
    delete_task_and_user()
    task_error()
