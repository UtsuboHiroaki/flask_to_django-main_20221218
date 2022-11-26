from config.settings import *

# mysql の charset は mtf8mb4-general-ci にすること
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'flask_to_django',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'charset': 'utf8mb4',
            'isolation_level': 'read committed',
            'sql_mode': 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO',
            'init_command': 'SET foreign_key_checks = 0;',
        },
    }
}
