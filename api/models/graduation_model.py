from api import db
from ..models.teacher_model import TeacherModel


teacher_graduation = db.Table(
    'teacher_graduation',
    db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id'), primary_key=True, nullable=False),
    db.Column('graduation_id', db.Integer, db.ForeignKey('graduation.id'), primary_key=True, nullable=False)
)


class GraduationModel(db.Model):
    __tablename__ = 'graduation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    teachers = db.relationship(TeacherModel, secondary='teacher_graduation', back_populates='graduations')
