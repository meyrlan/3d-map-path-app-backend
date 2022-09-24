"""Django base settings for UvU project."""

import sys
from datetime import timedelta
from pathlib import Path

import environ
from dateutil.relativedelta import relativedelta
from django.db import models
from django.urls import register_converter

AUTH_USER_MODEL = "core.User"

APPS_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
ROOT_DIR = APPS_DIR.parent
env = environ.Env()

IS_TESTING = len(sys.argv) > 1 and sys.argv[1] == "test"

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"))

ROOT_URLCONF = "config.urls"

STATIC_URL = "/static/"
STATICFILES_DIRS = [APPS_DIR / "static"]
STATIC_ROOT = ROOT_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = ROOT_DIR / "media"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

INSTALLED_APPS = [
    # Django Autocomplete Light should be before 'django.contrib.admin'.
    "dal",
    "dal_select2",
    # Django apps
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.forms",
    # Third party apps
    "safedelete",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    "simple_history",
    "django_admin_listfilter_dropdown",
    "rangefilter",
    "multiselectfield",
    "phonenumber_field",
    "fcm_django",
    "imagekit",
    "inline_actions",
    "adminsortable2",
    "colorfield",
    "django_filters",
    "admin_auto_filters",
    "django_celery_beat",
    "corsheaders",
    # Local apps
    "core.apps.CoreConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --- Django REST Framework settings ---
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # TODO: add auth later
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "api.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    # "DEFAULT_THROTTLE_CLASSES": [
    #     "rest_framework.throttling.AnonRateThrottle",
    # ],
    # "DEFAULT_THROTTLE_RATES": {
    #     "anon": "5/minute",
    # },
    "COERCE_DECIMAL_TO_STRING": False,
}

SPECTACULAR_SETTINGS = {
    "SCHEMA_PATH_PREFIX": "",
    "SERVE_URLCONF": None,
    "SERVE_PUBLIC": True,
    "SERVE_INCLUDE_SCHEMA": False,
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAuthenticated"],
    "SERVE_AUTHENTICATION": ["rest_framework.authentication.SessionAuthentication"],
    "TITLE": "UvU API",
    "VERSION": "1.0.0",
    "SERVERS": [
        {"url": "https://api.uvu.kz", "description": "Production server"},
        {"url": "http://127.0.0.1:8000", "description": "Development server"},
    ],
}

TEMPLATES_DIR = APPS_DIR / "templates"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# This option is required to use custom templates for custom formfield widgets
# The problem is that, by default, Django uses different template-paths for
# form rendering. This option says: use my TEMPLATES (see above) for form rendering
# NOTE: django.forms must be included in INSTALLED_APPS
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

ASGI_APPLICATION = "config.asgi.application"
WSGI_APPLICATION = "config.wsgi.application"

LANGUAGE_CODE = "en"
USE_TZ = True
TIME_ZONE = "Asia/Almaty"
USE_I18N = False
# Don't use locale specific date & time formats
USE_L10N = False
# Use 24-hour time format
TIME_FORMAT = "H:i"
DATETIME_FORMAT = "N j, Y, H:i"
SHORT_DATETIME_FORMAT = "m/d/Y H:i"
# Don't show seconds on input fields initial data
TIME_INPUT_FORMATS = [
    "%H:%M",  # '14:30'
    "%H:%M:%S",  # '14:30:59'
    "%H:%M:%S.%f",  # '14:30:59.000200'
]
DATETIME_INPUT_FORMATS = [
    "%Y-%m-%d %H:%M",  # '2006-10-25 14:30'
    "%Y-%m-%d %H:%M:%S",  # '2006-10-25 14:30:59'
    "%Y-%m-%d %H:%M:%S.%f",  # '2006-10-25 14:30:59.000200'
    "%m/%d/%Y %H:%M",  # '10/25/2006 14:30'
    "%m/%d/%Y %H:%M:%S",  # '10/25/2006 14:30:59'
    "%m/%d/%Y %H:%M:%S.%f",  # '10/25/2006 14:30:59.000200'
    "%m/%d/%y %H:%M",  # '10/25/06 14:30'
    "%m/%d/%y %H:%M:%S",  # '10/25/06 14:30:59'
    "%m/%d/%y %H:%M:%S.%f",  # '10/25/06 14:30:59.000200'
]
USE_THOUSAND_SEPARATOR = True

