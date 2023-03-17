import pytest

from backend import settings
from rest_framework.test import APIClient


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'postgres',
        'ATOMIC_REQUESTS': True,
    }


@pytest.fixture
def client():
    return APIClient()
