from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@t^wli-mv_h98)vptcmwcnw-*z(ayl61n3+)bs)*jgmf38b4t5'
DEBUG = True

import os
import dj_database_url
import pymysql

# Install pymysql as MySQLdb
pymysql.install_as_MySQLdb()

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
DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL:
    DATABASES['default'] = dj_database_url.config(default=DATABASE_URL)

