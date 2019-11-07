# Keith Kirtfield
# MAPMG Intern Challenge
# TODO   Flask Server App last, first name, position applied, school, degree program
# TODO   implement Exceptions and status codes

from flask import Flask, request, jsonify
from applicants import Applicant
from database import retrieve_applicants
from database import add_application
from database import close_db
from database import update_application
from database import delete_application
from database import retrieve_application
app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('Hey, we have Flask in a Ddededocker container!')

# GET all applicants
@app.route("/api/v1/applicants", methods=['GET', 'POST'])
def getConsumers():
    if request.method == 'GET':
        return jsonify(retrieve_applicants()), 200
    if request.method == 'POST':
        response = request.get_json() if request.is_json else "Not valid"
        for x in response:
            add_application(x)
        return jsonify({
            'success': True,
            'count': len(response),
            'data': response
        }), 201
    return jsonify({
        'success': False,
        'msg': 'Not a Valid HTTP Request'
    }), 400


@app.route('/api/v1/applicants/<app_id>', methods=['PUT', 'DELETE', 'GET'])
def modifyApplicants(app_id):
    if request.method == 'PUT':
        response = request.get_json() if request.is_json else "Not valid"
        return jsonify(update_application(app_id, response)), 201
    if request.method == 'DELETE':
        return jsonify(delete_application(app_id)), 200
    if request.method == 'GET':
        return jsonify(retrieve_application(app_id))
    return jsonify({
        'success': False,
        'msg': 'Not a Valid HTTP Request'
    }), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
