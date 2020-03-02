import os


# Make this unique, and don't share it with anybody.
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = '9$@zo91aw@v-4at#s0p4kocxhfcx#&o+&carc2dc12m9v3qnrx'


# Email Server Settings
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.getenv('SG_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('SG_PWD', '')
EMAIL_HOST = 'smtp.office365.com'
EMAIL_HOST_USER = "klein203@hotmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "klein203@hotmail.com"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


# Database Settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'dj_crm',
#         'USER': 'postgres',
#         'PASSWORD': 'root',
#         'HOST': os.getenv('DB_HOST', '127.0.0.1'),
#         'PORT': os.getenv('DB_PORT', '5432')
#     }
# }

# Server Customizations
ADMIN_EMAIL = "you@your_email.com"
URL_FOR_LINKS = "https://crm.example.com"

# default settings for CSRF
# CSRF_COOKIE_AGE = 31449600
# CSRF_COOKIE_DOMAIN = None
# CSRF_COOKIE_HTTPONLY = False
# CSRF_COOKIE_NAME = 'csrftoken'
# CSRF_COOKIE_PATH = '/'
# CSRF_COOKIE_SAMESITE = 'Lax'
# CSRF_COOKIE_SECURE = False
# CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
# CSRF_HEADER_NAME = 'HTTP_X_XSRF_TOKEN'
# CSRF_TRUSTED_ORIGINS = []
# CSRF_USE_SESSIONS = False


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/users/'
