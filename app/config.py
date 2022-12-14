import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))


class Config:
    # SECRET
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'

    # DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, '../app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MAIL
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = [os.environ.get('ADMINS', '').split(' ')]

    # PAGINATION SETTINGS
    POSTS_PER_PAGE = 5

    # PROJECT SETTINGS
    PROJECT_NAME = os.environ.get('PROJECT_NAME')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'
