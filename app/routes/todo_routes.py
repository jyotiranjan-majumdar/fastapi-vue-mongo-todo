from fastapi import APIRouter

router = APIRouter()

@router.get("/todo")
def todo():
    return {"todo": 1}

@router.get("/todo/{todo_id}")
def get_todo(todo_id: str):
    return {"todo_id": todo_id}

@router.get("/todos")
def get_todos(status: str = "todo", priority: str = "high"):
    return {"status": status}


from typing import Optional

@router.get("/todos_opt")
def get_todos(status: Optional[str] = None):
    return {"status": status}

# Request Body

@router.post("/todo_body")
def create_todo(todo: dict):
    return {
        "received": todo
    }


from app.schemas.todo_schema import TodoCreate

@router.post("/todo_schema")
def create_todo(todo: TodoCreate):
    return {
        "title": todo.title,
        "completed": todo.completed
    }