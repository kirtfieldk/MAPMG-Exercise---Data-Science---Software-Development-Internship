# Keith Kirtfield
# Database
import datetime
import sqlite3
from flask import jsonify
from werkzeug.security import safe_str_cmp
from sqlalchemy.orm.exc import NoResultFound
from middlewear import db
from models.applicants import Applicant
from models.positions import Positions
from models.admin import Admin
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
                return Errors('Only Current Open Positions: {}'.format(position.open_positions()), 400).to_json()
            else:
                response.append(applicant)
                applicant.save_to_db()
                position.save_to_db()
    except sqlite3.OperationalError:
        return Errors('Table Not Open', 500).to_json()
    except TypeError:
        return add_application([request])
    return jsonify({
        "count": len(response),
        "success": True,
        "data": list(map(lambda x: x.to_json(), response))
    }), 201

##############################
##GET apps by search methods##
##############################


def update_application(app_id, req):
    try:
        application = db.session.query(Applicant).filter_by(id=app_id).one()
        application.update(req)
        application.save_to_db()
        return jsonify({
            'success': True,
            'count': 1,
            'data': application.to_json()
        }), 200
    except sqlite3.OperationalError:
        return Errors('Table Not Open', 500).to_json()
    except NoResultFound:
        return Errors('Unable To Find Application', 404).to_json()

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
        return Errors('Unable To Find Application', 404).to_json()

# HELPER METHOD


def valid_request(req):
    errors = []
    for x in req:
        try:
            if x['last_name'] or x['last_name'] or x['school'] or x['position'] or x['degree'] is None:
                pass
        except KeyError:
            errors.append({'msg': 'Missing Important Keys'})
    return errors
