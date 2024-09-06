from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import User
from models import Task
from schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from sqlalchemy import exc
from slugify import slugify


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    """
    Получает список всех пользователей.

    Возвращает:
        Список объектов пользователей.
    """
    try:
        users = db.scalars(select(User)).all()
        return users

    except exc.SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500,
                            detail=f"Database error: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,
                            detail=f"User creation failed with error: {str(e)}")


@router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    """
      Получает пользователя по его ID.

      Аргументы:
          user_id (int): ID пользователя.

      Возвращает:
          Объект пользователя
    """
    user = db.scalar(select(User).where(User.id == user_id))
    if user:
        return user
    else:
        raise HTTPException(status_code=404,
                            detail="User was not found")


@router.get("/user_id/tasks")
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    """
          Возвращает список задач, связанных с указанным идентификатором пользователя.

          Аргументы:
              user_id (int): ID пользователя.

          Возвращает:
              Cписок задач, связанных с указанным идентификатором пользователя.
        """
    user = db.scalar(select(User).where(User.id == user_id))
    if user:
        tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
        if tasks:
            return tasks
        else:
            raise HTTPException(status_code=404,
                                detail="No tasks found for user")
    else:
        raise HTTPException(status_code=404,
                            detail="User was not found")


@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], user: CreateUser):
    """
    Создает нового пользователя.

    Аргументы:
        username (str): Имя пользователя.
        firstname (str): Имя.
        lastname (str): Фамилия.
        age (int): Возраст.

    Возвращает:
        Словарь {"status_code": 201, "transaction": "Successful"})
    """
    try:
        db.execute(insert(User).values(username=user.username,
                                       firstname=user.firstname,
                                       lastname=user.lastname,
                                       age=user.age,
                                       slug=slugify(user.username)))
        db.commit()
        return {"status_code": status.HTTP_201_CREATED,
                "transaction": "Successful"}

    except exc.IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=409,
                            detail=f"User {user.username} already exists")
    except exc.SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500,
                            detail=f"Database error: {str(e)}")


@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, user: UpdateUser):
    """
    Обновляет пользователя по ID.

    Аргументы:
        user_id (int): ID пользователя.
        firstname (str): Имя.
        lastname (str): Фамилия.
        age (int): Возраст.

    Возвращает:
        Словарь {"status_code": 200, "transaction": "User update is successful!"})
    """
    existing_user = db.scalar(select(User).where(User.id == user_id))
    if existing_user:
        db.execute(update(User).where(User.id == user_id).values(firstname=user.firstname,
                                                                 lastname=user.lastname,
                                                                 age=user.age))
        db.commit()
        return {"status_code": status.HTTP_200_OK,
                "transaction": "User update is successful!"}
    else:
        raise HTTPException(status_code=404,
                            detail="User was not found")


@router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    """
       Удаляет пользователя по ID и все связанные с ним задачи.

       Аргументы:
           user_id (int): ID пользователя.

       Возвращает:
           Словарь {"status_code": 200, "transaction": "User and associated tasks deleted successfully!"})
    """
    existing_user = db.scalar(select(User).where(User.id == user_id))
    if existing_user:
        db.execute(delete(Task).where(Task.user_id == user_id))
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {"status_code": status.HTTP_200_OK,
                "transaction": "User and associated tasks deleted successfully!"}
    else:
        raise HTTPException(status_code=404,
                            detail="User was not found")


@router.delete("/delete-all")
async def delete_all_users(db: Annotated[Session, Depends(get_db)]):
    """
       Удаляет всех пользователей и все задачи.

       Возвращает:
           Словарь {"status_code": 200, "transaction": "All users and tasks deleted successfully"})
    """
    try:
        db.execute(delete(Task))
        db.execute(delete(User))
        db.commit()
        return {"status_code": status.HTTP_200_OK,
                "transaction": "All users and tasks deleted successfully"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,
                            detail=f"Error during user delete: {str(e)}")
