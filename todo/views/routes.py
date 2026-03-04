from flask import jsonify, request

TODOS = []
NEXT_ID = 1


def register_routes(app):

    @app.get("/api/v1/health")
    def health():
        return jsonify({"status": "ok"}), 200


    @app.get("/api/v1/todos")
    def list_todos():
        return jsonify(TODOS), 200


    @app.post("/api/v1/todos")
    def create_todo():
        global NEXT_ID

        data = request.get_json(silent=True)

        if not data or "task" not in data:
            return jsonify({"error": "task required"}), 400

        todo = {
            "id": NEXT_ID,
            "task": data["task"]
        }

        TODOS.append(todo)
        NEXT_ID += 1

        return jsonify(todo), 201


    @app.delete("/api/v1/todos/<int:todo_id>")
    def delete_todo(todo_id):
        global TODOS

        for todo in TODOS:
            if todo["id"] == todo_id:
                TODOS.remove(todo)
                return jsonify(todo), 200

        return jsonify({"error": "not found"}), 404