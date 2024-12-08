from flask import Blueprint, jsonify, request, abort
from app.models import ToDoTable
from app.db import db

todo_bp = Blueprint('todo_bp', __name__)

# Add a new To-Do Task
@todo_bp.route('/', methods=['POST'])
def add_todo_task():
    data = request.get_json()
    if not data or not data.get('task'):
        abort(400, description="Task field is required.")
    new_task = ToDoTable(task=data['task'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"id": new_task.id, "task": new_task.task, "status": new_task.status}), 201

# Get all To-Do Tasks
@todo_bp.route('/', methods=['GET'])
def get_todos_list():
    todos = ToDoTable.query.all()
    return jsonify([{"id": todo.id, "task": todo.task, "status": todo.status} for todo in todos]), 200

# Edit or delete a specific To-Do Task
@todo_bp.route('/<int:task_id>', methods=['PUT', 'DELETE'])
def modify_todo_list(task_id):
    new_task = ToDoTable.query.get_or_404(task_id)

    if request.method == 'PUT':
        data = request.get_json()
        new_task.task = data.get('task', new_task.task)
        new_task.status = data.get('status', new_task.status)
        db.session.commit()
        return jsonify({"id": new_task.id, "task": new_task.task, "status": new_task.status}), 200

    if request.method == 'DELETE':
        db.session.delete(new_task)
        db.session.commit()
        return jsonify({"message": f"To-Do {task_id} deleted."}), 200

# Delete all To-Do Tasks
@todo_bp.route('/delete_all', methods=['DELETE'])
def delete_all_todos():
    ToDoTable.query.delete()
    db.session.commit()
    return jsonify({"message": "All To-Do tasks deleted."}), 200
