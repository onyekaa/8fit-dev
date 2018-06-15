from .base import *

DEBUG = False

import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

import django_heroku
import dj_database_url
django_heroku.settings(locals())


try:
    from .local import *
except ImportError:
    pass
