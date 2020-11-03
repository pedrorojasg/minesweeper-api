"""
WSGI config for cirbox project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_PATH = os.path.join(BASE_PATH, "static_deployment")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minesweeper.settings.production')

application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_PATH)
