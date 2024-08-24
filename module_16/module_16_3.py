from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[str, Path(description="Enter username", example="UrbanUser", min_length=5, max_length=20)],
    age: Annotated[int, Path(description="Enter age", example=24, ge=18, le=120)]
) -> str:
    if users:
        new_id = str(int(max(users, key=int)) + 1)
    else:
        new_id = '1'
    if int(new_id) > 100:
        return f"User not created. ID {new_id} is too big"
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[int, Path(description="Enter User ID", example=1, ge=1, le=100)],
    username: Annotated[str, Path(description="Enter username", example="UrbanProfi", min_length=5, max_length=20)],
    age: Annotated[int, Path(description="Enter age", example=28, ge=18, le=120)]
) -> str:
    user_id = str(user_id)
    if user_id not in users:
        return f"User {user_id} not found"
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[int, Path(description="Enter User ID", example=2, ge=1, le=100)]
) -> str:
    user_id = str(user_id)
    if user_id not in users:
        return f"User {user_id} not found"
    users.pop(user_id)
    return f"User {user_id} has been deleted"


@app.delete("/")
async def delete_all_user() -> str:
    users.clear()
    return f"Users cleared"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("module_16_3:app", host="127.0.0.1", port=8000, reload=True)
