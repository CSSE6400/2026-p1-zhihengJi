@app.post("/api/v1/todos")
def create_todo():
    global NEXT_ID

    data = request.get_json(silent=True)

    if not data or "title" not in data:
        return jsonify({"error": "title required"}), 400

    todo = {
        "id": NEXT_ID,
        "title": data["title"]
    }

    TODOS.append(todo)
    NEXT_ID += 1

    return jsonify(todo), 201