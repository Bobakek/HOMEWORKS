from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException, APIRouter, Depends, status
from typing import Annotated
from models import User
from models import Task
from backend.db_depends import get_db



router = APIRouter(prefix='/task', tags=['task'])


# Функция для получения всех пользователей
@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):

    users = db.scalars(select(User)).all()
    return users

# Функция для получения пользователя по ID
@router.get("/{user_id}")
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):

    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user

# Функция для получения всех задач пользователя
@router.get("/{user_id}/tasks")
async def tasks_by_user_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    return tasks

# Функция для удаления пользователя
@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.delete(user)  # Связанные задачи будут удалены каскадно
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User and all related tasks deleted successfully!"}