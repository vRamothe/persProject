from .base import *  # noqa

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "sciencelycee",
        "USER": "sciencelycee",
        "PASSWORD": "sciencelycee_secret",
        "HOST": "db",
        "PORT": "5432",
    }
}

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
