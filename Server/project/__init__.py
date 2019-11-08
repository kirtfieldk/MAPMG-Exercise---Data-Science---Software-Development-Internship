# Keith Kirtfield
# MAPMG Intern Challenge

import sys
from flask import Flask, request, jsonify
from models.applicants import Applicant
from models.positions import Positions
from database import (retrieve_applicants, add_application,
                      update_application, delete_application, retrieve_application)
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///applicants-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def hello_world():
    return('Hey, we have Flask in a Ddededocker container!')

# GET all applicants
# POST numerouse or one application
@app.route("/api/v1/applicants", methods=['GET', 'POST', 'PUT', 'DELETE'])
def getConsumers():
    if request.method == 'GET':
        return retrieve_applicants()
    if request.method == 'POST':
        response = request.get_json() if request.is_json else "Not valid"
        if response == 'Not valid':
            return jsonify({'success': False, 'count': 0, 'msg': 'Expecting Json Objects'}), 400
        return add_application(response)
    return jsonify({
        'success': False,
        'msg': 'Not a Valid HTTP Request'
    }), 405

# PUT update application
# DELETE delete application
# GET specific Application
@app.route('/api/v1/applicants/<app_id>', methods=['PUT', 'DELETE', 'GET', 'POST'])
def modifyApplicants(app_id):
    if request.method == 'PUT':
        response = request.get_json() if request.is_json else "Not valid"
        if response == 'Not valid':
            return jsonify({'success': False, 'count': 0, 'msg': 'Expecting Json Objects'}), 400
        return update_application(app_id, response)
    if request.method == 'DELETE':
        return delete_application(app_id)
    if request.method == 'GET':
        return retrieve_application(app_id)
    return jsonify({
        'success': False,
        'msg': 'Not a Valid HTTP Request'
    }), 405
