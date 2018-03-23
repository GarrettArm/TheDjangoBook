from .base import *


DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = '/var/www/django/static'

MEDIA_ROOT = '/var/www/django/media'
MEDIA_URL = '/media/'

INTERNAL_IPS = ['127.0.0.1', ]
