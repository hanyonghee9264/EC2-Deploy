from .base import *

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'wps9th.c3odv9dyz53u.ap-northeast-2.rds.amazonaws.com',
        'NAME': 'ec2_deploy',
        'USER': 'hanyonghee9264',
        'PASSWORD': 'han46633^^',
        'PORT': 5432,
    }
}
