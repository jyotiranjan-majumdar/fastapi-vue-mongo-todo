from fastapi import FastAPI

from app.routes.todo_routes import router

from app.routes.posts import route

from app.config.settings import settings

app = FastAPI()

# app.include_router(router)
app.include_router(route)

@app.get("/info")
def app_info():
    return {
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "debug": settings.DEBUG
    }

@app.get("/")
def  home():
    return "helloe from fastapi"

@app.get("/health")
def health():
    return {"status": "ok"}

