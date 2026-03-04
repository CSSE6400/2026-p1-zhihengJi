from flask import Flask, jsonify, request

# in-memory store (simple)
_TODOS = []
_NEXT_ID = 1

def create_app():
    app = Flask(__name__)

    @app.get("/api/v1/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.get("/api/v1/todos")
    def list_todos():
        return jsonify(_TODOS), 200

    @app.post("/api/v1/todos")
    def create_todo():
        global _NEXT_ID
        data = request.get_json(silent=True) or {}

        # very tolerant: accept any json object, but must be a dict
        if not isinstance(data, dict):
            return jsonify({"error": "invalid json"}), 400

        todo = {"id": _NEXT_ID, **data}
        _NEXT_ID += 1
        _TODOS.append(todo)
        return jsonify(todo), 201

    @app.delete("/api/v1/todos/<int:todo_id>")
    def delete_todo(todo_id: int):
        idx = next((i for i, t in enumerate(_TODOS) if t.get("id") == todo_id), None)
        if idx is None:
            return jsonify({"error": "not found"}), 404
        deleted = _TODOS.pop(idx)
        return jsonify(deleted), 200

    return app