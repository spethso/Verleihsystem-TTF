"""Module containing default config values."""

from random import randint
import logging

class Config(object):
    DEBUG = False
    TESTING = False
    RESTPLUS_VALIDATE = True
    BCRYPT_HANDLE_LONG_PASSWORDS = True
    JWT_CLAIMS_IN_REFRESH_TOKEN = True
    JWT_SECRET_KEY = ''.join(hex(randint(0, 255))[2:] for i in range(16))
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WEBPACK_MANIFEST_PATH = './build/manifest.json'
    LOG_LEVEL = logging.INFO
    LOGGING = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(asctime)s [%(levelname)s] [%(name)-16s] %(message)s <%(module)s, \
                 %(funcName)s, %(lineno)s; %(pathname)s>',
            },
            'auth': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
            'lending': {
                'format': '%(asctime)s [%(levelname)s] %(message)s',
            }
        },
        'handlers': {
            'default': {
                'class' : 'logging.handlers.RotatingFileHandler',
                'formatter' : 'default',
                'filename': '/tmp/ttf-default.log',
                'maxBytes' : 104857600,
                'backupCount': 10,
            },
            'auth' : {
                'class' : 'logging.handlers.RotatingFileHandler',
                'formatter' : 'auth',
                'filename': '/tmp/ttf-auth.log',
                'maxBytes' : 104857600,
                'backupCount': 10,
            },
            'lending' : {
                'class' : 'logging.handlers.RotatingFileHandler',
                'formatter' : 'lending',
                'filename': '/tmp/ttf-lending.log',
                'maxBytes' : 104857600,
                'backupCount': 100,
            },
        },
        'loggers': {
            'auth': {
                'level': LOG_LEVEL,
                'propagate': False,
                'handlers': ['auth'],
            },
            'lending': {
                'level': LOG_LEVEL,
                'propagate': False,
                'handlers': ['lending'],
            },
            'task': {
                'level': LOG_LEVEL,
                'propagate': False,
                'handlers': ['default'],
            },
        },
        'root': {
            'level': LOG_LEVEL,
            'handlers': ['default'],
        },
        'disable_existing_loggers': True,
    }
    CELERY_BROKER_URL = 'amqp://localhost',
    CELERY_RESULT_BACKEND = 'rpc://'
    TMP_DIRECTORY = '/tmp'
    DATA_DIRECTORY = '/tmp'

    LOGIN_PROVIDERS = ['Basic']

    BASIC_AUTH_ADMIN_PASS = ''.join(hex(randint(0, 255))[2:] for i in range(8))
    BASIC_AUTH_MOD_PASS = ''.join(hex(randint(0, 255))[2:] for i in range(8))

    LDAP_URI = ""
    LDAP_PORT = 0
    LDAP_SSL = False
    LDAP_START_TLS = False
    LDAP_USER_SEARCH_BASE = ""
    LDAP_GROUP_SEARCH_BASE = ""
    LDAP_USER_RDN = ""
    LDAP_USER_UID_FIELD = ""
    LDAP_GROUP_MEMBERSHIP_FIELD = ""
    LDAP_MODERATOR_FILTER = ""
    LDAP_ADMIN_FILTER = ""
    LDAP_MODERATOR_GROUP_FILTER = ""
    LDAP_ADMIN_GROUP_FILTER = ""

    MONITOR_REQUEST_PERORMANCE = True
    LONG_REQUEST_THRESHHOLD = 1

    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = False
    RESTPLUS_JSON = {'indent': None}


class ProductionConfig(Config):
    pass


class DebugConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    JWT_SECRET_KEY = 'debug'
    LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_ECHO = True
    LOGIN_PROVIDERS = ['Debug']


class TestingConfig(Config):
    TESTING = True
