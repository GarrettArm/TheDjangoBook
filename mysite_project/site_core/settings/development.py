import os

from .base import *


DEBUG = True

SECRET_KEY = '386$!xv=xbqfw42#!#a*1zq+wo5^u(_v=y_%-myi&(yb)06pd_'

ALLOWED_HOSTS = ['*', ]

INTERNAL_IPS = ['127.0.0.1', 'localhost', ]

STATIC_ROOT = '/var/www/django/static'

MEDIA_ROOT = '/var/www/django/media'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
