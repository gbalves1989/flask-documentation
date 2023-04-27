from api import ma
from ..models.course_model import CourseModel
from marshmallow import fields


class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model: CourseModel = CourseModel
        load_instance: bool = True
        fields: tuple = ('id', 'name', 'description', 'published_at', 'graduation')

    name: str = fields.String(required=True)
    description: str = fields.String(required=True)
    published_at: str = fields.Date(required=True)
    graduation: str = fields.String(required=True)
