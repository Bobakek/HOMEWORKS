from fastapi import FastAPI, HTTPException, Path

app = FastAPI()

# Словарь пользователей
users = {"1": "Имя: Example, возраст: 18"}

@app.get("/users")
async def get_users() -> dict:
    """Возвращает всех пользователей."""
    return users

@app.post("/user/{username}/{age}")
async def add_user(
    username: str = Path(..., min_length=3, max_length=50, description="Имя пользователя"),
    age: int = Path(..., ge=1, le=120, description="Возраст пользователя")
) -> str:
    """Добавляет нового пользователя."""
    if users:
        # Находим максимальный ключ и добавляем +1
        new_id = str(max(map(int, users.keys())) + 1)
    else:
        new_id = "1"
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: str = Path(..., description="ID пользователя"),
    username: str = Path(..., min_length=3, max_length=50, description="Новое имя пользователя"),
    age: int = Path(..., ge=1, le=120, description="Новый возраст пользователя")
) -> str:
    """Обновляет данные пользователя."""
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    raise HTTPException(status_code=404, detail=f"User {user_id} does not exist")

@app.delete("/user/{user_id}")
async def delete_user(
    user_id: str = Path(..., description="ID пользователя для удаления")
) -> str:
    """Удаляет пользователя по user_id."""
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    raise HTTPException(status_code=404, detail=f"User {user_id} does not exist")