LOCALE_PATHS = ("locale",)

# Logging config
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"}
    },
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "console"}},
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "auth": {
            "handlers": ["console"],
            "level": env("DJANGO_LOG_LEVEL", default="INFO"),
            "propagate": False,
        },
    },
}

# --- Allow "sensitive fields" in models Meta ---
models.options.DEFAULT_NAMES += ("sensitive_fields",)

# --- Email OTP ---
EMAIL_OTP_DEVICE_CODE_LENGTH = env.int(
    "EMAIL_OTP_DEVICE_CONFIRMATION_CODE_LENGTH", default=4
)
EMAIL_OTP_DEVICE_CODE_VALIDITY_INTERVAL = timedelta(
    seconds=env.int(
        "EMAIL_OTP_DEVICE_CONFIRMATION_CODE_VALIDITY_INTERVAL_SECONDS", default=600
    )
)

# https://www.here.com/
HERE = {}


# --- Internal settings ---
WEBSITE_ADDRESS = env("WEBSITE_ADDRESS", default="https://admin.uvu.kz")
INTERNAL_EMAIL_DOMAINS = env("INTERNAL_EMAIL_DOMAINS", default=("uvu.kz", "gokid.kz"))
DRIVER_TUTORIAL_URL = env("DRIVER_TUTORIAL_URL", default="https://youtu.be/wYRxz3-IlE8")

# Backdoor for Apple/Google to verify our app functionality.
BACKDOOR_EMAIL = env("BACKDOOR_EMAIL", default="demo@uvu.kz")
BACKDOOR_EMAIL_CODE = env("BACKDOOR_EMAIL_CODE", default="4444")

ON_DEMAND_ADDRESS_LIST_LIMIT = env.int("ON_DEMAND_ADDRESS_LIST_LIMIT", default=3)
SCHEDULE_ADDRESS_LIST_LIMIT = env.int("SCHEDULE_ADDRESS_LIST_LIMIT", default=10)

MINIMUM_PAYMENT_AMOUNT = env.int("MINIMUM_PAYMENT_AMOUNT", default=5000)
MINIMUM_AUTOMATIC_PAYMENT_AMOUNT = env(
    "MINIMUM_AUTOMATIC_PAYMENT_AMOUNT", default="100"
)
TEMPORARY_PAYMENT_AMOUNT = env.int("TEMPORARY_PAYMENT_AMOUNT", default=10)
ON_DEMAND_TRIP_PAYMENT_SLEEP_DURATION_SECONDS = env.int(
    "ON_DEMAND_TRIP_PAYMENT_SLEEP_DURATION_SECONDS", 1
)
ON_DEMAND_TRIP_PAYMENT_MAX_DURATION = env.int(
    "ON_DEMAND_TRIP_PAYMENT_MAX_DURATION_SECONDS", default=120
)

PAYMENTS_NOTIFICATION_EMAIL = env(
    "PAYMENTS_NOTIFICATION_EMAIL", default="payments@uvu.kz"
)

TRIP_SCHEDULE_NOTIFICATION_EMAIL = env(
    "TRIP_SCHEDULE_NOTIFICATION_EMAIL", default="schedules@uvu.kz"
)

DEFAULT_MAX_TRIP_DURATION = timedelta(
    minutes=env.int("DEFAULT_MAX_TRIP_DURATION_MINUTES", default=60)
)

MAXIMUM_CALENDAR_TIME_DIFFERENCE = relativedelta(
    months=env.int("MAXIMUM_CALENDAR_TIME_DIFFERENCE_MONTHS", default=1)
)

MAX_TIME_DIFFERENCE_TO_CHANGE_SCHEDULE_TIME = timedelta(
    minutes=env.int("MAX_TIME_DIFFERENCE_TO_CHANGE_SCHEDULE_TIME_MINUTES", default=15),
)

DEFAULT_FREE_TRIP_COUNT = env.int("DEFAULT_FREE_TRIP_COUNT", 2)
DEFAULT_HALF_PRICE_TRIP_COUNT = env.int("DEFAULT_HALF_PRICE_TRIP_COUNT", 4)

