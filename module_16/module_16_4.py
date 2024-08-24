from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import Annotated, List


class User(BaseModel):
    id: int = None
    username: str
    age: int = None


app = FastAPI()

users = []


@app.get("/users")
async def get_users() -> List[User]:
    return users


@app.get("/users/{user_id}")
async def get_user(user_id: Annotated[int, Path(description="Enter User ID", example=1, ge=1, le=100)]
                    ) -> User:
    try:
        user = next(filter(lambda x: x.id == user_id, users))
    except StopIteration:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(description="Enter username", example="UrbanUser", min_length=5, max_length=20)],
        age: Annotated[int, Path(description="Enter age", example=24, ge=18, le=120)]
) -> User:
    if users:
        new_id = max([user.id for user in users]) + 1
    else:
        new_id = 1
    if new_id > 100:
        raise HTTPException(status_code=400, detail=f"User not created. ID {new_id} is too big")
    user = User(id=new_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(description="Enter User ID", example=1, ge=1, le=100)],
        username: Annotated[str, Path(description="Enter username", example="UrbanProfi", min_length=5, max_length=20)],
        age: Annotated[int, Path(description="Enter age", example=28, ge=18, le=120)]
) -> User:
    try:
        user = next(filter(lambda x: x.id == user_id, users))
    except StopIteration:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    user.username = username
    user.age = age
    return user


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(description="Enter User ID", example=2, ge=1, le=100)]
) -> User:
    try:
        user = next(filter(lambda x: x.id == user_id, users))
    except StopIteration:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    users.remove(user)
    return user


@app.delete("/")
async def delete_all_user() -> str:
    users.clear()
    return "Users cleared"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("module_16_4:app", host="127.0.0.1", port=8000, reload=True)
