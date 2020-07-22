from .base import *

DEBUG = False
ADMINS = (
    ('Peter B', 'shell.appointment@gmail.com')
)

# ALLOWED_HOSTS = ['*']
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'educa',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#     }
# }

ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'OPTIONS': {
        #     'read_default_file': '/etc/mysql/my.cnf',
        # },
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'educa',
    }
}

# sudo uwsgi --module=educa.wsgi:application --env=DJANGO_SETTINGS_MODULE=educa.settings.pro --master --pidfile=/tmp/project-master.pid --http=127.0.0.1:8000 --uid=1000 --virtualenv=/home/educa/educaenv/ --plugin=python3

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
