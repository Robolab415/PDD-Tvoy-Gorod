# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^58xa+897cq=%%e^#ikg^6!ka_ewlqyct8dx&y+(hkx=f9&=4^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pdd_tvoy_gorod',
        'USER': 'pdd_user',
        'PASSWORD': '0000',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

SITE_NAME = 'ПДД Твой город'
MENU_LINKS = {
    # название ссылки : текст ссылки
    'index': SITE_NAME,
    'error': 'Учебник',
    'tickets': 'Билеты',
}
