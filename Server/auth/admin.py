from flask import jsonify
from flask_login import login_user, current_user, logout_user
from models.admin import Admin
from models.errors import Errors
from middlewear import db, bcrypt

# POST api/v1/admin


def create_admin(req):
    try:
        if current_user.is_authenticated:
            return Errors("Already logedin", 400).to_json()
        if valid_username(req['username']):
            password = bcrypt.generate_password_hash(
                req['password']).decode('utf-8')
            admin = Admin(username=req['username'], password=password)
            admin.save_to_db()
            return admin.to_json()
        return Errors("Username Already Taken", 400).to_json()
    except KeyError:
        errors.append({'msg': 'Missing Important Keys'})

# POST api/v1/admin/login


def login(username, password):
    if current_user.is_authenticated:
        return Errors("Already logedin", 400).to_json()
    user = db.session.query(Admin).filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'success': True, "msg": "Login {}".format(username)})
    return Errors("Could Not Login", 404).to_json()


def logout():
    logout_user()
    return jsonify({"msg": "Successful logout"})


def valid_username(name):
    if db.session.query(Admin).filter_by(username=name).all():
        return False
    return True
