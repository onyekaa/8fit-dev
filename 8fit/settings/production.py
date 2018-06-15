from .base import *

DEBUG = False

import os

SECRET_KEY = os.environ['SECRET_KEY']

import django_heroku
import dj_database_url
django_heroku.settings(locals())


try:
    from .local import *
except ImportError:
    pass
