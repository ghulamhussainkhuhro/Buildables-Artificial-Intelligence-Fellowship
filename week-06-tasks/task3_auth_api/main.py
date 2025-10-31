from fastapi import FastAPI, HTTPException, Header, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import os, json

# --- Load .env from project root ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
load_dotenv(os.path.join(ROOT_DIR, ".env"))

API_KEY = os.getenv("API_KEY")
FILE_PATH = os.path.join(os.path.dirname(__file__), "todos.json")

app = FastAPI(title="Task 3: FastAPI with Auth & DELETE")

# --- Pydantic Models ---
class TodoItem(BaseModel):
    task: str

class TodoResponse(BaseModel):
    id: int
    task: str


# --- Helper Functions ---
def load_todos():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_todos(todos):
    with open(FILE_PATH, "w") as f:
        json.dump(todos, f, indent=4)


# --- API Key Check Dependency ---
def verify_api_key(x_api_key: Optional[str] = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
    return True


# --- Routes ---
@app.get("/todos", response_model=List[TodoResponse])
def get_todos():
    """Return all todos"""
    return load_todos()


@app.post("/todos", response_model=TodoResponse, status_code=201, dependencies=[Depends(verify_api_key)])
def add_todo(item: TodoItem):
    """Add new todo (auth required)"""
    todos = load_todos()
    new_todo = {"id": len(todos) + 1, "task": item.task}
    todos.append(new_todo)
    save_todos(todos)
    return new_todo


@app.delete("/todos/{todo_id}", status_code=200, dependencies=[Depends(verify_api_key)])
def delete_todo(todo_id: int):
    """Delete todo by ID (auth required)"""
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            save_todos(todos)
            return {"status": "success", "message": f"Todo {todo_id} deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
