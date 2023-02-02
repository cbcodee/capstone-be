from app import db
from flask import Blueprint, jsonify, request, abort, make_response, json
from app.models.task import Task
import os
import requests

task_bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model


# new_task = Task.from_dict(request_body)
@task_bp.route("", methods=["POST"])
def create_task():
    request_body = request.get_json()
    
    new_task = Task.from_dict(request_body)
    

    db.session.add(new_task)
    db.session.commit()


    return jsonify(new_task.to_dict()), 201

# @task_bp.route("", methods=["POST"])
# def create_task():
#     request_body = request.get_json()
    
#     new_task = Task.from_dict(request_body)
    

#     db.session.add(new_task)
#     db.session.commit()

#     task_dict = new_task.to_dict()

#     return make_response(jsonify({"task": task_dict}), 201)



    # try:
    #     new_task = Task.from_dict(request_body)
    # except KeyError:
    #     abort(make_response({"details": "Invalid data"}, 400))

    # db.session.add(new_task)
    # db.session.commit()

    # return make_response(jsonify({'task': new_task.to_dict()}), 201)


@task_bp.route("", methods=["GET"])
def list_all_tasks():
    tasks = Task.query.order_by(Task.id).all()

    tasks_response = [task.to_dict() for task in tasks]

    return jsonify(tasks_response), 200


@task_bp.route("", methods=["GET"])
def handle_task():
    task = validate_model(Task, id)

    return jsonify(task.to_dict()), 200




@task_bp.route("/<id>", methods=["DELETE"])
def delete_task(id):
    task = validate_model(Task, id)
    

    db.session.delete(task)
    db.session.commit()

    return {"details": f'Task {task.id} "{task.title}" successfully deleted'}

@task_bp.route("/<id>/mark-complete", methods=["PATCH"])
def complete_task_with_id(id):
    task = validate_model(Task, id)

    task.is_complete = True

    db.session.commit()

    return jsonify(task.to_dict())

@task_bp.route("/<id>/mark-incomplete", methods=["PATCH"])
def incomplete_task_with_id(id):
    task = validate_model(Task, id)

    task.is_complete = False

    db.session.commit()

    return jsonify(task.to_dict())





# def is_complete():
    #     if "completed_at" in task_list == None:
    #         return True
    #     else:
    #         return False

    task_list = []

    # sort_query = request.args.get("sort")
    
    # if sort_query:
    #     if "asc" in sort_query:
    #         tasks = Task.query.order_by(Task.title)
    #     elif "desc" in sort_query:
    #         tasks = Task.query.order_by(Task.title.desc())
    # else:
    #     tasks = Task.query.all()   
    
    # for task in tasks:
    #     task_list.append({
    #         "id": task.task_id, 
    #         "title": task.title, 
    #         })
    # return jsonify(task_list)
