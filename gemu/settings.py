"""
Django settings for gemu project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # django-allauth: needs this from django
    # http://django-allauth.readthedocs.io/en/latest/installation.html#django
    'django.contrib.auth',
    'django.contrib.sites',
    # Django: Humanize to make more pretty some numbers.
    #https://docs.djangoproject.com/en/2.0/ref/contrib/humanize/
    'django.contrib.humanize',
    # django-allauth: Importing aplication
    # http://django-allauth.readthedocs.io/en/latest/installation.html#django
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # django-bootstrap4: Importing aplication
    'bootstrap4',
    # easy_thumbnails: Importing Aplication
    'easy_thumbnails',
    # django-activity-stream: Importing Aplication
    'actstream',
    # pinax-messages: Importing Aplication
    # https://github.com/pinax/pinax-messages
    'pinax.messages',
    # Gemu: Applications
    'core',
]
# django-allauth: Using Site ID
# http://django-allauth.readthedocs.io/en/latest/installation.html#django
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'gemu.urls'
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
                # django-allauth: needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]
WSGI_APPLICATION = 'gemu.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
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

# django-allauth: Authentication Backends
# http://django-allauth.readthedocs.io/en/latest/installation.html#django
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# django-allauth: Log In/Log Out redirection
# http://django-allauth.readthedocs.io/en/latest/configuration.html
LOGIN_REDIRECT_URL = 'timeline_following'

# django-allauth: Email Registration Delivery
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gemu.io.app@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'gemu.io.app@gmail.com'

# django-allauth: Sign Up Validation
ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_BLACKLIST = ['admin']
ACCOUNT_USERNAME_MIN_LENGTH = 4

# easy-thumbnails: Extension when a image its transparent.
THUMBNAIL_TRANSPARENCY_EXTENSION = 'png'

# easy-thumbnails: Every size for all images.
THUMBNAIL_ALIASES = {
    '': {
        'header': {'size': (825, 312), 'crop': 'smart', 'upscale' : True},
        'header_255x143': {'size': (255, 143), 'crop': 'smart', 'upscale' : True},
        'avatar': {'size': (255, 255), 'crop': 'smart', 'upscale' : True},
        'avatar_50x50': {'size': (50, 50), 'crop': 'smart', 'upscale' : True},
        'avatar_explore': {'size': (65, 65), 'crop': 'smart', 'upscale' : True},
        'post': {'size': (540, 0), 'crop': 'smart', 'upscale' : True},
    },
}
# easy_thumbnails: Renaming the image uploads.
THUMBNAIL_NAMER = 'easy_thumbnails.namers.hashed'

# django-heroku: Activate Django-Heroku.
import django_heroku 
django_heroku.settings(locals())