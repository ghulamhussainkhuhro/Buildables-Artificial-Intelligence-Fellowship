from flask import Flask, jsonify, request
import json, os

app = Flask(__name__)

DATA_FILE = "todos.json"

# 🔹 Load existing todos from file (if file exists)
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        try:
            todos = json.load(f)
        except json.JSONDecodeError:
            todos = []
else:
    todos = []

# Route: GET /todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({
        "status": "success",
        "data": todos
    }), 200


# Route: POST /todos
@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()

    if not data or 'task' not in data:
        return jsonify({
            "status": "error",
            "message": "Invalid request. 'task' field required."
        }), 400

    new_todo = {
        "id": len(todos) + 1,
        "task": data['task']
    }
    todos.append(new_todo)

    # 🔹 Save updated list to JSON file
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=4)

    return jsonify({
        "status": "success",
        "message": "Todo added successfully!",
        "data": new_todo
    }), 201


# Default route
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the Flask Todo API 👋",
        "endpoints": ["/todos (GET)", "/todos (POST)"]
    })


if __name__ == '__main__':
    app.run(debug=True)
