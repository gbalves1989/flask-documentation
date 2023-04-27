from ..models.user_model import UserModel
from ..entities.user_entity import UserEntity
from api import db


def create(entity: UserEntity) -> UserModel:
    user_db: UserModel = UserModel(
        name=entity.name,
        email=entity.email,
        password=entity.password
    )

    user_db.encrypt_password()
    db.session.add(user_db)
    db.session.commit()
    return user_db


def find_by_email(email: str) -> UserModel:
    return UserModel.query.filter_by(email=email).first()


def find_by_id(user_id: int) -> UserModel:
    return UserModel.query.filter_by(id=user_id).first()


def find_by_api_key(api_key: str) -> UserModel:
    return UserModel.query.filter_by(api_key=api_key).first()
