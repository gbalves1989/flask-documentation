from api import ma
from ..models.teacher_model import TeacherModel
from marshmallow import fields


class TeacherSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model: TeacherModel = TeacherModel
        load_instance: bool = True
        fields: tuple = ('id', 'name', 'age')

    name: str = fields.String(required=True)
    age: int = fields.Integer(required=True)
