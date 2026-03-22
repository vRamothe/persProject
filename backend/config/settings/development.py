from .base import *  # noqa
from decouple import config as decouple_config
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASE_URL = decouple_config("DATABASE_URL", default=None)

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600),
    }
else:
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

# Email — print to console in dev
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "ScienceLycée <noreply@sciencelycee.fr>"
