from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.user import User
from app.models.task import Task

user_bp = Blueprint("users_bp", __name__, url_prefix="/users")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message": f"{cls.__name__} {model_id} not found"}, 404))

    return model


@user_bp.route("", methods=["POST"])
def create_user():
    request_body = request.get_json()

    if request_body["username"] == "":
        abort(make_response({"message":"Please include a username"}, 400))

    users = User.query.all()

    for user in users:
        if request_body["username"] == user.username:
            abort(make_response({"message":f"The username {request_body['username']} is taken. Please choose another username."}, 400))

    new_user = User(username=request_body["username"])

    db.session.add(new_user)
    db.session.commit()

    return make_response(jsonify({"id": new_user.id, "username": new_user.username}), 201)


@user_bp.route("<id>/tasks", methods=["GET"])
def read_all_user_tasks(id):

    task_query = Task.query.filter(Task.id == id)
    
    task_response = [task.to_dict() for task in task_query]

    return jsonify(task_response), 200



@user_bp.route("", methods=["GET"])
def read_all_users():
    users = User.query.all()

    users_response = []
    for user in users:
        users_response.append(
            {
                "id": user.id,
                "name": user.username
            }
        )
    return jsonify(users_response)

@user_bp.route("/<username>", methods=["GET"])
def read_one_user(username):
    user = validate_model(User, username)

    return make_response(jsonify({"id": user.id, "username": user.username}), 200) 