from ..models.teacher_model import TeacherModel
from ..entities.teacher_entity import TeacherEntity
from api import db


def create(entity: TeacherEntity) -> TeacherModel:
    teacher_db: TeacherModel = TeacherModel(
        name=entity.name,
        age=entity.age
    )

    db.session.add(teacher_db)
    db.session.commit()
    return teacher_db


def find_by_id(teacher_id: int) -> TeacherModel:
    teacher_db: TeacherModel = TeacherModel.query.filter_by(id=teacher_id).first()
    return teacher_db


def update(teacher_db: TeacherModel, teacher_entity: TeacherEntity) -> None:
    teacher_db.name = teacher_entity.name
    teacher_db.age = teacher_entity.age
    db.session.commit()


def delete(teacher_db: TeacherModel) -> None:
    db.session.delete(teacher_db)
    db.session.commit()
