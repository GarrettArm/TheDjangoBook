import os

from .base import *


DEBUG = False

with open('secret_keys.env', 'r') as f:
    SECRET_KEY = f.read().strip()

ALLOWED_HOSTS = ['18.188.30.182', 'gaularmstrong.com', 'www.gaularmstrong.com', '*', ]

INTERNAL_IPS = ['127.0.0.1', ]

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = '/var/www/django/static'

MEDIA_ROOT = '/var/www/django/media'
MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
