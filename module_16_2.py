from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def main_page() -> dict:
    return {'message': 'Main page'}

@app.get('/user/admin')
async def admin() -> dict:
    return {'message': 'You have logged in as admin'}

@app.get('/user/{user_id}')
async def greet_user(user_id: int = Path(..., ge=1, le=100, description='Enter User ID', examples={"default": 1})) -> dict:
    return {'message': f'Hello, you have logged in as {user_id}'}

@app.get('/user/{username}/{age}')
async def user(
    username: Annotated[str, Path(..., min_length=5, max_length=20, description='Enter username', examples={"default": "UrbanUser"})],
    age: Annotated[int, Path(..., ge=18, le=120, description='Enter your age', examples={"default": 24})]
) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
