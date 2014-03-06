SITE_ID = 1
DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'saurondb' ,
        'USER': 'sauron_u',
        'PASSWORD': 'sauron_u',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}



#settings this for debug tools
INTERNAL_IPS = ('127.0.0.1','10.0.2.2')
