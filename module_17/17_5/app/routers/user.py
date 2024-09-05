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
    users = db.scalars(select(User)).all()
    return users


@router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user:
        return user
    else:
        raise HTTPException(status_code=404,
                            detail="User was not found")


@router.get("/user_id/tasks")
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
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
    existing_user = db.scalar(select(User).where(User.id == user_id))
    if existing_user:
        db.execute(update(User).where(User.id == user_id).values(firstname=user.firstname,
                                                                 lastname=user.lastname,
                                                                 age=user.age))
        db.commit()
        return {"status_code": status.HTTP_200_OK,
                "transaction": f"User ID {user_id} update is successful!"}
    else:
        raise HTTPException(status_code=404,
                            detail="User was not found")


@router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
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
    try:
        db.execute(delete(User))
        db.commit()
        return {"status_code": status.HTTP_200_OK,
                "transaction": "All users deleted successfully"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,
                            detail=f"Error during user delete: {str(e)}")
