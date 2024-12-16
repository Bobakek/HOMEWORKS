from __future__ import annotations
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session
from fastapi import HTTPException, APIRouter, Depends, status
from typing import Annotated
from backend.db_depends import get_db
from schemas import CreateTask, UpdateTask
from models import User
from models import Task


router = APIRouter(prefix='/user', tags=['user'])

@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):

    tasks = db.scalars(select(Task)).all()
    return tasks

# Функция для получения задачи по ID
@router.get("/{task_id}")
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):

    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    return task

# Функция для создания задачи
@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_task(new_task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):

    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    stmt = insert(Task).values(
        title=new_task.title,
        #description=new_task.description,
        user_id=user_id,
    )
    db.execute(stmt)
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}

# Функция для обновления задачи
@router.put("/update/{task_id}")
async def update_task(task_id: int, updated_task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    stmt = update(Task).where(Task.id == task_id).values(
        title=updated_task.title,
        description=updated_task.description,
    )
    result = db.execute(stmt)
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task was not found")
    return {"status_code": status.HTTP_200_OK, "transaction": "Task update is successful!"}

# Функция для удаления задачи
@router.delete("/delete/{task_id}", status_code=status.HTTP_200_OK)
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):

    stmt = delete(Task).where(Task.id == task_id)
    result = db.execute(stmt)
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task was not found")
    return {"status_code": status.HTTP_200_OK, "transaction": "Task deleted successfully!"}
