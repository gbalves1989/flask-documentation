from ..schemas.course_schema import CourseSchema
from ..entities.course_entity import CourseEntity
from ..repositories import graduation_repository
from ..models.course_model import CourseModel
from ..models.graduation_model import GraduationModel
from ..repositories.course_repository import create, find_by_id, update, delete
from ..requests.course_request import CourseBody, CourseQuery
from flask import make_response, Response
from ..utils.paginate import paginate
from ..utils.http_error_message import http_error_message


def create_course(request: CourseBody) -> Response:
    cs: CourseSchema = CourseSchema()
    graduation_db: GraduationModel = graduation_repository.find_by_id(int(request.graduation))

    if graduation_db is None:
        return http_error_message('Graduation not found', 404)

    new_course: CourseEntity = CourseEntity(
        name=request.name,
        description=request.description,
        published_at=request.published_at,
        graduation=graduation_db
    )

    result: CourseModel = create(new_course)
    return make_response(cs.jsonify(result), 201)


def list_courses(query: CourseQuery) -> Response:
    cs: CourseSchema = CourseSchema(many=True)
    return paginate(CourseModel, cs, query.page, query.per_page)


def show_course(course_id: int) -> Response:
    course_db: CourseModel = find_by_id(course_id)

    if course_db is None:
        return http_error_message('Course not found', 404)

    cs: CourseSchema = CourseSchema()
    return make_response(cs.jsonify(course_db), 200)


def update_course(course_id: int, request: CourseBody) -> Response:
    course_db: CourseModel = find_by_id(course_id)

    if course_db is None:
        return http_error_message('Course not found', 404)

    graduation_db: GraduationModel = graduation_repository.find_by_id(int(request.graduation))

    if graduation_db is None:
        return http_error_message('Graduation not found', 404)

    course_entity: CourseEntity = CourseEntity(
        name=request.name,
        description=request.description,
        published_at=request.published_at,
        graduation=graduation_db
    )

    update(course_db, course_entity)
    course: CourseModel = find_by_id(course_id)
    cs: CourseSchema = CourseSchema()
    return make_response(cs.jsonify(course), 202)


def delete_course(course_id: int) -> Response:
    course_db: CourseModel = find_by_id(course_id)

    if course_db is None:
        return http_error_message('Course not found', 404)

    delete(course_db)
    return make_response({'content': 'course removed with successfully'}, 204)
