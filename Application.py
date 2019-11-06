import sys
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Applcation(Base):
    __tablename__ = 'applicants'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    position = Column(String(250), nullable=False)
    school = Column(String(250), nullable=False)
    degree = Column(String(250), nullable=False)
    date = Column(DateTime())


# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///applicants-collection.db')

Base.metadata.create_all(engine)
