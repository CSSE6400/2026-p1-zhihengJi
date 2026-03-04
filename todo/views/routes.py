from flask import jsonify, request

TEST_TODO = {
    "id": 1,
    "title": "Watch CSSE6400 Lecture",
    "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
    "completed": True,
    "deadline_at": "2026-02-27T18:00:00",
    "created_at": "2026-02-20T14:00:00",
    "updated_at": "2026-02-20T14:00:00"
}


def register_routes(app):

    @app.get("/api/v1/health")
    def health():
        return jsonify({"status": "ok"}), 200


    @app.get("/api/v1/todos")
    def get_todos():
        return jsonify([TEST_TODO]), 200


    @app.get("/api/v1/todos/<int:todo_id>")
    def get_todo(todo_id):
        return jsonify(TEST_TODO), 200


    @app.post("/api/v1/todos")
    def create_todo():
        return jsonify(TEST_TODO), 201


    @app.put("/api/v1/todos/<int:todo_id>")
    def update_todo(todo_id):
        return jsonify(TEST_TODO), 200


    @app.delete("/api/v1/todos/<int:todo_id>")
    def delete_todo(todo_id):
        return jsonify(TEST_TODO), 200