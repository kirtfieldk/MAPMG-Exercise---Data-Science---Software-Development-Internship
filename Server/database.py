# Keith Kirtfield
# Database
# TODO uploading and retrieving data // Smart Selection
import sqlite3
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from applicants import Applicant, Base
import datetime


def create_conn():
    engine = create_engine('sqlite:///applicants-collection.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


def add_application(request):
    session = create_conn()
    applicant = Applicant(first_name=request['first_name'], last_name=request['last_name'],
                          position=request['position'], school=request['school'], degree=request['degree'], date=datetime.datetime.now())
    session.add(applicant)
    session.commit()


def retrieve_application(app_id):
    session = create_conn()
    try:
        application = session.query(Applicant).filter_by(id=app_id).first()

        return{
            'success': True,
            'count': 1,
            'data': application.toJson()
        }
    except:
        return {
            'success': False,
            'msg': 'Could nt locate applucation'
        }


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
    return {
        "success": True,
        "count": len(response),
        "data": responseArr
    }


def update_application(app_id, req):
    session = create_conn()
    try:
        application = session.query(Applicant).filter_by(id=app_id).one()
        # cprint(req['first_name'], 'green')
        application.update(req)
        session.add(application)
        session.commit()
        return{
            'success': True,
            'count': 1,
            'data': application.toJson()
        }
    except:
        return ({
            'success': False,
            'msg': 'Unable to find application'
        }), 404


def delete_application(app_id):
    session = create_conn()
    try:
        deleteApp = session.query(Applicant).filter_by(id=app_id).one()
        session.delete(deleteApp)
        session.commit()
        return {
            'success': True,
            'data': []
        }
    except:
        return ({
            'success': False,
            'msg': 'Unable to find application'
        }), 404


def close_db():
    conn = sqlite3.connect('applicant.db')
    conn.close()
