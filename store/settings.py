from .common import *
import os
from celery.schedules import crontab
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = 'from@alexbuy.com'

ADMINS = [
    ('Alex', 'admin@alex.com')
]






# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'djoser',
    'debug_toolbar',
    'corsheaders',
    'playground',
    'storeapp',
    'core',
    'tags' ,
    'likes' ,
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",

]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8001',
    'http://127.0.0.1:8001',
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


ROOT_URLCONF = 'store.urls'

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

WSGI_APPLICATION = 'store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases




# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = env.str("STATIC_URL",default='/static/')
STATIC_ROOT = env.str('STATIC_ROOT', default=BASE_DIR / 'staticfiles')
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = DEBUG


MEDIA_ROOT = env.str('MEDIA_ROOT', default=BASE_DIR / 'media')
MEDIA_URL = env.str("MEDIA_PATH",default='/media/')

CELERY_BROKER_URL = 'redis://localhost:6379/1'

CELERY_BEAT_SCHEDULE = {
    'notify_customers': {
        'task' : 'playground.tasks.notify_customers',
        'schedule' : 1,
        'args': ['Hello World'],
        
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING' : False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    }

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT')
}

AUTH_USER_MODEL = 'core.User'

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'core.serializers.UserCreateSerializer',
        'current_user': 'core.serializers.UserSerializer',
    }
}


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        'TIMEOUT': 10*60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : '{asctime} ({levelname}) - {name} - {message}',
            'style' : "{"
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        },
        'file': {
            'class' : 'logging.FileHandler',
            'filename' : 'general.log',
            'formatter': 'verbose',
        }
    },
    'loggers' : {
        '': {
            'handlers': ['console', 'file'],
            'level': os.environ.get('DJANGO_LOG_LEVEL','INFO')
        }
    },
    
}

SECURE_PROXY_SSL_HEADER={"HTTP_X_FORWARDED_PROTO",'https' }


SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['*']  # specify hosts explicitly in production



# Install pymysql as MySQLdb

# Default settings for database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'store3',
        'USER': 'root',
        'PASSWORD': '50528911Wwe',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Check if DATABASE_URL is set and override default settings if it is
