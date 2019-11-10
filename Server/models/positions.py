# Position class
from db import db


class Positions(db.Model):
    __tablename__ = 'positions'

    position_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    app_id = db.Column(db.Integer, db.ForeignKey('applicants.id'))
    positions = ['dev intern', 'fisher', 'cook', 'hvac mechanic']

    def check_error(self):
        match = []
        for x in self.positions:
            if x == self.title.lower():
                match.append(x)
        if len(match) == 0:
            return True
        else:
            return False

    def open_positions(self):
        str = ""
        for x in self.positions:
            str = str + x + ", "
        return str

    def toJson(self):
        return {
            'position': self.title
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
