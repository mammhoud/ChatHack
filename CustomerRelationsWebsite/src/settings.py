import os
import random, string
from pathlib import Path
from dotenv import load_dotenv
from distutils.util import strtobool
from django.contrib import messages
from helpers import ip

# import sentry_sdk

# sentry_sdk.init(
#     dsn="https://f72909208ff17ae7f6c0029df5e6b351@o4506322636111872.ingest.sentry.io/4506322648629248",
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     traces_sample_rate=1.0,
#     # Set profiles_sample_rate to 1.0 to profile 100%
#     # of sampled transactions.
#     # We recommend adjusting this value in production.
#     profiles_sample_rate=1.0,
# )
load_dotenv()  # take environment variables from .env.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = ''.join(random.choice(string.ascii_lowercase) for i in range(32))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

DEBUG = strtobool(os.getenv('DEBUG', "True"))

# Assets Management
ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')

# Hosts Settings
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com', '0.0.0.0', ip.get_ip()]

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', ip.get_ip()]
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://localhost:5085', 'http://127.0.0.1:8000',
                        'http://127.0.0.1:5085', 'https://' + ALLOWED_HOSTS[1], 'https://' + ALLOWED_HOSTS[2], ]
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Used by DEBUG-Toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'allauth',  # OAuth new
    'allauth.account',  # OAuth new
    # 'allauth.socialaccount',  # OAuth new
    # 'allauth.socialaccount.providers.github',  # OAuth new
    "sslserver",
    "apps.utils",
    "apps.core",
    "apps.customers",
    "apps.products",
   #'chatapp',
    "apps.accounts",
    "apps.api",
    "apps.charts",
    "apps.tables",
    "apps.tasks",

    "django_celery_results",

    'rest_framework',
    'rest_framework.authtoken',

    'timestamps',
    'drf_spectacular',
    'django_api_gen',

    'apps.organizations',

    "apps.consumers",
    "import_export",
    #"debug_toolbar",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    #"debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "src.urls"

UI_TEMPLATES = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [UI_TEMPLATES],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "src.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DB_ENGINE = os.getenv('DB_ENGINE', None)
DB_USERNAME = os.getenv('DB_USERNAME', None)
DB_PASS = os.getenv('DB_PASS', None)
DB_HOST = os.getenv('DB_HOST', None)
DB_PORT = os.getenv('DB_PORT', None)
DB_NAME = os.getenv('DB_NAME', None)

if DB_ENGINE and DB_NAME and DB_USERNAME:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.' + DB_ENGINE,
            'NAME': DB_NAME,
            'USER': DB_USERNAME,
            'PASSWORD': DB_PASS,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        },
    }
elif DB_ENGINE in ('mongodb', 'djongo'):
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'your_db_name',
            'HOST': 'localhost',
            'PORT': 27017,
        }}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '../db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ### Async Tasks (Celery) Settings ###

CELERY_SCRIPTS_DIR = os.path.join(BASE_DIR, "tasks_scripts")

CELERY_LOGS_URL = "/tasks_logs/"
CELERY_LOGS_DIR = os.path.join(BASE_DIR, "tasks_logs")

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://localhost:6379")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER", "redis://localhost:6379")

CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_CACHE_BACKEND = "django-cache"
CELERY_RESULT_BACKEND = "django-db"
CELERY_RESULT_EXTENDED = True
CELERY_RESULT_EXPIRES = 60 * 60 * 24 * 30  # Results expire after 1 month
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
########################################


LOGIN_REDIRECT_URL = '/'
EMAIL_BACKEND = "django.src.mail.backends.console.EmailBackend"

# ### API-GENERATOR Settings ### ## to-do
API_GENERATOR = {
    'product': "apps.products.models.Product",
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
########################################

# risky
SESSION_COOKIE_HTTPONLY = False

MESSAGE_TAGS = {
    messages.INFO: 'text-blue-800 border border-blue-300 bg-blue-50 dark:text-blue-400 dark:border-blue-800',
    messages.SUCCESS: 'text-green-800 border border-green-300 bg-green-50 dark:text-green-400 dark:border-green-800',
    messages.WARNING: 'text-yellow-800 border border-yellow-300 bg-yellow-50 dark:text-yellow-300 dark:border-yellow-800',
    messages.ERROR: 'text-red-800 border border-red-300 bg-red-50 dark:text-red-400 dark:border-red-800',
}
EMAIL_BACKEND = 'django.src.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mahmoud.mcrm@gmail.com'
EMAIL_HOST_PASSWORD = '**********'


#############################################################
# OAuth settings

GITHUB_ID = os.getenv('GITHUB_ID', None)
GITHUB_SECRET = os.getenv('GITHUB_SECRET', None)
GITHUB_AUTH = GITHUB_SECRET is not None and GITHUB_ID is not None

AUTHENTICATION_BACKENDS = (
    "src.custom-auth-backend.CustomBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'none'

SOCIALACCOUNT_PROVIDERS = {}

if GITHUB_AUTH:
    SOCIALACCOUNT_PROVIDERS['github'] = {
        'APP': {
            'client_id': GITHUB_ID,
            'secret': GITHUB_SECRET,
            'key': ''
        }
    }
