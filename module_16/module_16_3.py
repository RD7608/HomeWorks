from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()


users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
def get_users():
    return users


@app.post("/user/{username}/{age}")
def create_user(
    username: Annotated[str, Path(description="Enter username", example="UrbanUser", min_length=5, max_length=20)],
    age: Annotated[int, Path(description="Enter age", example=24, ge=18, le=120)]
):
    new_id = str(len(users) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[int, Path(description="Enter User ID", example=1, ge=1, le=100)],
    username: Annotated[str, Path(description="Enter username", example="UrbanProfi", min_length=5, max_length=20)],
    age: Annotated[int, Path(description="Enter age", example=28, ge=18, le=120)]
):
    user_id = str(user_id)
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
def delete_user(
    user_id: Annotated[int, Path(description="Enter User ID", example=2, ge=1, le=100)]
):
    user_id = str(user_id)
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    del users[user_id]
    return f"User {user_id} has been deleted"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("module_16_3:app", host="127.0.0.1", port=8000, reload=True)
