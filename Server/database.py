# Keith Kirtfield
# Database
# TODO uploading and retrieving data // Smart Selection
import sqlite3
from flask import jsonify
from db import db
from models.applicants import Applicant
from models.positions import Positions
import datetime


def add_application(request):
    response = []
    try:
        for x in request:
            applicant = Applicant(first_name=x['first_name'], last_name=x['last_name'],
                                  school=x['school'], degree=x['degree'], date=datetime.datetime.now())
            position = Positions(title=x['position'], applicant=applicant)
            response.append(applicant)
            db.session.add(applicant)
            db.session.add(position)
            db.session.commit()
    except TypeError:
        return add_application([request])
    return jsonify({
        "count": len(response),
        "success": True,
        "data": list(map(lambda x: x.toJson(), response))
    }), 201


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
    return jsonify({
        'success': True,
        'data': list(map(lambda x: x.toJson(), Applicant.query.all())),
        'count': len(Applicant.query.all())
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
