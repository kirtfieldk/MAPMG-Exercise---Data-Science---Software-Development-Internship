import sys
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from termcolor import colored, cprint
Base = declarative_base()


class Applicant(Base):
    __tablename__ = 'applicants'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    position = Column(String(250), nullable=False)
    school = Column(String(250), nullable=False)
    degree = Column(String(250), nullable=False)
    date = Column(DateTime())

    def __init__(self, first_name, last_name, position, school, degree, date):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.school = school
        self.degree = degree
        self.date = date

    def toJson(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'school': self.school,
            'position': self.position,
            'degree': self.degree,
            'date': self.date
        }

    def update(self, req):
        cprint(req, 'green')
        for x in req:
            if x == 'first_name' and req[x] != self.first_name:
                self.first_name = req[x]
            if x == 'last_name' and req[x] != self.last_name:
                self.last_name = req[x]
            if x == 'position' and req[x] != self.position:
                self.position = req[x]
            if x == 'school' and req[x] != self.school:
                self.school = req[x]
            if x == 'degree' and req[x] != self.degree:
                self.degree = req[x]


        # creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///applicants-collection.db')

Base.metadata.create_all(engine)
