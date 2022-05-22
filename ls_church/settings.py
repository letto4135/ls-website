"""
Django settings for ls_church project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import cloudinary
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
LOCAL = int(os.environ.get('IS_LOCAL_ENV', 1))

SECRET_KEY = os.environ.get('DJANGO_KEY', 'F190off40You(*&#$Piece983Of##$Junk34Qo91FOJ2o9{}P{:>OLP(*')

ALLOWED_HOSTS = [
    'ls-church-website.fly.dev',
    'localhost',
    '127.0.0.1',
    'test.libertystreetchurch.com',
    'test6.libertystreetchurch.com',
    'libertystreetchurch.com'
]

if LOCAL == 1:
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    }
else:
    # Connect to fly.io db
    DATABASES = {'default': dj_database_url.config(conn_max_age=600)}
    DEBUG = False




cloudinary.config(
    cloud_name=os.environ.get("CLOUD_NAME", "non-existent"),
    api_key=os.environ.get("CLOUD_KEY", "non-existent"),
    api_secret=os.environ.get("CLOUD_SECRET", "non-existent"),
    secure=True
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'captcha',
    'api',
    'frontend',
]

CAPTCHA_FONT_SIZE = 32
CAPTCHA_LENGTH = 6

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'ls_church.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': []
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

WSGI_APPLICATION = 'ls_church.wsgi.application'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
X_FRAME_OPTIONS = 'SAMEORIGIN'