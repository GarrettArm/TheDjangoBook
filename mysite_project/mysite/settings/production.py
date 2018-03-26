from .base import *

with open('../../django_secret_key.txt', 'r') as f:
    SECRET_KEY = f.read().strip()

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = '/var/www/django/static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'prod.sqlite3'),
    }
}

MEDIA_ROOT = '/var/www/django/media'
MEDIA_URL = '/media/'

INTERNAL_IPS = ['127.0.0.1', ]
