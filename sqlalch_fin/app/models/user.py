from sqlalchemy import Column, Integer, String, insert, select, update, delete
from sqlalchemy.orm import relationship, Session
from app.backend.db import Base
from app.backend.db_depends import get_db
from fastapi import HTTPException, APIRouter, Depends,status
from typing import Annotated
from app.routers.schemas import CreateUser, UpdateUser
from slugify import slugify



router = APIRouter()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    slug = Column(String, unique=True, index=True)

    # Связь с таблицей Task
    tasks = relationship("Task", back_populates="user")

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

# Функция для создания пользователя
@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(new_user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    slug = slugify(new_user.username)
    stmt = insert(User).values(
        username=new_user.username,
        firstname=new_user.firstname,
        lastname=new_user.lastname,
        age=new_user.age,
        slug=slug,
    )
    db.execute(stmt)
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}

# Функция для обновления пользователя
@router.put("/update/{user_id}")
async def update_user(
        user_id: int, updated_user: UpdateUser, db: Annotated[Session, Depends(get_db)]
):
    stmt = update(User).where(User.id == user_id).values(
        firstname=updated_user.firstname,
        lastname=updated_user.lastname,
        age=updated_user.age,
    )
    result = db.execute(stmt)
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User was not found")
    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}

# Функция для удаления пользователя
@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    stmt = delete(User).where(User.id == user_id)
    result = db.execute(stmt)
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User was not found")
    return {"status_code": status.HTTP_200_OK, "transaction": "User deleted successfully!"}