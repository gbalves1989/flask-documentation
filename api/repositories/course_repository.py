from ..models.course_model import CourseModel
from ..entities.course_entity import CourseEntity
from api import db


def create(entity: CourseEntity) -> CourseModel:
    course_db: CourseModel = CourseModel(
        name=entity.name,
        description=entity.description,
        published_at=entity.published_at,
        graduation=entity.graduation
    )

    db.session.add(course_db)
    db.session.commit()
    return course_db


def find_by_id(course_id: int) -> CourseModel:
    course_db: CourseModel = CourseModel.query.filter_by(id=course_id).first()
    return course_db


def update(course_db: CourseModel, course_entity: CourseEntity) -> None:
    course_db.name = course_entity.name
    course_db.description = course_entity.description
    course_db.published_at = course_entity.published_at
    course_db.graduation = course_entity.graduation
    db.session.commit()


def delete(course_db: CourseModel) -> None:
    db.session.delete(course_db)
    db.session.commit()
