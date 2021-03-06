"""
Django settings for blockserver project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os, socket, sys
from django.utils.translation import ugettext_lazy
from acom.utils.sysutil import isWindowsSystem, isLinuxSystem, isMacSystem
__builtins__['_'] = ugettext_lazy
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import join as pathjoin, exists as pathexists
from json import loads as jloads
from json import dump as jdump
from oscar.defaults import * 
from oscar import OSCAR_MAIN_TEMPLATE_DIR
from oscar import get_core_apps
from oscar_accounts import TEMPLATE_DIR as ACCOUNTS_TEMPLATE_DIR
#from oscar.defaults import *
#from oscar import OSCAR_MAIN_TEMPLATE_DIR
#from oscar import get_core_apps

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)
# Path helper
#location = lambda x: os.path.join(
#    os.path.dirname(os.path.realpath(__file__)), x)

if isWindowsSystem():
    DATA_DIR = r'C:\data'
    DATA1_DIR = r'C:\data1'
elif isLinuxSystem() or isMacSystem():
    DATA_DIR = '~/data'
    DATA1_DIR = '~/data1'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zyh@tj847wsq$p921d1s%m_q!md_#(b$87%swe4q$*%cuw8ike'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'captcha',
    'captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'semanticuiform',
    'pure_pagination',
    'blockuser',
    'debug_toolbar',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_celery_beat',
    'django_extensions',
    'widget_tweaks',
    'channels',
    # ... include the providers you want to enable:
    #'allauth.socialaccount.providers.telegram',
    #'allauth.socialaccount.providers.coinbase',
    #'allauth.socialaccount.providers.douban',
    #'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.gitlab',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.linkedin',
    #'allauth.socialaccount.providers.linkedin_oauth2',
    #'allauth.socialaccount.providers.twitter',
    #'allauth.socialaccount.providers.weibo',
    #'allauth.socialaccount.providers.weixin',
] + get_core_apps()
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ['127.0.0.1', ]
def check_test(request):
    ips = ['127.0.0.1']
    fpath = pathjoin(BASE_DIR, 'debugips.txt')
    if pathexists(fpath):
        with open(fpath, 'rt') as fp:
            for line in fp.readlines():
                ips.append(line.strip())
    if request.META.get('REMOTE_ADDR', None) in ips:
        return True
    else:
        return False
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': check_test
}

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'blockserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 OSCAR_MAIN_TEMPLATE_DIR,
                 ACCOUNTS_TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'blockserver.context_processors.templatevars',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
# enable to cache template files
#             'loaders': [
#                 ('django.template.loaders.cached.Loader', [
#                     'django.template.loaders.filesystem.Loader',
#                     'django.template.loaders.app_directories.Loader',
#                 ]),
#             ],
        'builtins': ['semanticuiform.templatetags.semanticui',
                     'blockserver.templatetags.commontags']
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

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_URL = '/static/'
MEDIA_ROOT = location("media")
MEDIA_URL = '/media/'
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
LOGGING = {}
MONGO = {}
# custom settings
def load_config(config_path, config={}):
    if not pathexists(config_path):
        sys.stderr.write('Can not get config file %s\n' % config_path)
    else:
        with open(config_path) as fp:
            item = jloads(fp.read())
        config.update(item)

def update_config(config_path, config={}):
    with open(config_path, 'w') as fp:
        jdump(config, fp)
        
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
    mongo_name = 'mongo-online.json'
    ENV_MODE_BLOCKSERVER = 'online'
elif re.compile(r'^pre').match(hostname):
    print('run on pre idc, hostname(%s)' % hostname)
    if TEST_MODE:
        # 测试运行环境！不使用正式数据库
        config_name = 'siteconfig-uat.json'
        caches_name = 'caches-uat.json'
        mongo_name = 'mongo-uat.json'
    else:
        # 正常运行环境，使用正式数据库
        config_name = 'siteconfig-pre.json'
        caches_name = 'caches-pre.json'
        mongo_name = 'mongo-pre.json'
    ENV_MODE_BLOCKSERVER = 'pre'
elif re.compile(r'^uat').match(hostname):
    print('run on uat idc, hostname(%s)' % hostname)
    config_name = 'siteconfig-uat.json'
    caches_name = 'caches-uat.json'
    mongo_name = 'mongo-uat.json'
    ENV_MODE_BLOCKSERVER = 'uat'
else:
    print('run on localhost idc??, hostname(%s)' % hostname)
    config_name = 'siteconfig-localhost.json'
    caches_name = 'caches-localhost.json'
    mongo_name = 'mongo-localhost.json'
    ENV_MODE_BLOCKSERVER = 'localhost'

print('loading %s %s %s' % (config_name, caches_name, mongo_name))
load_config(pathjoin(BASE_DIR, '..', 'conf', config_name), SITE_CONFIG)
load_config(pathjoin(BASE_DIR, '..', 'conf', caches_name), CACHES)
load_config(pathjoin(BASE_DIR, '..', 'conf', mongo_name), MONGO)
logsfile_name = 'loggings.json'
load_config(pathjoin(BASE_DIR, '..', 'conf', logsfile_name), LOGGING)

flags_name = 'blocks-flags.json'
FLAGS_PATH = pathjoin(BASE_DIR, '..', 'conf', flags_name)

THREADS_PERPAGE = 20
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 5,
    'MARGIN_PAGES_DISPLAYED': 2,
}

#AUTH_USER_MODEL = 'blockuser.BlockUser'
AUTHENTICATION_BACKENDS = (
                'django.contrib.auth.backends.RemoteUserBackend',
                'django.contrib.auth.backends.ModelBackend',
                'allauth.account.auth_backends.AuthenticationBackend',
                'oscar.apps.customer.auth_backends.EmailBackend',
                'django.contrib.auth.backends.ModelBackend',
                        )
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

ACCOUNT_FORMS = {
    'login': 'allauth.account.forms.LoginForm',
    'signup': 'allauth.account.forms.SignupForm',
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
}
# site custom settings
INSTALLED_APPS.extend((
    'djcom',
    'blockdjcom',
    'blockserver',
    'fcoin',
    'exwss',
    'oscar_accounts',
    'oscarapi',
    'rest_framework',
    'paypal',
    'blockoscar',
    'chat',
    'wslog',
    'sanjiao',
    'duiqiao'
    ))
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    },
   'google': {
    'SCOPE': [
        'profile',
        'email',
    ],
    'AUTH_PARAMS': {
        'access_type': 'online',
    }},
   'weixin': {
        'AUTHORIZE_URL': 'https://open.weixin.qq.com/connect/oauth2/authorize',  # for media platform
        'SCOPE': ['snsapi_base'],
    }
}

ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_EMAIL_VERIFICATION="mandatory"
# email configuration
EMAIL_HOST = 'smtp.qq.com'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_USER = '16260924@qq.com'
EMAIL_HOST_PASSWORD = 'wxhsttvfcopgbjcc'
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
                'NAME': os.path.join(BASE_DIR, 'db-exchangeserver.sqlite3'),
                'OPTIONS': {
                    'timeout': 5,
                }
            }
        }
    else:
#         DATABASES = SITE_CONFIG.get('DATABASES')
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db-exchangeserver.sqlite3'),
                'OPTIONS': {
                    'timeout': 5,
                },
                'TEST': {
                    'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3')
                }
            }
        }
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

SITE_ID  = 1
SITE_DOMAIN = '127.0.0.1:8000'
SITE_URL = 'http://127.0.0.1:8000/'
SITE_NAME = 'blockmangae'
DATABASE_ROUTERS = ['blockdjcom.router.DbRouter', ]

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ()
CORS_ORIGIN_REGEX_WHITELIST = ()

CELERY_BROKER_URL = 'amqp://admin:030973513@localhost:5672/myvhost'               # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  # 指定 Backend
#CELERY_TIMEZONE='Asia/Shanghai'                     # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'                             
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERYD_CONCURRENCY = 2

CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'tasks'
CELERY_DEFUALT_EXCHANGE_TYPE = 'topic'
CELERY_DEFAULT_ROUTING_KEY = 'task.default'
ENCRYPTED_FIELDS_KEYDIR = pathjoin(BASE_DIR, '..', 'fieldkeys') 

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}

OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': 'Accounts',
        'icon': 'icon-globe',
        'children': [
            {
                'label': 'Accounts',
                'url_name': 'accounts-list',
            },
            {
                'label': 'Transfers',
                'url_name': 'transfers-list',
            },
            {
                'label': 'Deferred income report',
                'url_name': 'report-deferred-income',
            },
            {
                'label': 'Profit/loss report',
                'url_name': 'report-profit-loss',
            },
        ]
    })

PAYPAL_API_USERNAME = 'test_xxxx.gmail.com'
PAYPAL_API_PASSWORD = '123456789'
PAYPAL_API_SIGNATURE = '...'
OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': 'PayPal',
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('Express transactions'),
                'url_name': 'paypal-express-list',
            },
        ]
    })
OSCAR_ALLOW_ANON_CHECKOUT = False

OSCAR_SHOP_NAME = 'BearQuant'
OSCAR_SHOP_TAGLINE = '专注数字通证资产量化策略开发'

# Taken from PayPal's documentation - these should always work in the sandbo
PAYPAL_CALLBACK_HTTPS = False
PAYPAL_API_VERSION = '119'

# These are the standard PayPal sandbox details from the docs - but I don't
# think you can get access to the merchant dashboard.
PAYPAL_API_USERNAME = 'sdk-three_api1.sdk.com'
PAYPAL_API_PASSWORD = 'QFZCWN5HZM8VBG7Q'
PAYPAL_API_SIGNATURE = 'A-IzJhZZjhg29XQ2qnhapuwxIDzyAZQ92FRP5dqBzVesOkzbdUONzmOU'

# Standard currency is GBP
PAYPAL_CURRENCY = PAYPAL_PAYFLOW_CURRENCY = 'GBP'
PAYPAL_PAYFLOW_DASHBOARD_FORMS = True

LOGIN_REDIRECT_URL = '/accounts/'

OSCAR_FROM_EMAIL= '16260924@qq.com'

ASGI_APPLICATION = "blockserver.routing.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
