import requests
# Создаем несколько пользователей для тестирования задания 16.5

# 1. username - UrbanUser, age - 24
requests.post("http://127.0.0.1:8000/user/UrbanUser/24")
# 2. username - UrbanTest, age - 22
requests.post("http://127.0.0.1:8000/user/UrbanTest/22")
# 3. username - Capybara, age - 60
requests.post("http://127.0.0.1:8000/user/Capybara/60")
