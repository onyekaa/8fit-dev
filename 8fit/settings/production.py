from .base import *

DEBUG = False
# Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()


try:
    from .local import *
except ImportError:
    pass
