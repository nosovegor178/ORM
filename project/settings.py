import os
from dotenv import load_dotenv


load_dotenv()
DB_ENGINE = os.getenv('ENGINE')
DB_HOST = os.getenv('HOST')
DB_PORT = os.getenv('PORT')
DB_NAME = os.getenv('NAME')
DB_USER = os.getenv('USER')
DB_PASSWORD = os.getenv('PASSWORD')
DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
    }
}

DEBUG = os.getenv('DEBUG')

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
