from fastapi import APIRouter

router = APIRouter()

@router.get("/todo")
def todo():
    return {"todo": 1}

@router.get("/todo/{todo_id}")
def get_todo(todo_id: int):
    return {"todo_id": todo_id}

