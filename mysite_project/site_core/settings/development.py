import os

from .base import *


DEBUG = True

SECRET_KEY = '386$!xv=xbqfw42#!#a*1zq+wo5^u(_v=y_%-myi&(yb)06pd_'

# INSTALLED_APPS += ['debug_toolbar', ]

# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

INTERNAL_IPS = ['127.0.0.1', 'localhost', ]
