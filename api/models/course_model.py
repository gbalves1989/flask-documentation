from api import db
from ..models.graduation_model import GraduationModel


class CourseModel(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    published_at = db.Column(db.Date, nullable=False)

    graduation_id = db.Column(db.Integer, db.ForeignKey('graduation.id'))
    graduation = db.relationship(GraduationModel, backref=db.backref('courses', lazy='dynamic'))
