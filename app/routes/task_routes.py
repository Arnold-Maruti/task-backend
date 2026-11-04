from flask import Blueprint, jsonify, request
from app.models import Task,User,Category
from app import db

task_bp=Blueprint("task_bp",__name__,url_prefix="/api/tasks")

@task_bp.route("/",methods=["GET,POST"])
def get_all_user_tasks():
    user_id=request.args.get("X-User-Id")

    if not user_id:
        return jsonify({"error":"User-Id  is required"}),401

    user=User.query.get(user_id)
    if not user:
        return jsonify({"error":"User not found"}),404

    if request.method=="GET":
       tasks=Task.query.filter_by(user_id=user_id).all()

       return jsonify([task.to_dict() for task in tasks]),200

    task_data=request.get_json()

    title=task_data.get("title")
    description=task_data.get("description")
    status=task_data.get("status","pending")
    due_date=task_data.get("due_date")
    priority=task_data.get("priority","medium")
    category_id=task_data.get("category_id")

    new_task=Task(
        title=title,
        description=description,
        status=status,
        due_date=due_date,
        priority=priority,
        category_id=category_id,
        user_id=user_id
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message":"Task created successfully","task":new_task.to_dict()}),201


@task_bp.route("/<int:task_id>",methods=["GET"])
def get_task(task_id):
    task=Task.query.get(task_id)
    if task:
        return jsonify(task.to_dict()),200
    
    return jsonify({"error":"Task not found"}),404


@task_bp.route("/<int:task_id>",methods=["PUT"])
def update_task(task_id):
    task=Task.query.get(task_id)
    if not task:
        return jsonify({"error":"Task not found"}),404

    data=request.get_json()

    task.title=data.get("title",task.title)
    task.description=data.get("description",task.description)
    task.status=data.get("status",task.status)
    task.due_date=data.get("due_date",task.due_date)
    task.priority=data.get("priority",task.priority)
    task.category_id=data.get("category_id",task.category_id)

    db.session.commit()

    return jsonify({"message":"Task updated successfully","task":task.to_dict()}),200


@task_bp.route("/<int:task_id>",methods=["DELETE"])
def delete_task(task_id):
    task=Task.query.get(task_id)
    if not task:
        return jsonify({"error":"Task not found"}),404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message":"Task deleted successfully"}),200
