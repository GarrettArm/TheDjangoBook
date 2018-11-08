from .base import *
import os


SECRET_KEY = os.environ['PROD_SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['18.188.30.182', 'gaularmstrong.com', 'www.gaularmstrong.com', '*']


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = '/var/www/django/static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

MEDIA_ROOT = '/var/www/django/media'
MEDIA_URL = '/media/'

INTERNAL_IPS = ['127.0.0.1', ]
