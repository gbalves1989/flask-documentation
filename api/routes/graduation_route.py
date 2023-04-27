from api import api, security
from flask_openapi3 import APIBlueprint, Tag
from api.requests.graduation_request import GraduationBody, GraduationPath, GraduationQuery
from ..services.graduation_service import \
    create_graduation, list_graduations, show_graduation, update_graduation, delete_graduation
from ..responses.graduation_response import GraduationResponse, GraduationListResponse
from ..responses.errors_response import ErrorsResponse
from ..responses.no_content_response import NoContentResponse
from flask_jwt_extended import jwt_required


tag: Tag = Tag(name='Graduations', description='List of graduations')
api_graduation: APIBlueprint = APIBlueprint(
    'graduations',
    __name__,
    url_prefix='/graduations',
    abp_tags=[tag],
    abp_security=security
)


@api_graduation.post(
    '/',
    summary='Create a new graduation',
    description='Responsible to create and return a new graduation',
    responses={'201': GraduationResponse}
)
@jwt_required()
async def store(body: GraduationBody):
    return create_graduation(body)


@api_graduation.get(
    '/',
    summary='Return a list of graduations',
    description='Responsible to return a list of graduations',
    responses={'200': GraduationListResponse}
)
@jwt_required()
async def index(query: GraduationQuery):
    return list_graduations(query)


@api_graduation.get(
    '/<int:graduation_id>',
    summary='Return some graduation by id',
    description='Responsible to return some graduation by id',
    responses={
        '200': GraduationResponse,
        '404': ErrorsResponse
    }
)
@jwt_required()
async def show(path: GraduationPath):
    return show_graduation(path.graduation_id)


@api_graduation.put(
    '/<int:graduation_id>',
    summary='Update the data graduation by id',
    description='Responsible to update the data graduation by id',
    responses={
        '202': GraduationResponse,
        '404': ErrorsResponse
    }
)
@jwt_required()
async def update(path: GraduationPath, body: GraduationBody):
    return update_graduation(path.graduation_id, body)


@api_graduation.delete(
    '/<int:graduation_id>',
    summary='Remove some graduation by id',
    description='Responsible to remove some graduation by id',
    responses={
        '204': NoContentResponse,
        '404': ErrorsResponse
    }
)
@jwt_required()
async def delete(path: GraduationPath):
    return delete_graduation(path.graduation_id)


api.register_api(api_graduation)
