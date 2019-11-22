"""
WSGI config for soul project.

It exposes the WSGI callable as a module-level variable named ``application``.
web server gateway inteerface -- to forward request to other server
For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soul.settings')

application = get_wsgi_application()
