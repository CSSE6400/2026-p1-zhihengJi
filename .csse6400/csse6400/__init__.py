from flask import Flask, request

def create_app():
    app = Flask(__name__)

    # --- In-memory store (Week1 stub) ---
    todos = {}
    next_id = 1

    @app.get("/api/v1/health")
    def health():
        return {"status": "ok"}

    @app.get("/api/v1/todos")
    def list_todos():
        #  todo
        return list(todos.values())

    @app.post("/api/v1/todos")
    def create_todo():
        nonlocal next_id
        data = request.get_json(silent=True) or {}

        # title 
        title = data.get("title")
        if not isinstance(title, str) or not title.strip():
            return {"error": "title is required"}, 400

        todo = {
            "id": next_id,
            "title": title.strip(),
            "done": bool(data.get("done", False)),
        }
        todos[next_id] = todo
        next_id += 1
        return todo, 201

    @app.get("/api/v1/todos/<int:todo_id>")
    def get_todo(todo_id: int):
        todo = todos.get(todo_id)
        if not todo:
            return {"error": "not found"}, 404
        return todo

    @app.put("/api/v1/todos/<int:todo_id>")
    def update_todo(todo_id: int):
        todo = todos.get(todo_id)
        if not todo:
            return {"error": "not found"}, 404

        data = request.get_json(silent=True) or {}
        if "title" in data:
            if not isinstance(data["title"], str) or not data["title"].strip():
                return {"error": "title is required"}, 400
            todo["title"] = data["title"].strip()
        if "done" in data:
            todo["done"] = bool(data["done"])

        todos[todo_id] = todo
        return todo

    @app.delete("/api/v1/todos/<int:todo_id>")
    def delete_todo(todo_id: int):
        if todo_id not in todos:
            return {"error": "not found"}, 404
        del todos[todo_id]
        return "", 204

    return app