import requests
from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated, List
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Создаем объект Jinja2Templates с папкой templates
templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    id: int = None
    username: str
    age: int = None


users = []


@app.get("/")
def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/users/{user_id}")
def get_user(request: Request, user_id: int = Path(..., ge=1, title="The ID of the user to get")):
    try:
        user = next(filter(lambda x: x.id == user_id, users))
        return templates.TemplateResponse("users.html", {"request": request, "user": user})
    except StopIteration:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")


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


# Для добавления пользователей:
    # 1. username - UrbanUser, age - 24
    # 2. username - UrbanTest, age - 22
    # 3. username - Capybara, age - 60
# используйте add_users_16_5.py


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("module_16_5:app", host="127.0.0.1", port=8000)
