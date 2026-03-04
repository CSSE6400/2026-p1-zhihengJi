from fastapi import FastAPI

app = FastAPI()

todos = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def create_todo(todo: dict):
    todos.append(todo)
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if 0 <= todo_id < len(todos):
        return todos.pop(todo_id)
    return {"error": "not found"}