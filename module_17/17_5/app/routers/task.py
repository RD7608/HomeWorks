from fastapi import APIRouter, Depends, status, HTTPException
from slugify import slugify
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import Task, User
from schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from sqlalchemy import exc

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task:
        return task
    else:
        raise HTTPException(status_code=404,
                            detail="Task was not found")


@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, task: CreateTask):
    try:
        user = db.scalar(select(User).where(User.id == user_id))
        if user:
            db.execute(insert(Task).values(title=task.title,
                                           content=task.content,
                                           priority=task.priority,
                                           user_id=user_id,
                                           slug=slugify(task.title)))

            db.commit()
            return {"status_code": status.HTTP_201_CREATED,
                    "transaction": "Successful"}
        else:
            raise HTTPException(status_code=404,
                                detail="User was not found to create task")
    except exc.IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=409,
                            detail=f"Task already exists for user")

    except exc.SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500,
                            detail=f"Database error: {str(e)}")


@router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, task: UpdateTask):
    existing_task = db.scalar(select(Task).where(Task.id == task_id))
    if existing_task:
        db.execute(update(Task).where(Task.id == task_id).values(title=task.title,
                                                                 content=task.content,
                                                                 priority=task.priority))
        db.commit()
        return {"status_code": status.HTTP_200_OK,
                "transaction": "Task update is successful!"}
    else:
        raise HTTPException(status_code=404,
                            detail="Task was not found to update")


@router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    existing_task = db.scalar(select(Task).where(Task.id == task_id))
    if existing_task:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {"status_code": status.HTTP_200_OK,
                "transaction": "Task delete is successful!"}
    else:
        raise HTTPException(status_code=404,
                            detail="Task was not found to delete")


@router.delete("/delete-all")
async def delete_all_tasks(db: Annotated[Session, Depends(get_db)]):
    try:
        db.execute(delete(Task))
        db.commit()
        return {"status_code": status.HTTP_200_OK,
                "transaction": "All tasks deleted successfully"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,
                            detail=f"Error during task delete: {str(e)}")
