from api import api
from flask_openapi3 import APIBlueprint, Tag
from api.requests.user_request import UserBody, LoginBody, AuthorizationQuery
from ..services.user_service import create_user, login_user, refresh_token
from ..responses.user_response import UserResponse, LoginResponse, RefreshResponse
from ..responses.unauthorized_response import UnauthorizedResponse


tag: Tag = Tag(name='Users', description='List of users')
api_user: APIBlueprint = APIBlueprint('users', __name__, url_prefix='/users', abp_tags=[tag])


@api_user.post(
    '/',
    summary='Create a new user',
    description='Responsible to create and return a new user',
    responses={'201': UserResponse}
)
async def store(body: UserBody):
    return create_user(body)


@api_user.post(
    '/login',
    summary='login user',
    description='Responsible to login user and return a access token',
    responses={'200': LoginResponse, '401': UnauthorizedResponse}
)
async def login(body: LoginBody):
    return login_user(body)


@api_user.post(
    '/token/refresh',
    summary='refresh token to access',
    description='Responsible to refresh token to new access',
    responses={'200': RefreshResponse}
)
async def refresh(query: AuthorizationQuery):
    return refresh_token(query)

api.register_api(api_user)
