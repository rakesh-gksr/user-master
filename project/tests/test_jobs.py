# project/tests/test_users.py


import json
import datetime

from project import db
from project.api.models.users import User
from project.tests.base import BaseTestCase
from project.tests.utils import add_user


class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_add_job(self):
        """Ensure a new user can be added to the database."""
        # add_user('test', 'test@test.com', 'test')
        # # update user
        # user = User.query.filter_by(email='test@test.com').first()
        # user.admin = True
        # db.session.commit()
        with self.client:
            # user login
            # resp_login = self.client.post(
            #     '/auth/login',
            #     data=json.dumps(dict(
            #         email='test@test.com',
            #         password='test'
            #     )),
            #     content_type='application/json'
            # )
            response = self.client.post(
                '/jobs',
                data=json.dumps(dict(
                    content='Hello this is test job',
                    user_id='1',
                    job_desc='this is job description'
                )),
                content_type='application/json',
                # headers=dict(
                #     Authorization='Bearer ' + json.loads(
                #         resp_login.data.decode()
                #     )['auth_token']
                # )
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('was added!', data['message'])
            self.assertIn('success', data['status'])
