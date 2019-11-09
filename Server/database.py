# Keith Kirtfield
# Database
import datetime
import sqlite3
from flask import jsonify
from sqlalchemy.orm.exc import NoResultFound
from db import db
from models.applicants import Applicant
from models.positions import Positions
from models.errors import Errors


def add_application(request):
    response = []
    try:
        for x in request:
            applicant = Applicant(first_name=x['first_name'].lower(), last_name=x['last_name'].lower(),
                                  school=x['school'].lower(), degree=x['degree'].lower(), date=datetime.datetime.now())
            position = Positions(
                title=x['position'].lower(), applicant=applicant)
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
    except AttributeError:
        return Errors('Unable To Find Application', 404).toJson()


def retrieve_application_firstname(app_id):
    app_id = app_id.lower()
    try:
        response = db.session.query(
            Applicant).filter_by(first_name=app_id).all()
        return jsonify({
            'success': True,
            'count': len(response),
            'data': list(map(lambda x: x.toJson(), response))
        }), 200
    except AttributeError:
        return Errors('Unable To Search Application with First Name: {}'.format(app_id), 404).toJson()


def retrieve_application_school(school):
    school = school.lower()
    try:
        response = db.session.query(
            Applicant).filter_by(school=school).all()
        # if len(response) == 0:
        #     return Errors('Unable To Search Application with School: {}'.format(school), 404).toJson()
        return jsonify({
            'success': True,
            'count': len(response),
            'data': list(map(lambda x: x.toJson(), response))
        }), 200
    except AttributeError:
        return Errors('Unable To Search Applications with School'.format(school), 404).toJson()


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
    except NoResultFound:
        return Errors('Unable To Find Application', 404).toJson()


def delete_application(app_id):
    try:
        deleteApp = db.session.query(Applicant).filter_by(id=app_id).one()
        db.session.delete(deleteApp)
        db.session.commit()
        return jsonify({
            'success': True,
            'data': []
        }), 200
    except NoResultFound:
        return Errors('Unable To Find Application', 404).toJson()


def valid_request(req):
    errors = []
    for req in req:
        if req['first_name'] is None:
            errors.append("Please include a first name")
        if req['last_name'] is None:
            errors.append("Please include a last name")
        if req['school'] is None:
            errors.append("Please include a school")
        if req['position'] is None:
            errors.append("Please include a position")
        if req['degree'] is None:
            errors.append("Please include a degree")
    return errors
