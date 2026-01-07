from config.settings.base import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'apps.users.api.exception_handler.custom_exception_handler',
}