# Keith Kirtfield
# MAPMG Intern Challenge
# TODO   Flask Server App last, first name, position applied, school, degree program
# TODO   implement Exceptions and status codes

from flask import Flask, request, jsonify
from Applicant import Applicant
from database import retrieve_applicants
app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('Hey, we have Flask in a Ddededocker container!')

# GET all applicants
@app.route("/api/v1/applicants", methods=['GET', 'POST'])
def getConsumers():
    if request.method == 'GET':

        return retrieve_applicants()
    if request.method == 'POST':
        response = request.get_json() if request.is_json else "Not valid"
        applicant = Applicant(response['first'], response['last'],
                              response['school'], response['position'], response['degree'])
        applicant.addToDatabase()
        return jsonify(applicant.toJson())
    return "Hello world"


@app.route('/api/v1/applicants/<id>', methods=['PUT', 'DELETE'])
def modifyApplicants():
    if request.method == 'PUT':
        return "PUT request"
    if request.method == 'DELETE':
        return "DELETE request"
    return "Hello world"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
