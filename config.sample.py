import os

SECRET_KEY = ''
DEBUG = True

CACHE_TYPE = 'simple'

SQLALCHEMY_DATABASE_URI = ''

CSRF_ENABLED = True
CSRF_SESSION_KEY = ''

SECURITY_POST_LOGIN_VIEW = '/terminal/'

SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_TRACKABLE = True

SECURITY_EMAIL_SENDER = ''
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_CONFIRM_SALT = ''
SECURITY_RESET_SALT = ''
SECURITY_LOGIN_SALT = ''
SECURITY_REMEMBER_SALT = ''

MAIL_SERVER = ''
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''

GOOGLE_ANALYTICS_ACCOUNT = ''

del os