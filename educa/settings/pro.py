from .base import *

DEBUG = False
ADMINS = (
    ('Peter B', 'shell.appointment@gmail.com')
)
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}
