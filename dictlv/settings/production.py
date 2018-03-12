from .base import *

with open('/etc/dictlv_django_secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

DEBUG = False

ALLOWED_HOSTS = ['dictlv.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'let_trans',
        'USER': 'dictlv',
        'PASSWORD': os.environ['DICTLV_POSTGRES_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}