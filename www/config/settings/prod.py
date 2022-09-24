"""
Django production settings for gokid project.
"""


import firebase_admin
import requests
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *  # noqa
from .base import env


# Sentry logging
def before_send(event, hint):
    # TODO: Enable this error again, once ELB check is fixed
    if "logger" in event and event["logger"] == "django.security.DisallowedHost":
        return
    return event


DEBUG = False
SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=[
        "api.gokid.kz",
        "admin.gokid.kz",
        "api.uvu.kz",
        "admin.uvu.kz",
    ],
)
try:
    EC2_IP = requests.get("http://169.254.169.254/latest/meta-data/local-ipv4").text
    ALLOWED_HOSTS.append(EC2_IP)
except requests.exceptions.RequestException:
    pass

CORS_ALLOW_ALL_ORIGINS = True  # TODO: Disable after front is done
CORS_URLS_REGEX = r"^/(website-api/logistics|api/tilda)/.*$"

DATABASES = {
    "default": {
        "ENGINE": env("SQL_ENGINE"),
        "NAME": env("SQL_DATABASE"),
        "USER": env("SQL_USER"),
        "PASSWORD": env("SQL_PASSWORD"),
        "HOST": env("SQL_HOST"),
        "PORT": env("SQL_PORT"),
    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                (
                    env("REDIS_HOST", default="localhost"),
                    env.int("REDIS_PORT", default="6379"),
                )
            ],
        },
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

EMAIL_HOST = "smtp.yandex.ru"
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DEBUG_PROPAGATE_EXCEPTIONS = env.bool("DEBUG_PROPAGATE_EXCEPTIONS", default=False)

sentry_sdk.init(
    dsn=env("SENTRY_DSN"),
    environment="prod",
    integrations=[DjangoIntegration()],
    before_send=before_send,
    traces_sample_rate=0.025,
    attach_stacktrace=True,
    send_default_pii=True,
)

# S3 global settings
# 'collectfast' must come before 'django.contrib.staticfiles'.
INSTALLED_APPS.insert(0, "collectfast")  # noqa: F405
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME", default="uvu-kz")
AWS_S3_CUSTOM_DOMAIN = env(
    "AWS_S3_CUSTOM_DOMAIN", default=f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
)
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME", default="eu-central-1")
AWS_DEFAULT_ACL = None
AWS_AUTO_CREATE_BUCKET = False
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_S3_SIGNATURE_VERSION = "s3v4"
# S3 static settings
COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
STATICFILES_STORAGE = "common.storage.StaticStorage"
STATIC_LOCATION = "static/"
# S3 default (private) media settings
DEFAULT_FILE_STORAGE = "common.storage.PrivateMediaStorage"
PRIVATE_MEDIA_LOCATION = "media/"
# S3 public media settings
PUBLIC_FILE_STORAGE = "common.storage.PublicMediaStorage"
PUBLIC_MEDIA_LOCATION = "media-public/"

# HERE settings
HERE = {
    "api_key": env("HERE_API_KEY", default=None),
}

# --- Firebase ---
# Check that the file with credentials exists.
env.path("GOOGLE_APPLICATION_CREDENTIALS", required=True)
firebase_admin.initialize_app()
FCM_DJANGO_SETTINGS = {"FCM_SERVER_KEY": env("FCM_API_KEY")}

# --- Kassa.com settings ---
KASSA_PROJECT_ID = env("KASSA_PROJECT_ID")
KASSA_PARTNER_EMAIL = env("KASSA_PARTNER_EMAIL")
KASSA_API_KEY = env("KASSA_API_KEY")
KASSA_NOTIFICATIONS_API_KEY = env("KASSA_NOTIFICATIONS_API_KEY").encode()

# --- ReLog API settings
RELOG_API_KEY = env("RELOG_API_KEY")

# --- Yandex Maps API settings ---
YANDEX_GEOCODER_API_KEYS = env.list("YANDEX_GEOCODER_API_KEYS_LIST")
YANDEX_ROUTER_API_KEY = env("YANDEX_ROUTER_API_KEY")

# --- Kassa.com settings ---
KASSA_PROJECT_ID = env("KASSA_PROJECT_ID")
KASSA_PARTNER_EMAIL = env("KASSA_PARTNER_EMAIL")
KASSA_API_KEY = env("KASSA_API_KEY")
KASSA_NOTIFICATIONS_API_KEY = env("KASSA_NOTIFICATIONS_API_KEY").encode()

# --- Traccar ---
TRACCAR_ADMIN_EMAIL = env("TRACCAR_ADMIN_EMAIL")
TRACCAR_ADMIN_PASSWORD = env("TRACCAR_ADMIN_PASSWORD")
TRACCAR_URL = env("TRACCAR_URL")

# --- Interpaysys.com settings ---
INTERPAYSYS_TOKEN = env("INTERPAYSYS_TOKEN")
INTERPAYSYS_SERVICE_KEY = env("INTERPAYSYS_SERVICE_KEY")
INTERPAYSYS_CONTRACT_SOURCE_ID = env.int("INTERPAYSYS_CONTRACT_SOURCE_ID")

# --- brain-server microservice settings ---
BRAIN_SERVER_HOST = env("BRAIN_SERVER_HOST")
BRAIN_SERVER_PORT = env("BRAIN_SERVER_PORT", default=8001)

# --- Celery ---
# https://github.com/celery/celery/issues/3773
BROKER_TRANSPORT_OPTIONS = {"socket_keepalive": True, "health_check_interval": 4}

# --- ORS settings ---
ORS_URL = env("ORS_URL", default="http://localhost:8010/ors")
ORS_TIMEOUT = env.int("ORS_TIMEOUT", 300)

# --- BeaconstacQR settings ---
# This is not a super-vital use case, so don't fail if it's not provided.
BEACONSTACQR_ORGANIZATION = env.int("BEACONSTACQR_ORGANIZATION", default=0)
BEACONSTACQR_TOKEN = env("BEACONSTACQR_TOKEN", default=None)
