import requests

# Отправляем GET-запрос к API
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Проверяем статус код ответа
if response.status_code == 200:
    data = response.json()  # Преобразуем полученный ответ в формат JSON
    for post in data:
        print(f"Post #{post['id']}: {post['title']}")  # Выводим название каждого поста в консоль
else:
    print("Ошибка при запросе данных. Статус код:", response.status_code)
