from ..repositories.teacher_repository import create, find_by_id, update, delete
from ..requests.teacher_request import TeacherBody, TeacherQuery
from ..schemas.teacher_schema import TeacherSchema
from ..entities.teacher_entity import TeacherEntity
from ..models.teacher_model import TeacherModel
from flask import make_response, Response
from ..utils.paginate import paginate
from ..utils.http_error_message import http_error_message


def create_teacher(request: TeacherBody) -> Response:
    ts: TeacherSchema = TeacherSchema()

    new_teacher: TeacherEntity = TeacherEntity(
        name=request.name,
        age=request.age
    )

    result: TeacherModel = create(new_teacher)
    return make_response(ts.jsonify(result), 201)


def list_teachers(query: TeacherQuery) -> Response:
    ts: TeacherSchema = TeacherSchema(many=True)
    return paginate(TeacherModel, ts, query.page, query.per_page)


def show_teacher(teacher_id: int) -> Response:
    teacher_db: TeacherModel = find_by_id(teacher_id)

    if teacher_db is None:
        return http_error_message('Teacher not found', 404)

    ts: TeacherSchema = TeacherSchema()
    return make_response(ts.jsonify(teacher_db), 200)


def update_teacher(teacher_id: int, request: TeacherBody) -> Response:
    teacher_db: TeacherModel = find_by_id(teacher_id)

    if teacher_db is None:
        return http_error_message('Teacher not found', 404)

    teacher_entity: TeacherEntity = TeacherEntity(
        name=request.name,
        age=request.age
    )

    update(teacher_db, teacher_entity)
    teacher: TeacherModel = find_by_id(teacher_id)
    ts: TeacherSchema = TeacherSchema()
    return make_response(ts.jsonify(teacher), 202)


def delete_teacher(teacher_id: int) -> Response:
    teacher_db: TeacherModel = find_by_id(teacher_id)

    if teacher_db is None:
        return http_error_message('Teacher not found', 404)

    delete(teacher_db)
    return make_response({'content': 'teacher removed with successfully'}, 204)
