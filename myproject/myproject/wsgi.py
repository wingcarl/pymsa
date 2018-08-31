"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

#import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

#application = get_wsgi_application()

import os

from os.path import join,dirname,abspath

PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys
sys.path.insert(0,PROJECT_DIR) 


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE","myproject.settings")


application = get_wsgi_application()
