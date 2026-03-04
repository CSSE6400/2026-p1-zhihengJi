from flask import jsonify, request

TODOS = []
NEXT_ID = 1


def register_routes(app):

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/todos")
    def list_todos():
        return jsonify(TODOS)

    @app.post("/todos")
    def create_todo():
        global NEXT_ID

        data = request.get_json(silent=True) or {}
        task = data.get("task")

        if not task:
            return jsonify({"error": "task required"}), 400

        todo = {"id": NEXT_ID, "task": task}
        TODOS.append(todo)
        NEXT_ID += 1

        return jsonify(todo), 201

    @app.delete("/todos/<int:todo_id>")
    def delete_todo(todo_id):
        global TODOS

        for todo in TODOS:
            if todo["id"] == todo_id:
                TODOS.remove(todo)
                return jsonify(todo), 200

        return jsonify({"error": "not found"}), 404