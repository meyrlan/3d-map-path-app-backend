"""
Django development settings for UvU project.
"""

import logging
import sys

from .base import *  # noqa
from .base import ROOT_DIR, env

DEBUG = True
SECRET_KEY = "whatever"

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": env("SQL_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": env("SQL_DATABASE", default=str(ROOT_DIR / "db.sqlite3")),
        "USER": env("SQL_USER", default="postgres"),
        "PASSWORD": env("SQL_PASSWORD", default=""),
        "HOST": env("SQL_HOST", default="localhost"),
        "PORT": env("SQL_PORT", default="5432"),
    }
}

CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST_USER = "no-reply@uvu.kz"

TEST_RUNNER = env("TEST_RUNNER", default="common.testing.DiscoverRunner")
TEST_OUTPUT_DIR = "../reports"
TEST_OUTPUT_FILE_NAME = "tests.xml"

ADD_LOGS = env.bool("ADD_LOGS", default=False)

if IS_TESTING and not ADD_LOGS:  # noqa
    logging.disable(logging.CRITICAL)

CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
}


TESTING = "test" in sys.argv


# Use weak passwords hashing algorithm for tests
# https://docs.djangoproject.com/en/3.1/topics/testing/overview/#password-hashing
if TESTING:
    PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]


FCM_DJANGO_SETTINGS = {"FCM_SERVER_KEY": "only-for-tests"}


# --- ReLog API settings
RELOG_API_KEY = env("RELOG_API_KEY", default="9b97e020d81942b5b49cdf7d3e42f95a")


# --- Yandex Maps API settings ---
# TODO: change it with actual keys.
YANDEX_GEOCODER_API_KEYS = env.list(
    "YANDEX_GEOCODER_API_KEYS_LIST", default=["a420171f-7c99-44ce-b32b-2614d9cae884"]
)
# TODO: change it with actual key.
YANDEX_ROUTER_API_KEY = env(
    "YANDEX_ROUTER_API_KEY", default="a2630729-f737-4461-8301-8260e198c9a4"
)

# --- Kassa.com settings ---
KASSA_PROJECT_ID = "3508"
KASSA_PARTNER_EMAIL = "management@uvu.kz"
KASSA_API_KEY = "0F3C884A-9A43-46CE-BA45-BFECF8F6C99A"
KASSA_NOTIFICATIONS_API_KEY = b"TEST"

# --- Traccar settings ---
TRACCAR_ADMIN_EMAIL = env("TRACCAR_ADMIN_EMAIL", default="")
TRACCAR_ADMIN_PASSWORD = env("TRACCAR_ADMIN_PASSWORD", default="")
TRACCAR_URL = env("TRACCAR_URL", default="http://0.0.0.0:80")

# --- Interpaysys.com settings ---
INTERPAYSYS_TOKEN = env("INTERPAYSYS_TOKEN", default=None)
INTERPAYSYS_SERVICE_KEY = env("INTERPAYSYS_SERVICE_KEY", default=None)
INTERPAYSYS_CONTRACT_SOURCE_ID = env.int("INTERPAYSYS_CONTRACT_SOURCE_ID", default=None)

# --- brain-server microservice settings ---
BRAIN_SERVER_HOST = env("BRAIN_SERVER_HOST", default="localhost")
BRAIN_SERVER_PORT = env("BRAIN_SERVER_PORT", default="8001")

# --- ORS settings ---
ORS_URL = env("ORS_URL", default="http://localhost:8080/ors")
ORS_TIMEOUT = env.int("ORS_TIMEOUT", 300)

# --- BeaconstacQR settings ---
BEACONSTACQR_ORGANIZATION = env.int("BEACONSTACQR_ORGANIZATION", default=1)
BEACONSTACQR_TOKEN = env("BEACONSTACQR_TOKEN", default="whatever")
