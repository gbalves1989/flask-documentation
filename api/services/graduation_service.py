from ..schemas.graduation_schema import GraduationSchema
from ..entities.graduation_entity import GraduationEntity
from ..models.graduation_model import GraduationModel
from ..repositories.graduation_repository import create, find_by_id, update, delete
from ..requests.graduation_request import GraduationBody, GraduationQuery
from flask import make_response, Response
from ..utils.paginate import paginate
from ..utils.http_error_message import http_error_message


def create_graduation(request: GraduationBody) -> Response:
    gs: GraduationSchema = GraduationSchema()

    new_graduation: GraduationEntity = GraduationEntity(
        name=request.name,
        description=request.description,
        teachers=request.teachers
    )

    result: GraduationModel = create(new_graduation)
    return make_response(gs.jsonify(result), 201)


def list_graduations(query: GraduationQuery) -> Response:
    gs: GraduationSchema = GraduationSchema(many=True)
    return paginate(GraduationModel, gs, query.page, query.per_page)


def show_graduation(graduation_id: int) -> Response:
    graduation_db: GraduationModel = find_by_id(graduation_id)

    if graduation_db is None:
        return http_error_message('Graduation not found', 404)

    gs: GraduationSchema = GraduationSchema()
    return make_response(gs.jsonify(graduation_db), 200)


def update_graduation(graduation_id: int, request: GraduationBody) -> Response:
    graduation_db: GraduationModel = find_by_id(graduation_id)

    if graduation_db is None:
        return http_error_message('Graduation not found', 404)

    graduation_entity: GraduationEntity = GraduationEntity(
        name=request.name,
        description=request.description,
        teachers=request.teachers
    )

    update(graduation_db, graduation_entity)
    graduation: GraduationModel = find_by_id(graduation_id)
    gs: GraduationSchema = GraduationSchema()
    return make_response(gs.jsonify(graduation), 202)


def delete_graduation(graduation_id: int) -> Response:
    graduation_db: GraduationModel = find_by_id(graduation_id)

    if graduation_db is None:
        return http_error_message('Graduation not found', 404)

    delete(graduation_db)
    return make_response({'content': 'graduation removed with successfully'}, 204)
