# App class
from db import db


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

    def toJson(self):
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

    def update(self, req):
        for x in req:
            if x == 'first_name' and req[x] != self.first_name:
                self.first_name = req[x]
            if x == 'last_name' and req[x] != self.last_name:
                self.last_name = req[x]
            if x == 'position' and req[x] != self.position[0].title:
                self.position[0].title = req[x]
            if x == 'school' and req[x] != self.school:
                self.school = req[x]
            if x == 'degree' and req[x] != self.degree:
                self.degree = req[x]
