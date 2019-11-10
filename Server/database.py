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

# POST METHOD
# /api/v1/applicants


def add_application(request):
    response = []
    try:
        errs = valid_request(request)
        if len(errs):
            return jsonify(errs), 400
        for x in request:
            applicant = Applicant(first_name=x['first_name'].lower(), last_name=x['last_name'].lower(),
                                  school=x['school'].lower(), degree=x['degree'].lower(), date=datetime.datetime.now())
            position = Positions(
                title=x['position'].lower(), applicant=applicant)
            if position.check_error() == True:
                return Errors('Only Open Positions: {}'.format(position.open_positions()), 400).toJson()
            else:
                response.append(applicant)
                applicant.save_to_db()
                position.save_to_db()
    except sqlite3.OperationalError:
        return Errors('Table Not Open', 500).toJson()
    except TypeError:
        return add_application([request])
    return jsonify({
        "count": len(response),
        "success": True,
        "data": list(map(lambda x: x.toJson(), response))
    }), 201

# GET all apps
# /api/v1/applicants


def retrieve_applicants():
    try:
        return jsonify({
            'success': True,
            'data': list(map(lambda x: x.toJson(), Applicant.query.all())),
            'count': len(Applicant.query.all())
        }), 200
    except sqlite3.OperationalError:
        return Errors('Table Not Open', 500).toJson()

##############################
##GET apps by search methods##
##############################

# /api/v1/applicants/:app_id


def retrieve_application(app_id):
    try:
        application = db.session.query(Applicant).filter_by(id=app_id).first()
        return jsonify({
            'success': True,
            'count': 1,
            'data': application.toJson()
        }), 200
    except sqlite3.OperationalError:
        return Errors('Table Not Open', 500).toJson()
    except AttributeError:
        return Errors('Unable To Find Application', 404).toJson()

# /api/v1/applicants/firstname/:app_id


def retrieve_application_lastname(last_name):
    last_name = last_name.lower()
    try:
        print(last_name)
        response = db.session.query(
            Applicant).filter_by(last_name="kirtfield").all()
        print(response)
        return jsonify({
            'success': True,
            'count': len(response),
            'data': list(map(lambda x: x.toJson(), response))
        }), 200
    except sqlite3.OperationalError:
        return Errors('Table Not Open', 500).toJson()
    except AttributeError:
        return Errors('Unable To Search Application with First Name: {}'.format(last_name), 404).toJson()

# /api/v1/applicants/school/:school


def retrieve_application_school(school):
    school = school.lower()
    try:
        response = db.session.query(
            Applicant).filter_by(school=school).all()
        return jsonify({
            'success': True,
            'count': len(response),
            'data': list(map(lambda x: x.toJson(), response))
        }), 200
    except sqlite3.OperationalError:
        return Errors('Table Not Open', 500).toJson()
    except AttributeError:
        return Errors('Unable To Search Applications with School'.format(school), 404).toJson()

# PUT an app
# /api/v1/applicants/:app_id


def update_application(app_id, req):
    try:
        application = db.session.query(Applicant).filter_by(id=app_id).one()
        application.update(req)
        application.save_to_db()
        return jsonify({
            'success': True,
            'count': 1,
            'data': application.toJson()
        }), 200
    except sqlite3.OperationalError:
        return Errors('Table Not Open', 500).toJson()
    except NoResultFound:
        return Errors('Unable To Find Application', 404).toJson()

# DELETE app
# /api/v1/applicants/:app_id


def delete_application(app_id):
    try:
        deleteApp = db.session.query(Applicant).filter_by(id=app_id).one()
        deleteApp.delete_db()
        return jsonify({
            'success': True,
            'data': []
        }), 200
    except NoResultFound:
        return Errors('Unable To Find Application', 404).toJson()

# HELPER METHOD


def valid_request(req):
    errors = []
    for x in req:
        try:
            if x['last_name'] is None:
                errors.append({'msg': "Please include a first name"})
            if len(x['last_name']) == 0:
                errors.append({'msg': "Please include a last name"})
            if x['school'] is None:
                errors.append({'msg': "Please include a school"})
            if x['position'] is None:
                errors.append({'msg': "Please include a position"})
            if x['degree'] is None:
                errors.append({'msg': "Please include a degree"})
        except KeyError:
            errors.append({'msg': 'Missing Important Keys'})
    return errors
