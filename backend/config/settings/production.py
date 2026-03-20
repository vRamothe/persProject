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
