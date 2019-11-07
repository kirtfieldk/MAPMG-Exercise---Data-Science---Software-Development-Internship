# Keith Kirtfield
# MAPMG Intern Challenge
# TODO   Flask Server App last, first name, position applied, school, degree program
# TODO   implement Exceptions and status codes

from flask import Flask, request, jsonify
from applicants import Applicant
from database import (retrieve_applicants, add_application,
                      update_application, delete_application, retrieve_application)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///applicants-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.route('/')
def hello_world():
    return ('Hey, we have Flask in a Ddededocker container!')

# GET all applicants
# POST numerouse or one application
@app.route("/api/v1/applicants", methods=['GET', 'POST'])
def getConsumers():
    print(request.url)
    if request.method == 'GET':
        return retrieve_applicants()
    if request.method == 'POST':
        response = request.get_json() if request.is_json else "Not valid"
        if response == 'Not valid':
            return jsonify({'success': False, 'count': 0, 'msg': 'Expecting Json Objects'}), 400
        try:
            for x in response:
                add_application(x)
        except TypeError:
            add_application(response)
        return jsonify({
            'success': True,
            'count': len(response),
            'data': response
        }), 201
    return jsonify({
        'success': False,
        'msg': 'Not a Valid HTTP Request'
    }), 400

# PUT update application
# DELETE delete application
# GET specific Application
@app.route('/api/v1/applicants/<app_id>', methods=['PUT', 'DELETE', 'GET'])
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
    }), 400


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0')
