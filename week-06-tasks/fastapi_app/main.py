# fastapi_app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json, os

# Initialize app
app = FastAPI(title="To-Do API with File Storage")

# JSON file path
FILE_PATH = os.path.join(os.path.dirname(__file__), "todos.json")

# Pydantic models
class TodoItem(BaseModel):
    task: str

class TodoResponse(BaseModel):
    id: int
    task: str

# Helper functions
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

# Routes
@app.get("/todos", response_model=List[TodoResponse])
def get_todos():
    """Return all todos from JSON file"""
    return load_todos()

@app.post("/todos", response_model=TodoResponse, status_code=201)
def add_todo(item: TodoItem):
    """Add a new todo and save to JSON"""
    todos = load_todos()
    new_todo = {"id": len(todos) + 1, "task": item.task}
    todos.append(new_todo)
    save_todos(todos)
    return new_todo
