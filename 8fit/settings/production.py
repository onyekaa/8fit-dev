from .base import *

DEBUG = True

import os

SECRET_KEY = os.environ['SECRET_KEY']

import django_heroku
import dj_database_url
django_heroku.settings(locals())


INSTALLED_APPS += (
    'storages',
)

try:
    from .local import *
except ImportError:
    pass

###################################
# s3 storage
###################################

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_STORAGE_BUCKET_NAME = 'ony-heroku-dev'

S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = S3_URL
S3_USE_SIGV4 = True
AWS_S3_HOST = 's3.eu-west-2.amazonaws.com'
AWS_S3_REGION_NAME = 'eu-west-2'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_FILE_OVERWRITE = True
AWS_QUERYSTRING_AUTH = False

AWS_ACCESS_KEY_ID = os.environ['AWS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SKEY']
