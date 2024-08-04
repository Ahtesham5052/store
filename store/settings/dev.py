from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@t^wli-mv_h98)vptcmwcnw-*z(ayl61n3+)bs)*jgmf38b4t5'
DEBUG = True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'store3',
		'USER': 'root',
		'PASSWORD': '50528911Wwe',
		'HOST':'localhost',
		'PORT':'3306',
	}
}

