from api import api, security
from flask_openapi3 import APIBlueprint, Tag
from api.requests.teacher_request import TeacherBody, TeacherPath, TeacherQuery
from ..services.teacher_service import \
    create_teacher, list_teachers, show_teacher, update_teacher, delete_teacher
from ..responses.teacher_response import TeacherResponse, TeacherListResponse
from ..responses.errors_response import ErrorsResponse
from ..responses.no_content_response import NoContentResponse
from flask_jwt_extended import jwt_required


tag: Tag = Tag(name='Teachers', description='List of teachers')
api_teacher: APIBlueprint = APIBlueprint(
    'teachers',
    __name__,
    url_prefix='/teachers',
    abp_tags=[tag],
    abp_security=security
)


@api_teacher.post(
    '/',
    summary='Create a new teacher',
    description='Responsible to create and return a new teacher',
    responses={'201': TeacherResponse}
)
@jwt_required()
async def store(body: TeacherBody):
    return create_teacher(body)


@api_teacher.get(
    '/',
    summary='Return a list of teachers',
    description='Responsible to return a list of teachers',
    responses={'200': TeacherListResponse}
)
@jwt_required()
async def index(query: TeacherQuery):
    return list_teachers(query)


@api_teacher.get(
    '/<int:teacher_id>',
    summary='Return some teacher by id',
    description='Responsible to return some teacher by id',
    responses={
        '200': TeacherResponse,
        '404': ErrorsResponse
    }
)
@jwt_required()
async def show(path: TeacherPath):
    return show_teacher(path.teacher_id)


@api_teacher.put(
    '/<int:teacher_id>',
    summary='Update the data teacher by id',
    description='Responsible to update the data teacher by id',
    responses={
        '202': TeacherResponse,
        '404': ErrorsResponse
    }
)
@jwt_required()
async def update(path: TeacherPath, body: TeacherBody):
    return update_teacher(path.teacher_id, body)


@api_teacher.delete(
    '/<int:teacher_id>',
    summary='Remove some teacher by id',
    description='Responsible to remove some teacher by id',
    responses={
        '204': NoContentResponse,
        '404': ErrorsResponse
    }
)
@jwt_required()
async def delete(path: TeacherPath):
    return delete_teacher(path.teacher_id)


api.register_api(api_teacher)
