"""
Django settings for blockserver project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os, socket, sys
from os.path import join as pathjoin, exists as pathexists
from json import loads as jloads

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zyh@tj847wsq$p921d1s%m_q!md_#(b$87%swe4q$*%cuw8ike'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blockserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blockserver.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

CACHE_LONG_TIMEOUT = 3600*24
CACHE_SHORT_TIMEOUT = 3600 / 2
CACHE_ONE_MINUTE_TIMEOUT = 60
CACHE_LATEST_TIMEOUT = 60 * 2
CACHE_TOP_TIMEOUT = 60 * 2
CACHE_HOT_TIMEOUT = 60 * 2
CACHE_DAY_TIMEOUT = 3600 * 24
CACHE_VCODE_EXPIRE_TIME = 30
CACHE_SHARE_EXPIRE_TIME = 60

SITE_CONFIG = {}
CACHES = {}
# custom settings
def load_config(config_path):
    global SITE_CONFIG
    if not pathexists(config_path):
        sys.stderr.write('Can not get config file %s\n' % config_path)
    else:
        with open(config_path) as fp:
            config = jloads(fp.read())
        SITE_CONFIG.update(config)

def load_caches(caches_path):
    global CACHES
    if not pathexists(caches_path):
        sys.stderr.write('Can not get caches file %s\n' % caches_path)
    else:
        with open(caches_path) as fp:
            config = jloads(fp.read())
        CACHES.update(config)
TEST_MODE = 'test' in sys.argv or pathexists(pathjoin(BASE_DIR, '.localdb'))
RUNSERVER_MODE = 'runserver' in sys.argv or 'runsrv' in sys.argv
RUNSERVER_VERBOSE_MODE = 'runserver' in sys.argv

import re
import platform
hostname = platform.node()

if re.compile(r'^online').match(hostname):
    print('run on online idc, hostname(%s)' % hostname)
    config_name = 'siteconfig-online.json'
    caches_name = 'caches-online.json'
    ENV_MODE_BLOCKSERVER = 'online'
elif re.compile(r'^pre').match(hostname):
    print('run on pre idc, hostname(%s)' % hostname)
    if TEST_MODE:
        # 测试运行环境！不使用正式数据库
        config_name = 'siteconfig-uat.json'
        caches_name = 'caches-uat.json'
    else:
        # 正常运行环境，使用正式数据库
        config_name = 'siteconfig-pre.json'
        caches_name = 'caches-pre.json'
    ENV_MODE_BLOCKSERVER = 'pre'
elif re.compile(r'^uat').match(hostname):
    print('run on uat idc, hostname(%s)' % hostname)
    config_name = 'siteconfig-uat.json'
    caches_name = 'caches-uat.json'
    ENV_MODE_BLOCKSERVER = 'uat'
else:
    print('run on localhost idc??, hostname(%s)' % hostname)
    config_name = 'siteconfig-localhost.json'
    caches_name = 'caches-localhost.json'
    ENV_MODE_BLOCKSERVER = 'localhost'

print('loading %s %s' % (config_name, caches_name))
load_config(pathjoin(BASE_DIR, '..', 'conf', config_name))
load_caches(pathjoin(BASE_DIR, '..', 'conf', caches_name))
THREADS_PERPAGE = 20
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 5,
    'MARGIN_PAGES_DISPLAYED': 2,
}
# site custom settings
INSTALLED_APPS.extend((
    'djcom',
    'blockdjcom',
    'blockserver',
    'blockmanage',
    ))


# email configuration
EMAIL_HOST = 'smtp.qq.com'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_USER = 'admin@test.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = u'[blockserver]'
#EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# TEMPLATES[0]['OPTIONS']['context_processors'].extend((
    #'device.context_processors.templatevars',
#     )
# )

TEST_RUNNER = 'blockdjcom.testrunner.NoDbTestRunner'
if TEST_MODE:
    print('use local db')
    idc = SITE_CONFIG['idc']
    if idc == 'online':
        raise RuntimeError('Can not run test on online env!!!')

    if 'NoDbTestRunner' not in TEST_RUNNER:
        raise RuntimeError('Can not do test with database recreate in testcases!!!')

    if idc not in ('pre', 'uat', 'localhost'):
        raise RuntimeError('unknown idc(%s)' % idc)

    if 'DATABASES' not in SITE_CONFIG:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db-bookserver.sqlite3'),
                'OPTIONS': {
                    'timeout': 5,
                }
            }
        }
    else:
        DATABASES = SITE_CONFIG.get('DATABASES')
else:
    print('use remote db')
    if 'DATABASES' not in SITE_CONFIG:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'bookserver',
                'USER': 'bookserver',
                'PASSWORD': 'aabbccddeeff',
                'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
                'PORT': '3306',
                'CONN_MAX_AGE': 7200,
            }
        }
    else:
        DATABASES = SITE_CONFIG.get('DATABASES')

#SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

SITE_DOMAIN = ''
SITE_URL = ''
SITE_NAME = ''

DATABASE_ROUTERS = ['blockdjcom.router.DbRouter', ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        #'special': {
        #    '()': 'project.logging.SpecialFilter',
        #    'foo': 'bar',
        #},
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        #    'filters': ['special']
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/data/logs/blockserver/blockserver.log',
            'formatter': 'verbose',
			'maxBytes': 100 * 1024 * 1024,
			'backupCount': 30,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file','console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

