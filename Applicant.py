
# Keith Kirtfield
# Database
# TODO uploading and retrieving data // Smart Selection
import sqlite3


class Applicant():
    def __init__(self, first, last, school, position, degree):
        self.firstName = first
        self.lastName = last
        self.school = school
        self.position = position
        self.degree = degree

    def toJson(self):
        return {
            'first_name': self.firstName,
            'last_name': self.lastName,
            'school': self.school,
            'position': self.position,
            'degree': self.degree
        }

    def addToDatabase(self):
        self.databaseModify("add", -1)

    def deleteFromDatabase(self, id):
        self.databaseModify(self, id)

    def getApplicants(self):
        self.databaseModify(self, -1)

    def databaseModify(self, code, id):
        with sqlite3.connect('applicant.db') as conn:
            c = conn.cursor()
            if code == "add":
                c.execute(
                    'INSERT INTO applicants VALUES (?, ?, ?, ?, ?)', (
                        self.firstName, self.lastName, self.school, self.position, self.degree)
                )
                conn.commit()
            if code == "delete":
                c.execute('FROM applicants SELECT * WHERE app_id = ?', id)
                conn.commit()
            if code == "get":
                c.execute('SELECT * FROM applicants')
                print(c.fetchone())
        # conn.close()
