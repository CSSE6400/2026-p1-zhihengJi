from flask import Flask, jsonify, request

# simple in-memory store
TODOS = []
NEXT_ID = 1


def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.get("/todos")
    def list_todos():
        return jsonify(TODOS), 200

    @app.post("/todos")
    def create_todo():
        global NEXT_ID

        data = request.get_json(silent=True) or {}

        if not isinstance(data, dict):
            return jsonify({"error": "invalid json"}), 400

        task = data.get("task")
        if not task:
            return jsonify({"error": "task required"}), 400

        todo = {
            "id": NEXT_ID,
            "task": task
        }

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

    return app