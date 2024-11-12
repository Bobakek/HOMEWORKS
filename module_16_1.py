from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main_page() -> dict:
    return {'message': 'Main page'}


@app.get('/user/admin')
async def admin() -> dict:
    return {'message': 'You have logged in as admin'}


@app.get('/user/{user_id}')
async def greet_user(user_id: int) -> dict:
    return {'message': f'Hello, you have logged in as {user_id}'}

@app.get('/user')
async def user(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
