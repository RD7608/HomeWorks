import requests

# 1. GET /users
response = requests.get("http://127.0.0.1:8000/users")
print(1, response.json())
# 2. POST /user/{username}/{age} (username - UrbanUser, age - 24)
response = requests.post("http://127.0.0.1:8000/user/UrbanUser/24")
print(2, response.text)
# 3. POST /user/{username}/{age} (username - UrbanTest, age - 36)
response = requests.post("http://127.0.0.1:8000/user/UrbanTest/36")
print(3, response.text)
# 4. POST /user/{username}/{age} (username - Admin, age - 42)
response = requests.post("http://127.0.0.1:8000/user/Admin/42")
print(4, response.text)
# 5. PUT /user/{user_id}/{username}/{age} (user_id - 1, username - UrbanProfi, age - 28)
response = requests.put("http://127.0.0.1:8000/user/1/UrbanProfi/28")
print(5, response.text)
# 6. DELETE /user/{user_id} (user_id - 2)
response = requests.delete("http://127.0.0.1:8000/user/2")
print(6, response.text)
# 7. GET /users
response = requests.get("http://127.0.0.1:8000/users")
print(7, response.json())
# 8. DELETE /user/{user_id} (user_id - 2)
response = requests.delete("http://127.0.0.1:8000/user/2")
print(8, response.text)

