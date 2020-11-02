"""
WSGI config for cirbox project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if os.path.exists(os.path.join(BASE_PATH, '.envdev')):
    # reading .env file
    # Get enviroment variables and permit their access
    MY_SCOPE = os.environ.get('MY_ENV_SCOPE', default='minesweeper.settings.development')
else:
    # No puede haber un archivo .envdev en producción.
    MY_SCOPE = os.environ.get('MY_ENV_SCOPE', default='')

print('MY_SCOPE')
print(MY_SCOPE)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', MY_SCOPE)

application = get_wsgi_application()
