from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


@app.get("/")
async def main_page():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin_page():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user_page(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)]):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def user_info(
    username: Annotated[str, Path(description="Enter username", example="UrbanUser", min_length=5, max_length=20)],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("module_16_2:app", host="127.0.0.1", port=8000, reload=True)
