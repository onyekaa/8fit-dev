from .base import *

DEBUG = False
# Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()

import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']


try:
    from .local import *
except ImportError:
    pass
