# Keith Kirtfield
# Database
# TODO uploading and retrieving data // Smart Selection
import sqlite3
from sqlalchemy import create_engine
from flask import jsonify
from sqlalchemy.orm import sessionmaker
from db import db
from applicants import Applicant, Base
import datetime


def add_application(request):

    applicant = Applicant(first_name=request['first_name'], last_name=request['last_name'],
                          position=request['position'], school=request['school'], degree=request['degree'], date=datetime.datetime.now())
    db.session.add(applicant)
    db.session.commit()


def retrieve_application(app_id):
    try:
        application = db.session.query(Applicant).filter_by(id=app_id).first()

        return jsonify({
            'success': True,
            'count': 1,
            'data': application.toJson()
        }), 200
    except:
        return jsonify({
            'success': False,
            'msg': 'Could not locate application'
        }), 404


def retrieve_applicants():
    responseArr = []
    conn = sqlite3.connect('applicants-collection.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM applicants''')
    response = c.fetchall()
    for app_id, first_name, last_name, position, school, degree, date in response:
        responseArr.append({
            'first_name': first_name,
            'id': app_id,
            'last_name': last_name,
            'position': position,
            'school': school,
            'degree': degree,
            'date': date
        })
    # cprint(response, 'green')
    return jsonify({
        "success": True,
        "count": len(response),
        "data": responseArr
    }), 200


def update_application(app_id, req):
    try:
        application = db.session.query(Applicant).filter_by(id=app_id).one()
        application.update(req)
        db.session.add(application)
        db.session.commit()
        return jsonify({
            'success': True,
            'count': 1,
            'data': application.toJson()
        }), 200
    except:
        return jsonify({
            'success': False,
            'msg': 'Unable to find application'
        }), 404


def delete_application(app_id):
    try:
        deleteApp = db.session.query(Applicant).filter_by(id=app_id).one()
        db.session.delete(deleteApp)
        db.session.commit()
        return jsonify({
            'success': True,
            'data': []
        }), 200
    except:
        return jsonify({
            'success': False,
            'msg': 'Unable to find application'
        }), 404
