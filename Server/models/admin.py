# App class
from flask_login import UserMixin
from middlewear import db, login_manager
from models.errors import Errors


@login_manager.user_loader
def load_user(id):
    return Admin.query.get(int(id))


class Admin(db.Model):
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
