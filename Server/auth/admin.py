from flask import jsonify
from models.admin import Admin
from models.errors import Errors
from middlewear import db


def create_admin(req):
    from project import bcrypt
    try:
        if valid_username(req['username']):
            password = bcrypt.generate_password_hash(
                req['password']).decode('utf-8')
            admin = Admin(username=req['username'], password=password)
            admin.save_to_db()
            return admin.to_json()
        return Errors("Username Already Taken", 400).to_json()
    except KeyError:
        errors.append({'msg': 'Missing Important Keys'})


def valid_username(name):
    if db.session.query(Admin).filter_by(username=name).all():
        return False
    return True
