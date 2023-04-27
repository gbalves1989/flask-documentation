from api import db
from passlib.hash import pbkdf2_sha256


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def encrypt_password(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def check_password(self, password: str):
        return pbkdf2_sha256.verify(password, self.password)
