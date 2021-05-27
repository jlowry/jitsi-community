"""
Django settings for accountmanager project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from os import path, urandom
from pathlib import Path
from base64 import b64decode

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: the following settings are based on
#     manage.py check --deploy
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 5
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = urandom(32)
#key_path = path.join('/etc/meet-accountmanager', 'key')
#if path.isfile(key_path):
#    with open(key_path, 'r') as key_file:
#        SECRET_KEY = bytes.fromhex(key_file.read())
settings_file = r'/etc/meet-accountmanager/settings.py'
if path.isfile(settings_file):
    exec(open(settings_file).read())

if SECRET_KEY:
    SECRET_KEY = b64decode(SECRET_KEY)
else:
    SECRET_KEY = urandom(32)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'jitsi@publiccode.net'
#EMAIL_HOST_PASSWORD = '' #past the key or password app here
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'do-not-reply@publiccode.net'

#email_password_path = path.join('/etc/meet-accountmanager', 'email_password')
#if path.isfile(email_password_path):
#    with open(email_password_path, 'r') as email_password_file:
#        EMAIL_HOST_PASSWORD = email_password_file.read()

ALLOWED_HOSTS = ['*']

#REGISTRATION_ADMINS = [('Approval Needed', 'meet-community-approval@publiccode.net')]

# Application definition
# PASSWORD_HASHERS = [
#    'prosody_scram.hashers.ScramSha256PasswordHasher'
#]

INSTALLED_APPS = [
    'accounts',
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'bootstrap4',
]

ACCOUNT_ACTIVATION_DAYS = 3

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'accountmanager.urls'
# TODO: Setting the LOGIN_URL here is a work around because the
# login_required decorator is not applying the script name correctly.
LOGIN_URL = '/accountmanager/login/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

STATIC_ROOT = BASE_DIR / 'static2'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

WSGI_APPLICATION = 'accountmanager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/meet-accountmanager/database.cnf',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static2/'
