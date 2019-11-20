# App class
from db import db
from models.errors import Errors


class Admin(db.Model):
    from project import login_manager
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            "password": self.password
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def login(self, username, password):
        user = db.session.query(password=self.password).one
        if user:
            return True
        return False
