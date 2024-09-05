from fastapi import APIRouter

from schemas import CreateTask, UpdateTask

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks():
    pass


@router.get("/task_id")
async def task_by_id(task_id: int):
    pass


@router.post("/create")
async def create_task(task: CreateTask):
    pass


@router.put("/update")
async def update_task(task_id: int, task: UpdateTask):
    pass


@router.delete("/delete")
async def delete_task(task_id: int):
    pass
