from api import ma
from ..models.user_model import UserModel
from marshmallow import fields


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model: UserModel = UserModel
        load_instance: bool = True
        fields: tuple = ('id', 'name', 'email', 'password')

    name: str = fields.String(required=True)
    email: str = fields.String(required=True)
    password: str = fields.String(required=True)


class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model: UserModel = UserModel
        load_instance: bool = True
        fields: tuple = ('id', 'name', 'email', 'password')

    name: str = fields.String(required=False)
    email: str = fields.String(required=True)
    password: str = fields.String(required=True)
