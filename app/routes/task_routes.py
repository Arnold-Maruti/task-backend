from flask import Blueprint, jsonify, request
from app.models import Task,User,Category
from app import db

task_bp=Blueprint("task_bp",__name__,url_prefix="/api/tasks")

@task_bp.route("/",methods=["GET"])
def get_all_tasks():
    tasks=Task.query.all()
    return jsonify([task.to_dict() for task in tasks]),200