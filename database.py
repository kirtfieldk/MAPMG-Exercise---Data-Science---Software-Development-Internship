# Keith Kirtfield
# Database
# TODO uploading and retrieving data // Smart Selection
import sqlite3
import secrets
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from applicants import Applicant, Base
import datetime
from termcolor import colored, cprint


def create_conn():
    engine = create_engine('sqlite:///applicants-collection.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


def create_teable():
    conn = sqlite3.connect('applicant.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE if NOT EXISTS applicants(
        app_id text UNIQUE,
        first_name text NOT NULL,
        last_name text NOT NULL,
        position text NOT NULL,
        school text NOT NULL,
        degree text NOT NULL,
        PRIMARY KEY (app_id)
    )''')
    conn.commit()


def add_application(request):
    session = create_conn()
    applicant = Applicant(first_name=request['first'], last_name=request['last'],
                          position=request['position'], school=request['school'], degree=request['degree'], date=datetime.datetime.now())
    session.add(applicant)
    session.commit()


def retrieve_applicants():
    responseArr = []
    conn = sqlite3.connect('applicants-collection.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM applicants''')
    response = c.fetchall()
    for x in response:
        responseArr.append({
            'id': x[0],
            'first_name': x[1],
            'last_name': x[2],
            'position': x[3],
            'school': x[4],
            'degree': x[5],
            'date': x[6]
        })
    # cprint(response, 'green')
    return {
        "success": True,
        "count": len(response),
        "data": responseArr
    }


def update_application(app_id, req):
    session = create_conn()
    editApp = session.query(Applicant).filter_by(id=app_id).one()
    editApp.first_name = req['first']
    editApp.last_name = req['last']
    editApp.position = req['position']
    editApp.school = req['school']
    editApp.degree = req['degree']
    cprint(editApp.first_name, 'green')
    session.add(editApp)
    session.commit()
    return{
        'success': True,
        'count': 1,
        'data': [{
            'first_name': editApp.first_name,
            'last_name': editApp.last_name,
            'position': editApp.position,
            'school': editApp.school,
            'degree': editApp.degree
        }]
    }


def delete_application(app_id):
    session = create_conn()
    deleteApp = session.query(Applicant).filter_by(id=app_id).one()
    session.delete(deleteApp)
    session.commit()
    return {
        'success': True,
        'data': []
    }


def close_db():
    conn = sqlite3.connect('applicant.db')
    conn.close()
