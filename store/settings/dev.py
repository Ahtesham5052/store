from .common import *
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

SECRET_KEY = 'uqx5(^x4_u_^0+p+^6^!efam8k8$=qtt9!ddovb2@8v87ni2ua'
DEBUG = True
