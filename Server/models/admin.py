# App class
from db import db
from models.errors import Errors


class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def to_json(self):
        return {
            'id': self.id,
            'user_name': self.user_name
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    def login(self):
        user = db.session.query(password=self.password)
        if user:
            return True
        return false
