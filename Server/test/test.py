import os
import unittest
# from models.item import ItemModel
# from Server.applicants import Applicant
# from database import add_application
from db import db

TEST_DB = 'applicants-collections.db'


class Tester(unittest.TestCase):
    # Execute before each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()

        db.session.drop_all()
        db.session.create_all()


def test_main_page(self):
    response = self.app.get('/', follow_redirects=True)
    self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
