# Keith Kirtfield
# MAPMG Intern Challenge

import sys
from flask import Flask, request, jsonify
from db import db
from models.applicants import Applicant
from models.positions import Positions
from models.errors import Errors
from database import (retrieve_applicants, add_application,
                      update_application, delete_application, retrieve_application, retrieve_application_lastname,
                      retrieve_application_school)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///applicants-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
db.init_app(app)


@app.before_first_request
def create_tables():
    # db.drop_all()
    db.create_all()


@app.route('/')
def hello_world():
    return("Keith Kirtfield's simple api!")

# GET all applicants
# POST numerouse or one application
@app.route('/api/v1/applicants', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_apps():
    if request.method == 'GET':
        return retrieve_applicants()
    if request.method == 'POST':
        response = request.get_json() if request.is_json else "Not valid"
        if response == 'Not valid':
            return Errors('Expecting A JSON Object', 400).to_json()
        return add_application(response)
    return Errors('Not a Valid HTTP Request on This Route', 405).to_json()

# PUT update application
# DELETE delete application
# GET specific Application
@app.route('/api/v1/applicants/<app_id>', methods=['PUT', 'DELETE', 'GET', 'POST'])
def modify_applicants(app_id):
    if request.method == 'PUT':
        response = request.get_json() if request.is_json else "Not valid"
        if response == 'Not valid':
            return Errors('Expecting A JSON Object', 400).to_json()
        return update_application(app_id, response)
    if request.method == 'DELETE':
        return delete_application(app_id)
    if request.method == 'GET':
        return retrieve_application(app_id)
    return Errors('Not a Valid HTTP Request on This Route', 405).to_json()

# GET all apps via last name
@app.route('/api/v1/applicants/lastname/<last_name>', methods=['PUT', 'DELETE', 'GET', 'POST'])
def retrieve_app_name(last_name):
    if request.method == 'GET':
        return retrieve_application_lastname(last_name)
    return Errors('Not a Valid HTTP Request on This Route', 405).to_json()

# GET all apps via school
@app.route('/api/v1/applicants/school/<school>', methods=['PUT', 'DELETE', 'GET', 'POST'])
def retrieve_app_schools(school):
    if request.method == 'GET':
        return retrieve_application_school(school)
    return Errors('Not a Valid HTTP Request on This Route', 405).to_json()
