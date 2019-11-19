# App class
from flask import jsonify
from db import db

from models.positions import Positions
from models.errors import Errors


class Applicant(db.Model):
    __tablename__ = 'applicants'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    position = db.relationship('Positions', backref='applicant', lazy=True)
    school = db.Column(db.String(250), nullable=False)
    degree = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime)

    def __init__(self, first_name, last_name, school, degree, date):
        self.first_name = first_name
        self.last_name = last_name
        self.school = school
        self.degree = degree
        self.date = date

    def to_json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'school': self.school,
            'position': {
                'title': self.position[0].title
            },
            'degree': self.degree,
            'date': self.date
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, req):
        for x in req:
            if x == 'first_name' and req[x] != self.first_name:
                self.first_name = req[x]
            if x == 'last_name' and req[x] != self.last_name:
                self.last_name = req[x]
            if x == 'position' and req[x] != self.position[0].title:
                pos = Positions(title=req[x].lower(), applicant=self)
                if pos.check_error():
                    pass
                else:
                    self.position[0].title = req[x]
            if x == 'school' and req[x] != self.school:
                self.school = req[x]
            if x == 'degree' and req[x] != self.degree:
                self.degree = req[x]
    @classmethod
    def find_by_id(cls, id):
        try:
            application = cls.query.filter_by(id=id).first()
            return jsonify({
                'success': True,
                'count': 1,
                'data': application.to_json()
            }), 200
        except AttributeError:
            return Errors('Unable To Find Application', 404).to_json()
    @classmethod
    def find_by_school(cls, school):
        school = school.lower()
        try:
            response = cls.query.filter_by(school=school).all()
            return jsonify({
                'success': True,
                'count': len(response),
                'data': list(map(lambda x: x.to_json(), response))
            }), 200
        except AttributeError:
            return Errors('Unable To Search Applications with School'.format(school), 404).to_json()
        
    @classmethod
    def find_by_lastname(cls, lastname):
        lastname = lastname.lower()
        try:
            response = cls.query.filter_by(last_name=lastname).all()
            return jsonify({
                'success': True,
                'count': len(response),
                'data': list(map(lambda x: x.to_json(), response))
            }), 200
        except AttributeError:
            return Errors('Unable To Search Application with Last Name: {}'.format(lastname), 404).to_json()