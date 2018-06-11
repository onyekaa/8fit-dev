from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0)baa^zd92m)(nfd3304wjdbr*^6=%_gx^*0f8c+nt@@_%fh3u'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']


# Honor the 'X-Forwarded-Proto' header for request.is_secure()


try:
    from .local import *
except ImportError:
    pass
