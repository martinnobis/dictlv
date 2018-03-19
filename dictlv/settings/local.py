from .base import *

SECRET_KEY = '-j%%h$g^u8^!y5ei3d!$&gz$fpvkq&ws6+*_lb4w2_4u7%ut$9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS += ['django_nose']
INSTALLED_APPS += ['debug_toolbar']

INTERNAL_IPS = ['127.0.0.1']

TEST_RUNNER =  'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--nologcapture',
    '--cover-package=translations',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'translations',
        'USER': 'dictlv',
        'PASSWORD': os.environ['DICTLV_POSTGRES_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']