from api import ma
from ..models.graduation_model import GraduationModel
from ..schemas.course_schema import CourseSchema
from ..schemas.teacher_schema import TeacherSchema
from marshmallow import fields
from typing import List


class GraduationSchema(ma.SQLAlchemyAutoSchema):
    teachers = ma.Nested(TeacherSchema, many=True, only=('id', 'name'))

    class Meta:
        model: GraduationModel = GraduationModel
        load_instance: bool = True
        fields: tuple = ('id', 'name', 'description', 'courses', 'teachers')

    name: str = fields.String(required=True)
    description: str = fields.String(required=True)
    courses: List = fields.List(fields.Nested(CourseSchema, only=('id', 'name')))
