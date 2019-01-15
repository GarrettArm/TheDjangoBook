import os

from .base import *


DEBUG = True

SECRET_KEY = '386$!xv=xbqfw42#!#a*1zq+wo5^u(_v=y_%-myi&(yb)06pd_'

ALLOWED_HOSTS = ['*', ]

INTERNAL_IPS = ['127.0.0.1', 'localhost', ]

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = '../static'

MEDIA_ROOT = '../media'
MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'runserver_db',
    }
}

INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
