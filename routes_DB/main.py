from fastapi import FastAPI
from routers import task, user
app = FastAPI()


@app.get("/")
async def test_main():
    return {"message": "Test route works"}

app.include_router(user.router)
app.include_router(task.router)
