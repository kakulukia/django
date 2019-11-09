# This is an example test settings file for use with the Django test suite.
#
# The 'sqlite3' backend requires only the ENGINE setting (an in-
# memory database will be used). All other backends will require a
# NAME and potentially authentication information. See the
# following section in the docs for more information:
#
# https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/
#
# The different databases that Django supports behave differently in certain
# situations, so it is recommended to run the test suite against as many
# database backends as possible.  You may want to create a separate settings
# file for each of the backends you test against.
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '127.0.0.1',
        'PORT': int(os.getenv('DB_PORT', 3306)),
        'NAME': 'default_django',
        'USER': 'django',
        'PASSWORD': 'django',
        'TEST': {
            'NAME': 'default_test_django',
        },
    },
    'other': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '127.0.0.1',
        'PORT': int(os.getenv('DB_PORT', 3306)),
        'NAME': 'other_django',
        'USER': 'django',
        'PASSWORD': 'django',
        'TEST': {
            'NAME': 'other_test_django',
        },
    },
}

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
