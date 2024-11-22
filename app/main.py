from fastapi import FastAPI
from app.routes.task import router as task_router
from app.routes.user import router as user_router

# Создание приложения
app = FastAPI()

# Главный маршрут
@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

# Подключение маршрутизаторов
app.include_router(task_router)
app.include_router(user_router)
