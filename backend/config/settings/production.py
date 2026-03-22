from .base import *  # noqa

DEBUG = False

# Ensure Heroku-assigned *.herokuapp.com hosts are always accepted.
if ".herokuapp.com" not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(".herokuapp.com")

# Heroku terminates SSL at the router; trust forwarded proto to avoid redirect loops.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Email — transactional SMTP (Brevo, Mailgun, etc.)
from decouple import config
EMAIL_BACKEND = "django.core.mail.backends.smtp.SMTPBackend"
EMAIL_HOST = config("EMAIL_HOST", default="smtp-relay.brevo.com")
EMAIL_PORT = config("EMAIL_PORT", default=587, cast=int)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="ScienceLycée <noreply@sciencelycee.fr>")

# Sentry — error tracking
from decouple import config as _config_sentry
_sentry_dsn = _config_sentry("SENTRY_DSN", default="")
if _sentry_dsn:
    import sentry_sdk
    sentry_sdk.init(
        dsn=_sentry_dsn,
        traces_sample_rate=0.2,
        profiles_sample_rate=0.1,
    )

# Force SSL on Heroku Postgres (DYNO is only set on real Heroku dynos, not local Docker)
import os as _os
if _os.environ.get("DYNO") and DATABASES.get("default"):
    DATABASES["default"].setdefault("OPTIONS", {})
    DATABASES["default"]["OPTIONS"]["sslmode"] = "require"
