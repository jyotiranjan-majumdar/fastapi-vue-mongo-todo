from fastapi import FastAPI

from app.routes.todo_routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def  home():
    return "helloe from fastapi"

@app.get("/health")
def health():
    return {"status": "ok"}

