from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0)baa^zd92m)(nfd3304wjdbr*^6=%_gx^*0f8c+nt@@_%fh3u'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

# Use sqlite locally

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


try:
    from .local import *
except ImportError:
    pass
