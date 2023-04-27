from api import db


class TeacherModel(db.Model):
    __tablename__ = 'teacher'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    graduations = db.relationship('GraduationModel', secondary='teacher_graduation', back_populates='teachers')
