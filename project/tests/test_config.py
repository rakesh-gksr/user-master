# project/tests/test_config.py


import os
import unittest

from flask import current_app
from flask_testing import TestCase
import pytest
from project import create_app

app = create_app()

SECRET_KEY = "qn1p7wyfd%)-yh$_x+(b2a&+ys1$ph)9@tnq06hmgp^bfq11@g"
DATABASE_URL = "postgresql://postgres:django1234@localhost:5433/user_master"

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        print os.environ.get('REPORTING_SPLUNK')
        print "************"
        print app.config
        self.assertTrue(
            app.config['SECRET_KEY'] == SECRET_KEY
        )
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == DATABASE_URL
        )
        self.assertTrue(app.config['BCRYPT_LOG_ROUNDS'] == 4)
        self.assertTrue(app.config['TOKEN_EXPIRATION_DAYS'] == 30)
        self.assertTrue(app.config['TOKEN_EXPIRATION_SECONDS'] == 0)

# class TestTestingConfig(TestCase):
#     def create_app(self):
#         app.config.from_object('project.config.TestingConfig')
#         return app
#
#     def test_app_is_testing(self):
#         self.assertTrue(
#             app.config['SECRET_KEY'] == SECRET_KEY
#         )
#         self.assertTrue(app.config['DEBUG'])
#         self.assertTrue(app.config['TESTING'])
#         self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
#         self.assertTrue(
#             app.config['SQLALCHEMY_DATABASE_URI'] == DATABASE_URL
#         )
#         self.assertTrue(app.config['BCRYPT_LOG_ROUNDS'] == 4)
#         self.assertTrue(app.config['TOKEN_EXPIRATION_DAYS'] == 0)
#         self.assertTrue(app.config['TOKEN_EXPIRATION_SECONDS'] == 3)
#
# class TestProductionConfig(TestCase):
#     def create_app(self):
#         app.config.from_object('project.config.ProductionConfig')
#         return app
#
#     def test_app_is_production(self):
#         self.assertTrue(
#             app.config['SECRET_KEY'] == SECRET_KEY
#         )
#         self.assertFalse(app.config['DEBUG'])
#         self.assertFalse(app.config['TESTING'])
#         self.assertTrue(app.config['BCRYPT_LOG_ROUNDS'] == 13)
#         self.assertTrue(app.config['TOKEN_EXPIRATION_DAYS'] == 30)
#         self.assertTrue(app.config['TOKEN_EXPIRATION_SECONDS'] == 0)


if __name__ == '__main__':
    unittest.main()
