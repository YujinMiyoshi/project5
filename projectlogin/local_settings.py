from projectlogin.settings import BASE_DIR


SECRET_KEY = 'django-insecure-p5%o0cts-p85(98t=wojp$s60nyv9bnssin&cbaxj4ducjhzis'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True