from flask import make_response, Response, jsonify
from ..repositories.user_repository import create, find_by_email
from ..schemas.user_schema import UserSchema, LoginSchema
from ..entities.user_entity import UserEntity
from ..requests.user_request import LoginBody, UserBody, AuthorizationQuery
from ..models.user_model import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from datetime import timedelta


def create_user(request: UserBody) -> Response:
    us: UserSchema = UserSchema()

    new_user: UserEntity = UserEntity(
        name=request.name,
        email=request.email,
        password=request.password
    )

    result: UserModel = create(new_user)
    return make_response(us.jsonify(result), 201)


def login_user(request: LoginBody) -> Response:
    ls: LoginSchema = LoginSchema()
    user_db: UserModel = find_by_email(request.email)

    if user_db and user_db.check_password(password=request.password):
        access = create_access_token(
            identity=user_db.id,
            expires_delta=timedelta(seconds=300)
        )

        refresh = create_refresh_token(identity=user_db.id)

        return make_response(jsonify({
            'access_token': access,
            'refresh_token': refresh,
            'message': 'Login are successfully'
        }), 200)

    return make_response(jsonify({
        'message': "Credentials aren't valid."
    }), 401)


def refresh_token(query: AuthorizationQuery) -> Response:
    user_token = query.authorization

    access = create_access_token(
        identity=user_token,
        expires_delta=timedelta(seconds=300)
    )

    refresh = create_refresh_token(identity=user_token)

    return make_response({
        'access_token': access,
        'refresh_token': refresh
    }, 200)
