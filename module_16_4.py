from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
class User(BaseModel):
    id: int
    username: str
    age: int

# Список пользователей
users: List[User] = []

# Модель пользователя

@app.get("/users", response_model=List[User])
async def get_users() -> List[User]:
    """Возвращает список всех пользователей."""
    return users

@app.post("/user/{username}/{age}", response_model=User)
async def add_user(username: str, age: int) -> User:
    """Добавляет нового пользователя."""
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: int, username: str, age: int) -> User:
    """Обновляет данные пользователя."""
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int) -> User:
    """Удаляет пользователя из списка."""
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
