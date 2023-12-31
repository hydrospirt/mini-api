"""
Django settings for mini_drive project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import logging
import os
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'],


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'services.apps.ServicesConfig',
    'files.apps.FilesConfig',
    'rest_framework',
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

ROOT_URLCONF = 'mini_drive.urls'

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

WSGI_APPLICATION = 'mini_drive.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# API VERSION
API_VERSION = 'v1/'

# Settings For Google API

EMAIL_USER = os.environ['YOUR_EMAIL']

INFO = {
    'type': os.environ['TYPE'],
    'project_id': os.environ['PROJECT_ID'],
    'private_key_id': os.environ['PRIVATE_KEY_ID'],
    'private_key': os.environ['PRIVATE_KEY'],
    'client_email': os.environ['CLIENT_EMAIL'],
    'client_id': os.environ['CLIENT_ID'],
    'auth_uri': os.environ['AUTH_URI'],
    'token_uri': os.environ['TOKEN_URI'],
    'auth_provider_x509_cert_url': os.environ['AUTH_PROVIDER_X509_CERT_URL'],
    'client_x509_cert_url': os.environ['CLIENT_X509_CERT_URL']
}

# For logging
os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)
LOGS_DIR = os.path.join(BASE_DIR, "logs", "api_docs.log")
FORMAT_LOGRECORD = (
    "%(asctime)s [%(levelname)s] %(message)s, "
    "%(funcName)s: %(lineno)s"
)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "main_format": {
            "format": FORMAT_LOGRECORD,
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "main_format",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "main_format",
            "filename": LOGS_DIR,
            "mode": "w",
            "encoding": "utf-8",
            "backupCount": 5,
            "maxBytes": 4999999
        },
    },
    "loggers": {
        "main": {
            "handlers": ["console", "file"],
            "level": "INFO" if not DEBUG else "DEBUG",
            "propagrate": True,
        },
    },
}
logger = logging.getLogger("main")
