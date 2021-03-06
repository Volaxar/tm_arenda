"""
Django settings for tmarenda project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

from tmarenda import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.secretkey

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'arenda.apps.ArendaConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'pipeline',
    'grid_images'
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

ROOT_URLCONF = 'tmarenda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'tmarenda.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': config.db_default,
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_URL = '/static/'
STATIC_ROOT = 'collectstatic/'

PIPELINE = {
    'PIPELINE_ENABLED': False,
    'JAVASCRIPT': {
        'main': {
            'source_filenames': (
                'arenda/js/js.coffee',
            ),
            'output_filename': 'js/main.js',
            'extra_context': {
                'defer': True
            }
        },
        'vendor': {
            'source_filenames': (
                'vendor/js/jquery-3.2.1.min.js',
                'vendor/js/lightslider.min.js',
                'vendor/js/lightgallery.min.js',
                'vendor/js/lg-thumbnail.min.js',
                'vendor/js/lg-zoom.min.js',
            ),
            'output_filename': 'js/vendor.js',
            'extra_context': {
                'defer': True
            }
        },
        'ltie9': {
            'source_filenames': (
                'vendor/js/ltie9/html5shiv.js',
                'vendor/js/ltie9/respond.js'
            ),
            'output_filename': 'js/ltie9.js',
            'extra_context': {
                'defer': True
            }
        }
    },
    'STYLESHEETS': {
        'main': {
            'source_filenames': (
                'arenda/css/style.scss',
            ),
            'output_filename': 'css/main.css',
            'extra_context': {
                'media': 'all',
            },
        },
        'vendor': {
            'source_filenames': (
                'vendor/css/lightslider.min.css',
                'vendor/css/lightgallery.min.css',
            ),
            'output_filename': 'css/vendor.css',
            'extra_context': {
                'media': 'all',
            },
        },
    },
    'COMPILERS': (
        'pipeline.compilers.sass.SASSCompiler',
        'pipeline.compilers.coffee.CoffeeScriptCompiler',
    ),
    'SASS_BINARY': '/home/vagrant/bin/sass',
    'COFFEE_SCRIPT_BINARY': '/home/vagrant/node_modules/coffee-script/bin/coffee',
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

UPLOAD_PHOTO_URL = 'photo'

YANDEX_UM = config.yandex_um

# Параметры почты

EMAIL_HOST = config.email['host']
EMAIL_HOST_USER = config.email['user']
EMAIL_HOST_PASSWORD = config.email['password']
EMAIL_SENDER = config.email['sender']
EMAIL_COPY_TO = config.email['copyto']
