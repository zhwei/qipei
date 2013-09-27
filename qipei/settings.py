#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Django settings for qipei project.
import os
DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DOMAIN = "http://qp.gotit.asia"
#DOMAIN = "http://210.44.176.58:8080"

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
    # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    # 'NAME': os.path.join(os.path.dirname(__file__), 'db/mysite.db').replace('\\','/'),                      # Or path to database file if using sqlite2
        'NAME': 'qqq',
    # Or path to database file if using sqlite2
        # The following settings are not used with sqlite3:
        'USER': 'root', #开发用
        'PASSWORD': 'group_0611',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh_CN'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(DIR, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(DIR, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '02ax4@b#0=6uqxzo199s9te3-h%e1e16%#a3pa!xp@bhei2pvs'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'qipei.apps.pagination',
    'qipei.apps.need',
    'qipei.apps.search',
    'qipei.apps.product',
    'qipei.apps.account',
    'qipei.apps.store',
    'qipei.apps.custom',
    'qipei.apps.forum',
    'mptt',
    'DjangoUeditor',
    'notifications',
    'upload_avatar',
    # 'ajax_upload',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'qipei.apps.pagination.middleware.PaginationMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'qipei.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'qipei.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(DIR, 'templates'),
    os.path.join(DIR, 'apps/account/templates'),
    os.path.join(DIR, 'apps/product/templates'),
    os.path.join(DIR, 'apps/store/templates'),
    os.path.join(DIR, 'apps/info/templates'),
    os.path.join(DIR, 'apps/welcome/templates'),
    os.path.join(DIR, 'apps/custom/templates'),
    os.path.join(DIR, 'apps/expert.bak/templates'),
    os.path.join(DIR, 'apps/forum/templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DIR, 'apps/layout'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    #"django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    #"django.core.context_processors.static",
    #"django.contrib.messages.context_processors.messages")
    "django.core.context_processors.request"
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# xapian
HAYSTACK_CONNECTIONS = {
    'default': {
    'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    'PATH': os.path.join(os.path.dirname(__file__), 'xapian_index'),
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'



# ueditor 设置

UEDITOR_SETTINGS={
        "toolbars": {           #定义多个工具栏显示的按钮，允行定义多个
            "simple": [[ 'source', '|','bold', 'italic', 'underline']],

            "common":[['source','|','undo', 'redo', '|','bold', 'italic',
                     'underline', 'autotypeset', '|', 'forecolor',
                     'backcolor','|', 'link', 'unlink','|','insertimage']],
            "list": [['insertorderedlist']],
            "img": [['insertimage']]
        },
        "images_upload": {
            "allow_type": "jpg,png",                            #定义允许的上传的图片类型
            "path": "ueditor_upload/image_upload",                 #定义默认的上传路径
            "max_size": "5000kb"                                #定义允许上传的图片大小, 不可以设置为0
        },
        "files_upload": {
            "allow_type": "zip,rar",   #定义允许的上传的文件类型
            "path": "ueditor_upload/file_upload",                   #定义默认的上传路径
            "max_size": "5000kb"       #定义允许上传的文件大小，不可以设置为0
        },
        "image_manager": {
            "path": ""         #图片管理器的位置,如果没有指定，默认跟图片路径上传一样
        },
        "scrawl_upload": {
            "path":""           #涂鸦图片默认的上传路径
        }
    }


# django-upload-avatar 设置

UPLOAD_AVATAR_UPLOAD_ROOT = os.path.join(DIR, 'media/avatars/upload')
UPLOAD_AVATAR_AVATAR_ROOT = os.path.join(DIR, 'media/avatars/cropped')
UPLOAD_AVATAR_URL_PREFIX_ORIGINAL = '/media/avatars/upload/'
UPLOAD_AVATAR_URL_PREFIX_CROPPED = '/media/avatars/cropped/'

UPLOAD_AVATAR_RESIZE_SIZE = [50, 100, 180]

UPLOAD_AVATAR_WEB_LAYOUT = {
    'preview_areas': [
        {
            'size': 50,
            'text': '最小预览'
        },
        {
            'size': 100,
            'text': '中等预览'
        },
        {
            'size': 180,
            'text': '最大预览'
        },
    ]
}
