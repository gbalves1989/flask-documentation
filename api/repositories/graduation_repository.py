from ..models.graduation_model import GraduationModel
from ..entities.graduation_entity import GraduationEntity
from ..repositories import teacher_repository
from api import db


def create(entity: GraduationEntity) -> GraduationModel:
    graduation_db: GraduationModel = GraduationModel(
        name=entity.name,
        description=entity.description
    )

    print(entity.teachers)

    for i in entity.teachers:
        teacher = teacher_repository.find_by_id(i)
        graduation_db.teachers.append(teacher)

    db.session.add(graduation_db)
    db.session.commit()
    return graduation_db


def find_by_id(graduation_id: int) -> GraduationModel:
    graduation_db: GraduationModel = GraduationModel.query.filter_by(id=graduation_id).first()
    return graduation_db


def update(graduation_db: GraduationModel, graduation_entity: GraduationEntity) -> None:
    graduation_db.name = graduation_entity.name
    graduation_db.description = graduation_entity.description

    for i in graduation_entity.teachers:
        teacher = teacher_repository.find_by_id(i)
        graduation_db.teachers.append(teacher)

    db.session.commit()


def delete(graduation_db: GraduationModel) -> None:
    db.session.delete(graduation_db)
    db.session.commit()
