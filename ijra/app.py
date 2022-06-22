from ijra import jwt, db
from ijra.models import (
    AuthUser,
    Category,
    ToDoAction,
)
from ijra.serializers import (
    user_schema,
    category_schema,
    categories_schema,
    action_schema,
    actions_schema,
)
from flask_jwt_extended import create_access_token, decode_token
from flask import jsonify, request, Blueprint
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

ijra = Blueprint("ijra", __name__)


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(jwt_header, jwt_data):
    identity = jwt_data["identity"]
    return AuthUser.query.filter_by(id=identity).one_or_none()


@ijra.route("/api/v1/register", methods=["POST"])
def register():
    # some validation
    try:
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        new_user = AuthUser(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user), 201
    except (UniqueViolation, IntegrityError):
        # logging as e
        return (
            jsonify({"response": "User with provided credentials already exists"}),
            403,
        )


@ijra.route("/api/v1/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = AuthUser.query.filter_by(username=username).one_or_none()
    if not user or user.check_password(password) is False:
        return jsonify({"response": "Wrong login or password"}), 401
    additional_claims = {"user_id": user.id, "username": user.username}
    access_token = create_access_token(
        identity=user, additional_claims=additional_claims
    )
    return jsonify(access_token=access_token)


@ijra.route("/api/v1/categories", methods=["GET", "POST"])
def create_category():
    if request.method == "GET":
        if request.args.get("user"):
            user_categories = Category.query.filter_by(owner=request.args.get("user"))
            return categories_schema.jsonify(user_categories), 200
        list_categories = Category.query.all()
        return jsonify(categories_schema.dump(list_categories)), 200

    category_name = request.json.get("name", "")
    owner_id = request.json.get("owner", "")
    new_category = Category(name=category_name, owner=owner_id)
    db.session.add(new_category)
    db.session.commit()
    return category_schema.jsonify(new_category), 201


@ijra.route("/api/v1/actions", methods=["GET", "POST", "PUT", "DELETE"])
def actions():
    if request.method == "GET":
        if request.args.get("user"):
            user_actions = ToDoAction.query.filter_by(
                created_by=request.args.get("user")
            )
            return actions_schema.jsonify(user_actions), 200

        list_actions = ToDoAction.query.all()
        return jsonify(actions_schema.dump(list_actions), 200)

    if request.method == "POST":
        title = request.json.get("title")
        description = request.json.get("description")
        category_id = request.json.get("category_id")
        created_by = request.json.get("created_by")
        try:
            new_action = ToDoAction(
                title=title,
                description=description,
                category_id=category_id,
                created_by=created_by,
            )
            db.session.add(new_action)
            db.session.commit()
            return action_schema.jsonify(new_action), 201
        except IntegrityError:
            # log
            return (
                jsonify({"response": "Couldn't create action with provided data"}),
                400,
            )
    if request.method == "PUT":
        # additionally parse users permissions for patch request (decode jwt)
        if request.args.get("action_name"):
            action = ToDoAction.query.filter_by(
                title=request.args.get("action_name")
            ).one_or_none()
            try:
                title = request.json.get("title")
                description = request.json.get("description")
                category_id = request.json.get("category_id")
                created_by = request.json.get("created_by")
                action.title = title
                action.description = description
                action.category_id = category_id
                action.created_by = created_by
                db.session.add(action)
                db.session.commit()
                return action_schema.jsonify(action), 200
            except AttributeError:
                return jsonify({"response": "Such action name does not exist"}), 404

        return jsonify({"response": "Pls provide all related fields"}), 400

    if request.method == "DELETE":
        if request.args.get("action_name"):
            action = ToDoAction.query.filter_by(
                title=request.args.get("action_name")
            ).one_or_none()
            if not action:
                return jsonify({"response": "Such action name does not exist"}), 404
            db.session.delete(action)
            db.session.commit()
            return jsonify({"response": "Deleted successfully"}), 200


@ijra.route("/api/v1/verify", methods=["POST"])
def verify():
    token = request.headers.get("Authorization")
    decode_token(token.split(" ")[1])
    return jsonify({"response": "Token is valid"}), 200