PROMOCODE_LENGTH = env.int("PROMOCODE_LENGTH", default=5)
PROMOCODE_BONUS_AMOUNT = env.int("PROMOCODE_BONUS_AMOUNT", default=2000)
PROMOCODE_MAX_ATTEMPTS_TO_CREATE = env.int(
    "PROMOCODE_MAX_ATTEMPTS_TO_CREATE", default=50
)
PROMOCODE_DEFAULT_INVITE_COUNT = env.int("PROMOCODE_DEFAULT_INVITE_COUNT", 5)

SHOULD_ADD_ADDRESS_AFTER_SCHOOL_PAYMENT = env.bool(
    "SHOULD_ADD_ADDRESS_AFTER_SCHOOL_PAYMENT", default=True
)

MARKETING_SCHEDULE_PRICE = env.int("MARKETING_SCHEDULE_PRICE", 750)

# --- Yandex routing data excel file upload settings ---
MAX_MINUTES_TO_SEPARATE_ROUTE_TO_SUBROUTE = env.int(
    "MAX_MINUTES_TO_SEPARATE_ROUTE_TO_SUBROUTE", default=20
)
MAX_MINUTES_TO_NOT_ADD_NEXT_LINE_WAITING_TIME = timedelta(
    minutes=env.int("MAX_MINUTES_TO_NOT_ADD_NEXT_LINE_WAITING_TIME", default=20)
)

CREATE_ON_DEMAND_VISIBLE_EARNING_DELAY = timedelta(
    minutes=env.int("CREATE_ON_DEMAND_VISIBLE_EARNING_DELAY", default=20)
)
CREATE_PER_DAY_VISIBLE_EARNING_DELAY = timedelta(
    minutes=env.int("CREATE_PER_DAY_VISIBLE_EARNING_DELAY", default=40)
)

SIMPLE_HISTORY_REVERT_DISABLED = True

# --- Celery  ---
# Broker settings
BROKER_USER = env("RABBITMQ_DEFAULT_USER", default="guest")
BROKER_PASSWORD = env("RABBITMQ_DEFAULT_PASS", default="guest")
BROKER_HOST = env("RABBITMQ_HOST", default="localhost")
BROKER_PORT = env("RABBITMQ_PORT", default="5672")

CELERY_ENABLED = env.bool("CELERY_ENABLED", default=False)
# http://docs.celeryproject.org/en/latest/userguide/configuration.html
CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = (
    f"amqp://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}/"
)
CELERY_RESULT_BACKEND = "rpc://"
CELERY_RESULT_PERSISTENT = False
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_TIME_LIMIT = env.int("CELERY_TASK_TIME_LIMIT", 1000)
CELERY_TASK_SOFT_TIME_LIMIT = env.int("CELERY_TASK_SOFT_TIME_LIMIT", 100)
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "max_retries": 3,
    "interval_start": 0,
    "interval_step": 0.2,
    "interval_max": 1,
}

# --- Telegram ---
TELEGRAM_BOT_TOKEN = env("TELEGRAM_BOT_TOKEN", default=None)
TELEGRAM_DEFAULT_CHAT_ID = env("TELEGRAM_DEFAULT_CHAT_ID", default=None)

# --- Interpaysys.com ---
INTERPAYSYS_PAYOUT_URL = "https://api.interpaysys.com/v1/svc/card_withdrawal/requests"
INTERPAYSYS_MINIMUM_PAYOUT_AMOUNT = env.int(
    "INTERPAYSYS_MINIMUM_PAYOUT_AMOUNT", default=500
)
INTERPAYSYS_MINIMUM_PAYOUT_FEE = 150
INTERPAYSYS_MINIMUM_AMOUNT_WITHOUT_FEE = 10_000
INTERPAYSYS_REQUEST_TIMEOUT_SEC = env.int("INTERPAYSYS_REQUEST_TIMEOUT_SEC", default=10)

# --- Traccar ---
TRACCAR_REQUEST_TIMEOUT_SEC = 5

MINIMUM_EVENT_CAPACITY = env.int(
    "MINIMUM_EVENT_CAPACITY", default=1)
