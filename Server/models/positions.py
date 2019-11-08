from db import db


class Positions(db.Model):
    __tablename__ = 'positions'

    position_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    app_id = db.Column(db.Integer, db.ForeignKey('applicants.id'))

    positions = ['dev intern', 'fisher', 'cook', 'hvac mechanic']

    def noMatch(self):
        if self.title is None:
            return True

    def toJson(self):
        return {
            'position': self.position
        }
