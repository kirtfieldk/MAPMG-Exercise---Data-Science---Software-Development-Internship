from project import app, db
from flask import json
import unittest
import os


# ###############
###TEST CASES####
#################
TEST_DB = "applicants-collection"

print(os.path)


class TestCase(unittest.TestCase):
     # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        #     os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        # db.drop_all()
        # db.create_all()

        # # Disable sending emails during unit testing
        # mail.init_app(app)
        # self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    def test_index(self):
        tester = app.test_client(self)
        res = tester.get('/api/v1/applicants', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_index_without_json(self):
        tester = app.test_client(self)
        res = tester.get('/api/v1/applicants', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_fetch_application(self):
        tester = app.test_client(self)
        res = tester.get('/api/v1/applicants/22',
                         content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_fetch_application_nonexist(self):
        tester = app.test_client(self)
        res = tester.get('/api/v1/applicants/200',
                         content_type='application/json')
        self.assertEqual(res.status_code, 404)

    def test_delete_nonexisting_index(self):
        tester = app.test_client(self)
        res = tester.delete('/api/v1/applicants/200 ',
                            content_type='application/json')
        self.assertEqual(res.status_code, 404)

    def test_delete_exists_index(self):
        tester = app.test_client(self)
        res = tester.delete('/api/v1/applicants/35',
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_fetch_application_nonexist_after_delete(self):
        tester = app.test_client(self)
        res = tester.get('/api/v1/applicants/2',
                         content_type='application/json')
        self.assertEqual(res.status_code, 404)

    def test_post_app(self):
        tester = app.test_client(self)
        res = self.app.post(
            '/api/v1/applicants',
            data=json.dumps(dict(first_name='bar', last_name="Kirtfield",
                                 school='VCU', position='dev engineer', degree='eyesight')),
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(res.status_code, 201)

    def test_update_some_prop(self):
        tester = app.test_client(self)
        res = self.app.put(
            '/api/v1/applicants/7',
            data=json.dumps(dict(first_name='bar')),
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(res.status_code, 200)

    def test_update_all_prop(self):
        tester = app.test_client(self)
        res = self.app.put(
            '/api/v1/applicants/7',
            data=json.dumps(dict(first_name='bar', last_name="Kirtfield",
                                 school='VCU', position='dev engineer', degree='eyesight')),
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(res.status_code, 200)

    # def test_post_multiple_app(self):
    #     tester = app.test_client(self)
    #     res = self.app.post(
    #         '/api/v1/applicants',
    #         data=json.dumps(dict(first_name='bar', last_name="Kirtfield",
    #                              school='VCU', position='dev engineer', degree='eyesight'),
    #                         dict(first_name='bar', last_name="Kirtfield",
    #                              school='VCU', position='dev engineer', degree='eyesight')),
    #         content_type='application/json',
    #         follow_redirects=True)

    #     self.assertEqual(res.status_code, 201)
    ###########################
    ##TEST POST IN PUT METHOD##
    ###########################
    def test_wrong_method(self):
        tester = app.test_client(self)
        res = self.app.post(
            '/api/v1/applicants/7',
            data=json.dumps(dict(first_name='bar', last_name="Kirtfield",
                                 school='VCU', position='dev engineer', degree='eyesight')),
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(res.status_code, 405)
    ###########################
    ##TEST POST IN GET METHOD##
    ###########################

    def test_wrong_method_post_in_get(self):
        tester = app.test_client(self)
        res = self.app.post(
            '/api/v1/applicants/7',
            data=json.dumps(dict(first_name='bar', last_name="Kirtfield",
                                 school='VCU', position='dev engineer', degree='eyesight')),
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(res.status_code, 405)
    ###########################
    ##TEST PUT IN GET METHOD###
    ###########################

    def test_wrong_method_put_in_get(self):
        tester = app.test_client(self)
        res = self.app.put(
            '/api/v1/applicants',
            data=json.dumps(dict(first_name='bar', last_name="Kirtfield",
                                 school='VCU', position='dev engineer', degree='eyesight')),
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(res.status_code, 405)

    ###########################
    ##TEST PUT WITH EMPTY######
    ###########################

    def test_wrong_method_put_empty(self):
        tester = app.test_client(self)
        res = self.app.put(
            '/api/v1/applicants',
            data=json.dumps(dict()),
            content_type='application/json',
            follow_redirects=True
        )
        self.assertEqual(res.status_code, 405)


if __name__ == '__main__':
    unittest.main()
