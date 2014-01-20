#!/usr/bin/env python

"""
settings.py

Critical settings for Django.
Further information @ docs.djangoproject.com

"""

__author__      = "Keir 'Kaffo' Smith, Josh 'prtscr' McGhee"
__copyright__   = "Copyright 2014, Apoapsis"
__version__     = "0.1"
__status__      = "Development"

# Operating System -------------------------------------------------------------

import os
BASE_DIR        = os.path.dirname(os.path.dirname(__file__))

# Security Options -------------------------------------------------------------

SECRET_KEY      = ')=xths&sz@l5b=bad1scqy1y#el8i0_-y78ei%x!g5-!08bil1'
DEBUG           = True
TEMPLATE_DEBUG  = True
TEMPLATE_DIRS   = (os.path.join(BASE_DIR, "templates"),)
ALLOWED_HOSTS   = []

# Location of Media Files ------------------------------------------------------

MEDIA_ROOT      = os.path.join(BASE_DIR, "media")
MEDIA_URL       = '/media/'

# Installed Applications -------------------------------------------------------

INSTALLED_APPS  = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'game',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF        = 'wizards.urls'
WSGI_APPLICATION    = 'wizards.wsgi.application'

# Store Static URLs ------------------------------------------------------------

STATIC_ROOT         = os.path.join(BASE_DIR, 'static')
STATIC_URL          = '/static/'
STATICFILES_DIRS    = (os.path.join(BASE_DIR, 'staticfiles'),)

LOGIN_URL           = '/wizards/login'

# Set Default Database to SQLite3 ----------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalisation Options -------------------------------------------------

LANGUAGE_CODE   = 'en-'
TIME_ZONE       = 'UTC'
USE_I18N        = True
USE_L10N        = True
USE_TZ          = True
