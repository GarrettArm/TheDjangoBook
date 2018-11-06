from .base import *

with open('../../django_secret_key.txt', 'r') as f:
    SECRET_KEY = f.read().strip()

DEBUG = False

ALLOWED_HOSTS = ['18.188.30.182', 'gaularmstrong.com', 'www.gaularmstrong.com']


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
