import os
import sys
import django.core.handlers.wsgi
from django.conf import settings

# Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

sys.stdout = sys.stderr

DEBUG = True

application = django.core.handlers.wsgi.WSGIHandler()
