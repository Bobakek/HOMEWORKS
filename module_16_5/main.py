from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import List, Optional

# Инициализация приложения и шаблонов
app = FastAPI()
templates = Jinja2Templates(directory="templates")


# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int


# Список пользователей
users: List[User] = []


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Главная страница с отображением списка пользователей.
    """
    return templates.TemplateResponse(
        "users.html", {"request": request, "users": users}
    )


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    """
    Отображение данных конкретного пользователя по ID.
    """
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse(
        "users.html", {"request": request, "user": user}
    )


@app.post("/user", response_model=User)
async def add_user(username: str = Form(...), age: int = Form(...)):
    """
    Добавление нового пользователя.
    """
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int, username: str = Form(...), age: int = Form(...)):
    """Обновляет данные пользователя."""
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    """Удаляет пользователя из списка."""
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")