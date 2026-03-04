from flask import Flask, jsonify, request

todos = []
next_id = 1


def create_app():
    app = Flask(__name__)

    @app.route("/api/v1/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"})

    @app.route("/api/v1/todos", methods=["GET"])
    def get_todos():
        return jsonify(todos)

    @app.route("/api/v1/todos", methods=["POST"])
    def create_todo():
        global next_id
        data = request.get_json()

        todo = {
            "id": next_id,
            "title": data.get("title"),
            "completed": False
        }

        todos.append(todo)
        next_id += 1

        return jsonify(todo), 201

    @app.route("/api/v1/todos/<int:todo_id>", methods=["GET"])
    def get_todo(todo_id):
        for todo in todos:
            if todo["id"] == todo_id:
                return jsonify(todo)

        return jsonify({"error": "Not found"}), 404

    @app.route("/api/v1/todos/<int:todo_id>", methods=["PUT"])
    def update_todo(todo_id):
        data = request.get_json()

        for todo in todos:
            if todo["id"] == todo_id:
                todo["title"] = data.get("title", todo["title"])
                todo["completed"] = data.get("completed", todo["completed"])
                return jsonify(todo)

        return jsonify({"error": "Not found"}), 404

    @app.route("/api/v1/todos/<int:todo_id>", methods=["DELETE"])
    def delete_todo(todo_id):
        global todos
        todos = [t for t in todos if t["id"] != todo_id]
        return "", 204

    return app