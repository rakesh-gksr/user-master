# project/config.py


import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))


class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "qn1p7wyfd%)-yh$_x+(b2a&+ys1$ph)9@tnq06hmgp^bfq11@g"
    BCRYPT_LOG_ROUNDS = 13
    TOKEN_EXPIRATION_DAYS = 30
    TOKEN_EXPIRATION_SECONDS = 160
    TEST_ENV = os.environ.get('SECRET_KEY', 'hello')
    DATABASE_URL = os.environ.get('DATABASE_URL')


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URL = os.environ.get('DATABASE_URL')
    BCRYPT_LOG_ROUNDS = 4


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URL = os.environ.get('DATABASE_URL')
    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRATION_DAYS = 0
    TOKEN_EXPIRATION_SECONDS = 160


class StagingConfig(BaseConfig):
    """Staging configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URL = os.environ.get('DATABASE_URL')


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URL = os.environ.get('DATABASE_URL')
