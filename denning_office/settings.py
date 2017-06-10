#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Django settings for Opsclick project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6%yd7zq%dc=2e_$w2qa_!-(s%t*m^kr(82ke5=m-j*in2*ve*^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",

    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',

    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.stripe',

    # 'tinymce',
]

# Internal applications
INSTALLED_APPS += [
    'project',
    'api'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'denning_office.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'PAGE_SIZE': 10
}

# AUTHENTICATION_BACKENDS = (
#     # `allauth` specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',
# )

SITE_ID = 1

WSGI_APPLICATION = 'denning_office.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

'''DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'Denning_Office',
    'USER': 'root',
    'PASSWORD': 'root', 
    'HOST': 'localhost',
    # 'HOST': 'supercarreport.com',
    'PORT': 3306,
    }
}'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = ''
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4'}}

STATIC_URL = '/static/'

COUNTRY = [
             {"name": "USA", "flag": "us", "currency_rate": 1, "currency": "$"},
             {"name": "UK", "flag": "gb", "currency_rate": 0.8, "currency": "£"}, 
             {"name": "France", "flag": "fr", "currency_rate": 0.96, "currency": "€"}, 
             {"name": "Germany", "flag": "de", "currency_rate": 0.96, "currency": "€"}, 
             {"name": "Italy", "flag": "it", "currency_rate": 0.96, "currency": "€"}, 
             {"name": "Switzerland", "flag": "sz", "currency_rate": 1.03, "currency": "Fr"}, 
          ]

CURRENCY = {
             "USD": {"name": "USD", "currency_rate": 1, "currency": "$"},
             "EUR": {"name": "EUR", "currency_rate": 0.96, "currency": "€"},
             "GBP": {"name": "GBP", "currency_rate": 0.8, "currency": "£"},
             "CHF": {"name": "CHF", "currency_rate": 1.03, "currency": "Fr"},
          }

